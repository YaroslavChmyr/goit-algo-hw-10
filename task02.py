import numpy as np
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Визначення функції для обчислення інтегралу за допомогою методу Монте-Карло
def monte_carlo_integration(f, a, b, num_points=10000):
    count_under_curve = 0
    max_f = max(f(np.linspace(a, b, 1000)))

    for _ in range(num_points):
        x = np.random.uniform(a, b)
        y = np.random.uniform(0, max_f)
        if y <= f(x):
            count_under_curve += 1

    area_rectangle = (b - a) * max_f
    ratio = count_under_curve / num_points
    integral = ratio * area_rectangle
    return integral

# Виклик функції для обчислення інтеграла
integral = monte_carlo_integration(f, a, b, num_points=100000)

print("Значення інтеграла за допомогою методу Монте-Карло:", integral)

# Перевіряємо значення за допомогою функції quad

result, error = spi.quad(f, a, b)

print("Значення інтеграла за допомогою функції quad: ", result)