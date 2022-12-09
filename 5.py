def make_number(n: int) -> int:
    n = bin(n)[2:]
    n = f"10{n[2:]}0" if sum(map(int, n)) % 2 == 0 else f"11{n[2:]}1"
    return int(n, base=2)


for i in range(1000000):
    if make_number(i) > 40:
        print(i)
        break
