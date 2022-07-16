import diff
import methods
import simplif
import helpFunc
import time
import simpleDeriv
import math
#import sympy


#print(helpFunc.isNumber(input()))

#print(simpleDeriv.diffPower('sin','cos'))

equation = diff.converter(input())
equation = diff.distr(equation)
print('diff check - ' + equation)
equation = simplif.simplificator(equation)
print('\n' + 'answer -', equation + '\n')

#print()
#print('Enter number: ')
#number = int(input())
#equation = helpFunc.returnTo(equation)
#print(equation, ' -- modified equation')
#equation1 = sympy.sympify(equation)
#print(equation1.subs('x', number))


#print(helpFunc.founder('(1)*(x)+(x)*(1)', '*1'))

#print(helpFunc.goUntil('x^2', 0, -1, ['s']))

#print(helpFunc.bracketFounder('(dadasd)', 7, -1))
