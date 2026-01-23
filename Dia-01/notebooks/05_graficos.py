#%%[markdown]
# Importando pacotes
#%% 
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
##%%
df = pd.read_csv('../data/processed/superstore_clean.csv')
df.head()

# %%
vendas_ano = df.groupby(['order_year'])[['sales']].sum()
vendas_ano
# %%
plt.figure(figsize= (10,6))
plt.title('Vendas por Ano(faturamento)')
plt.ylabel('Faturamento (USD)')
plt.xlabel('Ano')
sns.barplot(x= vendas_ano.index, y=vendas_ano['sales'])
plt.savefig('../outputs/faturamento_por_ano.png',dpi=300, bbox_inches='tight')
plt.show()
# %%[markdown]
# Aqui pode-se ver um aumento das vendas entre 2015 e 2018
# quanto a 2019 parece ter dados faltantes para justificar essa queda brusca nas vendas
# %%
vendas_regiao = df.groupby(['region'])[['sales']].sum()
vendas_regiao
# %%
plt.figure(figsize=(10,6))
plt.title('Vendas por Região')
plt.ylabel('Faturamento (USD)')
plt.xlabel('Região')
sns.barplot(x=vendas_regiao.index, y=vendas_regiao['sales'])
plt.savefig('../outputs/vendas_por_regiao.png',dpi=300, bbox_inches='tight')
plt.show()
# %%[markdown]
# No grafico acima podemos ver que as regioes East e West são as que
# mais compram na loja. Com a regiao South sendo a que menos compra.
# Uma ação de marketing na regiao sul pode atrair mais compradores

# %%
ticket_medio_mes = df.groupby(['order_month'])[['sales']].mean()
ticket_medio_mes
# %%
plt.figure(figsize=(10,6))
plt.title('Ticket médio mensal')
plt.ylabel('Valor médio de venda por registro (USD) ')
plt.xlabel('Mes')
sns.barplot(x=ticket_medio_mes.index, y=ticket_medio_mes['sales'])
plt.show()
# %%[markdown]
# Aqui podemos ver que existe um leve aumento no ticket médio mensal no ultimo trimestre do ano, periodo de festa.
# e um pico de venda em março, pode ser reflexo de alguns feriados estaduais como St.patricks day
# ou spring break

# %%
vendas_categoria = df.groupby(['category'])[['sales']].sum()
# %%
plt.figure(figsize=(10,6))
plt.title('Vendas por Categoria de Produto')
plt.ylabel('Valor de venda por categoria (USD) ')
plt.xlabel('Mes')
sns.barplot(x=vendas_categoria.index, y=vendas_categoria['sales'])
plt.savefig('../outputs/vendas_por_categoria.png',dpi=300, bbox_inches='tight')
plt.show()
# %%
