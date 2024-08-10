def solve():
    xc, yc, k = (int(z) for z in input().split())
    for i in range(1, k//2 + 1):
        x = xc - i
        y = yc - i
        print(f"{x} {y}")
    for i in range(1, k//2 + 1):
        x = xc + i
        y = yc + i
        print(f"{x} {y}")
    if k % 2 == 1:
        print(f"{xc} {yc}")


if __name__ == "__main__":
    tc = 1
    tc = int(input())
    for _ in range(tc):
        solve()
