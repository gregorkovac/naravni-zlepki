import numpy as np
import matplotlib.pyplot as plt

class Polinom:
    def __init__(self, a_0, a_1, a_2, a_3):
        self.a_0 = a_0
        self.a_1 = a_1
        self.a_2 = a_2
        self.a_3 = a_3

    def v(self, x):
        return self.a_0 + self.a_1 * x + self.a_2 * x ** 2 + self.a_3 * x ** 3

class Zlepek:
    def __init__(self, x, y):
        self.interpolacijske_tocke = np.array([x, y])
        self.polinomi = []

    def coefs(self, x, i):
        return [0] * 4 * i + [1, x, x ** 2, x ** 3] + [0] * (4 * (self.interpolacijske_tocke.shape[1] - i - 2))
    
    def coefs_prime(self, x, i):
        return [0] * 4 * (i - 1) + [0, 1, 2 * x, 3 * x ** 2, 0, -1, -2 * x, -3 * x ** 2] + [0] * (4 * (self.interpolacijske_tocke.shape[1] - i - 2))

    def coefs_double_prime(self, x, i):
        return [0] * 4 * (i - 1) + [0, 0, 2, 6 * x, 0, 0, -2, -6 * x] + [0] * (4 * (self.interpolacijske_tocke.shape[1] - i - 2))

    def coefs_natural(self, x, i):
        return [0] * 4 * i + [0, 0, 2, 6 * x] + [0] * (4 * (self.interpolacijske_tocke.shape[1] - i - 2))

def interpoliraj(x, y):
    Z = Zlepek(x, y)

    A = []
    b = []

    for i in range(len(x) - 1):

        x1 = x[i]
        x2 = x[i + 1]
        y1 = y[i]
        y2 = y[i + 1]

        A.append(Z.coefs(x1, i))
        b.append(y1)

        A.append(Z.coefs(x2, i))
        b.append(y2)

        if i > 0:
            A.append(Z.coefs_prime(x1, i))
            b.append(0)

            A.append(Z.coefs_double_prime(x1, i))
            b.append(0)
        
        if i == 0:
            A.append(Z.coefs_natural(x1, i))
            b.append(0)
        elif i == len(x) - 2:
            A.append(Z.coefs_natural(x2, i))
            b.append(0)


    A = np.array(A)
    b = np.array(b)

    x = np.linalg.solve(A, b)

    for i in range(len(x) // 4):
        Z.polinomi.append(Polinom(x[4 * i], x[4 * i + 1], x[4 * i + 2], x[4 * i + 3]))

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
    y = x ** 4

    Z = interpoliraj(x, y)
    plot(Z)

if __name__ == "__main__":
    main()