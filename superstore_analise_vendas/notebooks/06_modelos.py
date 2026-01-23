#%%[markdown]
# Aqui veremos se conseguimos prever uma venda de alto valor baseado nas informações
# que temos disponiveis em nosso dataset

# %%[markdown]
#Importando pacotes
# %%
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
from matplotlib import pyplot as plt

# %%
df = pd.read_csv('../data/processed/superstore_clean.csv')
df.head()
# %%
df.describe()
# %%[markdown]
# Criando nosso target, baseado na nossa premissa de prever vendas de alto valor
#%%
df['high_sales'] = df['sales'] > 210.6

# %%[markdown]
# Separando features e targets e transformando variaveis categoricas com one-hot enconding

#%%
features_num = [
    'shipping_delay',
    'order_year',
    'order_month'
]

features_num = [
    'order_year',
    'order_month'
]

features_cat = [
    'category',
    'sub_category',
    'region',
    'segment',
    'ship_mode'
]

X = df[features_num + features_cat]

target = 'high_sales'

y = df[target]
#%%
preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', features_num),
        ('cat', OneHotEncoder(handle_unknown='ignore'), features_cat)
    ]
)

# %%[markdown]
# Split treino test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

#%%[markdown]
# Como high_sales é desbalanceado os dados tiveram que ser
# dividios em conjunto treino teste com estratificação para preservar a proporção do target
#%%
model1 = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

pipeline1 = Pipeline(
    steps=[
        ('preprocess', preprocessor),
        ('model', model1)
    ]
)

# %%[markdown]
# Treinando os Modelos (LogistRegression e RandomForestClassifier)

#%%
pipeline1.fit(X_train, y_train)

y_pred1 = pipeline1.predict(X_test)


# %%
model2 = LogisticRegression(
    max_iter= 3000,
    solver='lbfgs',
    random_state=42
)

pipeline2 = Pipeline(
    steps=[
        ('preprocess', preprocessor),
        ('model', model2)
    ]
)
#%%
pipeline2.fit(X_train, y_train)

y_pred2 = pipeline2.predict(X_test)
# %%[markdown]
#Avaliação dos modelos
#%%
from sklearn.metrics import accuracy_score, confusion_matrix,recall_score,classification_report
# %%
print('Accuracy Random Forest Classifier:', accuracy_score(y_test, y_pred1))
print('Accuracy Logistic Regression:', accuracy_score(y_test, y_pred2))


print('Classification report RFC:\n', classification_report(y_test, y_pred1))

print('Classification report LR:\n',classification_report(y_test, y_pred2))
# %%
sns.heatmap(confusion_matrix(y_test,y_pred1), annot= True, fmt='d')
plt.title('Confusion Matrix - Random Forest Classifier')
plt.show()
# %%
sns.heatmap(confusion_matrix(y_test,y_pred2), annot= True, fmt='d')
plt.title('Confusion Matrix - Logistic Regression')
plt.show()
# %%[markdown]
# Podemos ver que ambos modelos se sairam bem em predizer o target, com o modelo de Logistic Regression
# se saindo um pouco melhor (Recall 0.91) e na matriz de confusão onde gerou menos falsos positivos e falso negativos em comparação ao Random Forest Classifier
# 
# %%
