Cristinas-MacBook-Air:~ cristinamonarrez$ cd desktop
Cristinas-MacBook-Air:desktop cristinamonarrez$ cd Dojo_Assignments
Cristinas-MacBook-Air:Dojo_Assignments cristinamonarrez$ cd Python
Cristinas-MacBook-Air:Python cristinamonarrez$ python firsty.py
/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python: can't open file 'firsty.py': [Errno 2] No such file or directory
Cristinas-MacBook-Air:Python cristinamonarrez$ cd first.py
-bash: cd: first.py: Not a directory
Cristinas-MacBook-Air:Python cristinamonarrez$ pwd
/Users/cristinamonarrez/desktop/Dojo_Assignments/Python
Cristinas-MacBook-Air:Python cristinamonarrez$ cd first.py
-bash: cd: first.py: Not a directory
Cristinas-MacBook-Air:Python cristinamonarrez$ python first.py
Cristinas-MacBook-Air:Python cristinamonarrez$ 3+4=
-bash: 3+4=: command not found
Cristinas-MacBook-Air:Python cristinamonarrez$ python first.py
Cristinas-MacBook-Air:Python cristinamonarrez$ python
Python 2.7.13 (default, Dec 18 2016, 07:03:39)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4+5=
  File "<stdin>", line 1
    4+5=
       ^
SyntaxError: invalid syntax
>>> 4 + 5
9
>>> 5 + 234=
  File "<stdin>", line 1
    5 + 234=
           ^
SyntaxError: invalid syntax
>>>  234+2349
  File "<stdin>", line 1
    234+2349
    ^
IndentationError: unexpected indent
>>> 83 - 92
-9
>>> 3423 / 934
3
>>> 2349.3 / 38
61.823684210526324
>>> me_shark = "hammerhead"
>>> my_car = surfboard
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'surfboard' is not defined
>>> my_shark = hammerhead
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hammerhead' is not defined
>>> my_shark = "hammerhead"
>>> my_car = "surfboard"
>>> my_age = 26
>>> my_shark = "galapagos shark"
>>> my_shark
'galapagos shark'
>>> "my" + "name"
'myname'
>>> "i" + "am" 26
  File "<stdin>", line 1
    "i" + "am" 26
                ^
SyntaxError: invalid syntax
>>> "my" + "age" + "is" "26"
'myageis26'
>>> 
