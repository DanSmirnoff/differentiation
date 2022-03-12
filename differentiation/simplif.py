import helpFunc

def simplificator(equation):
    parts = helpFunc.founder(equation, '^1')
    exceptions = []         #��� ����������, ����� ���������� ����� ������ ��������
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
        equation = helpFunc.replacer(equation, 'x^0', '1', exceptions)
    parts = helpFunc.founder(equation, '1*')
    for i in parts:
        if len(parts) > 0:
            if i == 0 and equation[i+1] == '*':
                equation = helpFunc.replacer(equation, '1*', '', exceptions = [])
            elif equation[i+1] == '*' and not equation[i-1].isdigit():
                equation = helpFunc.replacer(equation, '1*', '', exceptions = [])
    parts = helpFunc.founder(equation, '*1')
    for i in parts:
        if len(parts) > 0:
            if i == len(equation) - 1 and equation[i-1] == '*':
                equation = helpFunc.replacer(equation, '*1', '', exceptions = [])
            elif equation[i-1] == '*' and not equation[i-1].isdigit():
                equation = helpFunc.replacer(equation, '*1', '', exceptions = [])
    return equation