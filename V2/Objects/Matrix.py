from V2.Objects.ParentEquation import ParentEquation


class Matrix(ParentEquation):

#cross_product : MxN * NxP = MxP



    def __init__(self, input_string):
        self.matrix = []
        self.size = (0, 0)

        raw_rows = input_string.split(";")

        for row in raw_rows:
            row_list = []
            for number in row:
                num = self.evaluate(number)
                if num:
                    row_list.append(num)

            self.matrix.append(row_list)

    def __str__(self):
        mystr = str(self.matrix)
        mystr = mystr.replace("],", "]\n")
        mystr = mystr.replace(",", " ,")

        mystr = mystr.replace("]]", "]")
        mystr = mystr.replace("[[", "[ ")

        mystr = mystr.replace(" [", "[ ")
        mystr = mystr.replace("]", " ]")
        #
        #
        return mystr

    #call computer evaluate function
    @staticmethod
    def evaluate(string_number):
        if string_number.isdigit():
            return int(string_number)
        else:
            return None

