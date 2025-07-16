import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def f(x1, x2):
    return (
        0.5
        + (np.sin(x1**2 - x2**2) ** 2 - 0.5)
        / (1 + 0.001 * (x1**2 + x2**2)) ** 2
    )


def main():
    x1 = np.linspace(-2.0, 2.0, 300)
    x2 = np.linspace(-2.0, 2.0, 300)
    X1, X2 = np.meshgrid(x1, x2)
    Z = f(X1, X2)

    fig = plt.figure(figsize=(12, 8))
    gs = gridspec.GridSpec(
        2, 2, height_ratios=[2.2, 1], hspace=0.40, wspace=0.60
    )

    ax1 = fig.add_subplot(gs[0, 0], projection='3d')
    ax1.plot_surface(X1, X2, Z, cmap='viridis')
    ax1.set_xlabel('x1')
    ax1.set_ylabel('x2')
    ax1.set_zlabel('f(x1, x2)')
    ax1.set_title('Поверхность функции f(x1, x2)')
    ax1.view_init(elev=20, azim=-50)

    ax2 = fig.add_subplot(gs[0, 1])
    contour = ax2.contourf(X1, X2, Z, levels=500, cmap='viridis')
    ax2.set_xlabel('x1')
    ax2.set_ylabel('x2')
    ax2.set_title('Вид сверху f(x1, x2)')
    fig.colorbar(contour, ax=ax2, label='f(x1, x2)', shrink=0.6)
    ax2.set_aspect('equal')

    ax3 = fig.add_subplot(gs[1, 0])
    ax4 = fig.add_subplot(gs[1, 1])

    x10 = 0.0
    x20 = 0.0

    x2_line = np.linspace(-2.0, 2.0, 300)
    f_x10_x2 = f(np.full_like(x2_line, x10), x2_line)
    ax3.plot(x2_line, f_x10_x2, color='blue')
    ax3.set_xlabel('x2')
    ax3.set_ylabel('f(x1=0, x2)')
    ax3.set_title('f(x1=0, x2)')

    x1_line = np.linspace(-2.0, 2.0, 300)
    f_x1_x20 = f(x1_line, np.full_like(x1_line, x20))
    ax4.plot(x1_line, f_x1_x20, color='green')
    ax4.set_xlabel('x1')
    ax4.set_ylabel('f(x1, x2=0)')
    ax4.set_title('f(x1, x2=0)')

    ax1.scatter(x10, x20, f(x10, x20), color='red', s=50)
    ax2.scatter(x10, x20, color='red', s=50)

    fig.text(
        0.5,
        0.40,
        f"x₁₀ = {x10}\nx₂₀ = {x20}\nf(x₁₀, x₂₀) = {f(x10, x20):.2f}",
        fontsize=13,
        color='red',
        ha='center',
        va='center',
    )

    results_dir = os.path.join(os.path.dirname(__file__), "results")
    if not os.path.exists(results_dir):
        os.mkdir(results_dir)

    plt.savefig(os.path.join(results_dir, "Ex3_plot.png"))
    plt.close()


if __name__ == "__main__":
    main()