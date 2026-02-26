# list ko example
this_list = [1, 2, 3, 4, 2, 5, 3]

# Loop through the list
for i in this_list:
    if this_list.count(i) > 1:  # Check if item is duplicate
        this_list.remove(i)      # Remove the first occurrence
        break                     # Stop after removing first duplicate

print("new List dulicate hateye paxi:", this_list)