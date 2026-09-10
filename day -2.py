Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#chapter three --functon practices and loops
def  my_name()
SyntaxError: expected ':'
def  my_name():
      print('melkamu kebede')
      print('AASTU student')

      
my_name
<function my_name at 0x0000023DC92EDC70>
my_name()
melkamu kebede
AASTU student
def my(string)
SyntaxError: expected ':'
def my(string):
    print(string)
    print(string)

    
my('melkamu kebede')
melkamu kebede
melkamu kebede
#string in bracket of function is parameter
def my('string'):
    print('string')
    print('string')
    
SyntaxError: invalid syntax
def my(strin):
    print(strin)
    print(strin)

    
my('melkamu')
melkamu
melkamu
def my(strin):
    print(strin)

    
my('melkamu')
melkamu
def my(strin):
    print(strin)

    
def my(stri):
    print(strin)

    

my('melkamu')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    my('melkamu')
  File "<pyshell#25>", line 2, in my
    print(strin)
NameError: name 'strin' is not defined. Did you mean: 'stri'?
KeyboardInterrupt
def my(strin):
    print(strin)

    
my(12)
12
my(float(12))
12.0
def repate(word,n):
    print(word*n)

    
repate(spam,8)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    repate(spam,8)
NameError: name 'spam' is not defined
repate('spam',8)
spamspamspamspamspamspamspamspam
repate('spam ',8)
spam spam spam spam spam spam spam spam 
def adj(ad1,adj2):
    print(adj1,adj2)

    
def spam_song():
    repate('spame,', 4)
    repate('spame,', 4)
    repate('spame,', 2)
    adj('Lovely Spam',' Wonderful Spam!')
    repate('spame',2)

    
spam_song()
spame,spame,spame,spame,
spame,spame,spame,spame,
spame,spame,
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    spam_song()
  File "<pyshell#47>", line 5, in spam_song
    adj('Lovely Spam',' Wonderful Spam!')
  File "<pyshell#40>", line 2, in adj
    print(adj1,adj2)
NameError: name 'adj1' is not defined. Did you mean: 'ad1'?
def spam_song():
    repate('spame,', 4)
    repate('spame,', 4)
    repate('spame,', 2)
    adj('Lovely Spam',' Wonderful Spam!')
    repate('spame',2)

    
def adj(adj1,adj2):
    print(adj1,adj2)

    
def spam_song():
    repate('Spame,', 4)
    repate('Spame,', 4)
    repate('Spame,', 2)
    adj('Lovely Spam',' Wonderful Spam!')
    repate('Spame',2)

    


spam_song()
Spame,Spame,Spame,Spame,
Spame,Spame,Spame,Spame,
Spame,Spame,
Lovely Spam  Wonderful Spam!
SpameSpame
#THis shiws i can create functions, add parametrs, call funcitons with arguents and use in other functions
#let practice more on repetition
# fore loop
#structure of fore loop looks [ for inttialize in terminaatiion
for i in range(5):
    print(i)

    
0
1
2
3
4
for i in range
SyntaxError: expected ':'
for i in range(2):
    print('verse',  i)
    spam_song()

    
verse 0
Spame,Spame,Spame,Spame,
Spame,Spame,Spame,Spame,
Spame,Spame,
Lovely Spam  Wonderful Spam!
SpameSpame
verse 1
Spame,Spame,Spame,Spame,
Spame,Spame,Spame,Spame,
Spame,Spame,
Lovely Spam  Wonderful Spam!
SpameSpame
def print_verse(n):
for i in range(n):
    print('verse',  i)
    spam_song()
    
SyntaxError: expected an indented block after function definition on line 1
def print_verse(n):
      for i in range(n):
          print('verse',  i)spam_song()
          
SyntaxError: invalid syntax

def print_verse(n):
      for i in range(n):
          print('verse',  i) spam_song()
          
SyntaxError: invalid syntax
def print_verse(n):
      for i in range(n):
          print('verse',  i)                                                                                                   spam_song()
          
SyntaxError: invalid syntax
def print_verse(n):
    for i in range(n):
        spam_song()

        
print_verse(6)
Spame,Spame,Spame,Spame,
Spame,Spame,Spame,Spame,
Spame,Spame,
Lovely Spam  Wonderful Spam!
SpameSpame
Spame,Spame,Spame,Spame,
Spame,Spame,Spame,Spame,
Spame,Spame,
Lovely Spam  Wonderful Spam!
SpameSpame
Spame,Spame,Spame,Spame,
Spame,Spame,Spame,Spame,
Spame,Spame,
Lovely Spam  Wonderful Spam!
SpameSpame
Spame,Spame,Spame,Spame,
Spame,Spame,Spame,Spame,
Spame,Spame,
Lovely Spam  Wonderful Spam!
SpameSpame
Spame,Spame,Spame,Spame,
Spame,Spame,Spame,Spame,
Spame,Spame,
Lovely Spam  Wonderful Spam!
SpameSpame
Spame,Spame,Spame,Spame,
Spame,Spame,Spame,Spame,
Spame,Spame,
Lovely Spam  Wonderful Spam!
SpameSpame
def print_verse(n):
      for i in range(n):
          print('verse',  i)

          
print_verse(3)
verse 0
verse 1
verse 2
def print_verse(n):
      for i in range(n):
          print('verse',  i)                                                                                                   spam_song()
          
SyntaxError: invalid syntax
def print_verse(n):
      for i in range(n):                                                                                                  spam_song()
       print('verse',  i
             
SyntaxError: unexpected indent
def 
[DEBUG ON]
def print_verse(n):
      for i in range(n):                                                                                                  spam_song()

      
[DEBUG ON]
[DEBUG OFF]
print_verse(3)
Spame,Spame,Spame,Spame,
Spame,Spame,Spame,Spame,
Spame,Spame,
Lovely Spam  Wonderful Spam!
SpameSpame
Spame,Spame,Spame,Spame,
Spame,Spame,Spame,Spame,
Spame,Spame,
Lovely Spam  Wonderful Spam!
SpameSpame
Spame,Spame,Spame,Spame,
Spame,Spame,Spame,Spame,
Spame,Spame,
Lovely Spam  Wonderful Spam!
SpameSpame
def print-right(word):
    
SyntaxError: expected '('
def print_right(word):
     #to make leading space enouph and last letter 40th culomen
    # let i try my guest 1, use lens to get total string lenth and leading space and string length give 39 lenth of space it looks print(''*n, + word)
    # n looks 39-lenth of word, i ger it now, let i try
    n= 39-len(word)
    print(''*n, + word)
    
    print(word)
    space= len(word)

    



print_right('monday')
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    print_right('monday')
  File "<pyshell#91>", line 6, in print_right
    print(''*n, + word)
TypeError: bad operand type for unary +: 'str'
def print_right(word):
      n= 39-len(word)
      print(''*n, + word)

      
print_right('monday')
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    print_right('monday')
  File "<pyshell#98>", line 3, in print_right
    print(''*n, + word)
TypeError: bad operand type for unary +: 'str'
def print_right(word):
      n= 39-len(word)
      print(''*n+ word)

      
print_right('monday')
monday
def print_right(word):
      n= 39-len(word)
      print(' '*n+ word)

      
print_right('monday')
                                 monday
KeyboardInterrupt
print_right('teuseday')
                               teuseday
print_right('wednesday')
                              wednesday
print_right('ryurtyrysretytryert')
                    ryurtyrysretytryert
print_right('Monty')
                                  Monty
print_right('Pythos')
                                 Pythos
print_right('Flying Circus')
                          Flying Circus
#exrcise two , create triangle  by letter
                          
# it hink i hve to use for loop
def trianglle(leter,height)
SyntaxError: expected ':'
def trianglle(leter,height):
    for i in height:
        print(leter*height)

        
triangle('L',5)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    triangle('L',5)
NameError: name 'triangle' is not defined. Did you mean: 'trianglle'?
trianglle('L',5)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    trianglle('L',5)
  File "<pyshell#118>", line 2, in trianglle
    for i in height:
TypeError: 'int' object is not iterable
def trianglle(leter,height):
    for i in height:
        print(leter*int(height))

        
trianglle('L',5)
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    trianglle('L',5)
  File "<pyshell#122>", line 2, in trianglle
    for i in height:
TypeError: 'int' object is not iterable
def trianglle(leter,height):
    for i in range(height):
        print(leter*int(height))

        
trianglle('L',5)
LLLLL
LLLLL
LLLLL
LLLLL
LLLLL
def trianglle(leter,height):
    for i in range(height):
        print(leter*i)

        
trianglle('L',5)

L
LL
LLL
LLLL
def trianglle(leter,height):
    i=1
    for i in range(height):
        print(leter*i)

        
trianglle('L',5)


L
LL
LLL
LLLL
def trianglle(leter,height):
    i=-1
    for i in range(height):
        print(leter*i)


trianglle('L',5)

L
LL
LLL
LLLL
def trianglle(leter,height):
    for i in range(height, 2):
        print(leter*i)

        
trianglle('L',5)
def trianglle(leter,height):
    for i in range(height, 1):
        print(leter*i)

        
trianglle('L',5)

trianglle('L',5)
def trianglle(leter,height):
    for i in range(height):
        print(leter*i)
        
SyntaxError: multiple statements found while compiling a single statement
def trianglle(leter,height):
    for i in range(height):
        print(leter*i)

        
trianglle('L',5)

L
LL
LLL
LLLL
trianglle('L',9)

L
LL
LLL
LLLL
LLLLL
LLLLLL
LLLLLLL
LLLLLLLL
def trianglle(leter,height):
    for i in range(height):
        print(leter*(1+))
        
SyntaxError: invalid syntax
def trianglle(leter,height):
    for i in range(height):
        print(leter*(1+i))

        
trianglle('L',5)

L
LL
LLL
LLLL
LLLLL
#i did triangle roblem byadding iteratr i +1 in print statemetn ang without range property check
#now create the reactangle that use three arguments
def rectangle(let, h,w)
SyntaxError: expected ':'
def rectangle(let, h,w):
    for i in range(h):
        print(let*i)
        for i in range(w):
            print(let*w)

            
rectangle('H',5,4)

HHHH
HHHH
HHHH
HHHH
H
HHHH
HHHH
HHHH
HHHH
HH
HHHH
HHHH
HHHH
HHHH
HHH
HHHH
HHHH
HHHH
HHHH
HHHH
HHHH
HHHH
HHHH
HHHH
def rectangle(let, h,w):
    for i in range(h):
        print(let*h)
        for i in range(w):
            print(let*w)

            
rectangle('H',5,4)

HHHHH
HHHH
HHHH
HHHH
HHHH
HHHHH
HHHH
HHHH
HHHH
HHHH
HHHHH
HHHH
HHHH
HHHH
HHHH
HHHHH
HHHH
HHHH
HHHH
HHHH
HHHHH
HHHH
HHHH
HHHH
HHHH
def rectangle(let, h,w):
    for i in range(0):
        print(let*h)
        for i in range(w):
            print(let*w)

            
rectangle('H',5,4)

def rectangle(let, h,w):
    for i in range(1):
        print(let*h)
        for i in range(w):
            print(let*w)

            
rectangle('H',5,4)
HHHHH
HHHH
HHHH
HHHH
HHHH
def rectangle(let, h,w):
    for i in range(1):
        print(let*h)
        for i in range(1):
            print(let*w)

            
rectangle('H',5,4)

HHHHH
HHHH
def rectangle(let, h,w):
    for i in range(1):
        print(let*h)
        for i in range(h):
            print(let*w)

            
rectangle('H',5,4)
HHHHH
HHHH
HHHH
HHHH
HHHH
HHHH
x='spam'
for i in range(len(x)):
    print(x[i])

    
s
p
a
m
for i in range(len(x)):
    println(x[i])

    
Traceback (most recent call last):
  File "<pyshell#205>", line 2, in <module>
    println(x[i])
NameError: name 'println' is not defined. Did you mean: 'print'?
for i in range(len(x)):
    println(x[i], end=' ')

    
Traceback (most recent call last):
  File "<pyshell#207>", line 2, in <module>
    println(x[i], end=' ')
NameError: name 'println' is not defined. Did you mean: 'print'?
for i in range(len(x)):
    print(x[i], end=' ')

    
s p a m 
list[x]
list['spam']
l= [1,2,3,4,5]
for x in l:
    x+=1

    
l
             
[1, 2, 3, 4, 5]
def listt()
SyntaxError: expected ':'
def lis():
    for x in l:
    x+=1
    
SyntaxError: expected an indented block after 'for' statement on line 2
def lis():
    for x in l:
      x+=1
      print(x)

      
lis()
2
3
4
5
6
def lis():
    for x in l:
      x+=1
      print(x, end=' ')

      
lis()
2 3 4 5 6 
x
6
def rectangle(let, h,w):
    for i in range(1,h):
        print(let*w)
        for i in range(h):
            print(let*h)

            
rectangle('H',5,5)
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
def rectangle(let, h,w):
    for i in range(1,h):
        print(let*w)
        for i in range(1,w):
            print(let*h)

            
rectangle('H',5,5)
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
HHHHH
rectangle('H',5,4)
HHHH
HHHHH
HHHHH
HHHHH
HHHH
HHHHH
HHHHH
HHHHH
HHHH
HHHHH
HHHHH
HHHHH
HHHH
HHHHH
HHHHH
HHHHH
KeyboardInterrupt
rectangle('H',1,4)

rectangle('H',2,4)
HHHH
HH
HH
HH
import jupyturtle
Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    import jupyturtle
ModuleNotFoundError: No module named 'jupyturtle'
#lrectangle that take sting and two intigers draws a rectangle , it input hieght and hieght then copy strings by loop based on range hieght and sring multiplication
def rectangle(l,h,w):
    " " " i want to make hieght only make vertical length and width horzontal by string multiplication " " "
       for i in range
       
SyntaxError: unexpected indent
def rectangle(l,h,w):
    " " " i want to make hieght only make vertical length and width horzontal by string multiplication " " "
       for i in range(h):
           
SyntaxError: unexpected indent
def rectangle(l,h,w):
    " " " i want to make hieght only make vertical length and width horzontal by string multiplication " " "
         for i in range(h):
             
SyntaxError: unexpected indent
def rectangle(l,h,w):
    " " " i want to make hieght only make vertical length and width horzontal by string multiplication " " "
              for i in range(h):
                  
SyntaxError: unexpected indent
def rectangle(l,h,w):
         " " " i want to make hieght only make vertical length and width horzontal by string multiplication " " "
         for i in range(1,h):
             print('H'*w )

             
rectangle('H',5,4)
HHHH
HHHH
HHHH
HHHH
def rectangle(l,h,w):
         " " " i want to make hieght only make vertical length and width horzontal by string multiplication, and i used loop only for height and it worked now # I also want to add why is width only 4 instead of five --let i check it by making  w
         =1" " "
         for i in range(1,h):
             print('H'*(1+w) )
             
SyntaxError: unterminated string literal (detected at line 2)
def rectangle(l,h,w):
         " " " i want to make hieght only make vertical length and width horzontal by string multiplication, and i used loop only for height and it worked now # I also want to add why is width only 4 instead of five --let i check it by making  " " "
         for i in range(1,h):
             print('H'*(1+w) )

             
rectangle('L',5,4)
HHHHH
HHHHH
HHHHH
HHHHH
rectangle(l,5,4)
HHHHH
HHHHH
HHHHH
HHHHH
rectangle(5,4)
Traceback (most recent call last):
  File "<pyshell#254>", line 1, in <module>
    rectangle(5,4)
TypeError: rectangle() missing 1 required positional argument: 'w'
rectangle('',5,4)
HHHHH
HHHHH
HHHHH
HHHHH
#I did it mmy secon exercise, that's amzing
#his said make funstion produce verse-- it's content is the same bu only changr is index that counts douwn, so let i beggin
def bottle_verse(n):
    #since only change the index change, ifirst i use four prints with index change
     for i in range(99,90,-1):
         print(f' {i} bottles of beer on the wall')
         print(f' {i} bottles of beer on the wall')print(f' {i} bottles of beer on the wall')
         
SyntaxError: invalid syntax
def bottle_verse(n):
    #since only change the index change, ifirst i use four prints with index change
     for i in range(99,90,-1):
         print(f' {i} bottles of beer on the wall')
         print(f' {i} bottles of beer')
         print('Take onedown,pass it around')
         print(f' {i-1} bottles of beer on the wall')

         
bottle_verse(1)
 99 bottles of beer on the wall
 99 bottles of beer
Take onedown,pass it around
 98 bottles of beer on the wall
 98 bottles of beer on the wall
 98 bottles of beer
Take onedown,pass it around
 97 bottles of beer on the wall
 97 bottles of beer on the wall
 97 bottles of beer
Take onedown,pass it around
 96 bottles of beer on the wall
 96 bottles of beer on the wall
 96 bottles of beer
Take onedown,pass it around
 95 bottles of beer on the wall
 95 bottles of beer on the wall
 95 bottles of beer
Take onedown,pass it around
 94 bottles of beer on the wall
 94 bottles of beer on the wall
 94 bottles of beer
Take onedown,pass it around
 93 bottles of beer on the wall
 93 bottles of beer on the wall
 93 bottles of beer
Take onedown,pass it around
 92 bottles of beer on the wall
 92 bottles of beer on the wall
 92 bottles of beer
Take onedown,pass it around
 91 bottles of beer on the wall
 91 bottles of beer on the wall
 91 bottles of beer
Take onedown,pass it around
 90 bottles of beer on the wall
#since i did it let proceed to chapter four-- functions and interfaces, but i do not know what interfacedesighn mean ?
 
import src
Traceback (most recent call last):
  File "<pyshell#267>", line 1, in <module>
    import src
ModuleNotFoundError: No module named 'src'
import sys
print
<built-in function print>
print(sys.dir)
Traceback (most recent call last):
  File "<pyshell#270>", line 1, in <module>
    print(sys.dir)
AttributeError: module 'sys' has no attribute 'dir'
print(sys.path)
['', 'C:\\Users\\LocalUser\\Documents', 'C:\\Users\\LocalUser\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\idlelib', 'C:\\Users\\LocalUser\\AppData\\Local\\Python\\pythoncore-3.14-64\\python314.zip', 'C:\\Users\\LocalUser\\AppData\\Local\\Python\\pythoncore-3.14-64\\DLLs', 'C:\\Users\\LocalUser\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib', 'C:\\Users\\LocalUser\\AppData\\Local\\Python\\pythoncore-3.14-64', 'C:\\Users\\LocalUser\\AppData\\Local\\Python\\pythoncore-3.14-64\\Lib\\site-packages']

========================================== RESTART: C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtledemo\forest.py ==========================================

================================================================================= RESTART: Shell =================================================================================
42 and true
Traceback (most recent call last):
  File "<pyshell#272>", line 1, in <module>
    42 and true
NameError: name 'true' is not defined. Did you mean: 'True'?
42 and True
True
# i fstatement contains if--> then condition then :
iff 10 > :
    
SyntaxError: invalid syntax
if 10 > 0:
    print("Hello world")

    
Hello world
x=10
y=12
if x==y :
    print('x and y are equale')
    elif x>y:
        
SyntaxError: invalid syntax
if x==y :
    print('x and y are equale')
     elif x>y:
         
SyntaxError: unexpected indent
if x==y :
    print('x and y are equale')
       elif x>y:
           
SyntaxError: unexpected indent
if x==y :
      print('x and y are equale')
         elif x>y:
             
SyntaxError: unexpected indent
if x==y :
    print('x and y are equale')
elif x>y:
    print("xis larger')
          
SyntaxError: unterminated string literal (detected at line 4)
if x==y :
    print('x and y are equale')
elif x>y:
    print('xis larger')
else:
    print("x is less than y")

    
x is less than y
def countdown
SyntaxError: expected '('
def countdown(n):
    if n<=0:
        print('Blstoff!)
              
SyntaxError: unterminated string literal (detected at line 3)
def countdown(n):
    if n<=0:
        print('Blstoff!')
    else :
        print(n)
        countdown(n-1)

        
countdown(5)
5
4
3
2
1
Blstoff!
#recursive example two, by theway- recursive is so important in many app like reptiton loop feuters
#let write a function that print a string n times
def print
SyntaxError: expected '('



def print_n_times(string,n):
    if n > 0:
        print(string)
        print_n_times(string,n-1)

        
print__n_times('recursive', 6)
Traceback (most recent call last):
  File "<pyshell#312>", line 1, in <module>
    print__n_times('recursive', 6)
NameError: name 'print__n_times' is not defined. Did you mean: 'print_n_times'?
print_n_times('recursive', 6)
recursive
recursive
recursive
recursive
recursive
recursive
n =input('waht id your name')
waht id your name
input('what is your name?\n')
what is your name?
melkamu kebde
'melkamu kebde'
y = int(n)
Traceback (most recent call last):
  File "<pyshell#316>", line 1, in <module>
    y = int(n)
ValueError: invalid literal for int() with base 10: ''
n=input('what is\n')
what is
23
y=int(n)
x =  5
y = 6
import turtle
t = turtle.Turtle()
t.forwar(100)
Traceback (most recent call last):
  File "<pyshell#323>", line 1, in <module>
    t.forwar(100)
AttributeError: 'Turtle' object has no attribute 'forwar'. Did you mean: 'forward'?
t.forward(100)
t.left(90)
t.forward(100)
def turtle_d(n):
    if n>=0:
       t.left(n)
t.forward(n)
SyntaxError: invalid syntax
def turtle_d(n):
    if n>=0:
       t.left(n)
       t.forward(n)
       turtle_d(n-1)

       
turtle_d(50)
turtle_d(50)

Traceback (most recent call last):
  File "<pyshell#334>", line 1, in <module>
    turtle_d(50)
  File "<pyshell#332>", line 3, in turtle_d
    t.left(n)
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 1767, in left
    self._rotate(angle)
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 3394, in _rotate
    self._update()
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 2744, in _update
    self._update_data()
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 2730, in _update_data
    self.screen._incrementudc()
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 1320, in _incrementudc
    raise Terminator
turtle.Terminator
t = turtle.Turtle()

turtle_d(50)
turtle_d(150)
t = turtle.Turtle()

Traceback (most recent call last):
  File "<pyshell#338>", line 1, in <module>
    t = turtle.Turtle()
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
t = turtle.Turtle()
turtle_d(360)
Traceback (most recent call last):
  File "<pyshell#340>", line 1, in <module>
    turtle_d(360)
  File "<pyshell#332>", line 5, in turtle_d
    turtle_d(n-1)
  File "<pyshell#332>", line 5, in turtle_d
    turtle_d(n-1)
  File "<pyshell#332>", line 5, in turtle_d
    turtle_d(n-1)
  [Previous line repeated 43 more times]
  File "<pyshell#332>", line 3, in turtle_d
    t.left(n)
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 1767, in left
    self._rotate(angle)
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 3394, in _rotate
    self._update()
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 2744, in _update
    self._update_data()
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 2730, in _update_data
    self.screen._incrementudc()
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\turtle.py", line 1320, in _incrementudc
    raise Terminator
turtle.Terminator
>>> t = turtle.Turtle()
>>> turtle_d(160)
>>> 
=================== RESTART: Shell ==================
>>> #turtle master- turtle is pythons built in drwawing module---prefect ffor begginers to programming through visuale feedback
>>> """ Getting starting to turtle"""
' Getting starting to turtle'
>>> import turtle
>>> screen = turtle.screen()
Traceback (most recent call last):
  File "<pyshell#346>", line 1, in <module>
    screen = turtle.screen()
AttributeError: module 'turtle' has no attribute 'screen'. Did you mean: 'Screen'?
>>> screen = turtle.Screen()
>>> t = turtle.Turtle()
>>> screen.mainloop()
