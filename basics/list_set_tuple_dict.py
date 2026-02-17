test_list = [1, "12", 12, "arun"]
test_set = {1, "12", 12, "arun"}

print(10 in test_set)

print("---")
print(list(test_set)[1])

print("---")
for item in test_set:
    print(item)


#list
print("---")

numbers = [1, 2, 3, 2]
numbers.append(4)
print(numbers[0])   # Indexing allowed

#tuple - immutable
coords = (10, 20)
print(coords[0])  # Works

#set
nums = {1, 2, 3, 3}
print(nums)   # {1, 2, 3}

#dict
person = {
    "name" : "asish",
    "age": 35,
    "status" : "live"
}

print(person["status"])