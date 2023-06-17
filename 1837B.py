def calculate_cost(n: int, s: str) -> int:
    if n <= 0:
        return 0

    count, max_count = 1, 1
    for i in range(1, n):
        if s[i] == s[i-1]:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 1

    cost = max_count + 1
    return cost


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        cost = calculate_cost(n, s)
        print(cost)


if __name__ == "__main__":
    main()
