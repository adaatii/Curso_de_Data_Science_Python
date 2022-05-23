# Operações com Arrays.

# Com escalares.

import numpy as np

np.random.seed(32)

a1 = np.random.randint(1, 20, 8)

print(a1 - 2)  # Subtrai 2 de todos os elementos do array

# Entre arrays

a2 = np.random.randint(1, 100, 8)
print(a1)
print(a2)
print(a1 + a2)  # Para operações entre arrays, eles devem ter o m esmo shape
print(a1 * a2)  # Multiplica elemnto por elemento

# (3x2)x(2x3) = (3x3)
m1 = np.random.randint(1, 10, (3, 2))
print(m1)

m2 = np.random.randint(1, 10, (2, 3))
print(m2)

print(m1.dot(m2))

m3 = np.ones((3, 2))
m4 = np.ones((2, 3))

print(m3.dot(m4))

# Comparações

a1 = np.array([1, 2, 2, 1])
a2 = np.array([3, 2, 3, 1])

print(a1 == a2)  # Compara elemento por elemento
print(np.array_equal(a1, a2))  # Compara o array inteiro
