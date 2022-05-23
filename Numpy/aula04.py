# Indexação e Cortes(slices) de Arrays.
import numpy as np

a = np.arange(10, 21)
print(a)

print(a[10])
print(a[-11])
print('-='*50)

b = np.random.rand(5, 5)
print(b)
print(b[0, 1])  # (Acessar) 1° indice linha 2° indice Coluna.

b[0, 1] = 10  # (Alterar).
print(b)
print('-='*50)
#Slices

a = np.arange(10, 21)
print(a)
print(a[2:5])  # Vai da posição inicial a penultima posição final informada.
print(a[:5])  # Se não especificar o incio, ele parte do  inicio do array.
print(a[2:])  # Se não especificar o final, ele vai até o fim do array.
print(a[2:9:2])  # 3° indice ref ao passo.
print(a[8:2:-1])  # Array invertido.
print('-='*50)

b = np.random.rand(5, 5)
print(b)
print('\n')
print(b[0:2, 2])
print('-='*50)



