class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        # Sieve of Eratosthenes
        isPrime = [True] * (n + 1)
        if n >= 0:
            isPrime[0] = False
        if n >= 1:
            isPrime[1] = False

        i = 2
        while i * i <= n:
            if isPrime[i]:
                j = i * i
                while j <= n:
                    isPrime[j] = False
                    j += i
            i += 1

        primes = sum(isPrime)

        def fact(x):
            res = 1
            for i in range(2, x + 1):
                res = (res * i) % MOD
            return res

        return (fact(primes) * fact(n - primes)) % MOD