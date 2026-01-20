#%%[markdown]
## Dia 2 - Checklist
# Converter nome colunas para snake_case;
# Remover espaços e caracteres especiais;
# Usar nomes semanticos;

# %%[markdown]
# Importando pacotes e lendo o dataset
# %%
import pandas as pd
import numpy as np

path = '../data/raw/train.csv'

df = pd.read_csv(path)

df

#%%[markdown]
# Padronizando o nome das colunas
# %%
columns_new_names = {'Row ID': 'row_id', 'Order ID':'order_id','Order Date':'order_date', 'Ship Date': 'ship_date', 'Ship Mode': 'ship_mode','Customer ID':'custumer_id', 'Customer Name': 'customer_name', 'Segment': 'segment', 'Country': 'country', 'City': 'city', 'State': 'state', 'Postal Code': 'postal_code', 'Region': 'region', 'Product ID': 'product_id', 'Category': 'category', 'Sub-Category': 'sub_category', 'Product Name': 'product_name', 'Sales': 'sales'}
df.rename(columns= columns_new_names, inplace= True)
df
# %%[markdown]
# Ajuste de tipos e adição de novas features 
# %%
columns_date = ['order_date', 'ship_date']
for columns in columns_date:
    df[columns] = pd.to_datetime(df[columns],format= '%d/%m/%Y')
    df['order_year'] = pd.DatetimeIndex(df[columns]).year
    df['order_month'] = pd.DatetimeIndex(df[columns]).month

df['shipping_delay'] = df['ship_date'] - df['order_date']
df['sales_log'] = np.log1p(df['sales'])
df
# %%[markdown]
# O dataset não traz informações sobre custo ou profit de cada venda, por isso não foram criadas metricas de margem para levar a inferencias erroneas

# As colunas order_date e ship_date foram convertidas para o formato datetime
# separamos também o ano e o mes de cada venda e fizemos a coluna shipping_delay, que mostra o timedelta entre a compra e a postagem
# %%[markdown]
# Também criamos a coluna sales_log, que é uma maneira de reduzir as assimetrias da distribuição e melhorar os modelos estatisticos
# %%
df.to_csv('../data/processed/superstore_clean.csv')
# %%
