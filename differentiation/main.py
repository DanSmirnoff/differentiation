import diff
import methods
import simplif
import helpFunc
import time
import simpleDeriv


#print(simpleDeriv.diffPower('sin','cos'))

equation = diff.converter(input())
equation = diff.distr(equation)
print('diff check - ' + equation)
print('\n' + 'answer -', simplif.simplificator(equation) + '\n')

#print(helpFunc.founder('(1)*(x)+(x)*(1)', '*1'))

#print(helpFunc.goUntil('x^2', 0, -1, ['s']))

#print(helpFunc.bracketFounder('(dadasd)', 7, -1))
