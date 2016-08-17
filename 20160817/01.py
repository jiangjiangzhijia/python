Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print 'hello world'

hello world
>>> 2+2
4
>>> 1/2
0
>>> 1/2.0
0.5
>>> from __future__ import division
>>> 1/2
0.5
>>> 
1/2
0.5
>>> 1//2
0
>>> 1%2
1
>>> 2*3
6
>>> 2**3
8
>>> -3**2
-9
>>> (-3)**2
9
>>> 0xAf
175
>>> 010
8
>>> x=3
>>> x*2
6
>>> print x
3
>>> print(42)
42
>>> print(x)
3
>>> input("the meanint of line:")
the meanint of line:12
12
>>> input()
aaa

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    input()
  File "<string>", line 1, in <module>
NameError: name 'aaa' is not defined
>>> input_raw()

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    input_raw()
NameError: name 'input_raw' is not defined
>>> input_row

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    input_row
NameError: name 'input_row' is not defined
>>> input(x)
3

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    input(x)
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> input(x)
3

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    input(x)
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> x = input("x:")
x:12
>>> y = input("y:")
y:12
>>> x+y
24
>>> print x+y
24
>>> if 1==2 : print '1=2'

>>> if 1<>2 : print '<>'

<>
>>> print time

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print time
NameError: name 'time' is not defined
>>> time()

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    time()
NameError: name 'time' is not defined
>>> pow(2,3)
8
>>> round(3.9)
4.0
>>> floor(3.9)

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    floor(3.9)
NameError: name 'floor' is not defined
>>> import math
>>> math.floor(3.9)
3.0
>>> floor(3.9)

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    floor(3.9)
NameError: name 'floor' is not defined
>>> import __future__ import math
SyntaxError: invalid syntax
>>> from math import floor
>>> floor(3.9)
3.0
>>> ceil(3.9)

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    ceil(3.9)
NameError: name 'ceil' is not defined
>>> from math import ceil
>>> ceil(3.9)
4.0
>>> foo = math.floor()

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    foo = math.floor()
TypeError: floor() takes exactly one argument (0 given)
>>> foo = math.floor
>>> foo(3.9)
3.0
>>> from math import sqrt
>>> sqrt(-1)

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    sqrt(-1)
ValueError: math domain error
>>> import cmatch

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    import cmatch
ImportError: No module named cmatch
>>> import cmath
>>> foo = cmath.sqrt
>>> foo(-1)
1j
>>> math.
SyntaxError: invalid syntax
>>> 
