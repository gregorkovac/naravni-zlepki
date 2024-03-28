import numpy as np
import matplotlib.pyplot as plt

class Polinom:
    def __init__(self, a_0, a_1, a_2, a_3, x1):
        self.a_0 = a_0
        self.a_1 = a_1
        self.a_2 = a_2
        self.a_3 = a_3
        self.x1 = x1

    def v(self, x):
        return self.a_0 + self.a_1 * (x - self.x1) + self.a_2 * (x - self.x1) ** 2 + self.a_3 * (x - self.x1) ** 3

class Zlepek:
    def __init__(self, x, y):
        self.interpolacijske_tocke = np.array([x, y])
        self.polinomi = []

def f(x):
    return x ** 4

def dfdx(x):
    return 4 * x ** 3

def interpoliraj(x, y):
    Z = Zlepek(x, y)

    for i in range(len(x) - 1):
        x1 = x[i]
        x2 = x[i + 1]
        y1 = y[i]
        y2 = y[i + 1]

        h = x2 - x1
        a_0 = y1
        a_1 = dfdx(x1)
        a_2 = 3 / h ** 2 * (y2 - y1) - 1 / h * (dfdx(x2) + 2 * dfdx(x1))
        a_3 = 2/h ** 3 * (y1 - y2) + 1/h ** 2 * (dfdx(x1) + dfdx(x2))

        Z.polinomi.append(Polinom(a_0, a_1, a_2, a_3, x1))

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
    x = np.array([-2, -1, 0, 1, 2])
    y = f(x)

    Z = interpoliraj(x, y)
    plot(Z)

if __name__ == "__main__":
    main()