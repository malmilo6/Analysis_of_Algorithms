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


# 3 Matrix exponentiation
def fib_matrix(n):
    i = np.array([[0, 1], [1, 1]])
    return np.matmul(matrix_power(i, n), np.array([1, 0]))[1]


def multiply(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]]:
    matrix_c = []
    n = len(matrix_a)
    for i in range(n):
        list_1 = []
        for j in range(n):
            val = 0
            for k in range(n):
                val = val + matrix_a[i][k] * matrix_b[k][j]
            list_1.append(val)
        matrix_c.append(list_1)
    return matrix_c


def identity(n: int) -> list[list[int]]:
    return [[int(row == column) for column in range(n)] for row in range(n)]


def nth_fibonacci_matrix(n: int) -> int:
    if n <= 1:
        return n
    res_matrix = identity(2)
    fibonacci_matrix = [[1, 1], [1, 0]]
    n = n - 1
    while n > 0:
        if n % 2 == 1:
            res_matrix = multiply(res_matrix, fibonacci_matrix)
        fibonacci_matrix = multiply(fibonacci_matrix, fibonacci_matrix)
        n = int(n / 2)
    return res_matrix[0][0]


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
    # exec_time = timeit.timeit(lambda: rec_fib(number), number=1)
    # y_0.append(round(exec_time, 5))

    exec_time = timeit.timeit(lambda: dynamic_fib(number), number=1)
    y_1.append(round(exec_time, 5))

    exec_time = timeit.timeit(lambda: doubling_fib(number), number=1)
    y_2.append(round(exec_time, 5))

    exec_time = timeit.timeit(lambda: nth_fibonacci_matrix(number), number=1)
    y_3.append(round(exec_time, 5))

    exec_time = timeit.timeit(lambda: f_fib(number), number=1)
    y_4.append(round(exec_time, 5))

    exec_time = timeit.timeit(lambda: i_fib(number), number=1)
    y_5.append(round(exec_time, 5))

# Create prettytable
res_table.field_names = x_s
# create_table(y_0, 0, res_table)
create_table(y_1, 1, res_table)
create_table(y_2, 2, res_table)
create_table(y_3, 3, res_table)
create_table(y_4, 4, res_table)
create_table(y_5, 5, res_table)
print(res_table)

# Draw the graphs
# plt.title("Matrix Exponentiation Method")
# # plt.plot(x_slow, y_1, '-r', marker='o', label='Dynamic Programming Method')
# # plt.plot(x_slow, y_2, '-b', marker='o', label='Doubling Method')
# plt.plot(x_slow, y_3, '-y', marker='o')
# # plt.plot(x_slow, y_4, '-m', marker='o', label='Binet Formula Method')
# # plt.plot(x_slow, y_5, '-g', marker='o', label='Iterative Method')
# plt.legend()
# plt.grid()
# plt.xlabel('N-th Fibonacci Number')
# plt.ylabel('Time (s)')
# plt.show()
