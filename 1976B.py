def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    result = 0
    val_within = False
    closest_val = 2000000000
    for i in range(n):
        if a[i] <= b[n] <= b[i] or a[i] >= b[n] >= b[i]:
            val_within = True
        if abs(a[i] - b[n]) < abs(closest_val - b[n]):
            closest_val = a[i]
        if abs(b[i] - b[n]) < abs(closest_val - b[n]):
            closest_val = b[i]
        result += abs(a[i] - b[i])
    if not val_within:
        result += abs(closest_val - b[n])
    result += 1
    print(result)


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        solve()
