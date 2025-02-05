#6. Write a program which can filter prime numbers in a list by using `filter` function.
#Note: Use `lambda` to define anonymous functions.


def is_prime(num):
    if num < 2:
        return False 
    for i in range(2, int(num ** 0.5) + 1): 
        if num % i == 0:
            return False
    return True


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


prime_numbers = list(filter(lambda x: is_prime(x), numbers))


print("Prime numbers in the list:", prime_numbers)
