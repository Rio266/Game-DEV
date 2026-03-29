matrix = [[1, 2], [3, 4]]
print(matrix[0][1])

print(len(matrix))
print(len(matrix[0]))

matrix = []
rows = int(input("What is the number of rows?"))
columns = int(input("What is the number of columns?"))
for i in range(rows):
    brackets = []
    for j in range(columns):
        elements = input("What elements would you like to add?")
        brackets.append(elements)
    matrix.append(brackets)
print(matrix)

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
resultmatrix = [[0, 0], [0, 0]]
resultmatrix1 = [[0, 0], [0, 0]]
resultmatrix2 = [[0, 0], [0, 0]]
resultmatrix3 = [[0, 0], [0, 0]]

for k in range(2):
    for l in range(2):
        resultmatrix[k][l] = matrix1[k][l] + matrix2[k][l]
        resultmatrix1[k][l] = matrix1[k][l] - matrix2[k][l]
        resultmatrix2[k][l] = matrix1[k][l] * matrix2[k][l]
        resultmatrix3[k][l] = matrix1[k][l] / matrix2[k][l]
print(resultmatrix)
print(resultmatrix1)
print(resultmatrix2)
print(resultmatrix3)