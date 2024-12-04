import re


mul_search = re.compile(r"mul\(\d{1,3},\d{1,3}\)")

disable_mul = "don't()"
enable_mul = "do()"

# Tracks state of enabled and disabled mul statement
should_mul = True


def mul(phrase: str) -> int:
    num1, num2 = phrase.split(",")

    return int(num1[num1.index("(") + 1 :]) * int(num2[:-1])


with open("input.txt", "r") as f:

    total = 0
    memory = f.read()
    filtered_memory = ""
    results = mul_search.findall(f.read())

    for idx in range(len(memory)):
        if idx >= 6:
            if memory[idx] == ")":
                if memory[idx - 6 : idx + 1] == disable_mul:
                    should_mul = False
                if memory[idx - 3 : idx + 1] == enable_mul:
                    should_mul = True
        if should_mul:
            filtered_memory += memory[idx].strip()

    results = mul_search.findall(filtered_memory)
    for res in results:
        total += mul(res)
print(total)
