from V2.Objects.SimpleEquation import SimpleEquation

# out = self.tokenize(input)
# # print("tokenize list is: ", out)
# out = self.replace_known_variables(out)
# # print("replace var list is: ", out)
# result = self.apply_operations(out)


# print("final result is: ", out)
class Equation(SimpleEquation):

    def __init__(self, raw_input):
        self.raw_input = raw_input
        self.tokenize = None
        self.value = None

    def reduce(self):
        self.tokenize = self.tokenize(self.raw_input)
        self.value = self.apply_operations(self.tokenize)

    def __str__(self):
        st = (("%0.*f" % (self.precision, self.value)).rstrip('0').rstrip('.'))
        return
