name = "John"
age = 23
#and , or, in

#The "in" operator could be used to check if a specified object exists within
# an iterable object container, such as a list:

if name == "John" and age == 23:
    print("success")


#A statement is evaulated as true if one of the following is correct: 1.
# The "True" boolean variable is given, or calculated using an expression,
# such as an arithmetic comparison. 2. An object which is not considered "empty" is passed.
#Here are some examples for objects which are considered as empty: 1. An empty string: ""
# 2. An empty list: [] 3. The number zero: 0 4. The false boolean variable: False
test_list =[1, 2, 3]
if test_list:
    print('success')
