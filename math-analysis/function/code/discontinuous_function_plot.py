# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np
def removable_discontinuity():
    xs = np.arange(-2, 2, 0.01)
    ys = np.zeros_like(xs)
    _, ax = plt.subplots()
    edx = 0
    for idx, x in enumerate(xs):
        if x < 1:
            ys[idx] = x * x
            ax.plot(xs[:idx], ys[:idx], color="blue")
            edx = idx
        elif 1-0.001 < x < 1+0.001:
            ys[idx] = 0
            ax.plot(x, 0, 'ro')
        else:
            ys[idx] = 2-x
            ax.plot(xs[edx:], ys[edx:], color="green")

    # ax.plot(xs, ys, color="blue")
    plt.title("Removable Discontinuity")
    print(idx, edx)
    plt.grid()
    plt.tight_layout()
    plt.show()



if __name__ == '__main__':
    removable_discontinuity()
