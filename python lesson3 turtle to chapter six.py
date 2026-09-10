Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import turtle
>>> screen = turtle.TurtleScreen()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    screen = turtle.TurtleScreen()
TypeError: TurtleScreen.__init__() missing 1 required positional argument: 'cv'
>>> screen = turtle.Screen()
>>> t= turtle.Turtle()
>>> screen.title('My Art')
>>> screen.bgcolor('green')
>>> turtle.colormode(255)
>>> t.pencolor(50,200,127)
>>> t.pencolor(150,20,17)
>>> def spril(size):
...     for i in range(size):
...         t.forward(i*2)
...         t.rirht(120)
...         .
...         
SyntaxError: invalid syntax
>>> def spril(size):
...     for i in range(size):
...         t.forward(i*2)
...         t.rirht(120)
... 
...         
>>> spril(100)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    spril(100)
  File "<pyshell#16>", line 4, in spril
    t.rirht(120)
AttributeError: 'Turtle' object has no attribute 'rirht'. Did you mean: 'right'?
>>> def spril(size):
...     for i in range(size):
...         t.forward(i*2)
...         t.right(120)
... 
...         
>>> spril(100)
>>> def spril(size):
...     for i in range(size):
...         t.forward(i*2)
...         t.right(360)
... 
        
spril(500)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    spril(500)
  File "<pyshell#22>", line 4, in spril
    t.right(360)
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 1746, in right
    self._rotate(-angle)
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 3394, in _rotate
    self._update()
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 2744, in _update
    self._update_data()
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 2730, in _update_data
    self.screen._incrementudc()
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 1320, in _incrementudc
    raise Terminator
turtle.Terminator
screen = turtle.Screen()
t= turtle.Turtle()
screen.bgcolor('green')
turtle.colormode(255)
t.pencolor(150,20,17)
def spril(size):
    for i in range(size):
        t.forward(i*2)
        t.right(360)

        
spril(100)
def spril(size):
    for i in range(size):
        t.forward(i*2)
        t.right(120)

        
spril(500)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    spril(500)
  File "<pyshell#33>", line 3, in spril
    t.forward(i*2)
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 1705, in forward
    self._go(distance)
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 1666, in _go
    self._goto(ende)
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 3276, in _goto
    screen._pointlist(self.currentLineItem),
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 747, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\tkinter\__init__.py", line 2997, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".!canvas"
screen = turtle.Screen()
turtle.colormode(255)
turtle.colormode(255)
t= turtle.Turtle()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    t= turtle.Turtle()
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 3960, in __init__
    RawTurtle.__init__(self, Turtle._screen,
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 2641, in __init__
    self._update()
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 2744, in _update
    self._update_data()
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 2730, in _update_data
    self.screen._incrementudc()
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 1320, in _incrementudc
    raise Terminator
turtle.Terminator
t= turtle.Turtle()
turtle.colormode(255)
t.pencolor(150,20,17)
screen.bgcolor('green')
def spril(size):
    for i in range(size):
        t.forward(i*2)
        t.right(120)

        
spril(500)

t.clear
<bound method RawTurtle.clear of <turtle.Turtle object at 0x000002207BA0BC50>>








t.cles
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    t.cles
AttributeError: 'Turtle' object has no attribute 'cles'. Did you mean: 'clear'?
t.clear()
def spril(size):
    for i in range(size):
        t.forward(i*2)
        t.right(144)

        
spril(100)
t= turtle.Turtle()
spril(100)
num = 7
if num % 2==0:
    print('even')
else:
    print('odd')

    
odd
for i in range(10):
    print(i%4)

    
0
1
2
3
0
1
2
3
0
1
# second functionn of modules
number = 12345
last = number %10
print(last)
5
import random
number =  random.randint(1,9)
print(number)
2
print(number)
2
print(number)
2
number =  random.randint(1,9)
print(number)
1
#let practice chapter four exercise
from turtle import  penup, penddown
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    from turtle import  penup, penddown
ImportError: cannot import name 'penddown' from 'turtle' (C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py). Did you mean: 'pendown'?
from turtle import  penup, pendown
def jump(leng):
    penup()
    fd(leng)
    pedown()

    
jump(45)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    jump(45)
  File "<pyshell#83>", line 3, in jump
    fd(leng)
NameError: name 'fd' is not defined. Did you mean: 'id'?
def jump(leng):
    penup()
    forward(leng)
    pedown()

    
jump(45)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    jump(45)
  File "<pyshell#86>", line 3, in jump
    forward(leng)
NameError: name 'forward' is not defined
clear()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    clear()
NameError: name 'clear' is not defined
from turtle import  penup, pendown, screen, clear
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    from turtle import  penup, pendown, screen, clear
ImportError: cannot import name 'screen' from 'turtle' (C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py). Did you mean: 'Screen'?
from turtle import  penup, pendown, Screen, clear
Screen()
<turtle._Screen object at 0x000002207BA0A710>
clear()

==================== RESTART: Shell ===================
from turtle import *
shape('turtle')
speed(0)
pensize(3)
forward(100)
right(90)
forward(!00)
SyntaxError: invalid syntax
forward(100)
bgcolor('green')
colors = ['red','blue', 'yellow','purple','orange']
def spiral(rang):
    for i in range(rang):
        pencolor(colors[i%6])
        forward(i*2)
        right(61)

        
spiral(200)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    spiral(200)
  File "<pyshell#108>", line 3, in spiral
    pencolor(colors[i%6])
IndexError: list index out of range
clear()
colors = ['red','blue', 'yellow','purple','orange','white']
def spiral(rang):
    for i in range(rang):
        pencolor(colors[i%6])
        forward(i*2)
        right(61)

        
spiral(200)
bgcolor('black')
spiral(200)
clear()
spiral(200)
clear()
shape('turtle')
spiral(200)
clear()
Turtle()
<turtle.Turtle object at 0x000002C78DF560D0>
goto(0,0)
clear()
spiral(200)
clear()
penup()
goto(0,0)
penup()
goto(-20,0)
goto(-50,0)
up(30)
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    up(30)
TypeError: up() takes 0 positional arguments but 1 was given
pendown()
goto(30)
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    goto(30)
  File "<string>", line 8, in goto
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 1842, in goto
    self._goto(Vec2D(*x))
TypeError: turtle.Vec2D() argument after * must be an iterable, not int
forward(80)
right()
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    right()
TypeError: right() missing 1 required positional argument: 'angle'
right(60)
foewar(40)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    foewar(40)
NameError: name 'foewar' is not defined. Did you mean: 'forward'?
forward(40)
                       
forward(40)
                       
for i in range(40):
                       right(60)
                       forward(80)

                       
def comb(n):
    for i in range(2):
        forward(80)
        right(60)

        
comb(n)
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    comb(n)
NameError: name 'n' is not defined
def comb():
    for i in range(2):
        forward(80)
        right(60)

        
comb(n)
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    comb(n)
NameError: name 'n' is not defined
comb()
KeyboardInterrupt
def comb():
    for i in range(8):
        forward(80)
        right(60)

        
comb()
KeyboardInterrupt
comb()
comb()
comb()
def comb():
    for i in range(150):
         if i%6 :
             
        forward(80)
        right(60)
        
SyntaxError: unindent does not match any outer indentation level
def comb():
    for i in range(150):
         if i%6 :      
          forward(80)
          right(60)
          else:
              
SyntaxError: invalid syntax
def comb():
    for i in range(150):
         if i%6 :      
          forward(80)
          right(60)
        else:
            
SyntaxError: unindent does not match any outer indentation level
KeyboardInterrupt
def comb():
    for i in range(150):
         if i%6 :      
          forward(80)
          right(60)
         else:
             right(60)
             forward(80)

             
clear()
penip()
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    penip()
NameError: name 'penip' is not defined. Did you mean: 'penup'?
penup()
goto(0,0)
set(0)
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    set(0)
TypeError: 'int' object is not iterable
seth(90)
comb()
goto(0,0)
pegdown()
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    pegdown()
NameError: name 'pegdown' is not defined. Did you mean: 'pendown'?
pendown()
comb()
def comb():
    for i in range(150):
         if i%6=0 :      
          forward(80)
          right(60)
         else:
             right(60)
             forward(80)

SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
def comb():
    for i in range(150):
         if i%6==0 :      
          forward(80)
          right(60)
         else:
             right(60)
             forward(80)

             
clear()
penup()
goto(0,0)
pendown()
comb()
def newr():
    clear()
    penup()
    goto(0,0)
    pendown()

    
newr()
def comb():
    for i in range(150):
         if i>=0 and i%==7 :      
          forward(80)
          right(60)
          #to ger every hexa gona ne hehagona, we to make after eiht to change its p
         else :
             right(120)
             forward(80)

             
SyntaxError: invalid syntax
def comb():
    for i in range(150):
         if i%8==0 :      
          forward(80)
          right(60)
         else:
             right(120)
             forward(80)

             
comb()
def comb():
    for i in range(150):
         if i%8==0 :      
          forward(80)
          right(60)
         else:
             right(110)
             forward(80)

             
newr()
newr()
comb()
newr()
def comb():
    for i in range(150):
         if i%8==0 :      
            right(110)
             forward(80)
         else:
             forward(80)
             
SyntaxError: unexpected indent
def comb():
    for i in range(150):
         if i%8==0 :      
          right(120)
          forward(90)
         else:
             forward(90)
             right(60)

comb()
def comb():
    for i in range(150):
         if i%8==0 or i%8==0:      
          right(120)
          forward(90)
         else:
             forward(90)
             right(60)

             
comb()
def comb():
    for i in range(150):
         if i%8==0 or i%9==0:      
          right(120)
          forward(90)
         else:
             forward(90)
             right(60)

             
newr()
def newr():
    clear()
    penup()
    goto(0,0)
    pendown()
    steh(90)

    
newr()
Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    newr()
  File "<pyshell#219>", line 6, in newr
    steh(90)
NameError: name 'steh' is not defined
def newr():
    clear()
    penup()
    goto(0,0)
    pendown()
    seth(90)

    
newr()
comb()
newr()
for i in range
SyntaxError: expected ':'
for i in range(6):
    forward(40)
    right(90)

    
newr()
for i in range(5):
    if i==0 and i==2:
        right(60)
        forward(100)
     elif i==1 and i==3:
        right(120)
        forward(100)
        
SyntaxError: unindent does not match any outer indentation level

for i in range(5):
    if i==0 and i==2:
        right(60)
        forward(100)
    elif i==1 and i==3:
        right(120)
        forward(100)

        
for i in range(5):
    if i==0 and i==2:
        right(60)
        forward(100)
    elif i==1 and i==3:
        right(120)
        forward(100)

        
for i in range(5):
    if i==0 and i==2:
        forward(100)
        right(60)
    elif i==1 and i==3:
        right(120)
        forward(100)

        
for i in range(5):
    if i==0 and i==2:
        right(60)
        forward(100)
    elif i==1 and i==3:
        right(120)
        forward(100)

        
for i in range(5):
    if i==0 and i==2:
        right(60)
        forward(100)
    elif i==1 and i==3:
        right(120)
        forward(100)
     else:
         
SyntaxError: unindent does not match any outer indentation level
for i in range(5):
    if i==0 and i==2:
        right(60)
        forward(100)
    elif i==1 and i==3:
        right(120)
        forward(100)
    else:
        right(120)
        forward(100)

        
KeyboardInterrupt
for i in range(5):
    if i==0 and i==2:
        right(60)
        forward(100)
    else:
        right(120)
        forward(100)

        
newr()
for i in range(5):
    if i==0 and i==2:
        right(120)
        forward(100)
    else:
        right(60)
        forward(100)

        
newr()
right(60)
forward(100)
right(60)
seth(180)
seth(0)
forward(100)
right(60)
right(60)
forward(100)
left(60)
right(120)
forward(100)
newr()
right(30)
newr()
for i in range(5):
    if i==0 and i==1 :
        right(30)
        forward(100)
    else:
        right(120)
        forward(100)

        
newr()
right(30)
f0rward(100)
Traceback (most recent call last):
  File "<pyshell#291>", line 1, in <module>
    f0rward(100)
NameError: name 'f0rward' is not defined. Did you mean: 'forward'?
forward(100)
right(30)
right(30)
forward(100)
right
<function right at 0x000002C78DFFCB40>
right(120)
forward(100)
right(60)
forward(100)
rhombus
Traceback (most recent call last):
  File "<pyshell#301>", line 1, in <module>
    rhombus
NameError: name 'rhombus' is not defined
def rehom()
SyntaxError: expected ':'
def rehom():
    right(30)
    forward(100)
    right(60)
    forward(100)
    right(120)
    forward(100)
    right(60)
    forward(100)

    
rehom()
rehom()
rehom()
rehom()
rehom()
# this create rehombus flower , let create petal flower
def flower(petal,size, angle):
    for i in range(petals)
    
SyntaxError: expected ':'
def flower(petals,size, angle):
    for i in range(petals):
        petals(size,angle)
        left

        
def petal(size,angle):
    begin_fill()
    for i in range(2):
        forward(size)
        left(angle)

        
def petal(size,angle):
    begin_fill()
    for i in range(2):
        forward(size)
        left(angle)
        forward(size)
        left(180-angle)
    end_fill()

    
def flower(petals,size, angle):
    for i in range(petals):
        petals(size,angle)
        left(360/ petals)

        
pencolor('pink')
fillcolor('pink')
newr()
flower(8,50,60)
Traceback (most recent call last):
  File "<pyshell#338>", line 1, in <module>
    flower(8,50,60)
  File "<pyshell#334>", line 3, in flower
    petals(size,angle)
TypeError: 'int' object is not callable
def flower(petals,size, angle):
    for i in range(petals):
        petal(size,angle)
        left(360/ petals)

        
flower(8,50,60)
fillcolor('yellow')
newr()
flower(8,50,60)
newr
<function newr at 0x000002C78DFFF1C0>
newr()
flower(30,150,120)
KeyboardInterrupt
flower(30,13,70)
newr()
flower(30,130,70)
#exercises from chapter six
from time import *
now  time(()
          
SyntaxError: '(' was never closed
time()
          
1788424402.3000598
now = time()
          
print(now//(24*60*60))
          
20699.0
day = print(now//(24*60*60))

20699.0
print(day//12)
          
Traceback (most recent call last):
  File "<pyshell#358>", line 1, in <module>
    print(day//12)
TypeError: unsupported operand type(s) for //: 'NoneType' and 'int'
print(day/12)
          
Traceback (most recent call last):
  File "<pyshell#359>", line 1, in <module>
    print(day/12)
TypeError: unsupported operand type(s) for /: 'NoneType' and 'int'
day = now//(24*60*60)
          
print(day/12)
          
1724.9166666666667
1724/360
          
4.788888888888889
20699/360
          
57.49722222222222
clear()
          
def koch(length,level):
    if level == 0:
        forward(length)
        else:
            
SyntaxError: invalid syntax
def koch(length,level):
    if level == 0:
        forward(length)
    else:
        koch(length/3, level-1)
        lefgt(60)
         koch(length/3, level-1)
        lefgt(60)
        
SyntaxError: unexpected indent
def koch(length,level):
    if level == 0:
        forward(length)
    else:
        koch(length/3, level-1)
        lefgt(60)
        koch(length/3, level-1)
        lefgt(120)
        koch(length/3, level-1)
        lefgt(60)
        koch(length/3, level-1)

        
def animated_snoflake():
    speed(0)
    bgcolor('lightblue'_
            
SyntaxError: '(' was never closed
def animated_snoflake():
    speed(0)
    bgcolor('lightblue')
    pensize(2)
    tracer(0)

    
def animated_snoflake():
    speed(0)
    bgcolor('lightblue')
    pensize(2)
    tracer(0)
    forr level in range(6):
        
SyntaxError: invalid syntax
def animated_snoflake():
    speed(0)
    bgcolor('lightblue')
    pensize(2)
    tracer(0)
    for level in range(6):
        clear()
        penup()
        goto(-200,100)
        pendown()

        
def animated_snoflake():
    speed(0)
    bgcolor('lightblue')
    pensize(2)
    tracer(0)
    for level in range(6):
        clear()
        penup()
        goto(-200,100)
        pendown()
        for i in range(3):
            koch(400,level)
            right(120)
         update
         
SyntaxError: unindent does not match any outer indentation level
def animated_snoflake():
    speed(0)
    bgcolor('lightblue')
    pensize(2)
    tracer(0)
    for level in range(6):
        clear()
        penup()
        goto(-200,100)
        pendown()
        for i in range(3):
            koch(400,level)
            right(120)
            update()
            goto(0,-200)
            write(f"Level:{level}", align="center", font=("Arial",24,"bold"))

            
animate_snowflake()
Traceback (most recent call last):
  File "<pyshell#400>", line 1, in <module>
    animate_snowflake()
NameError: name 'animate_snowflake' is not defined. Did you mean: 'animated_snoflake'?
animated_snoflake()
Traceback (most recent call last):
  File "<pyshell#401>", line 1, in <module>
    animated_snoflake()
  File "<pyshell#399>", line 12, in animated_snoflake
    koch(400,level)
  File "<pyshell#376>", line 6, in koch
    lefgt(60)
NameError: name 'lefgt' is not defined. Did you mean: 'left'?
def koch(length,level):
    if level == 0:
        forward(length)
    else:
        koch(length/3, level-1)
        left(60)
        koch(length/3, level-1)
        left(120)
        koch(length/3, level-1)
        left(60)
        koch(length/3, level-1)

        
animated_snoflake()

clear()
animated_snoflake()

+++++++++++
SyntaxError: invalid syntax



















clear()
animated_snoflake()


def animated_snoflake():
    speed(0)
    bgcolor('lightblue')
    pensize(2)
    tracer(0)
    
    for level in range(6):
        clear()
        penup()
        goto(-200,100)
        pendown()
        
        for i in range(3):
            koch(400,level)
            right(120)

        update()
        time.sleep(1)
        goto(0,-200)
        write(f"Level:{level}", align="center", font=("Arial",24,"bold"))

        
animated_snoflake()
Traceback (most recent call last):
  File "<pyshell#416>", line 1, in <module>
    animated_snoflake()
  File "<pyshell#415>", line 18, in animated_snoflake
    time.sleep(1)
AttributeError: 'builtin_function_or_method' object has no attribute 'sleep'
import time
clear()
animated_snoflake()
clear()
animated_snoflake()
def animated_snoflake():
    speed(2)
    bgcolor('lightblue')
    pensize(2)
    tracer(0)
    
    for level in range(6):
        clear()
        penup()
        goto(-200,100)
        pendown()
        
        for i in range(3):
            koch(400,level)
            right(120)

        update()
        time.sleep(1)
        goto(0,-200)
        write(f"Level:{level}", align="center", font=("Arial",24,"bold"))

        
def animated_snoflake():
    speed(0)
    bgcolor('lightblue')
    pensize(2)
    tracer(0)
    
    for level in range(6):
        clear()
        penup()
        goto(-200,100)
        pendown()
        
        for i in range(3):
            koch(400,level)
            right(120)

        update()
        time.sleep(1)
        goto(0,-200)
        write(f"Level:{level}", align="center", font=("Arial",24,"bold"))

        

def animated_snoflake():
    speed(2)
    bgcolor('lightblue')
    pensize(2)
    tracer(0)
    
    for level in range(6):
        clear()
        penup()
        goto(-200,100)
        pendown()
        
        for i in range(3):
            koch(400,level)
            right(120)

        update()
        time.sleep(1)
        goto(0,-200)
        write(f"Level:{level}", align="center", font=("Arial",24,"bold"))

        

animated_snoflake()
animated_snoflake()
animated_snoflake()
 def  fibonacci(n):
     if n == 0:
          return 0
     elif n == 1:
          return 1
     else:
          return fibonacci(n-1) + fibonacci(n-2)
        
SyntaxError: unexpected indent
def  fibonacci(n):
     if n == 0:
          return 0
     elif n == 1:
          return 1
     else:
          return fibonacci(n-1) + fibonacci(n-2)

        
fibonacci(15)
610
def fact(n):
    if n==0:
        return 0
    else:
        reurse = fact(n-1)*n
        return reurse

    
fact(10)
0
def fact(n):
    if n==0:
        return 1
    else:
        reurse = fact(n-1)*n
        return reurse

    
fact(5)
120
fact(120)
6689502913449127057588118054090372586752746333138029810295671352301633557244962989366874165271984981308157637893214090552534408589408121859898481114389650005964960521256960000000000000000000000000000
def absol(x):
    if x<0:
        return -x
    else:
        return x

    
absol(-4)
4
# i'm going to write hypotenous calculate dfunction
def hypot(ad,op):
    return 0

hypot(0,0)
0
def hypot(ad,op):
    # since input is two values and hypo is square root of bot squares let assighn values and write functions
    r = ad**2 + op**2
    hyp = math.sqrt(r)
    return hyp

hypot(3,4)
Traceback (most recent call last):
  File "<pyshell#470>", line 1, in <module>
    hypot(3,4)
  File "<pyshell#469>", line 4, in hypot
    hyp = math.sqrt(r)
NameError: name 'math' is not defined. Did you forget to import 'math'?
import math
hypot(3,4)
5.0
import math *
SyntaxError: invalid syntax
import math*
SyntaxError: invalid syntax
KeyboardInterrupt
import math  *
SyntaxError: invalid syntax
hypot(34, 13)
36.40054944640259
def is_between(x,y,z):
    if x<y<z or z<y<x:
        return True
    else:
        False

        
is_between(3,7,9)
True
is_between(3,2,9)
def is_between(x,y,z):
    if x<y<z or z<y<x:
        return True
    else:
        return False

    
is_between(3,2,9)
False
def ack(m,n):
    if m= =0:
        
SyntaxError: invalid syntax
def ack(m,n):
    if m==0:
        return n+1
    elif m>o and n==0:
        return ack(m-1,1)
    elif m>0 and n>0 :
        return ack(m-1,ack(m,n-1))
    else
    
SyntaxError: expected ':'
def ack(m,n):
    if m==0:
        return n+1
    elif m>o and n==0:
        return ack(m-1,1)
    elif m>0 and n>0 :
        return ack(m-1,ack(m,n-1))
    else:
        return 'not in bound'

    
ack(5,5)
Traceback (most recent call last):
  File "<pyshell#500>", line 1, in <module>
    ack(5,5)
  File "<pyshell#499>", line 4, in ack
    elif m>o and n==0:
NameError: name 'o' is not defined
def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0 :
        return ack(m-1,ack(m,n-1))
    else:
        return 'not in bound'

    
ack(5,5)
Traceback (most recent call last):
  File "<pyshell#503>", line 1, in <module>
    ack(5,5)

  File "<pyshell#502>", line 7, in ack
    return ack(m-1,ack(m,n-1))
  File "<pyshell#502>", line 7, in ack
    return ack(m-1,ack(m,n-1))
  File "<pyshell#502>", line 7, in ack
    return ack(m-1,ack(m,n-1))
  [Previous line repeated 2 more times]
  File "<pyshell#502>", line 5, in ack
    return ack(m-1,1)
  File "<pyshell#502>", line 7, in ack
    return ack(m-1,ack(m,n-1))
  File "<pyshell#502>", line 7, in ack
    return ack(m-1,ack(m,n-1))
  File "<pyshell#502>", line 7, in ack
    return ack(m-1,ack(m,n-1))
  [Previous line repeated 1016 more times]
  File "<pyshell#502>", line 5, in ack
    return ack(m-1,1)
RecursionError: maximum recursion depth exceeded
ack(1,3)
5
ack(o,5)
Traceback (most recent call last):
  File "<pyshell#505>", line 1, in <module>
    ack(o,5)
NameError: name 'o' is not defined
ack(0,5)
6
ack(4,0)
13
