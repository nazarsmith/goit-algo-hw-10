import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sp
import random

def mot_carl_int(a, b, num_experiments, x_boundaries: tuple = (-1, 3)):
    # Визначення функції та межі інтегрування
    def f(x):
        return x ** 2

    # Створення діапазону значень для x
    x = np.linspace(x_boundaries[0], x_boundaries[1], num_experiments)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, f(x), 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(f(x)) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()

    result, _ = sp.quad(f, a, b)

    print("Quad:", result)

    def is_inside(x, y):
        return f(x) <= y

    points = [random.uniform(-0.5, 2.5) for _ in range(num_experiments)]
    inside_points = [points[point] for point in range(len(points)) if is_inside(points[point], x[point])]

    N = len(points)
    M = len(inside_points)

    Sm = (M / N) * (b - a)
    print("Monte-Carlo:", np.pi * (Sm ** 2))

if __name__ == "__main__":
    # for i in range(20):
    mot_carl_int(x_boundaries = (-0.5, 2.5), a = 0, b = 2, num_experiments = 15000)