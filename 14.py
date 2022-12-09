alph = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']
for x in alph:
    if (int(f"123{x}5", base=15) + int(f"1{x}233", base=15)) % 14 == 0:
        print(x)
        print((int(f"123{x}5", base=15) + int(f"1{x}233", base=15)) // 14)
        break
