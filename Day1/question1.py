from typing import List


left_side: List[int] = list()
right_side: List[int] = list()

with open("input.txt", "r") as f:
    for line in f.readlines():
        left_num, right_num = line.split()

        left_side.append(int(left_num))
        right_side.append(int(right_num))


left_side.sort()
right_side.sort()

dist = 0
print(left_side, right_side)
for left_num, right_num in zip(left_side, right_side):
    dist += abs(left_num - right_num)

print(dist)
