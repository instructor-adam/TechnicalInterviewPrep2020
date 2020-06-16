import math

# This algorithm can be even further optimized, especially in the
# generate prime function.

def find_largest_prime(num):
    primes = [2]
    while num > 1:
        # All prime numbers greater than the square root can be arrived at by
        # dividing by smaller prime number.
        greatest = math.sqrt(num) // 1
        if primes[-1] > greatest:
            return num
        if (num % primes[-1]) == 0:
            num /= primes[-1]
        else:
            generate_prime(primes)
    return primes[-1]


def generate_prime(primes):
    if primes == []:
        primes.append(2)
        return
    num = primes[-1]
    if (num) == 2:
        primes.append(3)
        return
    while True:
        for prime in primes:
            if (num % prime) == 0:
                num += 2
                break
        else:
            primes.append(num)
            return


print(find_largest_prime(600851475143))
