import methods
import simpleDeriv
import helpFunc
import simplif


def converter(equation):        #This block convertes all '(x)' for nothing because we don't need it and removes ' '
    i = 0
    while i < len(equation):
        if equation[i] == '(':
            if equation[i + 1] == 'x':
                if i+3 < len(equation):
                    equation = equation[:i] + equation[i+3:]
                else:
                    equation = equation[:i]
        i += 1
    index = helpFunc.founder(equation, '^')
    for i in index:
        if equation[i-1] == ')':
            part1 = helpFunc.goUntil(equation, i-2, -1, ['('])
        else:
            part1 = helpFunc.goUntil(equation, i-1, -1, ['*','/','+','-','^'])
        if equation[i+1] == '(':
            part2 = helpFunc.goUntil(equation, i+2, 1, [')'])
        else:
            part2 = helpFunc.goUntil(equation, i+1, 1, ['*','/','+','-','^'])
    print(part1 + '^' + part2)
    equation = helpFunc.replacer(equation, part1 + '^' + part2, 'power(' + part1 + ',' + part2 + ')', '')
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