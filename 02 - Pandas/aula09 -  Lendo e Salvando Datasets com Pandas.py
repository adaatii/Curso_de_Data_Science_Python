import pandas as pd
import numpy as np

# Carregando arquivo csv
df = pd.read_csv('dataset/titanic_train.csv')
print(df.head())  # Por padrão o '.head' traz as 5 primeiras linhas porem é possivel setar a quantidade de linhas '.head(7)' - retorna 7 linhas
print('-='*20)
print(df.tail())  # Por padrão retorna as 5 últimas linhas, aceita parametros como o '.head'
print('-='*20)




