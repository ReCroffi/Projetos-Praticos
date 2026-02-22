# %% [markdown]
## Carregar e inspecionar os dados
#
# %%
import pandas as pd


path = '../data/raw/creditcard.csv'

df = pd.read_csv(path)
# %%
df.head()
# %%
df.shape
# %% [markdown]
#Temos um dataset com 284807 linhas e 31 colunas<br>
#Nossa variavel alvo é a Class, onde 1 é operação fraudulenta e 0 não


# %%
df['Class'].value_counts(normalize=True)

# %% [markdown] 
#Nosso dataset apresenta 99.82% de transações normais e 0.017% de fraudulentas<br>
#Não possui ID <br>
#Nossas features são anonimizadas
# %% [markdown]
## Analise da variavel alvo
#Nossa variavel alvo é a Class, ela diz se uma operação é fraudulenta(1) ou não(0).<br>
#Como vimos anteriormente apenas 0.017% das operações são fraudes, isso mostra que nosso dataset é desbalanceado
#e faria com que a previsão de não fraude fosse enviesada, mostrando uma acuracia alta mas não refletindo a realidade

# %% [markdown]
## Hipóteses iniciais
# Fraudes ocorrem em operações com alto valor<br>

# O dataset traz dados realistas, mas também é difícil <br>

# As features (V1 a V28) tem valores muito diferentes entre elas pra um mesmo registro



# %% [markdown]
## Observações
# Nosso problema consiste em determinar se uma operação é fraudulenta ou não.<br>
# É um problema complexo, tendo em vista que não temos informações das features, além do dataset ser extremamente desbalanceado.<br>
# Dessa maneira ainda não podemos usar esses dados num modelo de ML, teremos que, de alguma maneira, balancear nosso dataset<br>

# %%
