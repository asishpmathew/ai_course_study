#Use == for values
# Use is only for identity (mostly with None)

a = 10
b = 10

print(a == b)  # True
print(a is b)  # True (small integers are cached)

print("---")

a = 1000
b = 1000

print(a == b)  # True
print(a is b)  # Usually False

print("---")

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)  # True (same content)
print(list1 is list2)  # False (different objects)


# Using "not" before a boolean expression inverts it:
second_number = None
if not second_number:
    print("6")