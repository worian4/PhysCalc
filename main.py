from core.calc import Physics_Calculator



der_formulas = open('res/derivative_formulas.txt', 'r').read().split('\n')
formulas = open('res/base_formulas.txt', 'r').read().split('\n')
consts = open('res/consts.txt', 'r').read().split('\n')
sn_input = open('res/sn_input.txt', 'r').read().split('\n')
sn_output = open('res/sn_output.txt', 'r').read().split('\n')

inp = ['P = 400Wt', 'R = 10Om']  #examples of input
inp1 = ['Q = 4200J', 'c = 4200J/kg', 't1 = 100C', 't2 = 102C']

calc = Physics_Calculator(formulas, der_formulas, consts, sn_input, sn_output)

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
