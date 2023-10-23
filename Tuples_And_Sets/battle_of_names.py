odd_numbers = set()
even_numbers = set()

for row in range(1, int(input()) + 1):
    ascii_sum_of_name = sum(ord(letter) for letter in input()) // row

    if ascii_sum_of_name % 2 == 0:
        even_numbers.add(ascii_sum_of_name)
    else:
        odd_numbers.add(ascii_sum_of_name)

if sum(odd_numbers) == sum(even_numbers):
    print(*odd_numbers.union(even_numbers), sep=', ')
elif sum(odd_numbers) > sum(even_numbers):
    print(*odd_numbers.difference(even_numbers), sep=', ')
else:
    print(*odd_numbers.symmetric_difference(even_numbers), sep=', ')
