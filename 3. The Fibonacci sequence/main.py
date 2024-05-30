def fibonacci_sequence(n:int):
    """Calculates the first n numbers of the Fibonacci sequence.

    Args:
        n (int): number of the fibonacci sequence to calculate.

    Returns:
        tuple: Contains the first n numbers of the Fibonacci sequence.
    """
    a, b = 0, 1
    sequence = [0, 1]
    for _ in range(n-2):
        c = a + b
        a = b
        b = c
        sequence.append(c)
    return tuple(sequence)

fibo = fibonacci_sequence(50)
for n in fibo:
    print(n)