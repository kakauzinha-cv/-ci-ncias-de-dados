import pandas as pd

#Criação do DataFrame
df = pd.DataFrame({
    "idade": [20, 22, 20, 23, 24]
})

#descreve dados estatisticos do dataframe
print(df['idade'].describe())

print('Média: ' + str(df['idade'].mean()))
print('Médiana: ' + str(df['idade'].median()))
print('Moda: ' + str(df['idade'].mode().iloc[0]))