# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np


def power_function():
    xs = np.arange(-1, 1, 0.01)
    powers = 5
    ys = np.zeros([powers, len(xs)])
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    fig, axs = plt.subplots(2, figsize=(5, 8))
    for p in range(powers):
        ys[p] = xs ** (p + 1)
        axs[0].plot(xs, ys[p],
                    color=colors[p],
                    linewidth=1.5,
                    label=f"$y=x^{p + 1}$")
    axs[0].set_title("power function: $y=x^n$, n=1,2,3,4,5")
    axs[0].legend(loc="lower right")
    axs[0].grid(visible=True)

    powers = [1 / 2., 1 / 3., 3 / 2., 2 / 3.]
    y2s = np.zeros([len(powers), len(xs)])
    for idx, p in enumerate(powers):
        y2s[idx] = xs ** p
        axs[1].plot(xs, y2s[idx],
                    color=colors[idx],
                    linewidth=1.5,
                    label=f"$y=x^{{{p:.2f}}}$")
    axs[1].set_title("power function: $y=x^n$, n=1/2, 1/3, 3/2, 2/3")
    axs[1].legend(loc="lower right")
    axs[1].grid(visible=True)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    power_function()
