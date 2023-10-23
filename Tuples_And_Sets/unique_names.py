num_of_names = int(input())
name = [input() for _ in range(num_of_names)]
unique = {n for n in name}

for current_name in unique:
    print(current_name)