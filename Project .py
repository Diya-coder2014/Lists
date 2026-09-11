def process_range(start, end):
    squares = [x**2 for x in range(start, end + 1)]

    evens = [sq for sq in squares if sq % 2 == 0]
    odds = [sq for sq in squares if sq % 2 != 0]

    print("Even squares:", evens)
    print("Odd squares:", odds)

process_range(1, 10)