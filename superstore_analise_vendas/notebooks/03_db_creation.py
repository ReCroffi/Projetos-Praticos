#%%
import sqlalchemy
import pandas as pd 

df = pd.read_csv('../data/processed/superstore_clean.csv')

engine = sqlalchemy.create_engine('sqlite:///../data/processed/superstore.db')
df.to_sql('superstore', engine, if_exists='replace', index=False)
# %%
