import helpFunc

def simplificator(equation):

    eq1 = equation      # for tracing changes

    if len(equation) == 0:
        print('len(equation) == 0')
        return equation

    if equation[0] == '(' and equation[-1] == ')' and helpFunc.bracketFounder(equation, 0, 1) == len(equation)-1:
        print('()')
        equation = equation[1 : -1]

    parts = helpFunc.founder(equation, 'power(x,1)')
    exceptions = []
    equation = helpFunc.replacer(equation, 'power(x,1)', 'x', exceptions)

    parts = helpFunc.founder(equation, '^1')
    exceptions = []         
    if len(parts) != 0:
        for i in parts:
            if i+2 < len(equation):
                if equation[i+2].isdigit() or equation[i+2] == '.':
                    exceptions.append(i)
        equation = helpFunc.replacer(equation, '^1', '', exceptions)
    parts = helpFunc.founder(equation, '^0')
    exceptions = []
    if len(parts) != 0:
        for i in parts:
            if i+2 < len(equation):
                if equation[i+2] == '.':
                    exceptions.append(i)
        for i in range(len(exceptions)):
            exceptions[i] -= 1
        equation = helpFunc.replacer(equation, 'x^0', '1', exceptions)
    parts = helpFunc.founder(equation, '1*')
    exceptions = []
    if len(parts) > 0:
        for i in parts:
            if i != 0:
                if equation[i-1].isdigit():
                    exceptions.append(i)
        equation = helpFunc.replacer(equation, '1*', '', exceptions)
    parts = helpFunc.founder(equation, '*1')
    exceptions = []
    if len(parts) > 0:
        for i in parts:
            if i + 2 < len(equation):
                if equation[i+2].isdigit():
                    exceptions.append(i)
        equation = helpFunc.replacer(equation, '*1', '', exceptions)

    equation = helpFunc.replacer(equation, '*(1)', '', exceptions = '')  # Possibly break smth
    equation = helpFunc.replacer(equation, '(1)*', '', exceptions = '')


    equation = equation.replace('sin(x)', 'sin', 1)         
    equation = equation.replace('cos(x)', 'cos', 1)
    equation = equation.replace('tg(x)', 'tg', 1)
    equation = equation.replace('ctg(x)', 'ctg', 1)
    equation = equation.replace('arcsin(x)', 'arcsin', 1)         
    equation = equation.replace('arccos(x)', 'arccos', 1)
    equation = equation.replace('arctg(x)', 'arctg', 1)
    equation = equation.replace('arcctg(x)', 'arcctg', 1)


    exceptions = []
    minuses = helpFunc.founder(equation, '-')                  # There is hard to deal with things like -sin, so this thing replace it to (-1)*sin
    for i in range(len(minuses)):                              # Maybe in future i fix it, because it isn't optimized
        if equation[minuses[i]+1].isdigit():
            exceptions.append(minuses[i])
    equation = helpFunc.replacer(equation, '-', '+(-1)*', exceptions)
    if equation[0] == '+':
        equation = equation[1:]

    print(eq1, ' -> ', equation, ' -- simplificator check')

    return equation
