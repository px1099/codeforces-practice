def solve():
    _, f, k = (int(x) for x in input().split())
    a = [int(x) for x in input().split()]
    value = a[f-1]
    g_count = 0
    ge_count = 0
    for x in a:
        if x > value:
            g_count += 1
        if x >= value:
            ge_count += 1
    if g_count >= k:
        print("NO")
    elif ge_count <= k:
        print("YES")
    else:
        print("MAYBE")


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        solve()
