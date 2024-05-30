def solve():
    n, m = (int(x) for x in input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    if n == 0:
        total = sum(b)
        results = [total - x for x in b]
        print(" ".join([str(x) for x in results]))
        return
    if m == 0:
        total = sum(a)
        results = [total - x for x in a]
        print(" ".join([str(x) for x in results]))
        return
    results = [0] * (n+m+1)
    n0_idx, n1_idx = n+m, n+m
    m0_idx, m1_idx = n+m, n+m
    n_count, m_count = 0, 0
    for i in range(n+m+1):
        if a[i] > b[i]:
            n_count += 1
            if n_count == n:
                n0_idx = i
            if n_count == n+1:
                n1_idx = i
        else:
            m_count += 1
            if m_count == m:
                m0_idx = i
            if m_count == m+1:
                m1_idx = i
    n_cap_first = (n0_idx < m0_idx)
    idx_0 = n0_idx if n_cap_first else m0_idx
    idx_1 = n1_idx if n_cap_first else m1_idx
    total = 0
    for i in range(idx_0+1):
        if a[i] > b[i]:
            total += a[i]
        else:
            total += b[i]
    for i in range(idx_0+1, n+m+1):
        if n_cap_first:
            total += b[i]
        else:
            total += a[i]
    if n_cap_first:
        total += a[idx_1]
    else:
        total += b[idx_1]
    for i in range(n+m+1):
        if n_cap_first:
            if i <= idx_0 and a[i] > b[i]:
                results[i] = total - a[i] - b[idx_1]
            else:
                results[i] = total - b[i] - a[idx_1]
        else:
            if i <= idx_0 and a[i] < b[i]:
                results[i] = total - b[i] - a[idx_1]
            else:
                results[i] = total - a[i] - b[idx_1]
    print(" ".join([str(x) for x in results]))


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        solve()
