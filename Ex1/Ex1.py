import math
import os
import matplotlib.pyplot as plt


def f(x):
    A = 418.9829
    return A - x * math.sin(math.sqrt(abs(x)))


def main():
    x_min = -500
    x_max = 500
    step = 5

    x_values = []
    y_values = []

    x = x_min
    while x <= x_max:
        x_values.append(x)
        y_values.append(f(x))
        x += step

    results_dir = os.path.join(os.path.dirname(__file__), "results")
    if not os.path.exists(results_dir):
        os.mkdir(results_dir)

    with open(os.path.join(results_dir, "Ex1_values.txt"), "w") as file:
        file.write("x           f(x)\n")
        for xi, yi in zip(x_values, y_values):
            file.write(f"{xi:.3f}    {yi:.3f}\n")

    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции f(x)')
    plt.grid(True)
    plt.savefig(os.path.join(results_dir, "Ex1_plot.png"))


if __name__ == "__main__":
    main()