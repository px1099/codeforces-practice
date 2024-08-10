def solve():
    n = int(input())
    p = [int(x) for x in input().split()]
    result = ""
    if n > 1:
        result = " ".join(str(x) for x in p[1:])
        result += " "
    result += str(p[0])
    print(result)


if __name__ == "__main__":
    tc = 1
    tc = int(input())
    for _ in range(tc):
        solve()
