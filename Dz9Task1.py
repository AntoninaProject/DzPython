# Дан список элементов.
# Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

import numpy

size = numpy.random.randint(5, 20)
array = numpy.random.randint(0, 10, size)
print(array)
nums, counts = numpy.unique(ar=array, return_counts=True)
unique_amt = numpy.count_nonzero(counts == 1)
print(f"Уникальных элементов в массиве: {unique_amt}")