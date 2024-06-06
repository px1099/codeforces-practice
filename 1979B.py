def solve():
    x, y = (int(x) for x in input().split())
    m = 0
    while (x%2) == (y%2):
        m += 1
        x = x >> 1
        y = y >> 1
    print(1 << m)


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        solve()
