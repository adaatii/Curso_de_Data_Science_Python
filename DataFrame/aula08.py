# DataFrame Criação e Indexação

import pandas as pd
import numpy as np

dados = np.array([[72, 180, 26],
                  [80, 170, 19],
                  [60, 165, 15]])

df = pd.DataFrame(data=dados, columns=['PESO', 'ALTURA', 'IDADE'])
print(df)

# Indexação
print('-='*20)
print(df['ALTURA'])  # Acessa a coluna
print('-='*20)
print(df.loc[0])  # Acessa a linha
print('-='*20)
print(df['ALTURA'][1])  # Acessa uma posição específica
print('-='*20)
print(df[['PESO', 'IDADE']])
print('-='*20)
print(df.iloc[2][1])  # acessa uma posição específica pelos indices



