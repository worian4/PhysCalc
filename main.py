from core.calc import Physics_Calculator



der_formulas = open('res/derivative_formulas.txt', 'r').read().split('\n')
formulas = open('res/base_formulas.txt', 'r').read().split('\n')
consts = open('res/consts.txt', 'r').read().split('\n')

inp = ['P = 400', 'R = 10']  #example for input
inp1 = ['Q = 4200', 'c = 4200', 't1 = 100', 't2 = 102']  #example for input

calc = Physics_Calculator(formulas, der_formulas, consts)

'''
formulas = calc.generate_derivative_formulas()  #to upgrade derivative formulas

with open('res/derivative_formulas.txt', 'w') as file:
    for i in formulas:
        print(i)
        file.write(' '.join(i)+'\n')
'''

out = calc.calculate([i.split(' = ') for i in inp1])  #to get calculated the input

for i in range(len(out[0])):
    print(out[0][i]+' = '+str(out[1][i]))
