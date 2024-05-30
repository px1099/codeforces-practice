def solve():
    n = int(input())
    pw = input()
    strong = True
    for i in range(n-1):
        prev, curr = pw[i], pw[i+1]
        if prev.isalpha() and curr.isdigit():
            strong = False
            break
        if prev.isalpha() and curr.isalpha() and prev > curr:
            strong = False
            break
        if prev.isdigit() and curr.isdigit() and prev > curr:
            strong = False
            break
    answer = "YES" if strong else "NO"
    print(answer)


if __name__ == "__main__":
    tc = 1
    tc = int(input())
    for _ in range(tc):
        solve()
