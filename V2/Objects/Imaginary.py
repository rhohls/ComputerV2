from V2.Objects.ParentEquation import ParentEquation


class Imaginary(ParentEquation):
    def __init__(self, raw_input):
        super().__init__(raw_input)
        self.real_token = None
        self.imagine_token = None

    def reduce(self):
        i = 0

        print (self.token_list)

        while i < len(self.token_list):


            i += 1



        return token_list

    def __str__(self):
        return "Not Implimented"
        # return  str(self.real) + " " + str(self.imaginary) + "i"


