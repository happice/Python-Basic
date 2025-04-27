# Comparison operators
# The result of the comparison operation is always operation is always True or False
# ==    :   [equal to]
#           True if the same, False if different.

# !=    :   [not equal]
#           True if different, False if the same

# <     :   [less than]
#           True if the right side is larger (excluding equal values), otherwise return False.

# >     :   [greater than]
#           True if the left side is larger (excluding equal values), otherwise return False.

# <=    :   [less than or equal to]
#           True if the right side is larger or equal, otherwise return False.

# >=    :   [greater than or equal to]
#           True if the left side is larger or equal, otherwise False. 

# print(5 != 2)
# print(5 < 2)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# if(condition) :
#   Run if the above condition is True.
# elif(condition):
#   Run elif the above condition is True.
# else : 
#   Run if all the condition are False.

# if    : always use 1
# elif  : use range 0 - infinity
# else  : use 0 or 1
# if can be used by nesting within if. 

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# 100 - 90  : A
# 89 - 70   : B
# 69 - 60   : c
# 59-       : D

# score = int(input())

# if(100 >= score >= 90) :
#     print ('A')
# elif(89 >= score >= 70) :
#     print('B')
# elif(69 >= score >= 60) :
#     print('C')
# elif(59 >= score >= 0) :
#     print ('D')

# print("End")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# age = int(input("Enter your age :"))

# if(age < 12) :
#    print('Sorry, Only over 12 years watch the movie.' )
# elif(age >= 12) :
#    print('Good, Have fun watching.')


# teahcer code: 
# age = int(input("Enter your age : "))

# if(age >= 12) :
#     print('Good, Have fun watching.')
# else :
#     print('Sorry, Only over 12 years watch the movie.' )


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# print("Enter number.")
# number = int(input())

# if(number % 2 == 0 ) :      # Forgot ' == 0' 
#     print('Even')
# elif(number % 2 == 1 ) :
#     print('Odd.')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# not   : If True, the result is reto False. If it is False, the result is reversed to True.
# and   : True if both sides are True, False if even one side is False
# or    : False if both sides are false, True if at least one side is True 
# The execution order is executed in order is executed in the order of not, and, or.

# print(not(1 == 1))
# print((1 != 5) and (10 <= 15))
# print((6 != 6) or (5 == 3)) 

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Nested if
# if can be nested

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# print("Enter two numbers. ")
# number1 = int(input())
# number2 = int(input())

# print("What calculation do you want to run?")
# print("(1: Multiply, 2: Divide, 3: Add, 4: Subtract)")
# number = int(input())
# if(number == 1) :
#     print("Selected multiply,", number1, "*", number2, "=", number1*number2)
# elif(number == 2):
#     print("Selected divide,", number1, "/", number2, "=", number1//number2)
# elif(number == 3):
#     print("Selected add,", number1, "+", number2, "=", number1+number2)
# elif(number == 4):
#     print("Selected subtract,", number1, "-", number2, "=", number1-number2)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
