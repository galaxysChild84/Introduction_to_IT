# -----------------------------------------
# Wilson's Theorem Prime Checker
# -----------------------------------------

def factorial(n):
    """Return n! using a simple loop."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def isPrime(n):
    """Return True if n is prime using Wilson's Theorem."""
    if n <= 1:
        return False

    # Wilson's theorem: n is prime iff (n - 1)! % n == n - 1
    return (factorial(n - 1) + 1) % n == 0


def main():
    number = int(input("Enter a number: "))
    if isPrime(number):
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")


# Run the program
main()
