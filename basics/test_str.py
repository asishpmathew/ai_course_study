# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), 
# together with a format string, which contains normal text together with "argument specifiers", 
# special symbols like "%s" and "%d".

#Hello John Doe. Your current balance is $53.44.
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current is $%.2f"

#pass it as tuple
print(format_string % (data[0], data[1],data[2]))

print(format_string % data)
print(format_string % data)

first, last, balance = data
print(f"Hello {first} {last}. Your current is ${balance}")

print("---")

#String functions
test_string="hello world"
print(test_string.index("w"))
print(test_string.count("l"))
print(test_string[3:7])
print(test_string[3:7:-1])
print(test_string[7:3:-1])
print((test_string[7:3:-1]).upper())
print((test_string[7:3:-1]).split(" "))


print("--- not testes---")
s = "Hey thera! what shou"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" % s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
