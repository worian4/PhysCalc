from core.calc import Physics_Calculator



def calculate(inp):
    out = calc.calculate([i.split(' = ') for i in inp]) #to get calculated the input
    for i in range(len(out[0])): print(out[0][i]+' = '+str(out[1][i]))
def upgrade():
    formulas = calc.generate_derivative_formulas()  #to upgrade derivative formulas
    print('\n\nwriting down formulas...\n')
    with open('res/derivative_formulas.txt', 'w') as file:
        for i in range(len(formulas)):
            file.write(' '.join(formulas[i])+'\n')
    print('\n\n'+'-'*20+'UPGRADE-COMPLETE'+'-'*20+'\n\n')

der_formulas = open('res/derivative_formulas.txt', 'r').read().split('\n')
formulas = open('res/base_formulas.txt', 'r').read().split('\n')
consts = open('res/consts.txt', 'r').read().split('\n')
sn_input = open('res/sn_input.txt', 'r').read().split('\n')
sn_output = open('res/sn_output.txt', 'r').read().split('\n')

calc = Physics_Calculator(formulas, der_formulas, consts, sn_input, sn_output)

while 1:
    command = input()

    if command[:9]=="calculate": #example: calculate(Q = 4200J,c = 4200J/kg*C,t1 = 100C,t2 = 102C)
        try:
            command = command.replace("calculate","").replace("(","").replace(")","").split(",")
            calculate(command)
        except Exception as e:
            print(str(e))
    elif command == "upgrade": upgrade()
    else: print("command not found")
