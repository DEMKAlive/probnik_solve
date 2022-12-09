def find_repeating(arr: list[int]):
    for el in arr:
        if arr.count(el) > 1:
            yield el


def mean_no_repeat(arr: list[int]) -> float:
    repeating = list(set(find_repeating(arr)))
    s = 0
    c = 0
    for i in arr:
        if i not in repeating:
            s += i
            c += 1
    return s / c


def sum_repeat(arr: list[int]) -> int:
    return sum(list(set(find_repeating(arr))))

cnt = 0
with open("9.csv", "r") as f:
    for line in f.readlines():
        line = list(map(int, line[:-1].split(';')))
        if len(set(line)) + 1 != len(line):
            continue
        if mean_no_repeat(line) <= sum_repeat(line):
            cnt += 1
print(cnt)