sample_dict = { "name": "Anderson","age": 35, "salary": 5000, "city": "London"}

keys = ["name", "salary"]

new_dict = {k: sample_dict[k] for k in keys}

print("New Dictionary:", new_dict)