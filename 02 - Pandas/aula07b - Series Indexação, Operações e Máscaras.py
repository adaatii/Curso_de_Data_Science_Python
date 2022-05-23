import numpy as np
import pandas as pd

# Series
d = {'Python': 10, 'JavaScript': 9, 'Matlab': 7}

series = pd.Series(d)

print(series)


# Indexação
# Primeiro parametro saõ os dados / segundo parametro o indice
s = pd.Series(data=np.random.randint(1, 5, 10), index='A B C D E F G H I J'.split())
print(s)

# Podesse acessar tanto pelo incice numérico e o atribuido
print(s[0])
print(s['A'])
print(s[2:4])
print(s['C':'D'])
print(series['Python':'JavaScript'])

# Operações

s1 = pd.Series(data=np.random.randint(1, 100, 3), index='Facebook Instagram Youtube'.split())
s2 = pd.Series(data=np.random.randint(1, 100, 3), index='Zoom Instagram Youtube'.split())
print('-='*20)
print(s1)
print('-='*20)
print(s2)
print('-='*20)
print(s1+s2)  # O retorno de Facebook e Zoom será NaN(Not a Number) tenta somar um número com um campo vazio.
print('-='*20)
# Máscaras

print(s[s > 2])  # retorna os valores da Series maiores que 2
print('-='*20)
print(s[s > 2].index)  # retorna os indices onde o conteudo é maior que 2.

