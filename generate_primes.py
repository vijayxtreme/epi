def generate_primes(n):
    primes = []
    # is_prime[p] represents if p is prime or not.  Initially, set each to
    # true, expecting 0 and 1.  Then use sieving to eliminate nonprimes.
    is_prime = [False, False] + [True] * (n-1)

    for p in range(2, n+1):
        if is_prime[p]:
            primes.append(p)
            # Sieve p's multiples.
            for i in range(p, n+1, p):
                is_prime[i] = False
    return primes

# Optimized way to sieve and not do more work than square root of n
def generate_primes2(n):
    if n < 2:
        return []
    size = (n-3) // 2 + 1
    primes = [2]
    # is_prime[i] represents (2i + 3) is prime or not
    # Initially set each to true.  Then use sieving to eliminate nonprimes.
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i*2+3
            primes.append(p)
            # Sieving from p^2, where p^2 = (4i^2 + 12i + 9).  The index in is_prime
            # is (2i^2 + 6i + 3) because is_prime[i] represents 2i + 3.
            # 
            # Note that we need to use long for j because p^2 might overflow.
            for j in range(2 * i**2  + 6 * i + 3, size, p):
                is_prime[j] = False
    return primes

print(generate_primes2(100))
