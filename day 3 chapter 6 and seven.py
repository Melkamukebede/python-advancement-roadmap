Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#chapter seven searching using lopps
for i in 'hwllovbvb bvbbbn':
    print(i, end= ' ')

    
h w l l o v b v b   b v b b b n 
for i in 'hwllovbvb bvbbbn':
    if i== 'e' or i=='E':
    print(i, end= ' ')
    
SyntaxError: expected an indented block after 'if' statement on line 2
for i in 'hwllovbvb bvbbbn':
    if i== 'e' or i=='E':
       print(i, end= ' ')
       print('This word has an "e"')

       
for i in 'hwllovbvb bvbbbn':
    if i== 'e' or i=='E':
       print(i, end= ' ')
       print('This word has an "e"')
    else: print('This word has no an "e"')

    
This word has no an "e"
This word has no an "e"
This word has no an "e"
This word has no an "e"
This word has no an "e"
This word has no an "e"
This word has no an "e"
This word has no an "e"
This word has no an "e"
This word has no an "e"
This word has no an "e"
This word has no an "e"
This word has no an "e"
This word has no an "e"
This word has no an "e"
This word has no an "e"
#let prractice the word comptutions
for i in 'hwlloeveeeebvb bvbbbn':
    if i== 'e' or i=='E':
       print(i, end= ' ')
       print('This word has an "e"')

       
e This word has an "e"
e This word has an "e"
e This word has an "e"
e This word has an "e"
e This word has an "e"
def has_e():
    for i in 'Gadsby':
          if i== 'e' or i=='E':
              return True
            return False
        
SyntaxError: unindent does not match any outer indentation level
def has_e():
    for i in 'Gadsby':
          if i== 'e' or i=='E':
              return True
              return False

            
def has_e():
    for i in 'Gadsby':
          if i== 'e' or i=='E':
              return True
    return False

def has_e(word):
    for i in 'Gadsby':
          if i== 'e' or i=='E':
              return True
    return False

has_e('gadsey')
False
def has_e(word):
    for i in 'Gadsby':
          if i== 'e' or i=='E':
              return True
    return True

has_e('gadsey')
True
def has_e(word):
    for i in 'Gadsby':
          if i== 'e' or i=='E':
              return True
    return False

has_e('gadsey')
False
file_object = open('word.txt')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    file_object = open('word.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'word.txt'
file_object = open('word.txt')
file_object.readline()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    file_object.readline()
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 40: character maps to <undefined>
file_object.readline()
''
file_object.readline()
''
file_object.readline()
''
for line in open('word.txt'):
      word = line.strip()
      print(word)

      
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    for line in open('word.txt'):
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 40: character maps to <undefined>
for line in open('word.txt'):
      word = line.strip()
      print(word)

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    for line in open('word.txt'):
  File "C:\Users\LocalUser\AppData\Local\Python\pythoncore-3.14-64\Lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 40: character maps to <undefined>
for line in open('word.txt', 'r', encoding='utf-8'):
      word = line.strip()
      print(word)

      
To see how many words contain an “e,” we’ll need a word list. The one we’ll use is a
list of about 114,000 official crosswords; that is, words that are considered valid in
crossword puzzles and other word games.
The word list is in a file called words.txt, which is downloaded in the notebook for
this chapter. To read it, we’ll use the built-in function open, which takes the name of
the file as a parameter and returns a file object we can use to read
for line in open('word.txt', 'r', encoding='utf-8'):
      word = line.strip()
      print(word)

      
To see how many words contain an “e,” we’ll need a word list. The one we’ll use is a
list of about 114,000 official crosswords; that is, words that are considered valid in
crossword puzzles and other word games.
The word list is in a file called words.txt, which is downloaded in the notebook for
this chapter. To read it, we’ll use the built-in function open, which takes the name of
the file as a parameter and returns a file object we can use to read
total = 0
count = 0
for line in open('word.txt', 'r', encoding='utf-8'):
      word = line.strip()
      total =  total + 1
      if has_e(word):
           count = count + 1
           
SyntaxError: multiple statements found while compiling a single statement

total = 0
count = 0
for line in open('word.txt', 'r', encoding='utf-8'):
      word = line.strip()
      total =  total + 1
      if has_e(word):
           count = count + 1

           
total
6
count
0
file_object.read()
''
file_object.readlines()
[]
for line in open('word.txt', encoding='utf-8'):
      word = line.strip()
      total =  total + 1
      if has_e(word):
           count = count + 1

           
total
12
total
12
for linee in open('word.txt', encoding='utf-8'):
      word = linee.strip()
      total =  total + 1
      if has_e(word):
           count = count + 1

           
total
18
for linee in open('word.txt', encoding='utf-8'):
      word = linee.strip()
      total =  total + 1
      print(word)
      if has_e(word):
           count = count + 1

           
To see how many words contain an “e,” we’ll need a word list. The one we’ll use is a
list of about 114,000 official crosswords; that is, words that are considered valid in
crossword puzzles and other word games.
The word list is in a file called words.txt, which is downloaded in the notebook for
this chapter. To read it, we’ll use the built-in function open, which takes the name of
the file as a parameter and returns a file object we can use to read
for linee in open('word.txt', encoding='utf-8'):
      word = linee.strip()
      total =  total + 1
      print(word, total)
      if has_e(word):
           count = count + 1

           
To see how many words contain an “e,” we’ll need a word list. The one we’ll use is a 25
list of about 114,000 official crosswords; that is, words that are considered valid in 26
crossword puzzles and other word games. 27
The word list is in a file called words.txt, which is downloaded in the notebook for 28
this chapter. To read it, we’ll use the built-in function open, which takes the name of 29
the file as a parameter and returns a file object we can use to read 30
for linee in open('word.txt', encoding='utf-8'):
      word = linee.strip()
      total =  total + 1
      print(word, total)

      
To see how many words contain an “e,” we’ll need a word list. The one we’ll use is a 31
list of about 114,000 official crosswords; that is, words that are considered valid in 32
crossword puzzles and other word games. 33
The word list is in a file called words.txt, which is downloaded in the notebook for 34
this chapter. To read it, we’ll use the built-in function open, which takes the name of 35
the file as a parameter and returns a file object we can use to read 36
file = open('word.txt', encoding='utf-8', 'r+')
SyntaxError: positional argument follows keyword argument
file = open('word.txt', 'r+', encoding='utf-8')
file.read()
'To see how many words contain an “e,” we’ll need a word list. The one we’ll use is a\nlist of about 114,000 official crosswords; that is, words that are considered valid in\ncrossword puzzles and other word games.\nThe word list is in a file called words.txt, which is downloaded in the notebook for\nthis chapter. To read it, we’ll use the built-in function open, which takes the name of\nthe file as a parameter and returns a file object we can use to read'
file.strip()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    file.strip()
AttributeError: '_io.TextIOWrapper' object has no attribute 'strip'
for linee in open('word.txt', 'r+', encoding='utf-8'):
      word = linee.strip()
      total =  total + 1
      print(word, total)

      
To see how many words contain an “e,” we’ll need a word list. The one we’ll use is a 37
list of about 114,000 official crosswords; that is, words that are considered valid in 38
crossword puzzles and other word games. 39
The word list is in a file called words.txt, which is downloaded in the notebook for 40
this chapter. To read it, we’ll use the built-in function open, which takes the name of 41
the file as a parameter and returns a file object we can use to read 42
for linee in open('word.txt', 'r+', encoding='utf-8'):
      word = linee.strip()
      total =  total + linee
      print(word, total)

      
Traceback (most recent call last):
  File "<pyshell#78>", line 3, in <module>
    total =  total + linee
TypeError: unsupported operand type(s) for +: 'int' and 'str'
for linee in open('word.txt', 'r+', encoding='utf-8'):
      word = linee.strip()
      total =  total + len(linee)
      print(word, total)

      
To see how many words contain an “e,” we’ll need a word list. The one we’ll use is a 127
list of about 114,000 official crosswords; that is, words that are considered valid in 214
crossword puzzles and other word games. 254
The word list is in a file called words.txt, which is downloaded in the notebook for 339
this chapter. To read it, we’ll use the built-in function open, which takes the name of 427
the file as a parameter and returns a file object we can use to read 495
for linee in open('word.txt', 'r+', encoding='utf-8'):
      word = linee.strip()
      total =  total + len(linee)
      print(word, total)

      
To see how many words contain an “e,” we’ll need a word list. The one we’ll use is alist of about 114,000 official crosswords; that is, words that are considered valid incrossword puzzles and other word games.The word list is in a file called words.txt, which is downloaded in the notebook forthis chapter. To read it, we’ll use the built-in function open, which takes the name ofthe file as a parameter and returns a file object we can use to read 943
for linee in open('word.txt', 'r+', encoding='utf-8'):
      word = linee.strip()
      total =  total + len(linee)
      print(word, total)
      if has_e(word):
          count = count + 1

          
To see how many words contain an “e,” we’ll need a word list. The one we’ll use is alist of about 114,000 official crosswords; that is, words that are considered valid incrossword puzzles and other word games.The word list is in a file called words.txt, which is downloaded in the notebook forthis chapter. To read it, we’ll use the built-in function open, which takes the name ofthe file as a parameter and returns a file object we can use to read 1391
count
0
def has_e(word):
    for i in word:
          if i== 'e' or i=='E':
              return True
    return False

has_e('rfhtgyju')
False
has_e('rfhtgyjuee')
True
for linee in open('word.txt', 'r+', encoding='utf-8'):
      word = linee.strip()
      total =  total + len(linee)
      print(word, total)
      if has_e(word):
          count = count + 1

          
To see how many words contain an “e,” we’ll need a word list. The one we’ll use is alist of about 114,000 official crosswords; that is, words that are considered valid incrossword puzzles and other word games.The word list is in a file called words.txt, which is downloaded in the notebook forthis chapter. To read it, we’ll use the built-in function open, which takes the name ofthe file as a parameter and returns a file object we can use to read 1839
count
1
file.count('a')
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    file.count('a')
AttributeError: '_io.TextIOWrapper' object has no attribute 'count'
def csl(filename,targl):
       with open(filename,'r', encoding='utf-8') as file:
           content = file.read().lower()

           
def csl(filename,targl):
       with open(filename,'r', encoding='utf-8') as file:
           content = file.read().lower()

        
def csl(filename,targl):
       with open(filename,'r', encoding='utf-8') as file:
           content = file.read().lower()
           for letter in targl:
               count = content.count(letter.lower())
               print(f' {letter} : {count}')

               
csl(word.txt, e)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    csl(word.txt, e)
AttributeError: 'str' object has no attribute 'txt'
csl('word.txt',' e')
   : 80
 e : 41
word =  open(filename,'r', encoding='utf-8')
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    word =  open(filename,'r', encoding='utf-8')
NameError: name 'filename' is not defined
word =  open(word.txt,'r', encoding='utf-8')
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    word =  open(word.txt,'r', encoding='utf-8')
AttributeError: 'str' object has no attribute 'txt'
word =  open('word.txt','r', encoding='utf-8')
'e' in word
False
n = 'wwfefrbr'
'e' in n
True
content=word.read().lower()
'e' in content
False
print(content)

content=word.read()
print(content)


print(word)
<_io.TextIOWrapper name='word.txt' mode='r' encoding='utf-8'>
def has_e(word):
    return 'e' in word.lower()

for line in open('word.txt', 'r+', encoding='utf-8'):
      word = line.strip()
      total =  total + 1
      if has_e(word):
          count = count + 1
print(total)
SyntaxError: invalid syntax
for line in open('word.txt', 'r+', encoding='utf-8'):
      word = line.strip()
      total =  total + 1
      if has_e(word):
          count = count + 1

          
print(total)
1840
print(count)
2
for line in open('word.txt',  encoding='utf-8'):
      word = line.strip()
      if word:
           total =  total + 1
           if has_e(word):
          count = count + 1
          
SyntaxError: unindent does not match any outer indentation level
for line in open('word.txt',  encoding='utf-8'):
      word = line.strip()
      if word:
           total =  total + 1
           if has_e(word):
               count = count + 1

          
print(count)
3
total = 0
count = 0
for line in open('word.txt',  encoding='utf-8'):
      word = line.strip()
      if word:
           total =  total + 1
           if has_e(word):
               count = count + 1


print(count)
1
total_words = 0
total_letter_e=0
for line in open('word.txt',  encoding='utf-8'):
      word = line.strip()
       total_words + =1
         e_c= word.count('e)
          total_letter_e += e_c
                         
SyntaxError: unexpected indent
for line in open('word.txt',  encoding='utf-8'):
      word = line.strip()
      total_words + =1
      e_c= word.count('e)
      total_letter_e += e_c
                      
SyntaxError: unterminated string literal (detected at line 4)
for line in open('word.txt',  encoding='utf-8'):
      word = line.strip()
      total_words + =1
      e_c= word.count('e')
      total_letter_e += e_c
                      
SyntaxError: invalid syntax
for line in open('word.txt',  encoding='utf-8'):
      word = line.strip()
      total_words +=1
      e_c= word.count('e')
      total_letter_e += e_c

                      
print(e_c)
                      
41
print(total_letter_e)
                      
41
KeyboardInterrupt
print(total_words)
                      
1
for line in open('word.txt',  encoding='utf-8'):
      word = line.strip()
      total_words + =1
      e_c= word.count('e')
      total_letter_e += e_c
                      
SyntaxError: invalid syntax
for line in open('word.txt',  encoding='utf-8'):
      word = line.strip()
      total_words +=1
      e_c= word.count('e')
      total_letter_e += e_c

        
for line in open('word.txt',  encoding='utf-8'):
      word = line.strip()
      total_words +=1
      e_c= word.count('e')
      total_letter_e += e_c
                      print(e_c)
                      
SyntaxError: unexpected indent
for line in open('word.txt',  encoding='utf-8'):
      word = line.strip()
      total_words +=1
      e_c= word.count('e')
      total_letter_e += e_c
                      print(e_c)
                      
SyntaxError: unexpected indent
KeyboardInterrupt
for line in open('word.txt',  encoding='utf-8'):
      word = line.strip()
      total_words +=1
      e_c= word.count('e')
      total_letter_e += e_c
      print(e_c)

                      
41
for line in open('word.txt',  encoding='utf-8'):
      word = line.strip()
      total_words =   total_words +1
      e_c= word.count('e')
      total_letter_e += e_c
      print(e_c)
       print(total_words)
                      
SyntaxError: unexpected indent
for line in open('word.txt',  encoding='utf-8'):
      word = line.strip()
      total_words =   total_words +1
      e_c= word.count('e')
      total_letter_e += e_c
      print(e_c)
      print(total_words)

                      
41
4
# to find total letter len(Word) and count total specfic letter by word.count()
                      
# here is breifest way for both
                      
total = sum(len(line.strip()) for line in open('word.txt',  encoding='utf-8'))
                      
total
                      
448
count = sum(line.count('e') for line in open('word.txt',  encoding='utf-8'))
                      
count
                      
41
# let proceed to searching
                      
#it uses two parameter , first word or file and second specific word
                      
def uses_any(word, letters)
SyntaxError: expected ':'
def uses_any(word, letters):
       for letter in word.lower():
           if letter in letters.;ower():
               
SyntaxError: invalid syntax
>>> def uses_any(word, letters):
...        for letter in word.lower():
...            if letter in letters.ower():
...                return True
...             return False
...         
SyntaxError: unindent does not match any outer indentation level
>>> def uses_any(word, letters):
...        for letter in word.lower():
...            if letter in letters.ower():
...                return True
...       return False
...     
SyntaxError: unindent does not match any outer indentation level
>>> def uses_any(word, letters):
...        for letter in word.lower():
...            if letter in letters.ower():
...                return True
...       return False
...     
SyntaxError: unindent does not match any outer indentation level
>>> def uses_any(word, letters):
...        for letter in word.lower():
...            if letter in letters.ower():
...                return True
...        return False
... 
...     
>>> uses_any('trytheeiuthgjhuhuiteurwyfgdg','aio')
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    uses_any('trytheeiuthgjhuhuiteurwyfgdg','aio')
  File "<pyshell#176>", line 3, in uses_any
    if letter in letters.ower():
AttributeError: 'str' object has no attribute 'ower'. Did you mean: 'lower'?
>>> def uses_any(word, letters):
...        for letter in word.lower():
...            if letter in letters.lower():
...                return True
...        return False
... 
...     
>>> uses_any('trytheeiuthgjhuhuiteurwyfgdg','aio')
... 
True
