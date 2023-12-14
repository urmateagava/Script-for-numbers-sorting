import pandas as pd

df1 = pd.read_excel('1.xlsx', skiprows=3, dtype='object')
df2 = pd.read_excel('2.xlsx', skiprows=3, dtype='object')


vtd = df1['Телефон клиента'].values
flt = ~df2['Телефон клиента'].isin(vtd)
df3 = df2.loc[flt, :]

df3.to_excel('result.xlsx')


