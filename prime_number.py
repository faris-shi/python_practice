"""
generate all possible prime numbers through the Sieve of Eratosthenes algorithm

Reference: https://en.wikipedia.org/wiki/Prime_number
Reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""

def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def primes_number():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(lambda x: x % n > 0, it)

if __name__ == '__main__':
    for i in primes_number():
        if i > 100:
            break
        print(i)