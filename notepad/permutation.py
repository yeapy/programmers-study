from itertools import permutations

numbers = [1, 2, 3]

my_list = list(permutations(numbers, 2))
answer = []
for number in my_list:
    answer.append(''.join(map(str, number)))

answer = list(map(int, answer))
answer.sort()
print(answer)