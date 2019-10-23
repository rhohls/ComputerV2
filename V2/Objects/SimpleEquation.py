import V2.mymath as math
import re
from abc import ABC, abstractmethod


class SimpleEquation(ABC):
    def __init__(self,input_string, token_list=None):
        self.input_string = input_string
        self.precision = 5

    @abstractmethod
    def reduce(self):
        pass

    def replace_known_variables(self, variables):
        i = 0

        while i < len(self.token_list):
            if type(self.token_list[i]) is list:
                self.replace_known_variables(self.token_list[i])
            elif self.token_list[i] in variables:
                self.token_list[i] = variables[self.token_list[i]]

            i += 1
        return self.token_list

    def mini_operation(self, equation, list_opperands):
        i = 0
        new_equation = []

        while i < len(equation):
            if equation[i] in list_opperands:
                # print("opperand", equation[i])
                # print("equation", equation)
                # print("new equation", new_equation, " len ", len(new_equation))
                #TODO handle bad syntax multiplication vs negative numbers
                if len(new_equation) < 1:
                    value = math.operation(0, equation[i + 1], equation[i])
                    new_equation.append(value)
                # if len(new_equation) >= 1 and i > 1:
                else:
                    #value from opperation = previously calc values [op] next value
                    #TODO check i+1 is a number
                    value = math.operation(new_equation[-1], equation[i + 1], equation[i])
                    new_equation[-1] = value
                i += 1
            else:
                new_equation.append(equation[i])
            i += 1

        return new_equation

    def apply_operations(self, tokenized_list):
        i = 0
        # () brackets
        while i < len(tokenized_list):
            if type(tokenized_list[i]) is list:
                tokenized_list[i] = self.apply_operations(tokenized_list[i])
            i += 1
        if self.debug :  print("post brackets", tokenized_list)

        tokenized_list = self.mini_operation(tokenized_list, ['^'])
        if self.debug : print("post power", tokenized_list)

        tokenized_list = self.mini_operation(tokenized_list, ['*', '/', '%'])
        if self.debug :  print("post mult", tokenized_list)

        tokenized_list = self.mini_operation(tokenized_list, ['+', '-'])
        if self.debug : print("post add", tokenized_list)

        if len(tokenized_list) > 1:
            raise Exception ("This should not be happening")
        return tokenized_list[0]

    @staticmethod
    def tokenize(input_string):
        split = re.split(r'([+,\-,\/,*,%,^,**,(,)])', input_string)

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
                teststr = SimpleEquation.str_from_list(split, i, j)
                cust_list = SimpleEquation.tokenize(teststr)

                new_list.append(cust_list)
                i = j

            #number and variable
            elif re.findall('([0-9]+)([A-z]+)',split[i]):
                result = re.findall('([0-9]+)([A-z]+)', split[i])
                # print("find: ", result)
                if len(result) != 1 or len(result[0]) != 2:
                    raise Exception("issue parsing and splitting variable")
                number, variable = result[0][0], result[0][1]
                number = float(number)
                new_list.extend([number, '*', variable])

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

    @staticmethod
    def str_from_list(mylist, start, end):
        newlist = ""
        for i in range (start + 1, end):
            newlist += mylist[i]
        # print("my new list is: " + newlist)
        return newlist