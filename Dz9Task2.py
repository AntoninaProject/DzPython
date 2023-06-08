import numpy
# Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.
rows = 5
cols = 5
size = (rows, cols)
matrix = numpy.random.randint(0, 10, size)

# matrix[rows - 1] = matrix[0]

print("Матрица:\n", matrix, sep="", end="\n\n")

corrcoefs = numpy.corrcoef(matrix)
print("Corrcoefs:\n", corrcoefs, sep="", end="\n\n")

amt1 = numpy.count_nonzero(corrcoefs > 0.999999999999999)
if amt1 > rows:
    print("Есть одинаковые строки")
else:
    print("Нет одинаковых строк")