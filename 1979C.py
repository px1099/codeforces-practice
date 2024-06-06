def solve():
    a = 16 * 9 * 5 * 7 * 11 * 13 * 17 * 19
    n = int(input())
    k = [int(x) for x in input().split()]
    bets = [a//x for x in k]
    if sum(bets) >= a:
        print(-1)
        return
    print(" ".join([str(x) for x in bets]))


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        solve()
