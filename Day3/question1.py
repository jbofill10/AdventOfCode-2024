import re


def mul(phrase: str) -> int:
    num1, num2 = phrase.split(",")

    return int(num1[num1.index("(") + 1 :]) * int(num2[:-1])


mul_search = re.compile(r"mul\(\d{1,3},\d{1,3}\)")

with open("input.txt", "r") as f:
    total = 0
    results = mul_search.findall(f.read())

    for res in results:
        total += mul(res)
    print(total)
