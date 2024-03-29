import V2.mymath as math
import re
from abc import ABC, abstractmethod
# from .Functions import Functions

class ParentEquation(ABC):
    def __init__(self, raw_input, token_list=None):
        self.raw_input = raw_input
        self.precision = 5
        self.token_list = None
        self.debug = 0
        self.value = None

        self.token_list = self.tokenize(self.raw_input)

    @abstractmethod
    def reduce(self):
        pass

    @abstractmethod
    def solve(self):
        pass

    def replace_known_variables(self, token_list, variables):
        i = 0

        while i < len(token_list):
            if type(token_list[i]) is list:
                self.replace_known_variables(token_list[i], variables)
            elif token_list[i] in variables:
                if isinstance(variables[token_list[i]], Functions):
                    raise Exception ("Cannot assign function")
                str_new_val = str(variables[token_list[i]])
                token_list[i] = self.tokenize(str_new_val)

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
                    #TODO check if i+1 is a number
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
                teststr = ParentEquation.str_from_list(split, i, j)
                cust_list = ParentEquation.tokenize(teststr)

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










"""
Circular reasoning sucks: move below into it owns file
"""






class Functions(ParentEquation):

    def __init__(self,raw_input, key, variable_list):
        super().__init__(raw_input)
        self.function_name, self.function_vars = self.isloate_key(key)

        self.check_used_variables(self.token_list, variable_list)


    def reduce(self):
        pass

    def isloate_key(self, key):
        func_name, func_variable = re.findall(r"([A-z]+)\((.*?)\)", key)[0]
        func_variable = func_variable.split(',')
        return func_name, func_variable

    def check_used_variables(self, token_list, function_var):
        for check in token_list:
            if type(check) is list:
                self.check_used_variables(check, function_var)
            elif any(x in token_list for x in function_var):
                raise Exception("Function variable already exists")
        return

    def solve(self, raw_input):
        pass

    def evaluate(self, input_variables):
        if len(input_variables) != self.function_vars:
            raise Exception("Function input variables not same as stored")

        evaluation_vars = {}
        for i in range(input_variables):
            evaluation_vars[self.function_vars[i]] = float(input_variables[i])

        eval_token_list = self.replace_known_variables(self.token_list, evaluation_vars)
        ans = self.apply_operations(eval_token_list)
        print("ans is", ans)
        return  ans


    def __str__(self):
        str1 = ""
        str1 += self.function_name + '(' + ' '.join(self.function_vars) + ') = '
        str1 += " "
        for x in self.token_list:
            if isinstance(x, str):
                str1 += x
            else:
                str1 += str(x)
            str1 += " "

        return str1

