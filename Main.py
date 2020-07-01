print("hello")  # два пробела между кодом и комментарием

# BASIC TYPES OF DATA ==================================================================================================

# Strings
print("")  # empty string
print("string")  # one word
print("Hello, world!")  # a sentence

print('a')  # single character
print('1234')  # a sequence of digits
print('Bonjour, le monde!')  # a sentence

# Numerical types
print(11)  # prints 11 - integer type
print(11.0)  # prints 11.0 - float type

print(0)  # prints 0
print(-5)  # prints -5 - negative integer type
print(-1.03)  # prints -1.03 - negative float type

# Printing types
print(type('hello'))  # <class 'str'>
print(type("world"))  # <class 'str'>

print(type(100))  # <class 'int'>
print(type(-50))  # <class 'int'>

print(type(3.14))  # <class 'float'>
print(type(-0.5))  # <class 'float'>

# Basic operations

print(10 + 10)  # 20
print(100 - 10)  # 90
print(10 * 10)  # 100
print(77 / 10)  # 7.7
print(77 // 10)  # 7

print(-10)  # -10
print(-(100 + 200))  # -300
print(-(-20))  # 20

print(7 % 2)  # 1, because 7 is an odd number
print(8 % 2)  # 0, because 8 is an even number

# Divide the number by itself
print(4 % 4)  # 0
# At least one number is a float
print(11 % 6.0)  # 5.0
# The first number is less than the divisor
print(55 % 77)  # 55
# With negative numbers, it preserves the divisor sign
print(-11 % 5)  # 4
print(11 % -5)  # -4

# Typing in Phyton
print(125 + 125)  # "250"

print("125" + "125")  # "125125"

print(125 * 4)  # "500"

print("125" * 4)  # "125125125125"

print("This is a number:", 125)  # "This is a number: 125"

# Explict time casting
f = 3.14  # the type is float
print(type(f))  # <class 'float'>

s = str(f)  # converting float to string
print(type(s))  # <class 'str'>

i = int(f)  # while converting a float value to an integer its fractional part is discarded
print(i)  # 3
print(type(i))  # <class 'int'>

f = float(i)
print(f)  # 3.0
print(type(f))  # <class 'float'>

# Built-in functions

number = "111"

# finding the length of an object
print(len(number))  # 3

# converting types
integer = int(number)
float_number = float(number)
print(str(float_number))  # "111.0"

# adding and rounding numbers
my_sum = sum((integer, float_number))

print(my_sum)  # 222.0
print(round(my_sum))  # 222

# finding the minimum and the maximum
print(min(integer, float_number))  # 111
print(type(max(integer, float_number, my_sum)))  # <class 'float'>

# Taking input

user_name = input()
print('Hello, ' + user_name)

user_name = input('Please, enter your name: ')
print('Hello, ' + user_name)

day = int(input())  # 4
month = input()  # October
print('Cinnamon roll day is celebrated on', month, day)
# Cinnamon roll day is celebrated on October 4

# Basic strings methods

message = "bonjour and welcome to Paris!"

print(message.upper())  # BONJOUR AND WELCOME TO PARIS!
# `message` is not changed
print(message)  # bonjour and welcome to Paris!

title_message = message.title()
# `title_message` contains a new string with all words capitalized
print(title_message)  # Bonjour And Welcome To Paris!

print(message.replace("Paris", "Lyon"))  # bonjour and welcome to Lyon!
replaced_message = message.replace("o", "!", 2)
print(replaced_message)  # b!nj!ur and welcome to Paris!

# again, the source string is unchanged, only its copy is modified
print(message)  # bonjour and welcome to Paris!

whitespace_string = "     hey      "
normal_string = "incomprehensibilities"

# delete spaces from the left side
whitespace_string.lstrip()  # "hey      "

# delete "i" or "s" or "is" from the left side
normal_string.lstrip("is")  # "ncomprehensibilities"

# delete spaces from the right side
whitespace_string.rstrip()  # "     hey"

# delete "i" or "s" or "is" from the right side
normal_string.rstrip("is")  # "incomprehensibilitie"

# no spaces from both sides
whitespace_string.strip()  # "hey"

# delete trailing "i" or "s" or "is" from both sides
normal_string.strip("is")  # "ncomprehensibilitie"

word = "Mississippi"
print(word.lstrip("ips"))  # "Mississippi"
print(word.rstrip("ips"))  # "M"
print(word.strip("Mips"))  # ""

sentence = "London is the capital of Great Britain."
sentence = sentence.lower()
sentence.upper()
sentence = sentence.replace("a", "x", 2)
sentence.capitalize()

print(sentence)

# Задача из заданий
one_cup_water = 200
one_cup_milk = 50
one_cup_coffee = 15
cups_quantity = int(input())

print(str(cups_quantity * one_cup_water) + " ml of water")
print(str(cups_quantity * one_cup_milk) + " ml of milk")
print(str(cups_quantity * one_cup_coffee) + " g of coffee beans")

# Проверка на тип
# isinstance(car,int) True или False
# id(x) выводит id можно определить ссылаются ли на одну ячейку в памяти
