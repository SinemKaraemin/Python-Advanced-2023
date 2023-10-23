nums = input().split()
len_of_first_set = int(nums[0])
len_of_second_set = int(nums[1])

first_set = set()
second_set = set()

for _ in range(len_of_first_set):
    num = int(input())
    first_set.add(num)

for _ in range(len_of_second_set):
    num2 = int(input())
    second_set.add(num2)

difference_between_sets = (first_set.intersection(second_set))

for different_set in difference_between_sets:
    print(different_set)