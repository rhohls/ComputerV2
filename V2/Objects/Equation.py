from V2.Objects.ParentEquation import ParentEquation

# out = self.tokenize(input)
# # print("tokenize list is: ", out)
# out = self.replace_known_variables(out)
# # print("replace var list is: ", out)
# result = self.apply_operations(out)


# print("final result is: ", out)
class Equation(ParentEquation):

    def solve(self):
        pass

    def __init__(self, raw_input):
        super().__init__(raw_input)

    def reduce(self):
        self.value = self.apply_operations(self.token_list)

    def __str__(self):
        st = (("%0.*f" % (self.precision, self.value)).rstrip('0').rstrip('.'))
        return st
