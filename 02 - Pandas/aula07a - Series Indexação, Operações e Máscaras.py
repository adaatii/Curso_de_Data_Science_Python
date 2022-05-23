import numpy as np
import pandas as pd

# Series é como uma coluna ou uma linha do DataFrame (tabela).
# Não é igual ao NUmpy array.

steps = pd.Series([4216, 3867, 7934, 4180, 5344])

print(steps)
print(type(steps))

print(steps.values)  # Retorna os valores da Series
print(steps.index)  # Retorna o indice da Series

steps = pd.Series(data=[4216, 3867, 7934, 4180, 5344], index=['seg', 'ter', 'quar', 'qui', 'sex'])

print(steps)
print(steps.index)
print(steps.min())
print(steps.max())
print(steps.mean())
print(steps.sum())
print(steps.describe())

# Estrutura Flexivel

print(steps*2)
print(np.sqrt(steps))


