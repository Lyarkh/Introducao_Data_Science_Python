import matplotlib.pyplot as plt 
from random import randrange

x = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
     'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
y = [randrange(10, 1000) for i in range(12)]

plt.plot(x, y, marker ='o')
plt.xlabel('Meses')
plt.ylabel('Gastos')
plt.title('Teste Plot')
plt.show()