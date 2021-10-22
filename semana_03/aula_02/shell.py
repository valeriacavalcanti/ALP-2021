Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> idade = 15
>>> idade
15
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'idade']
>>> idade = input()
200
>>> idade
'200'
>>> type(idade)
<class 'str'>
>>> idade/2
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    idade/2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> idade = int(idade)
>>> idade
200
>>> type(idade)
<class 'int'>
>>> idade = int(input())
100
>>> idade
100
>>> type(idade)
<class 'int'>
>>> idade = int(input())
quebom!
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    idade = int(input())
ValueError: invalid literal for int() with base 10: 'quebom!'
>>> idade = int(input())
100
>>> idade = int(input("Informe sua idade: "))
Informe sua idade: 100
>>> idade
100
>>> print('bom dia')
bom dia
>>> print(idade)
100
>>> print('Sua idade é',idade)
Sua idade é 100
>>> print(1,2,3,4,5,6,7,8)
1 2 3 4 5 6 7 8
>>> print(1,2,3,4,5,6,7,8, sep='@')
1@2@3@4@5@6@7@8
>>> print(1,2,3,4,5,6,7,8, sep='IFPB')
1IFPB2IFPB3IFPB4IFPB5IFPB6IFPB7IFPB8
>>> 
= RESTART: /Users/valeria/Documents/alp/1001.py
10
9
X =  19
>>> 
= RESTART: /Users/valeria/Documents/alp/1001.py
10
9
X = 19
>>> 
= RESTART: /Users/valeria/Documents/alp/1001.py
-10
4
X = -6
>>> 
= RESTART: /Users/valeria/Documents/alp/1001.py
15
-7
X = 8
>>> 