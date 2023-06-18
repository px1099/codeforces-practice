def find_solution(n: int, m: int):
    solution = None
    if n % 2 == 0:
        solution = [[1+i+j*n for j in range(m)] for i in range(n)]
    elif m % 2 == 0:
        solution = [[1+i*m+j for j in range(m)] for i in range(n)]
    else:
        solution = [[0 for _ in range(m)] for _ in range(n)]
        k = 1
        for i in range((n+1)//2):
            for j in range(m):
                solution[2*i][j] = k
                k += 1
        for i in range((n-1)//2):
            for j in range(m):
                solution[2*i+1][j] = k
                k += 1
    return solution


def main():
    t = int(input())
    for _ in range(t):
        n, m = input().split()
        n = int(n)
        m = int(m)
        solution = find_solution(n, m)
        for i in range(n):
            print(" ".join([str(solution[i][j]) for j in range(m)]))


if __name__ == "__main__":
    main()
