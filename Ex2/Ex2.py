import os
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(prog="Ex2")
parser.add_argument("filename", nargs='?', default='input.txt', help="Имя TXT файла с данными")
parser.add_argument("--width", type=int, help="Ширина окна графика в дюймах")
parser.add_argument("--height", type=int, help="Высота окна графика в дюймах")
args = parser.parse_args()


def main():
    width = args.width if args.width else 8
    height = args.height if args.height else 6
    filename = args.filename

    data_x = []
    data_y = []

    if os.path.exists(filename):
        path = filename
    elif os.path.exists(os.path.join("Ex2", filename)):
        path = os.path.join("Ex2", filename)
    else:
        print(f"Файл '{filename}' не найден.")
        return

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                try:
                    x = float(parts[0])
                    y = float(parts[1])
                    data_x.append(x)
                    data_y.append(y)
                except ValueError:
                    continue

    results_dir = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(results_dir, exist_ok=True)

    plt.figure(figsize=(width, height))
    plt.plot(data_x, data_y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции f(x)')
    plt.grid(True)
    plt.savefig(os.path.join(results_dir, "Ex2_plot.png"))


if __name__ == "__main__":
    main()
