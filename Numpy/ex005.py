# Métodos importantes:
# ndim — retorna a dimensão do array
# shape — retorna o formato do array
# dtype — retona o tipo de dados do array
# astype — altera o tipo de dado do array
# min — retorna o menor valor do array
# max - retorna o maior valor do array
# argmin - retorna a posição do menor elemento
# argmax - retorna a posição do maior elemento
# sum - soma dos elementos do array
# mean - media dos elementos do array
# var - variancia dos elementos
# std - retorna o desvio padrão dos elementos
# sort - ordena o array (crescente)
# T - calcular transposto de uma matriz
# reshape -

import numpy as np
array = np.random.randn(10)
print(array)
print()
mtx = np.random.randn(3, 3)
print(mtx)
print()
print(array.ndim)
print(mtx.ndim)
print()
print(array.shape)
print(mtx.shape)
print()
print(array.dtype)
print()
print(array.astype('int'))
print(mtx.astype('int'))
print()
print(array.astype('bool'))
print()
array[2] = 0
print(array)
print()
print(array.astype('bool'))
print()
print(array.min())
print(array.max())
print()
print(array.argmin())
print(array.argmax())
print()
print(array.sum())
print()
print(array.mean())
print()
print(array.var())
print()
print(array.std())
print()
print(array)
print(array.sort())
print()
print(mtx)
print(mtx.T)

# Mascaras

a = np.array([1, 2, 3, 4])
print(a)
print(a[[False, True, False, True]])
print(a >= 3)
print(a[a >= 3])
print(a[a % 2 == 0])





