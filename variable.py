# variable = value 
#Save the value in variable in the format above
# = Unlike the meaning of the symbol, the value is simply stored in a variable 
# Variable can be whatever you want as long as you follow the rules below 
# 1. Impossible to start with a number 
# 2. Special characters are not possible execpt the symbol "_"
# 3. No Spaing
# 4. Reserved words not possible 

# my_name = "Alice"


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Data types
# str   -> String       => made up of quotes " "  ' '
# float -> Float        => no quotes and has a decimal point
#  int  -> Integer      => no quotes and no decimal point
# Everyday words (English, Chinese, Korean, etc.) without quotes => error

# a = 10      # saves the integer 10 in the variable a 
# b= 'cit'    # saves the string 'cit' in the variable b

# name = 'Alice'
# age = 10
# height = 145


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print('text' or variable or numer)
# The print() function prints the 'text', number, or value of
# the variable inside the bracket and then adds a newline
# To print ,multiple items, use a comma (,)
# If you use print() with nothing inside, it prints an empty line

# name = 'Alice'
# age = 10
# height = 145
# school = 'YISS' 
# print(name)
# print()         # print an empty line
# print(age)
# print(height)
# print('hi')
# print()
# print(5)
# print(5*10)
# print(name, age, height, "hello")



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# input('text' or value or variable)
# Displays 'text' or the value of the variable, then waits for the keyboard input until Enter is pressed
#'text' or variable can be left out
# variable = input('text' or variable)
# Usually used in this format, without variable it the input value is not saved
# input() always saves the value as a str data type

var1 = 2
var2 = input("Insert anything :")

print(type(var2))

var2= int(var2)
print(type(var2))

sum = var1 + var2
print(sum)



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# Type casting 
# str(variable or value)     => converts variable or value to str data type 
# float(variable or value)   => converts variable or value to float data type
# int(variable or value)     => converts variable or value to int data type
# Just using them in calculations doesn't change the original variable's data type
# To change the original variable's data type, save it back into the variable [ ex. a = int(a) ]

# var1 = 2 
# var2 = '31'
# result = var1 + int(var2)   # saves var1 + var2 converted to int in result
# print(result)
# print(type(var2))
# var2 = int(var2)
# print(type(var2))

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# print('Hello. Enter your name.')
# name = input()  # variable = input

# print("Welcome.", name, ", Enter your age.")    # Use comma to seperate

# age = input()
# year = 2025 - int(age) 

# print("You were born in", year, '! Enter you height.')
# height = int(input())

# two_m = 200 - height
# print("There are", two_m, "cm left until 2m")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #