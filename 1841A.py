def find_winner(n: int) -> str:
    if n <= 4:
        return "Bob"
    return "Alice"


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        winner = find_winner(n)
        print(winner)


if __name__ == "__main__":
    main()
