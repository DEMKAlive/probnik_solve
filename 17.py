seq = []


def split_chunks(arr: list, n: int) -> list:
    return [arr[i:i + n] for i in range(0, len(arr), n)]


with open("17.txt", "r") as f:
    for line in f.readlines():
        seq.append(int(line[:-1]))
me = max(map(lambda x: 0 if x % 10 != 3 else int(x) ** 2, seq))
pairs = []
seq = split_chunks(seq, 2)
for pair in seq:
    s = pair[0] ** 2 + pair[1] ** 2
    if not (any(map(lambda x: x % 10 == 3, pair)) and not all(map(lambda x: x % 10 == 3, pair))):
        continue
    if s < me:
        continue
    pairs.append(s)
print(len(pairs), max(pairs))