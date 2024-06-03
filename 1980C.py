def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    m = int(input())
    d = [int(x) for x in input().split()]
    changes = {}
    for x in d:
        if x not in changes:
            changes[x] = 1
        else:
            changes[x] += 1
    for i in range(n):
        if a[i] == b[i]:
            continue
        if b[i] not in changes:
            print("NO")
            return
        changes[b[i]] -= 1
        if changes[b[i]] == 0:
            changes.pop(b[i])
    if d[m-1] not in b:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        solve()
