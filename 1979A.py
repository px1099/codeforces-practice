def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    k = 1000000000
    for i in range(n-1):
        if k >= max(a[i], a[i+1]):
            k = max(a[i], a[i+1]) - 1
    print(k)


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        solve()
