strs = ["flower", "flow", "flight"]
my_dict = {index:value for index, value in enumerate(strs)}
#print(my_dict)
for i, value in my_dict.items():
    for j in range(i + 1, len(my_dict)):
        if value.startswith(my_dict[j]):
            print(f"{value} starts with {my_dict[j]}")
        elif my_dict[j].startswith(value):
            print(f"{my_dict[j]} starts with {value}")