'''
1-ая должна принимать список. 
Добавлять в этот список элементы 'Element', 'start', 'finish'. 
Все элементы первоначального списка должны находиться между элементами 'start', 'finish'
print(func(['hello', 5, 'John', ]))
['Element', 'start', 'hello', 5, 'John', 'finish']
'''

def func1(lst):
    lst.insert(0, 'Element')
    lst.insert(1, 'start')
    lst.append('finish')
    return lst
print(func1(['hello', 5 , 'John']))

'''
2-ая должна принимать производное количество аргументов и возвращать словарь, где ключами являются принятые аргументы, 
а значениями числа от 1 до количества принятых аргументов
print(func('x', 5, 'John'))
{'x':1, 5:2, 'John':3}
'''
def func2(*args):
    k = []
    k.extend(args)
    count = len(k) + 1
    diction = {}
    j = 1
    while j < count:
        for z in k:
            diction[z] = j
            j += 1
    return diction
print(func2('x', 5, 'John'))

'''
3-я должна принять кортеж. Превращать этот кортеж в список и, используя анономные функции, выдавать нам на выход 2 списка. 
1-ый список должен состоять из всех чётных чисел введённого кортежа. 
2-ой со всеми элементами введённого кортежа возведёнными в квадратную степень
'''
def func3(kort):
    lst = list(kort)
    lst1 = list(filter(lambda x: x%2 == 0, lst))
    lst2 = []
    for j in lst:
        k = lambda x: x**2
        kk = k(j)
        lst2.append(kk)
    return lst1, lst2
print(func3((1, 2, 3, 4, 5)))