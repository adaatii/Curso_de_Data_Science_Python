# Arrays multidimensionais

# Construção manual de arrays

import numpy as np

b = np.array([[0, 1, 2], [3, 4, 5]])
print(b)
print(b.ndim)  # Retorna da dimenção do array
print(b.shape)  # Retorna o formato do array
print(len(b))
print('-='*50)
# Criação utilizando funções
# Cria array com tanho desejado de forma automatica
# Primeiro parametro inicial, segundo é o final, terceiro é o intervalo(passo)
# O final não inclui o último número(exemplo: para ir de 0 a 100, necessario declarar 0, 101)
c = np.arange(0, 101, 2)
print(c)
print('-='*50)
# se colocar só um parametro ele começa em 0 e vai até o número informado com passo de 1
c = np.arange(10)
print(c)
print('-='*50)
# permite que crie um array uniformemente espaçado,
# permite definir quantos elementos quer em determinado intervalo.
d = np.linspace(1, 10, 20)
print(d)
print('-='*50)
# Não incliu o ultimo elemento (endpoint=False)
d = np.linspace(1, 10, 13, endpoint=False)
print(d)
print('-='*50)

# Arrays Comuns

e = np.ones(10)
print(e)
print('-='*50)
# Usa o () Shape para definir as linhas e colunas da matriz
e = np.ones((5, 5))
print(e)
print('-='*50)
# Matriz de zeros
e = np.zeros((5, 5))
print(e)
print('-='*50)
f = np.random.rand(10, 3)
print(f)
print('-='*50)
# Matriz identidade
d = np.eye(3)
print(d)
print('-='*50)
# Matriz diagonal
e = np.diag(np.array([1, 2, 3, 4]))
print(e)
print('-='*50)

