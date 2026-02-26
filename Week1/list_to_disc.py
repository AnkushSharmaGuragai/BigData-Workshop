# Two lists
list_one = ['one', 'two', 'three']
list_two = [1, 2, 3]

my_dict = {}

# lopping with index
for i in range(len(list_one)):
    my_dict[list_one[i]] = list_two[i]

print("list combined disctionatry", my_dict)