from sympy import solve, parse_expr
from collections.abc import Iterable



class Physics_Calculator:

    def flatten(self, l):
        for el in l:
            if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
                yield from self.flatten(el)
            else:
                yield el

    def generator(self, formula, track):
        for i in range(len(formula)):
            for k in self.base_formulas:
                if formula[i] == k[0][0] and not (k[1] in track) and formula != k[0]:
                    edited_formula = formula
                    edited_formula[i] = ['(', k[0][2:], ')']
                    edited_formula = list(self.flatten(edited_formula))
                    track.append(k[1])
                    print(' '.join(edited_formula))
                    self.der_formulas.append(list(self.flatten(edited_formula)))
                    return self.generator(list(self.flatten(edited_formula)), track)
        
    def check(self):
        formulas = [list(self.flatten(self.der_formulas[0]))]
        for i in self.der_formulas:
            flag = False
            for k in formulas:
                if not self.eq_sim(i, k):
                    flag = True
            if flag: formulas.append(list(self.flatten(i)))
        return formulas
    
    def eq_sim(self, eq1: list, eq2: list) -> bool:
        var_eq1 = [a for a in eq1 if a.isalpha() == 1]
        var_eq2 = [a for a in eq2 if a.isalpha() == 1]
        return sorted(var_eq1) == sorted(var_eq2)

    def generate_derivative_formulas(self):
        self.der_formulas = []
        for k in self.base_formulas:
            self.der_formulas.append(list(self.flatten(k[0])))
            self.generator(list(self.flatten(k[0])), [k[1]])
        self.der_formulas = self.check()
        return self.der_formulas
    
    def find_formula(self, vars):
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
    
    def set_values(self, formula, vars):
        res = list(self.flatten(formula))
        for i in range(len(res)):
            for k in vars:
                if res[i] == k[0]: res[i] = k[1]
        return ' '.join(res)

    def solve_expression(self, formula):
        formula1 = formula.replace('=', '- (') + ' )'
        return solve(parse_expr(formula1))
    
    def calculate(self, vars):
        output = self.find_formula(vars)
        if output == [0]: return [0]
        
        formulas, needed = output[0], output[1]
        output = []
        for formula in formulas:
            f = self.set_values(formula, vars)
            output.append(self.solve_expression(f)[0])

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

        return [needed, output]
    
    def __init__(self, base_formulas, der_formulas, consts):
        self.base_formulas = list(i.split('  ') for i in base_formulas)
        for i in range(len(self.base_formulas)):
            for k in range(len(self.base_formulas[i])):
                self.base_formulas[i][k] = self.base_formulas[i][k].split(' ')
        self.der_formulas = tuple(i.split(' ') for i in der_formulas)
        self.consts = tuple(i.split(' ') for i in consts)
