def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True


def get_primes(some_list):
    for el in [num for num in some_list if num > 1]:
        if is_prime(el):
            yield el


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))