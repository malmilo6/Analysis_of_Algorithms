import time
import math
import matplotlib.pyplot as plt
import decimal


# Algorithms
import decimal

def gauss_legendre(n):
    # Setting precision for decimal calculations
    decimal.getcontext().prec = n + 2

    # Initial values
    a, b, t, p = 1, 1 / decimal.Decimal(2).sqrt(), 1 / decimal.Decimal(4), 1

    # Pi variable
    pi = None

    # Gauss-Legendre iterations
    for _ in range(n):
        an = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - an) * (a - an)
        a = an
        p *= 2

        # Computing pi
        pi = (a + b) * (a + b) / (4 * t)
    return +pi


def chudnovsky_algorithm(n):
    # Setting precision for decimal calculations
    decimal.getcontext().prec = n + 2

    # Chudnovsky constants
    C = 426880 * decimal.Decimal(10005).sqrt()
    K = 6.
    M = 1.
    X = 1
    L = 13591409

    # Initial sum
    S = decimal.Decimal(L)

    # Chudnovsky iterations
    for i in range(1, n):
        M = (K ** 3 - 16 * K) * M / i ** 3
        K += 12
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X

    # Computing pi
    pi = C / S
    return pi


def nilakantha_series(n):
    # Setting precision for decimal calculations
    decimal.getcontext().prec = n + 2

    # Initial value of pi
    pi = 3

    # Nilakantha iterations
    for i in range(1, n + 1):
        j = 2 * i * (2 * i + 1) * (2 * i + 2)
        if i % 2 == 0:
            pi -= 4 / decimal.Decimal(j)
        else:
            pi += 4 / decimal.Decimal(j)
    return +pi

# Empirical Analysis

def analyze_algorithm(algorithm, name):
    times = []
    precisions = []
    ns = list(range(1, 25))  # Change the range as needed
    for n in ns:
        start_time = time.time()
        pi = algorithm(n)
        end_time = time.time()
        runtime = end_time - start_time
        times.append(runtime)
        precision = abs(pi - decimal.Decimal(math.pi))  # Convert math.pi to Decimal
        precisions.append(precision)
    return ns, times, precisions



# Graphical Presentation

def plot_results(ns, times, precisions, name):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(ns, times, 'o-')
    plt.title('Runtime of ' + name)
    plt.xlabel('N')
    plt.ylabel('Time (seconds)')
    plt.subplot(1, 2, 2)
    plt.plot(ns, precisions, 'o-')
    plt.title('Precision of ' + name)
    plt.xlabel('N')
    plt.ylabel('Precision (error)')
    plt.tight_layout()
    plt.show()


# Perform the analysis
ns, times, precisions = analyze_algorithm(gauss_legendre, 'Gauss-Legendre')
plot_results(ns, times, precisions, 'Gauss-Legendre')

ns, times, precisions = analyze_algorithm(chudnovsky_algorithm, 'Chudnovsky')
plot_results(ns, times, precisions, 'Chudnovsky')

ns, times, precisions = analyze_algorithm(nilakantha_series, 'Nilakantha')
plot_results(ns, times, precisions, 'Nilakantha')

