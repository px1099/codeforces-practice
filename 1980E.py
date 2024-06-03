def solve():
    n, m = (int(x) for x in input().split())
    a = []
    b = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    for i in range(n):
        b.append([int(x) for x in input().split()])
    row_coord = [0] * (n*m)
    col_coord = [0] * (n*m)
    for i in range(n):
        for j in range(m):
            row_coord[a[i][j]-1] = i
            col_coord[a[i][j]-1] = j
    row_map = [-1] * n
    col_map = [-1] * m
    for i in range(n):
        for j in range(m):
            if row_map[row_coord[b[i][j]-1]] == -1:
                row_map[row_coord[b[i][j]-1]] = i
            elif row_map[row_coord[b[i][j]-1]] != i:
                print("NO")
                return
            if col_map[col_coord[b[i][j]-1]] == -1:
                col_map[col_coord[b[i][j]-1]] = j
            elif col_map[col_coord[b[i][j]-1]] != j:
                print("NO")
                return
    print("YES")


if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        solve()
