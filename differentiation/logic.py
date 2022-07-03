import methods
import simpleDeriv
import helpFunc
import simplif

def logic(equation):

    layer = 0

    for i in range(len(equation)):
        if equation[i] == '(':          #needed to fix
            layer += 1
        elif equation[i] == ')':
            layer -= 1
        else:
            if layer == 0:
                if equation[i] == '*':
                    return methods.multi(equation[:i], equation[i+1:])

    return equation
