class Matrix:
    def __init__(self, matrix_string):
        if type(matrix_string) != str:
            raise TypeError("incorrect argument type for: ", matrix_string )
        self.matrix = []
        self.matrix = self.make_matrix(matrix_string)

    def row(self, index):
        if index == 0:
            return []
        if index - 1 >= len(self.matrix):
            return []
        return self.matrix[index - 1]

    def column(self, index):
        ret = []
        for i in range(len(self.matrix)):
            ret.append(self.matrix[i][index-1])
        return ret

    def make_matrix(self, string):
        if len(string) == 0:
            return []
        string = string.split(' ')
        matrix = []
        i = 0
        carry = None
        for j in range(len(string)):
            if i > len(matrix) - 1:
                matrix.append([])
            if carry:
                matrix[i].append(int(carry))
                carry = None
            if string[j] != string[j].split()[0]:
                matrix[i].append(int(string[j].split()[0]))
                carry = string[j].split()[1]
                i += 1
            else:
                matrix[i].append(int(string[j]))
        return matrix

if __name__ == "__main__":
    m = Matrix('1 2\n3 4')
    print(m.matrix)
