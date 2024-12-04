from collections import defaultdict
from typing import Dict, List


left_side: List[int] = list()
right_side: Dict[int, int] = defaultdict(int)

with open("input.txt", "r") as f:
    for line in f.readlines():
        left_num, right_num = line.split()
        right_num = int(right_num)

        left_side.append(int(left_num))
        right_side[right_num] += 1


sim_score = 0

for num in left_side:
    if num in right_side:
        sim_score += num * right_side[num]
print(sim_score)
