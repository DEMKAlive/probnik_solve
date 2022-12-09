seq = []


def split_chunks(arr: list, n: int) -> list:
    return [arr[i:i + n] for i in range(0, len(arr), n)]


with open("17.txt", "r") as f:
    for line in f.readlines():
        seq.append(int(line[:-1]))
me = max(map(lambda x: 0 if x[-1] != 3 else int(x)**2))

seq = split_chunks(seq, 2)
for pair in seq:
    s = pair[0]**2 + pair[1]**2
