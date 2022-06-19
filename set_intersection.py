from typing import Generator


def squares_generator(n: int) -> Generator[int, None, None]:
    """Generator to return the perfect squares less than `n`."""
    if n > 0:
        i = next_square = 1
        while next_square < n:
            yield next_square
            i += 1
            next_square = i * i


def primes_generator(n: int) -> Generator[int, None, None]:
    """
    Very naive implementation of the Sieve of Eratosthenes to generate prime numbers.

    This is *not* suitable for production use.
    For an optimised algorithm, check out the work by Tim Peters et al @ActiveState, and Will Ness.
    https://stackoverflow.com/questions/2211990/how-to-implement-an-efficient-infinite-generator-of-prime-numbers-in-python/19391111#19391111

    :param n: The number to generate primes up to.
    :return: A generator of all positive prime numbers less than or equal to `n`.
    """
    if n >= 2:
        # start with the set of positive odd integers from 3 to `n`, inclusive.
        integers = set(range(3, n + 1, 2))
        # There's no point removing multiples of 2 from odd numbers.
        yield 2
        next_prime = 3
        while integers:
            yield next_prime
            # Remove all multiples of `next_prime`.
            integers.difference_update(range(next_prime, n + 1, 2 * next_prime))
            next_prime = min(integers, default=None)  # None if set is empty.



evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(evens)
print(odds)
print(odds.intersection(squares_generator(100)))
even_squares = evens.intersection(squares_generator(100))
print(even_squares)

print(odds - set(squares_generator(100)))

