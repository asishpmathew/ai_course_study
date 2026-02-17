numbers = []
strings = []
names = ["John", "Eric", "Jessica"]



for item in names:
    if isinstance(item, int):
        numbers.append(item)
    elif isinstance(item, str):
        strings.append(item)

# write your code here
second_name = strings[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)