def solve():
    _, m = (int(x) for x in input().split())
    problems = "ABCDEFG"
    counts = {x: 0 for x in problems}
    bank = input()
    for x in bank:
        counts[x] += 1
    result = 0
    for x in counts:
        if counts[x] < m:
            result += (m - counts[x])
    print(result)


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        solve()
