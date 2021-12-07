import math

epsilon = 0.5 * 10e-5
a = 2
b = 2.5
x0 = 2.5


def f(x):
    return math.e ** x - 4.6 * x


def first_derivative_f(x):
    return math.e ** x - 4.6


def phi(x):
    return math.log(4.6 * x)


'''Solution methods'''


def half_division():
    print("Метод половинного деления:")
    left = a
    right = b
    x = 0
    iteration_count = 1
    while math.fabs(f(left) - f(right)) > epsilon:
        mid = (left + right) / 2
        if f(mid) == 0 or abs(f(mid)) < epsilon:
            print("{} итераций".format(iteration_count))
            x = mid
            break
        elif f(left) * f(mid) < 0:
            right = mid
        else:
            left = mid
        iteration_count += 1
    print("Результат:  {} \n\n".format(x))


def newton():
    print("Метод Ньютона:")
    x = x0
    iteration_count = 1
    while True:
        xp = x - f(x) / first_derivative_f(x)
        if math.fabs(xp - x) <= epsilon:
            print("{} итераций".format(iteration_count))
            break
        x = xp
        iteration_count += 1
    print("Результат:  {}".format(x))


def mod_newton_method():
    print("\n\nМодифицированный метод Ньютона:")
    xn = x0
    iteration_count = 0
    while True:
        iteration_count += 1
        c = xn - f(xn) / first_derivative_f(x0)
        if math.fabs(c - xn) <= epsilon:
            print("{} итераций".format(iteration_count))
            print('Результат: ', c)
            break
        xn = c


def chord():
    print("\n\nМетод хорд:")
    xn = a
    iteration_count = 0
    while True:
        iteration_count += 1
        c = xn - (f(xn) * (xn - x0)) / (f(xn) - f(x0))
        if math.fabs(c - xn) <= epsilon:
            print("{} итераций".format(iteration_count))
            print('Результат: ', c)
            break
        xn = c


def movable_chord():
    print("\n\nМетод подвижных хорд:")
    prev = x0
    xn = a
    iteration_count = 0
    while True:
        iteration_count += 1
        c = xn - (f(xn) * (xn - prev)) / (f(xn) - f(prev))
        if math.fabs(c - xn) <= epsilon:
            print("{} итераций".format(iteration_count))
            print('Результат: ', c)
            break
        prev = xn
        xn = c


def simple_iteration():
    print("\n\nМетод простой итерации:")
    xn = x0
    iteration_count = 0
    while True:
        iteration_count += 1
        c = phi(xn)
        if math.fabs(c - xn) <= epsilon:
            print("{} итераций".format(iteration_count))
            print('Результат: ', c)
            break
        xn = c


if __name__ == '__main__':
    half_division()
    newton()
    mod_newton_method()
    chord()
    movable_chord()
    simple_iteration()
