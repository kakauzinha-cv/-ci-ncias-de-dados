import matplotlib.pyplot as plt
 

meses= ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
vendas = [200, 300 , 340, 305, 360, 400]

#gráficos de linhas
plt.plot(meses, vendas, color= 'yellow') 
plt.title('vendas no Primeiro semestre')

plt.xlabel('Meses')
plt.ylabel('Vendas')

plt.show()
plt.savefig ('aula03.png')