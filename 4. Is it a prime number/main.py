def is_prime(number:int):
    """Checks if the given number is prime.

    Args:
        number (int): Number to check if it's prime.

    Returns:
        bool: True if the number is prime; False if the number isn't prime.
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


print("Is it a prime number?\nIntroduce the number to check if it is prime.\n\n")

while True:
    try:
        number = int(input("Introduce the number: "))
        
        if is_prime(number):
            print("It's prime! :D\n")
        else:
            print("It isn't prime D:\n")
    except ValueError:
        print("Please provide an integer number\n")