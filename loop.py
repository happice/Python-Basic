# for variable in range (start, end, step) :
#     code to loop 

# ranger(start, end, step) where start, end, step are numbers [ex. range(1, 5, 2)]
# From the start to end-1(end not included), put the increased/decreased value by step into a variable and loop.
# Don't necessarily have to enter the start and step.'
# If start is not entered, 0
# If step is not entered, 1
# range(5)        => start and step not entered 
# range(0, 5)     => step not entered
# range(0, 5, 1)  => standard


# for i in range(0, 5, 1): #repeats 5 times with i taking values 0, 1, 2, 3, 4
#     print(i)             #use variable in the repeated code

# for i in range(0, 5, 1):
#     print('hello')      #do not use variable in the repeated code   

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# Print odd number from 1 to 100
# for i in range(1, 100, 2):
#     print(i)


# print multiples of 5 from 5 to 100
# for i in range(5, 101, 5):
#     print(i)

# print perfect square up to 10000, print (x*x)

for x in range(1,101,1): # did not put 101 but instead put something else
    print(x*x)