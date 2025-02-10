from sympy import solve, parse_expr
from collections.abc import Iterable



class Physics_Calculator:

    def flatten(self, l: list):
        for el in l:
            if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
                yield from self.flatten(el)
            else:
                yield el

    def input_to_sn(self, vars: list) -> list:
        turned_to_sn = []
        need_to_turn = []
        for i in vars:
            unit = []
            num = []
            for k in i[1]:
                if k.isalpha() or k in ['/', '*']: unit.append(k)
                else: num.append(k)
            unit = ''.join(unit)
            num = ''.join(num)
            for k in self.sn_input:
                if unit == k[0]:
                    expr = k[1].replace('x', num) + '-x'
                    num = str(solve(parse_expr(expr))[0])
                    if not [a for a in i[0] if a.isalpha()][0] in [a[0] for a in need_to_turn]:
                        need_to_turn.append([[a for a in i[0] if a.isalpha()][0], unit])
                    break
            turned_to_sn.append(num)
        return [turned_to_sn, need_to_turn]
    
    def sn_to_output(self, vals: list, vars: list, need_to_turn: list) -> list:
        for i in vars:
            for k in need_to_turn:
                var = ''.join([b for b in i if b.isalpha()])
                if var == k[0]:
                    for a in self.sn_output:
                        if k[1] == a[0]:
                            expr = a[1].replace('x', str(vals[vars.index(i)])) + '-x'
                            vals[vars.index(i)] = str(solve(parse_expr(expr))[0]) + k[1]
        return vals

    def generator(self, formula: list, track: list):
        for i in range(len(formula)):
            for k in self.base_formulas:
                if formula[i] == k[0][0] and not (k[1] in track) and formula != k[0]:
                    edited_formula = formula
                    edited_formula[i] = ['(', k[0][2:], ')']
                    edited_formula = list(self.flatten(edited_formula))
                    track.append(k[1])
                    #print(' '.join(edited_formula))
                    self.der_formulas.append(list(self.flatten(edited_formula)))
                    return self.generator(list(self.flatten(edited_formula)), track)
        
    def check(self):
        formulas = [list(self.flatten(self.der_formulas[0]))]
        for i in range(len(self.der_formulas)):
            flag = False
            for k in formulas:
                if not self.eq_sim(self.der_formulas[i], k): flag = True
            if flag: formulas.append(list(self.flatten(self.der_formulas[i])))
            print(str(round(i/len(self.der_formulas)*100,2))+'%')
        return formulas
    
    def eq_sim(self, eq1: list, eq2: list) -> bool:
        var_eq1 = [a for a in eq1 if a.isalpha() == 1]
        var_eq2 = [a for a in eq2 if a.isalpha() == 1]
        return sorted(var_eq1) == sorted(var_eq2)

    def generate_derivative_formulas(self):
        print('\n\ngenerating...')
        self.der_formulas = []
        for k in self.base_formulas:
            self.der_formulas.append(list(self.flatten(k[0])))
            self.generator(list(self.flatten(k[0])), [k[1]])
        print('\n\nchecking... please wait, this may take up to a few minuts\n\n')
        self.der_formulas = self.check()
        return self.der_formulas
    
    def find_formula(self, vars: list) -> list:
        known = [i[0] for i in vars]

        formulas = []
        need = []
        for formula in self.der_formulas: 
            f_known = [a for a in formula if a.isalpha()]
            needed = [a for a in f_known if not(a in known)]
            if len(needed) == 1:
                formulas.append(formula)
                need.append(needed[0])

        if formulas == []:
            print('Physics_Calculator: Unable to solve the task')
            return [0]
        
        for i in range(len(formulas)):
            formulas[i][formulas[i].index(need[i])] = 'x'
                
        return [formulas, need]
    
    def set_values(self, formula: list, vars: list) -> str:
        res = list(self.flatten(formula))
        for i in range(len(res)):
            for k in vars:
                if res[i] == k[0]: res[i] = k[1]
        return ' '.join(res)

    def solve_expression(self, formula: str):
        formula1 = formula.replace('=', '- (') + ' )'
        return solve(parse_expr(formula1))[0]
    
    def calculate(self, vars: list) -> list:
        sn = self.input_to_sn(vars)
        sn_vars, need_to_turn = sn[0], sn[1]
        for i in range(len(vars)): vars[i][1] = sn_vars[i]

        for i in self.consts:
            vars.append(i)
        output = self.find_formula(vars)
        if output == [0]: return [0]
        
        formulas, needed = output[0], output[1]
        output = []
        for formula in formulas:
            f = self.set_values(formula, vars)
            output.append(self.solve_expression(f))

        sorted_need = []
        sorted_output = []
        repeated = []
        for i in range(len(needed)):
            if not (needed[i] in sorted_need and output[i] in sorted_output):
                sorted_need.append(needed[i])
                sorted_output.append(output[i])
            else:
                repeated.append(i)
        i = len(repeated) - 1
        while i != -1:
            needed.pop(repeated[i])
            output.pop(repeated[i])
            i -= 1

        i = len(output) - 1
        while i != -1:
            if type(output[i]) == dict:
                output.pop(i)
                needed.pop(i)
            i -= 1

        output = self.sn_to_output(output, needed, need_to_turn)
        return [needed, output]
    
    def __init__(self, base_formulas, der_formulas, consts, sn_input, sn_output):
        self.base_formulas = list(i.split('  ') for i in base_formulas)
        for i in range(len(self.base_formulas)):
            for k in range(len(self.base_formulas[i])):
                self.base_formulas[i][k] = self.base_formulas[i][k].split(' ')
        self.der_formulas = tuple(i.split(' ') for i in der_formulas)
        self.consts = tuple(i.split(' ') for i in consts)
        self.sn_input = tuple(i.split(' ') for i in sn_input)
        self.sn_output = tuple(i.split(' ') for i in sn_output)
