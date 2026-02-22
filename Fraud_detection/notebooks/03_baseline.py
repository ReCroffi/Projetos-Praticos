



#%%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
path = '../data/raw/creditcard.csv'

df = pd.read_csv(path)
# %%
features = ['Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount']
target = ['Class']

X = df[features]
y = df[target]

#%%[markdown]
# Logistic Regression foi utilizada como baseline por ser um modelo simples, interpretável e amplamente utilizado como referência inicial em problemas de classificação.
# %%
def split(X, y, test_size=0.2, random_state=42, stratify=y):
    return train_test_split(X, y ,test_size=test_size, random_state=random_state, stratify=stratify)

#%%[markdown]
# O dataset apresenta forte desbalanceamento entre as classes, o que impacta diretamente a capacidade do modelo em aprender padrões da classe minoritária.
# %%
X_train, X_test, y_train, y_test = split(X, y)

# %%
pipeline = Pipeline(steps= [('scaler', StandardScaler()),('model', LogisticRegression())])
pipeline.fit(X_train,y_train)
# %%
pipeline.predict(X_test)
# %%[markdown]
# O modelo foi utilizado apenas para validar o fluxo de pré-processamento, sem foco em desempenho ou otimização. O próximo passo será avaliar o desempenho do modelo e explorar técnicas para lidar com o desbalanceamento dos dados, como mencionado anteriormente.

# %%
print(classification_report(y_test, pipeline.predict(X_test)))

# %%[markdown]  
#O modelo baseline apresentou bom desempenho inicial, conseguindo identificar 63% das fraudes, com precision de 83%. Apesar disso, ainda há uma quantidade significativa de fraudes não detectadas, indicando a necessidade de técnicas adicionais para lidar com o desbalanceamento e melhorar o recall.

# %%
sns.heatmap(confusion_matrix(y_test, pipeline.predict(X_test)), annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
# %%[markdown]
# O modelo baseline demonstrou capacidade inicial de identificar fraudes, mas apresentou limitações na detecção completa da classe minoritária. Na próxima etapa, serão aplicadas técnicas específicas para lidar com o desbalanceamento e melhorar o desempenho do modelo.

