def simple_recursion(n):
    if n == 0:
        return
    print(n)
    simple_recursion(n-1)

def sum_numbers(n) -> int:
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

if __name__ == "__main__":
    simple_recursion(5)
    print(sum_numbers(5))
    print(factorial(5))
    print(count_digits(12345))