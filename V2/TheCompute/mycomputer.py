import re

from V2.Objects.Imaginary import Imaginary
from V2.Objects.Matrix import Matrix
import V2.mymath as math



class Computer:
    #BODMAS - Brackets, Order, Division/Multiplication, Addition/Subtraction

    def __init__(self):
        self.variables = {}
        self.illegal_variables = ['i']

        # seperate terms
        #
        # iterate through terms
        # evaluate all terms / simplify / reduce
        # - already exsisting variables
        # - illegal / non exist variables
        #
        # - identify and assign imaginary
        # - then functions
        # - then matrix



    ###non matrix non function
    def tokenize(self, input_string):
        split = re.split('([+,\-,\/,*,%,^,**,(,)])', input_string)

        new_list = []
        i = 0
        while i < len(split):
            #parenthesis (recursive)
            if (split[i] == '('):
                j = i
                while j < len(split):
                    if split[j] == ')':
                        break
                    j += 1
                    if j == len(split):
                        raise Exception("Poorly formatted input: Missing parenthesis")
                teststr = self.str_from_list(split, i, j)
                cust_list = self.tokenize(teststr)

                new_list.append(cust_list)
                i = j

            #numbers
            else:
                try:
                    toadd = float(split[i])
                except:
                    toadd = split[i].strip()
                finally:
                    if toadd:
                        new_list.append(toadd)
            i += 1

        return new_list


    def replace_known_variables(self, token_list):
        i = 0

        while i < len(token_list):
            if type(token_list[i]) is list:
                self.replace_known_variables(token_list[i])
            elif token_list[i] in self.variables:
                token_list[i] = self.variables[token_list[i]]

            i += 1
        return token_list


    def apply_operations(self, equation):
        i = 0

        # () brackets
        while i < len(equation):
            if type(equation[i]) is list:
                equation[i] = self.apply_operations(equation[i])
            i += 1

        i = 0
        new_equation = []

        # ^ (power)
        while i < len(equation):
            if equation[i] == '^':
                value = math.custom_power(equation[i-1], equation[i+1])
                new_equation[-1] = value
                i += 1
            else:
                new_equation.append(equation[i])
            i += 1

        equation = new_equation
        i = 0
        new_equation = []

        # * / % multiplication
        while i < len(equation):
            if equation[i] in ['*', '/', '%']:
                value = math.operation (equation[i - 1], equation[i + 1], equation[i])
                new_equation[-1] = value
                i += 1
            else:
                new_equation.append(equation[i])
            i += 1

        equation = new_equation
        i = 0
        new_equation = []

        # + - add
        while i < len(equation):
            if equation[i] in ['+', '-']:
                value = math.operation(equation[i - 1], equation[i + 1], equation[i])
                new_equation[-1] = value
                i += 1
            else:
                new_equation.append(equation[i])
            i += 1

        if len(new_equation) > 1:
            raise Exception ("This shouldnt be happning")
        return new_equation[0]


    def read_loop(self):
        inp = None

        self.variables['a'] = 3

        inp = "4 - 5 + (1 + 2)^2 - 4 * (3 * 2 + a)"
        print("Intial input str: " + inp)
        # inp = "1 + 2 + 3 + 4"
        out = self.tokenize(inp)
        print("tokenize list is: ", out)

        out = self.replace_known_variables(out)
        print("replace var list is: ", out)

        out = self.apply_operations(out)
        print("final result is: ", out)




        # if len(re.findall(']', input_string)) >= 1:
        #     output = Matrix(input_string)

        # while inp != "exit":
        #     inp = input()
            # if inp.lower() == "exit":
            #     break
            #
            # # return value
            # if len(re.findall('=', inp)) == 0:
            #     if inp in self.variables:
            #         print("Value of \'" + inp + "\' is: \n" + str(self.variables[key]) + "\"")
            #     else:
            #         print("Variable doesnt exist")
            # # assign value
            # elif len(re.findall('=', inp)) == 1:
            #     key, rhs = [x.strip().lower() for x in inp.split('=')]
            #
            #     value = self.evaluate(rhs)
            #     self.variables[key] = value
            #
            # # inline equation

    @staticmethod
    def str_from_list(mylist, start, end):
        newlist = ""
        for i in range (start + 1, end):
            newlist += mylist[i]
        # print("my new list is: " + newlist)
        return newlist
