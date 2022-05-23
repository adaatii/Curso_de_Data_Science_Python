# Casos Confirmadoas de Covid

import pandas as pd
from urllib.request import urlretrieve
import matplotlib.pyplot as plt


url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'  # Url do .csv
urlretrieve(url, 'global_cases_covid19')

df_covid = pd.read_csv('global_cases_covid19')

print(df_covid.head())

df_covid.drop(['Lat', 'Long'], axis=1, inplace=True)  # .drop retira dados ( Neste caso latitude e longitude)

print(df_covid)
# .groupby faz o agrupamento em função de algo (Neste caso em função do País e Região)
# .sum logo em seguida fara a soma dos valores nesse agrupamento
df_country = df_covid.groupby('Country/Region').sum()

print(df_country.loc['Brazil'])  # .loc realiza a localização do termo e retorna a linha com os dados.

date = df_country.loc['Brazil'].index
cases = df_country.loc['Brazil'].values

print(date)
print(cases)

s_brazil = df_country.loc['Brazil']

s_brazil = s_brazil[s_brazil > 0]

tam = len(s_brazil)
plt.figure(figsize=(14, 8))
plt.xticks(rotation=60)
plt.bar(s_brazil.index[tam-60:], s_brazil.values[tam-60:])
plt.title('Total de casos confirmados COVID19 Brasil')

plt.show()  # Mostra o gráfico


