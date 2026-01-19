#%%[mardown]
# Análise Exploratória — Superstore Sales
# %%
#Importando pacotes
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import datetime as dt

path = '../data/raw/train.csv'

df = pd.read_csv(path)

# %%
# Primeiras visualizacoes do dataset
df.head()
# %%
df.info()
# %%
df.describe()
# %%
df.shape
# %%[markdown]
#aparentemente temos as colunas OrderDare e Shipdate como string, 10 das 18 colunas são categoricas

# %%[markdown]
#Verificar nulos
df.isnull().count(axis='columns')
#não temos nulos
# %%[markdown]
#Verificar duplicados
df.duplicated()
#não há nulos
# %%[markdown]
#Primeiros Gráficos
#%%
plt.figure(figsize=(10,6))
plt.title('Vendas Por Segmento')
sns.countplot(x= df['Segment'])
plt.show
#%%[markdown]
# Podemos ver que a venda pro consumidor final é a maior parte das vendas
# %%
plt.figure(figsize=(10,6))
sns.catplot(x= df['Sub-Category'], y= df['Sales'], kind='bar')
plt.xticks(rotation= 75)
plt.show
# %%[markdown]
# Temos aqui o gráfico Vendas para cadas sub-categoria, vemos que algumas sub-categorias se destacam no numero de vendas (Copiers e Machines)
# enquanto outras como Labels e Fasteners possuem pouquissimas vendas
# %%
df['Order Date'] = pd.to_datetime(df['Order Date'],format= '%d/%m/%Y')


# %%


df['year'] = pd.DatetimeIndex(df['Order Date']).year
df['month'] = pd.DatetimeIndex(df['Order Date']).month

# %%
plt.figure(figsize=(10,6))
sns.barplot(df.groupby('month').size())
plt.xticks(rotation= 75)
plt.show

# %%[markdown]
# Temos aqui numero de vendas para cada mes, aqui vemos um pico de vendas em 
# novembro e dezembro, novembro temos a black friday, e dezembro é o periodo de festas de fim de ano
# %%
