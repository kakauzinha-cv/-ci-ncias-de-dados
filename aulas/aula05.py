import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./dados/dados.csv')

#exibe as primeiras linhas do meu dataFrame
print(df.head())

#Grafico de boxplot
plt.boxplot(df['nota'])
plt.title('Boxplot das notas')
plt.ylabel('Notas')
plt.show()
plt.savefig('aula05-Boxplot')