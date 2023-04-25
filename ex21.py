# Word search
class Grid(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __wordSearchRight(self, index, word):
        for i in range(len(self.matrix[index])):
            if word[i] != self.matrix[index][i]:
                return False
        return True

    def __wordSearchBottom(self, index, word):
        for i in range(len(self.matrix)):
            if word[i] != self.matrix[i][index]:
                return False
        return True

    def word_search(self, word):   # iterate through right and bottom word by using previous helper methods
        for i in range(len(self.matrix)):
            if self.__wordSearchRight(i, word):
                return True

        for i in range(len(self.matrix[0])):
            if self.__wordSearchBottom(i, word):
                return True

        return False


matrix1 = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]
print(Grid(matrix1).word_search('FOAM'))
print(Grid(matrix1).word_search('AGF'))
