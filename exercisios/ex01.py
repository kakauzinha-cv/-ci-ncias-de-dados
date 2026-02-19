import matplotlib.pyplot as plt 

#Exercicio 01  Construa um gráfico de barras que compare a nota de popularidade de séries em 2025:

categorias= ['Stranger Things', 'It', 'Friends', 'Game of Thrones']
valores = [8.9, 2.0, 3.0, 4.0]

plt.bar(categorias, valores)
plt.show()
plt.savefig('./exercisios/ex01.png')

# Exercicio 2 Construa um gráfico de barras que compare os celulares mais vendidos em 2026:

# ele limpa o grafico criado para crias novos
plt.clf()

celulares = ['iphone17 Pro Max', 'iphone 17', 'xiaomi 17']
valores = [200000, 320000, 500000]

plt.bar(celulares, valores)
plt.show()
plt.savefig('./exercisios/ex02.png')
