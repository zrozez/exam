'''
Перед вами 10 программ. 
Ответьте какими типами данных будет обладать переменная x, в конце каждой программы:
'''
#1
x = str(int(float(5))) #строка
#2
x = 'aa' == 'AA' #Boolean
#3
x = {i: i**2 for i in range(5)} #словарь
#4
x = set(list((5, 6, 7))) #множество
#5
a = {1: 1, 2: 4, 3: 9}
x = a.get(4) #None
#6
x = [].append('j') #список
#7
for i in range(10):
		if i < 5:
				x = 'hello'
		else:
				x = 5 #integer
#8
x = input('Enter and integer: ') #ввод от пользователя
#9
a = 5
b = [1, 3, 5, ]
x = 'x'
a, b, x = x, a, b #список
#10
def func(x, y=5):
		return x + y
x = func('Jaguar ', 'hunter') #строка