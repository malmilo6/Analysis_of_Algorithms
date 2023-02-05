import decimal as d
from decimal import Context
import matplotlib.pyplot as plt
import timeit
import numpy as np
from numpy.linalg import matrix_power
from prettytable import PrettyTable

res_table = PrettyTable()
res_table.title = 'Implementation of Fibonacci Algorithms '
# 2 Arrays for creating pretty table
x_s = ['Algorithm / Fibonacci Nth', 501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000,
       12589, 15849]
x_f = ['Algorithm / Fibonacci Nth', 5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]


def create_table(row, order, table):
    row.insert(0, order)
    table.add_row(row)


x_slow = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
x_fast = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]

# Arrays for y-data for each method
y_0 = []
y_1 = []
y_2 = []
y_3 = []
y_4 = []
y_5 = []


# 0 Textbook Algorithm (recursive)
def rec_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fib(n - 1) + rec_fib(n - 2)


# 1 Dynamic
def dynamic_fib(n):
    # Taking 1st two fibonacci numbers as 0 and 1
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


# 2 Doubling
def doubling_fib(n):
    if n == 0:
        return 0, 1
    else:
        a, b = doubling_fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return c, d
        else:
            return d, c + d


# 3 Matrix exponential
def fib_matrix(n):
    i = np.array([[0, 1], [1, 1]])
    return np.matmul(matrix_power(i, n), np.array([1, 0]))[1]


def matrix_fib(n):
    F = [[1, 1],
         [1, 0]]
    if n == 0:
        return 0
    power(F, n - 1)

    return F[0][0]


def multiply(F, M):
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(F, n):
    M = [[1, 1],
         [1, 0]]

    for i in range(2, n + 1):
        multiply(F, M)


# 4 Binet Formula
def f_fib(n):
    rnd = Context(prec=50, rounding="ROUND_HALF_EVEN")
    phi = d.Decimal((1 + d.Decimal(5 ** (1 / 2))))
    phi1 = d.Decimal((1 - d.Decimal(5 ** (1 / 2))))

    return int((rnd.power(phi, d.Decimal(n)) - rnd.power(phi1, d.Decimal(n))) / (2 ** n * d.Decimal(5 ** (1 / 2))))


# 5 Iterative
def i_fib(n):
    fib = [0, 1]
    if n == 0:
        return fib[0]
    if n == 1:
        return fib[1]
    i = 2
    while i <= n:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    return fib[n]


# Use for loop for getting the numbers into functions, time calculation with timeit lib
for number in x_slow:
    exec_time = timeit.timeit(lambda: rec_fib(number), number=1)
    y_0.append(round(exec_time, 5))

    exec_time = timeit.timeit(lambda: dynamic_fib(number), number=1)
    y_1.append(round(exec_time, 5))

    exec_time = timeit.timeit(lambda: doubling_fib(number), number=1)
    y_2.append(round(exec_time, 5))

    exec_time = timeit.timeit(lambda: matrix_fib(number), number=1)
    y_3.append(round(exec_time, 5))

    exec_time = timeit.timeit(lambda: f_fib(number), number=1)
    y_4.append(round(exec_time, 5))

    exec_time = timeit.timeit(lambda: i_fib(number), number=1)
    y_5.append(round(exec_time, 5))

# Create prettytable
res_table.field_names = x_s
create_table(y_0, 0, res_table)
create_table(y_1, 1, res_table)
create_table(y_2, 2, res_table)
create_table(y_3, 3, res_table)
create_table(y_4, 4, res_table)
create_table(y_5, 5, res_table)
print(res_table)

# Draw the graphs
plt.title("Matrix exponential Fibonacci function")
plt.plot(x_slow, y_3)
plt.scatter(x_slow, y_3)
plt.grid()
plt.xlabel('N-th Fibonacci Number')
plt.ylabel('Time (s)')
plt.show()
