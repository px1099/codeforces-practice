def find_sol(q: int, query: str):
    if q <= 2:
        return "1" * q

    sol_list = ["0"] * q  # Initialize memory
    has_des = False
    first, prev = -1, -1
    i = -1
    for x in query.split():
        i += 1
        curr = int(x)
        if i == 0:
            sol_list[i] = "1"
            first, prev = curr, curr
            continue
        if not has_des:
            if curr >= prev:
                sol_list[i] = "1"
                prev = curr
            elif curr <= first:
                has_des = True
                sol_list[i] = "1"
                prev = curr
        else:
            if prev <= curr <= first:
                sol_list[i] = "1"
                prev = curr
    return "".join(sol_list)


def main():
    t = int(input())
    for _ in range(t):
        q = int(input())
        query = input()
        sol = find_sol(q, query)
        print(sol)


if __name__ == "__main__":
    main()
