import random
# create an empty list
my_list = []
my_list_2 = []

# fill the list with values
for item in range(1, 11):
    my_list.append(item)

# Loop through my_list and sum random number + nth element value
for item in my_list:
    my_list_2.append(item + random.randint(-1000, 1000))

# print result
print(my_list_2)
