def gcd(a: int, b: int) -> int:
    if b > a:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a % b)


def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [gcd(a[i], a[i+1]) for i in range(n-1)]
    count = 0
    first_idx = None
    last_idx = None
    for i in range(n-2):
        if b[i] > b[i+1]:
            count += 1
            if first_idx is None:
                first_idx = i
            last_idx = i
    if count == 0:
        print("YES")
        return
    if count >= 3:
        print("NO")
        return
    if last_idx - first_idx > 2:
        print("NO")
        return
    pre_list = [a[i] for i in range(max(0, last_idx-2), last_idx)]
    post_list = [a[i] for i in range(last_idx+3, min(last_idx+5, n))]
    cases = [
        pre_list + [a[last_idx+1], a[last_idx+2]] + post_list,
        pre_list + [a[last_idx], a[last_idx+2]] + post_list,
        pre_list + [a[last_idx], a[last_idx+1]] + post_list,
    ]
    for case in cases:
        gcd_list = [gcd(case[i], case[i+1]) for i in range(len(case)-1)]
        flag = True
        for i in range(len(gcd_list)-1):
            if gcd_list[i] > gcd_list[i+1]:
                flag = False
                break
        if flag:
            print("YES")
            return
        else:
            continue
    print("NO")


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        solve()
