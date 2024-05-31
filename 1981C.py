def same_bit_start(x1: int, x2: int) -> bool:
    l1 = x1.bit_length()
    l2 = x2.bit_length()
    if l1 >= l2:
        return (x1 >> (l1 - l2)) == x2
    return x1 == (x2 >> (l2 - l1))


def solve():
    # input
    n = int(input())
    a = [int(x) for x in input().split()]
    # find first known element
    curr_idx = -1
    for i in range(n):
        if a[i] != -1:
            curr_idx = i
            break
    if curr_idx == -1:
        curr_idx = n-1
        a[n-1] = 1
    # fill until first known element
    for i in range(curr_idx, 0 , -1):
        if a[i] > 1:
            a[i-1] = a[i] >> 1
        else:
            a[i-1] = a[i] << 1
    # fill between each known elements
    finished = False
    while True:
        next_idx = -1
        for i in range(curr_idx+1, n):
            if a[i] != -1:
                next_idx = i
                break
        if next_idx == -1:
            break
        dist = next_idx - curr_idx
        for i in range(curr_idx+1, next_idx):
            if not same_bit_start(a[i-1], a[next_idx]):
                a[i] = a[i-1] >> 1
            else:
                if a[i-1].bit_length() > a[next_idx].bit_length():
                    a[i] = a[i-1] >> 1
                elif a[i-1].bit_length() == a[next_idx].bit_length():
                    a[i] = a[i-1] << 1
                else:
                    a[i] = a[next_idx] >> (a[next_idx].bit_length() - a[i-1].bit_length() - 1)
        if ((a[next_idx-1] >> 1) != a[next_idx]) and (a[next_idx-1] != (a[next_idx] >> 1)):
            print(-1)
            return
        curr_idx = next_idx
    # fill from last known element
    for i in range(curr_idx+1, n):
        if a[i-1] > 1:
            a[i] = a[i-1] >> 1
        else:
            a[i] = a[i-1] << 1
    # print result
    print(" ".join([str(x) for x in a]))


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        solve()
