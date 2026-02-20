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



#3) Identifique na turma qual é o time de cada um e construa um gráfico de barras para mostrar a popularidade cada time.
#Grêmio: 3; Flamengo: 2; Palmeiras: 1; internacional:2; Vasco: 1
plt.clf()

times = [' Grẽmio' , 'Flamengo', 'Palmeiras', 'internacional', 'Vasco']
torcedores = [3, 2, 1, 2, 1]
cores = ['#FFFFFF', '#FFD700', ' #006437', '#E30613', '#000000']

plt.bar(times, torcedores, color= cores)
plt.xlabel('Times do campeonato brasieiro')
plt.ylabel('N° de torcedores')
plt.show()
plt.savefig('./exercisios/ex03.png')
