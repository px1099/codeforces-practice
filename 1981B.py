def solve():
    n, m = (int(x) for x in input().split())
    z = max(0, n-m) ^ (n+m)
    count = 0
    while z > 0:
        z = z >> 1
        count += 1
    result = (n + m) | ((1 << count) - 1)
    print(result)


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        solve()
