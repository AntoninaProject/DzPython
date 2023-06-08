# Создайте двумерный массив случайного размера.
# Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.

import numpy


rows = numpy.random.randint(2, 10)
cols = numpy.random.randint(2, 10)
size = (rows, cols)
matrix = numpy.random.randint(0, 10, size)
print(matrix)

imax, jmax = numpy.divmod(matrix.argmax(), cols)
imin, jmin = numpy.divmod(matrix.argmin(), cols)
print(f"Максимальный [{imax}][{jmax}]")
print(f"Минимальный [{imin}][{jmin}]")

print(matrix.diagonal())