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
            part1 = helpFunc.goUntil(equation, i-1, -1, ['*','/','+','-','^','('])    
        if equation[i+1] == '(':
            p2 = True
            part2 = equation[i+2 : helpFunc.bracketFounder(equation, i+1, 1)]
        else:
            part2 = helpFunc.goUntil(equation, i+1, 1, ['*','/','+','-','^', ')'])      
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


    print(equation, ' -- converter check')
    return equation


def distr(equation):                #This block distribute equation for easier tasks
    equation = simplif.simplificator(equation)
    
    while True:         #kostil no rabotaet\\\
        if equation[0] == '(' and equation[-1] == ')' and helpFunc.bracketFounder(equation, 0, 1) == len(equation)-1:   
            print('(...)')
            equation = equation[1 : -1]
        else:
            break

    layer = 0

    if '+' in equation:
        for i in range(len(equation)):
            if equation[i] == '(':          #needed to fix
                layer += 1
            elif equation[i] == ')':
                layer -= 1
            else:
                if layer == 0:
                    if equation[i] == '+':
                        return methods.summ(equation[:i], equation[i+1:])

    layer = 0

    if '*' in equation:
        for i in range(len(equation)):
            if equation[i] == '(':          #needed to fix
                layer += 1
            elif equation[i] == ')':
                layer -= 1
            else:
                if layer == 0:
                    if equation[i] == '*':
                        return methods.multi(equation[:i], equation[i+1:])



    if equation[0] == 'p':
        if equation[1:5] == 'ower':
            a = 5
            b = helpFunc.bracketFounder(equation, a, 1)
            j = 0           
            level = 0
            while True:
                if equation[a+j+1] == '(':
                    level += 1
                elif equation[a+j+1] == ')':
                    level -= 1
                elif equation[a+j+1] == ',' and level == 0:
                    index = a+j+1
                    break
                j += 1
            print(equation[a+1 : index],'__', equation[index+1 : b], 'POWER')
            return simpleDeriv.diffPower(equation[a+1 : index], equation[index+1 : b])

    if equation[0] == 'l':
        if equation[1:3] == 'og':
            a = 3
            b = helpFunc.bracketFounder(equation, a, 1)
            j = 0           
            level = 0
            while True:
                if equation[a+j+1] == '(':
                    level += 1
                elif equation[a+j+1] == ')':
                    level -= 1
                elif equation[a+j+1] == ',' and level == 0:
                    index = a+j+1
                    break
                j += 1
            print(equation[a+1 : index],'__', equation[index+1 : b], 'LOG')
            return simpleDeriv.diffLog(equation[a+1 : index], equation[index+1 : b])



    elif '(' in equation:           #эта вещь не работает из-за великолепного повер (теперь должна работать я хз)
        for i in range(len(equation)):
            if equation[i] == '(':          #needed to fix
                return methods.comp(equation[:i], equation[i+1:-1])

    else:
        if equation == 'x':
            return '1'
        elif equation == 'sin' or equation == 'cos' or equation == 'tg' or equation == 'ctg':
            return simpleDeriv.diffTrig(equation)
        elif equation == 'arcsin' or equation == 'arccos' or equation == 'arctg' or equation == 'arcctg':
            return simpleDeriv.diffArc(equation)
        elif helpFunc.isNumber(equation):
            return '0'
        
    #часть кода ниже нахуй не нужна но пусть будет на всякий
    print('бля как сюда код зашел')

    for i in range(len(equation)):
        if equation == 'x':
            return '1'
        elif equation == 'sin' or equation == 'cos' or equation == 'tg' or equation == 'ctg':
            return simpleDeriv.diffTrig(equation)
        elif equation[i] == '*':
            return methods.multi(equation[:i], equation[i+1:])
        elif equation[i] == '/':
            j = i + 1
            divider = ''
            while j < len(equation) and equation[j] != '+' and equation[j] != '-' and equation[j] != '*':
                divider += equation[j]
                j += 1
            return methods.div(equation[:i], divider)
        elif equation[i] == 'p':
            if equation[i+1:i+5] == 'ower':
                index = helpFunc.founder(equation,',')
                j = index[0]
                a = i+5
                b = helpFunc.bracketFounder(equation, a, 1)
                print(equation[a+1 : j], equation[j+1 : b])