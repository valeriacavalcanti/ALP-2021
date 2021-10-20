Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1+1
2
>>> 2**10
1024
>>> 2
2

>>> 
>>> nome = "Valeria"
>>> nome
'Valeria'
>>> idade = 15
>>> valor = 32.8
>>> existe = True
>>> nome
'Valeria'
>>> idade
15
>>> valor
32.8
>>> existe
True
>>> nada = None
>>> nada
>>> inf_sup = float('inf')
>>> inf_sup
inf
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'existe', 'idade', 'inf_sup', 'nada', 'nome', 'valor']
>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'nome': 'Valeria', 'idade': 15, 'valor': 32.8, 'existe': True, 'nada': None, 'inf_sup': inf}
>>> globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'nome': 'Valeria', 'idade': 15, 'valor': 32.8, 'existe': True, 'nada': None, 'inf_sup': inf}
>>> 
>>> 
>>> 
>>> 
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'existe', 'idade', 'inf_sup', 'nada', 'nome', 'valor']
>>> idade
15
>>> type(existe)
<class 'bool'>
>>> type(idade)
<class 'int'>
>>> type(inf_sup)
<class 'float'>
>>> type(nada)
<class 'NoneType'>
>>> type(nome)
<class 'str'>
>>> type(valor)
<class 'float'>
>>> idade
15
>>> type(valor)
<class 'float'>
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> teste = 1
>>> teste
1
>>> type(teste)
<class 'int'>
>>> teste = '1'
>>> teste
'1'
>>> type(teste)
<class 'str'>
>>> 
>>> 
>>> teste = 1
>>> teste = '1'
>>> teste
'1'
>>> type(teste)
<class 'str'>
>>> teste =
SyntaxError: invalid syntax
>>> 
>>> 
>>> teste = '123'
>>> teste
'123'
>>> type(teste)
<class 'str'>
>>> outra = int(teste)
>>> teste
'123'
>>> outra
123
>>> type(teste)
<class 'str'>
>>> type(outra)
<class 'int'>
>>> teste = int(teste)
>>> type(teste)
<class 'int'>
>>> teste
123
>>> outra = int('123valeria')
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    outra = int('123valeria')
ValueError: invalid literal for int() with base 10: '123valeria'
>>> 
>>> 
>>> 
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'existe', 'idade', 'inf_sup', 'nada', 'nome', 'outra', 'teste', 'valor']
>>> import sys
>>> max_float = sys.float_info.max
>>> max_float
1.7976931348623157e+308
>>> inf_supr
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    inf_supr
NameError: name 'inf_supr' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
>>> inf_sup
inf
>>> max_sup
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    max_sup
NameError: name 'max_sup' is not defined
>>> 
>>> max_float
1.7976931348623157e+308
>>> max_float > inf_sup
False
>>> max_float == inf_sup
False
>>> max_float < inf_sup
True
>>> 1 == 1
True
>>> int_max_float = int(max_float)
>>> int_max_float
179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368
>>> int_inf_sup = int(inf_sup)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    int_inf_sup = int(inf_sup)
OverflowError: cannot convert float infinity to integer
>>> 
>>> 
>>> 
>>> 
>>> 
>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'nome': 'Valeria', 'idade': 15, 'valor': 32.8, 'existe': True, 'nada': None, 'inf_sup': inf, 'teste': 123, 'outra': 123, 'sys': <module 'sys' (built-in)>, 'max_float': 1.7976931348623157e+308, 'int_max_float': 179769313486231570814527423731704356798070567525844996598917476803157260780028538760589558632766878171540458953514382464234321326889464182768467546703537516986049910576551282076245490090389328944075868508455133942304583236903222948165808559332123348274797826204144723168738177180919299881250404026184124858368}
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'existe', 'idade', 'inf_sup', 'int_max_float', 'max_float', 'nada', 'nome', 'outra', 'sys', 'teste', 'valor']
>>> 