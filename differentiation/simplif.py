import helpFunc

def simplificator(equation):
    print('check')
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
            if i < len(equation):
                if equation[i+1].isdigit():
                    exceptions.append(i)
        equation = helpFunc.replacer(equation, '*1', '', exceptions)

    return equation