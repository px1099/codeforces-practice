def solve():
    _, r = (int(x) for x in input().split())
    score = 0
    while r > 1:
        r = r // 2
        score += 1
    print(score)


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        solve()
