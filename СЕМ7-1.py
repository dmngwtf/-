import numpy as np
import math

# Часть 1a: Нелинейные уравнения с использованием метода дихотомии и метода Ньютона

# Определяем функцию и её производную
f = lambda x: x**3 - x - 1
f_prime = lambda x: 3*x**2 - 1

# Метод дихотомии
def bisection(f, a, b, tol=1e-5):
    if f(a) * f(b) >= 0:
        raise ValueError("f(a) и f(b) должны иметь противоположные знаки")
    while (b - a) > tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Метод Ньютона
def newton(f, f_prime, x0, tol=1e-5, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        fpx = f_prime(x)
        if fpx == 0:
            raise ValueError("Производная равна нулю при x={}".format(x))
        x = x - fx / fpx
    return x

# Часть 1b: Численное интегрирование с использованием метода левых прямоугольников и метода трапеций

# Определяем функцию для интегрирования
f_integral = lambda x: np.sin(x)
a = 0
b = math.pi

# Метод левых прямоугольников
def left_rectangle(f, a, b, n=100):
    delta_x = (b - a) / n
    x = np.linspace(a, b - delta_x, n)
    return delta_x * np.sum(f(x))

# Метод трапеций
def trapezoidal(f, a, b, n=100):
    delta_x = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return (delta_x / 2) * (y[0] + 2*sum(y[1:-1]) + y[-1])

# Часть 1c: Решение дифференциальных уравнений с использованием метода Рунге-Кутта 4-го порядка

# Определяем дифференциальное уравнение dy/dx = f(x, y)
f_diff = lambda x, y: x + y

# Метод Рунге-Кутта 4-го порядка
def rk4(f, x0, y0, h, n):
    x = x0
    y = y0
    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        x += h
    return x, y

# Часть 2a: Нелинейные уравнения с использованием модифицированного метода Ньютона

# Модифицированный метод Ньютона
def modified_newton(f, f_prime, x0, tol=1e-5, max_iter=100):
    fpx0 = f_prime(x0)
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        x = x - fx / fpx0
    return x

# Часть 2b: Численное интегрирование методом среднего прямоугольника

# Метод среднего прямоугольника
def mid_rectangle(f, a, b, n=100):
    delta_x = (b - a) / n
    x = np.linspace(a + delta_x/2, b - delta_x/2, n)
    return delta_x * np.sum(f(x))

# Часть 2c: Решение дифференциальных уравнений методом Эйлера

# Метод Эйлера
def euler(f, x0, y0, h, n):
    x = x0
    y = y0
    for i in range(n):
        y += h * f(x, y)
        x += h
    return x, y

# Главная функция для демонстрации всех методов
def main():
    # Часть 1a
    print("Решение нелинейного уравнения f(x) = x^3 - x - 1 = 0")
    root_bisect = bisection(f, 1, 2)
    print("Метод дихотомии:", root_bisect)
    root_newton = newton(f, f_prime, 1.5)
    print("Метод Ньютона:", root_newton)

    # Часть 1b
    print("\n")
    exact_value = 2
    approx_left = left_rectangle(f_integral, a, b)
    print("Метод левых прямоугольников:", approx_left)
    approx_trapez = trapezoidal(f_integral, a, b)
    print("Метод трапеций:", approx_trapez)
    print("Точное значение:", exact_value)

    # Часть 1c
    print("\nРешение dy/dx = x + y с y(0) = 0 от x=0 до x=1 методом Рунге-Кутта 4-го порядка")
    h = 0.1
    n = int((1 - 0) / h)
    x_final, y_final = rk4(f_diff, 0, 0, h, n)
    print("При x =", x_final, ", y ≈", y_final)
    print("Точное решение y = x^2 / 2 при x=1 равно 0.5")

    # Часть 2a
    print("\nЧасть 2a: Решение нелинейного уравнения с использованием модифицированного метода Ньютона")
    root_modified_newton = modified_newton(f, f_prime, 1.5)
    print("Корень с использованием модифицированного метода Ньютона:", root_modified_newton)

    # Часть 2b
    print("\nЧасть 2b: Численное интегрирование методом среднего прямоугольника")
    approx_mid = mid_rectangle(f_integral, a, b)
    print("Аппроксимация с использованием метода среднего прямоугольника:", approx_mid)
    print("Точное значение:", exact_value)

    # Часть 2c
    print("\nЧасть 2c: Решение dy/dx = x + y с y(0) = 0 от x=0 до x=1 с использованием метода Эйлера")
    x_final_euler, y_final_euler = euler(f_diff, 0, 0, h, n)
    print("При x =", x_final_euler, ", y ≈", y_final_euler)
    print("Точное решение y = x^2 / 2 при x=1 равно 0.5")

if __name__ == "__main__":
    main()