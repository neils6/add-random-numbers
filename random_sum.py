import random
# create an empty list
my_list = []
my_list_2 = []
my_list_3 = []

# fill the list with values
for x in range(1, 11):
    my_list.append(x)

# Loop through my_list and sum random number + nth element value
for item in my_list:
    my_list_2.append(item + random.randint(-1000, 1000))

# print result
print(my_list_2)

index = 0
for number in range(1, 11):
    my_list_3.append(my_list_2[index] - number)
    index += 1

print('Random number values: ', my_list_3)
