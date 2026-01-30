#%%[markdown]
## Pré-processamento e preparação
# - Separação treino/test<br>
# - Escala das variáveis<br>
# - Desbalanceamento<br>
# %%[markdown]
## Parte conceitual
# Como visto anteriormente, nosso alvo é a coluna Class.<br>
# Nossas features serão Time, que é uma diferença de tempo entre a primeira transação do dataset com a transação atual, sem segundos. 
#Passando por V1 até v28 e por fim Amount<br>
#Como o dataset é extremamente desbalanceado, possivelmente teremos que estratificar.

# %%[markdown]
## Split Treino/teste
# Quanto a proporção do split, será usada a 80/20. O grande volume de dados garante que
# as amostras terão proporções equivalentes dos dados.<br>
# Deve-se estratificar para garantir que, se o dataset possui 0.17% de fraudes, tanto o treino quanto o teste fiquem com 0.17% de fraudes.
# %%[markdown]
## Desbalanceamento
# Tem-se algumas opções para tratar o desbalanceamento:<br>
# - Class weights
# - Undersampling
# - Oversampling
# - Threshold Tuning
# <br>
# Cada uma dessas tem pontos negativos, como o aumento de falsos positivos (class weight), vazamento de dados entre outros.

# %%[markdown]
## Preparação prática

# %%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
path = '../data/raw/creditcard.csv'

df = pd.read_csv(path)
# %%
features = ['Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount']
target = ['Class']

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size=0.2, random_state=42, stratify=y)
# %%
pipeline = Pipeline(steps= [('scaler', StandardScaler()),('model', LogisticRegression())])
pipeline.fit(X_train,y_train)

# %%[markdown]
# Neste estágio, o modelo foi utilizado apenas como parte do pipeline para validar o fluxo de pré-processamento, sem foco em desempenho ou otimização.
# %%
