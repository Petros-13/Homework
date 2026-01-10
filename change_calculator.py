coins = [500, 100, 10, 5, 1]

def count_ways(n, index, current):
    if n == 0:
        print(current)
        return 1

    if n < 0 or index == len(coins):
        return 0

    total = 0
    coin = coins[index]

    for i in range(n // coin + 1):
        if i > 0:
            current.append(f"{i} x {coin}")
        total += count_ways(n - i * coin, index + 1, current)
        if i > 0:
            current.pop()

    return total


n = int(input("Enter amount: "))
print("\nWays to split", n, "using coins:")
total = count_ways(n, 0, [])
print("\nTotal number of ways:", total)
