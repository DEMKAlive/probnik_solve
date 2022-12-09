# 4096 - 32767
c = 0
for i in range(4096, 32768):
    i = oct(i)[2:]
    i = list(map(int, str(i)))
    if i.count(6) != 1:
        continue
    ind = i.index(6)
    if ind != 0:
        if ind != len(i) - 1:
            c += 1 if i[ind - 1] % 2 == 0 and i[ind + 1] % 2 == 0 else 0
        else:
            c += 1 if i[ind - 1] % 2 == 0 else 0
    else:
        c += 1 if i[ind + 1] % 2 == 0 else 0


print(c)
