import re

from V2.Objects.Matrix import Matrix


class Computer:

    def __init__(self):
        self.variables = {}

    def evaluate(self, rhs):
        #TODO do this better (determine if matrix)

        if len(re.findall(']', rhs)) >= 1:
            output = Matrix(rhs)
        else:
            output = rhs
        return output

    def read_loop(self):
        inp = None

        while inp != "exit":
            inp = input()
            if inp.lower() == "exit":
                break

            # return value
            if len(re.findall('=', inp)) == 0:
                if inp in self.variables:
                    print("Value of \'" + inp + "\' is: \n" + str(self.variables[key]) + "\"")
                else:
                    print("Variable doesnt exist")
            # assign value
            elif len(re.findall('=', inp)) == 1:
                key, rhs = [x.strip().lower() for x in inp.split('=')]

                value = self.evaluate(rhs)
                self.variables[key] = value

            # inline equation
