# 4096 - 32767
c = 0
for i in range(4096, 32768):
    i = str(i)
    if i.count('6') != 1:
        continue
    ind = i.index('6')
    if ind == 0:
        if i[ind] % 2 == 0:
            c += 1
            continue
    if ind == len(i) - 1:
        if i[ind-1] % 2 == 0:
            c += 1
            continue
    if i[ind - 1] % 2 == 0 and i[ind + 1] % 2 == 0:
        c+= 1

print(c)