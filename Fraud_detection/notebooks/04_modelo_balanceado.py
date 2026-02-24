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
# Como o dataset é altamente desbalanceado, o modelo baseline apresentou dificuldade em aprender padrões da classe fraude. Para mitigar esse problema, foi aplicada uma técnica de balanceamento, permitindo que o modelo atribuísse maior importância à classe minoritária.
#%%
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline

over = SMOTE(sampling_strategy='minority')
# %%
pipeline = ImbPipeline(steps=[
    ('over', over),
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])
# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
# %%
pipeline.fit(X_train, y_train)
# %%
y_pred = pipeline.predict(X_test)
# %%
print(classification_report(y_test, y_pred))
# %%
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
# %%[markdown]
# O modelo balanceado utilizando SMOTE apresentou uma melhoria significativa no recall, conseguindo identificar com mais precisão as transações fraudulentas. O aumento do recall indica que o modelo está conseguindo detectar uma maior proporção de fraudes, o que é crucial em cenários de detecção de fraudes, onde a prioridade é minimizar os falsos negativos. No entanto, é importante monitorar o impacto no precision, pois um aumento no recall pode levar a um aumento nos falsos positivos. O próximo passo será explorar outras técnicas de balanceamento e avaliar seu impacto no desempenho do modelo.

#%%[markdown]
# O uso do SMOTE aumentou significativamente o recall da classe fraude, passando de 0.63 para 0.90, permitindo que o modelo detectasse a grande maioria das fraudes. Apesar do possível aumento de falsos positivos, o novo modelo é mais adequado ao contexto do problema, onde o custo de não detectar uma fraude é maior que o custo de uma investigação adicional.
# %%
