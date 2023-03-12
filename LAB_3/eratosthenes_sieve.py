from math import sqrt
import timeit
import numpy as np
import matplotlib.pyplot as plt


def SieveofEratosthenes(n):
    arr = [True] * (n + 1)
    arr[1] = False
    i = 2
    while i <= n:
        if arr[i]:
            j = 2 * i
            while j <= n:
                arr[j] = False
                j = j + i
        i = i + 1
    return [i for i in range(1, n + 1) if arr[i]]


def ModifiedSieveofEratosthenes(n):
    arr = [True] * (n + 1)
    arr[1] = False
    i = 2
    while i <= n:
        j = 2 * i
        while j <= n:
            arr[j] = False
            j = j + i
        i = i + 1
    return [num for num in range(1, n + 1) if arr[num]]


def naive_alg(n):
    arr = [True] * (n + 1)
    arr[1] = False
    i = 2
    while i <= n:
        if arr[i]:
            j = i + 1
            while j <= n:
                if j % i == 0:
                    arr[j] = False
                j += 1
        i += 1
    return [num for num in range(1, n + 1) if arr[num]]


def trial_div_alg(n):
    arr = [True] * (n + 1)
    arr[1] = False
    i = 2
    while i <= n:
        j = 2
        while j < i:
            if i % j == 0:
                arr[i] = False
                break
            j += 1
        i += 1
    return [num for num in range(1, n + 1) if arr[num]]


def opt_trial_div_alg(n):
    arr = [True] * (n + 1)
    arr[1] = False
    i = 2

    while i <= n:
        j = 2
        while j <= int(sqrt(i)):
            if i % j == 0:
                arr[i] = False
                break
            j += 1
        i += 1

    return [num for num in range(1, n + 1) if arr[num]]


prime_algorithms = [
    {
        "name": "Sieve of Eratosthenes",
        "primes": lambda n: SieveofEratosthenes(n)
    },
    {
        "name": "Modified Sieve of Eratosthenes",
        "primes": lambda n: ModifiedSieveofEratosthenes(n)
    },
    {
        "name": "Naive algorithm",
        "primes": lambda n: naive_alg(n)
    },
    {
        "name": "Trial division algorithm",
        "primes": lambda n: trial_div_alg(n)
    },
    {
        "name": "Optimized trial division algorithm",
        "primes": lambda n: opt_trial_div_alg(n)
    }
]

elements = np.array([i * 100 for i in range(1, 50)])

for alg in prime_algorithms:
    times = list()
    start_time = timeit.default_timer()
    for i in range(1, 50):
        start_alg = timeit.default_timer()
        num = i * 100
        alg["primes"](num)
        end_alg = timeit.default_timer()
        times.append(end_alg - start_alg)
        print(alg["name"], "Calculated ", i * 1000, "Primes in ", end_alg - start_alg, "s")

    end_time = timeit.default_timer()
    print(alg["name"], "Calculated all Primes in", end_time - start_time, "s")

    plt.plot(elements, times, label=alg["name"])

plt.grid()
plt.legend()
plt.show()
