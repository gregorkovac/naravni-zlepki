import numpy as np
import matplotlib.pyplot as plt

class Polinom:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def v(self, x):
        return self.a * x**3 + self.b * x**2 + self.c * x + self.d

class Zlepek:
    interpolacijske_tocke = []
    polinomi = []

    def __init__(self, x, y):
        self.interpolacijske_tocke = np.array([x, y])


def interpoliraj(x, y):
    Z = Zlepek(x, y)

    for i in range(len(x) - 1):
        x1 = x[i]
        x2 = x[i + 1]
        y1 = y[i]
        y2 = y[i + 1]

        a = 0
        b = 0
        c = (y2 - y1) / (x2 - x1)
        d = y1 - c * x1

        Z.polinomi.append(Polinom(a, b, c, d))

    return Z

def plot(Z):
    x = Z.interpolacijske_tocke[0]
    y = Z.interpolacijske_tocke[1]

    for i in range(len(Z.polinomi)):
        p = Z.polinomi[i]
        x1 = x[i]
        x2 = x[i + 1]

        x_p= np.linspace(x1, x2, 100)
        y_p = p.v(x_p)

        col = i % 2 == 0 and 'b' or 'r'

        plt.plot(x_p, y_p, col)

    plt.plot(x, y, 'ko')
    plt.show()

def main():
    x = [0, 1, 2, 3, 4]
    y = [0, 1.5, 2, 1, 3]

    Z = interpoliraj(x, y)
    plot(Z)

if __name__ == "__main__":
    main()