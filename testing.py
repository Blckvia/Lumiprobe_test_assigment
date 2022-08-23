#1. Напишите функцию, которая на вход принимает строку, состоящую из строчных и заглавных латинских символов, 
# а возвращает кортеж из двух элементов: символа, который встречается в строке чаще всего (без учета регистра!), 
# и числа вхождений этого символа в строку. Если таких символов несколько, функция должна вернуть любой из них. 
# Например, для строки "aaaAAAbc" результатом работы функции будет ('a', 6).

from re import X


def str_func(some_str):
    d ={}
    some_str = some_str.lower()
    for i in some_str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    max_value = max(d.values())
          
    return {k: v for k, v in d.items() if v == max_value}
    
#  print(str_func("AAAAaaaabbbb")) # проверка

#2. Напишите функцию, которая на вход принимает единственное целое число N, 
# а возвращает целый квадратный корень из этого числа, если такой существует, 
# или None, если такого корня нет. Нельзя использовать функцию sqrt() из модуля 
# math для извлечения квадратного корня.

def sqrt_func(number):
    a = number
    while (a * a > number):
        a = (a + number/a) / 2
    if a == int(a):
        return int(a)
    else:
        return None    
    
print(sqrt_func(3)) # проверка

#3. Напишите функцию, которая принимает на вход строку, состояющую из символов '(' и ')', 
# задающих скобочную последовательность, и возвращает True, если последовательность корректна, иначе False.

def isValid(s):
    d = {'(': ')'}
    stack = []
    if len(s) % 2 != 0:
        return False
    for i in s:
        if i in d:
            stack.append(i)
        else:
            if (len(stack) and d[stack[-1]] == i):
                del stack[-1]
            else:
                return False
            
    return stack == []

print(isValid('()()')) # проверка
print(isValid('()((')) # проверка
