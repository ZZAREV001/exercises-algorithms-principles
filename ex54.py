# Sum of squares (dynamic programming approach)
def square_sums(n):
    squares = []

    i = 1
    while i * i <= n:
        squares.append(i)
        i = i + 1

    min_sums = [n] * (n + 1)
    min_sums[0] = 0

    for i in range(n + 1):
        for s in squares:
            if i + s < len(min_sums):
                min_sums[i + s] = min(min_sums[i + s], min_sums[i] + 1)

    print(min_sums)
    return min_sums[-1]


print(square_sums(13))
