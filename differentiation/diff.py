import methods
import simpleDeriv
import helpFunc
import simplif


def converter(equation):
    powerCounter = len(helpFunc.founder(equation, '^'))               #This block convertes a^b to power(a,b)
    i = 0
    while powerCounter != 0:
        for j in range(len(equation)):
            if equation[j] == '^':
                i = j
                break
        p1 = False
        p2 = False
        if equation[i-1] == ')':
            print('a')
            p1 = True
            part1 = equation[helpFunc.bracketFounder(equation, i-1, -1) + 1 : i-1]
            print(part1)
        else:
            part1 = helpFunc.goUntil(equation, i-1, -1, ['*','/','+','-','^','(',','])
        if equation[i+1] == '(':
            p2 = True
            part2 = equation[i+2 : helpFunc.bracketFounder(equation, i+1, 1)]
        else:
            part2 = helpFunc.goUntil(equation, i+1, 1, ['*','/','+','-','^', ')',','])
        print(part1 + '^' + part2)

        if p1 and p2:
            equation = equation.replace('(' +  part1 + ')' + '^' + '(' + part2 + ')', '(' +'power(' + part1 + ',' + part2 + ')' + ')', 1)
            print('++')
        elif p1 and not p2:
            equation = equation.replace('(' +  part1 + ')' + '^' + part2, '(' +'power(' + part1 + ',' + part2 + ')' + ')', 1)
            print('+-')
        elif p2 and not p1:
            equation = equation.replace(part1 + '^' + '(' + part2 + ')', '(' +'power(' + part1 + ',' + part2 + ')' + ')', 1)
            print('-+')
        else:
            equation = equation.replace(part1 + '^' + part2, '(' +'power(' + part1 + ',' + part2 + ')' + ')', 1)
            print('--')
        powerCounter -= 1

        print(equation + '&')


    i = 0                     #This block convertes all '(x)' for nothing because we don't need it and removes ' '
    while i < len(equation):
        if equation[i] == '(':
            if equation[i+1] == 'x' and equation[i+2] == ')':
                if i+3 < len(equation):
                    equation = equation[:i] + equation[i+3:]
                else:
                    equation = equation[:i]
        i += 1         

    print('converter check - ' + equation)
    return equation


def distr(equation):                #This block distribute equation for easier tasks
    equation = simplif.simplificator(equation)
    print('simplificator check - ' + equation)
    for i in range(len(equation)):
        if equation == 'x':
            return simpleDeriv.simplePow('x', '1')
        elif equation == 'sin' or equation == 'cos' or equation == 'tg' or equation == 'ctg':
            return simpleDeriv.trig(equation)
        elif equation[i] == '*':
            return methods.multi(equation[:i], equation[i+1:])
        elif equation[i] == '/':
            j = i + 1
            divider = ''
            while j < len(equation) and equation[j] != '+' and equation[j] != '-' and equation[j] != '*':
                divider += equation[j]
                j += 1
            return methods.div(equation[:i], divider)
        elif equation[i] == '(' and equation[i-1] != '*' and equation[i-1] != '+':        #обработать конструкции вида '(....'
            return methods.comp(equation[:i], equation[i+1:-1])
        elif equation[i] == '^' and equation[i-1] == 'x':
            power = ''
            if equation[i+1] == '(':
                j = i + 2
                while equation[j] != ')':
                    power += equation[j] 
                    j += 1               
            else:               #user-friendly 5 lines of code
                j = i + 1
                while j < len(equation) and equation[j] != '+' and equation[j] != '-' and equation[j] != '*' and equation[j] != '/' and equation[j] != '^':
                    power += equation[j] 
                    j += 1              
            return simpleDeriv.simplePow(equation[:i], power)