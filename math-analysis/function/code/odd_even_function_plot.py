# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def odd_even_function():
    xs = np.arange(-2, 2, 0.01)
    y1s = xs * xs
    y2s = y1s * xs

    fig, ax = plt.subplots()
    ax.plot(xs, y1s, color="blue", label="Odd Function")
    p1, p1m = (1, 1), (-1, 1)
    ax.plot(*p1, 'bo')
    ax.text(*p1, "(x,y)", {"fontsize": 18})
    ax.plot(*p1m, 'bo')
    ax.text(*p1m, "(-x,y)", {"fontsize": 18})
    ax.plot([p1[0], p1m[0]], [p1[1], p1m[1]], color="blue", linestyle='--')

    ax.plot(xs, y2s, color="green", label="even Function")
    p2, p2m = (1.5, 3.375), (-1.5, -3.375)
    ax.plot(*p2, 'go')
    ax.text(*p2, "(x,y)", {"fontsize": 18})
    ax.plot(*p2m, 'go')
    ax.text(*p2m, "(-x,y)", {"fontsize": 18})
    ax.plot([p2[0], p2m[0]], [p2[1], p2m[1]], color="green", linestyle='--')

    ax.set_title("odd function: $ y = x^2$, even function: $ y = x^3$")

    ax.axhline(y=0, color='black')
    ax.axvline(x=0, color='black')
    plt.grid()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    odd_even_function()
