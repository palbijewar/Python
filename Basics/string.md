# String in python
strings are immutable
    String types : " " , ' ' , " ' ' ", ` `

    >>> chai = "ginger chai"
>>> print(chai)
ginger chai
>>> chai = "masala chai"
>>> first_char = chai[0]
>>> first_char
'm'
>>> chai      
'masala chai'
>>> slice_chai = chai[0:6]
>>> slice_chai 
'masala'
>>> num_list = "0123456789"
>>> num_list[3:7]
'3456'
>>> num_list[3:7:2]
'35'
>>> num_list = "0123456789"
>>> num_list[0:7:2] 
'0246'
>>>
>>> chai
'masala chai'
>>> print(chai.lower())
masala chai
>>> print(chai.upper()) 
MASALA CHAI
>>> chai
'masala chai'
>>> chai = "             masala chai         "
>>> chai
'             masala chai         '
>>> print(chai.strip()) 
masala chai
>>>
>>> print(chai.strip().replace("masala", "ginger"))
ginger chai
>>> chai = "Lemon, Ginger, Masala, Mint"
>>> print(chai.split(,)) 
  File "<stdin>", line 1
    print(chai.split(,))
                     ^
SyntaxError: invalid syntax
>>> print(chai.split(","))
['Lemon', ' Ginger', ' Masala', ' Mint']
>>> print(chai.split(", "))
['Lemon', 'Ginger', 'Masala', 'Mint']
>>> chai = "Masala Chai"
>>> print(chai.find("Chai"))
7
>>> print(chai.find("chai")) 
-1
>>> chai = "Masala Chai Chai Chai"
>>> print(chai.count("chai"))      
0
>>> print(chai.count("Chai"))  
3
>>> chai_type = "Masala"
>>> quantity = 2
>>> order = "I ordered {} cups of {}!"
>>> print(order.format(quantity, chai_type))
I ordered 2 cups of Masala!
>>> order = "I ordered {} cups of {} coffee!"
>>> chai_type = "Capaccino"                   
>>> print(order.format(quantity, chai_type))  
I ordered 2 cups of Capaccino coffee!
>>> coffee_variety = ["latte", "mocha", "iced"]
>>> print(" ".join(coffee_variety))
latte mocha iced
>>> print(len(chai))
21
>>> chai = "He said, \"I am beauty queen\" "
>>> chai
'He said, "I am beauty queen" '
>>> chai = "Masala\nChai
  File "<stdin>", line 1
    chai = "Masala\nChai
           ^
SyntaxError: unterminated string literal (detected at line 1)     
>>> chai = "Masala\nChai"
>>> chai
'Masala\nChai'
>>> chai = r"Masala\nchai"
>>> chai
'Masala\\nchai'
>>> chai = r"c:\user\pwd"
>>> chai
'c:\\user\\pwd'