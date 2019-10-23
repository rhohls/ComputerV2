import re

from V2.Objects.Equation import Equation
from V2.Objects.Function import Function
from V2.Objects.Imaginary import Imaginary
from V2.Objects.Matrix import Matrix


class Computer:
    #BODMAS - Brackets, Order, Division/Multiplication, Addition/Subtraction

    def __init__(self):
        self.variables = {}
        self.illegal_variables = ['i']
        self.debug = 0
        self.precision = 5


    def read_loop(self):
        inp = None
        while inp != "exit":
            inp = input()
            if inp.lower() == "exit":
                break
            # elif: inp.lower() = "setprecision"
            else:
                self.handle_input(inp)

    def handle_input(self, inp):
        # return value
        if len(re.findall('=', inp)) == 0:
            # print(self.variables)
            if inp.lower() in self.variables:
                value = self.variables[inp.lower()]
                self.print_value(value)
            else:
                print("Variable does not exist")

        # assign value
        elif len(re.findall('=', inp)) == 1:
            self.assign_values(inp)

        # inline equation
        elif len(re.findall(r'\?', inp)) == 1:
            print("EVALUATE AND SOLVE")
        else:
            print("Error handling input")

    def assign_values(self, inp):
        key, rhs = [x.strip().lower() for x in inp.split('=')]

        if key.lower() == "i":
            print("Cannot have variable named i")
        else:
            value = self.evaluate(key, rhs)
            self.variables[key.lower()] = value
            self.print_value(value)

    def evaluate(self, key, raw_input):
        return_info = None
        ##function or matrix
        if "[" in raw_input:
            return_info = Matrix(raw_input)
        elif "fun(" in key:
            return_info = Function(key, raw_input)

        #imaginary or basic
        if self.is_imaginary(raw_input):
            return_info = Imaginary(raw_input)
        else:
            return_info = Equation(raw_input)

        return_info.replace_known_variables(self.variables)

        return_info.reduce()

        return return_info

    def print_value(self, value):
        if isinstance(value, int):
            print(int(value))
        elif isinstance(value, float):
            print(("%0.*f" % (self.precision, value)).rstrip('0').rstrip('.'))
        else:
            print(str(value))

    def is_imaginary(self, raw_input):
        token_list = self.tokenize(raw_input)
        if self.debug : print("tokenize list is: ", token_list)
        pass
