# to create a dictionary
my_dict = {}

# now populate it
for i in range(97, 97 + 26):
    # map character to ascii value
    my_dict[chr(i)] = i

print(my_dict)