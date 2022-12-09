import math

base_str = ""


def is_prime(num: int) -> bool:
    a = 2
    while a <= math.sqrt(num):
        if num % a < 1:
            return False
        a = a + 1
    return num > 1


def found(what: str) -> bool:
    return what in base_str


def replace(what: str, for_what: str) -> None:
    global base_str
    base_str = base_str.replace(what, for_what)


def execute(n: int) -> bool:
    global base_str
    base_str = f">{39 * '0'}{n * '1'}{39 * '2'}"
    while found(">1") or found(">2") or found(">0"):
        if found(">1"):
            replace(">1", "22>")
        if found(">2"):
            replace(">2", "2>")
        if found(">0"):
            replace(">0", "1>")
    return is_prime(sum(map(lambda x: int(x) if x != '>' else 0, list(base_str))))


for i in range(10000):
    if execute(i):
        print(i)
        break
