import numpy as np
import matplotlib.pyplot as plt

"""
Razred Polinom predstavlja polinom oblike a_0 + a_1 * x + a_2 * x^2 + a_3 * x^3.

Atributi:
    - a_0, a_1, a_2, a_3  (float): koeficienti polinoma

Metode:
    - v(x): vrne vrednost polinoma v točki x
        - Vhod: x (float) ... točka, v kateri računamo vrednost polinoma
        - Izhod: (float) vrednost polinoma v točki x
"""
class Polinom:
    def __init__(self, a_0, a_1, a_2, a_3):
        self.a_0 = a_0
        self.a_1 = a_1
        self.a_2 = a_2
        self.a_3 = a_3

    def v(self, x):
        return self.a_0 + self.a_1 * x + self.a_2 * x ** 2 + self.a_3 * x ** 3
    
"""
Razred Zlepek predstavlja zlepek polinomov, ki interpolirajo dane točke.

Atributi:
    - interpolacijske_tocke (numpy.ndarray, shape=(2, n)): koordinate interpolacijskih točk
    - polinomi (list[Polinom]): seznam polinomov, ki interpolirajo točke

Metode:
    - coefs(x, i): vrne koeficiente polinoma i v točki x za nastavitev sistema enačb.
        - Vhod: x (float) ... točka, v kateri računamo koeficiente polinoma
                i (int) ... indeks polinoma
        - Izhod: (list[float]) koeficienti polinoma i v točki x. Oblika: [0, ..., 0, 1, x, x^2, x^3, 0, ..., 0]

    - coefs_prime(x, i): vrne koeficiente razlike odvodov polinomov i in i - 1 v točki x za nastavitev sistema enačb.
        - Vhod: x (float) ... točka, v kateri računamo koeficiente
                i (int) ... indeks polinoma
        - Izhod: (list[float]) koeficienti razlike odvodov polinomov i in i - 1 v točki x. Oblika: [0, ..., 0, 0, 1, 2x, 3x^2, 0, -1, -2x, -3x^2, 0, ..., 0]

    - coefs_double_prime(x, i): vrne koeficiente razlike drugih odvodov polinomov i in i - 1 v točki x za nastavitev sistema enačb.
        - Vhod: x (float) ... točka, v kateri računamo koeficiente
                i (int) ... indeks polinoma
        - Izhod: (list[float]) koeficienti razlike drugih odvodov polinomov i in i - 1 v točki x. Oblika: [0, ..., 0, 0, 0, 2, 6x, 0, 0, -2, -6x, 0, ..., 0]

    - coefs_natural(x, i): vrne koeficiente drugega odvoda polinoma i v točki x za nastavitev sistema enačb.
        - Vhod: x (float) ... točka, v kateri računamo koeficiente
                i (int) ... indeks polinoma
        - Izhod: (list[float]) koeficienti drugega odvoda polinoma i v točki x. Oblika: [0, ..., 0, 0, 2, 6x, 0, ..., 0]
    
    - v(x): vrne vrednost zlepka v točki x
        - Vhod: x (float) ... točka, v kateri računamo vrednost zlepka
        - Izhod: (float) vrednost zlepka v točki x

"""
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
    
    def v(self, x):
        for i in range(len(self.interpolacijske_tocke[0]) - 1):
            if x >= self.interpolacijske_tocke[0][i] and x <= self.interpolacijske_tocke[0][i + 1]:
                return self.polinomi[i].v(x)
            
        return None

"""
interpoliraj(x, y): interpolira dane točke (x, y) z zlepkom.

Vhod:
    - x (numpy.ndarray, shape=(n,)): x koordinate interpolacijskih točk
    - y (numpy.ndarray, shape=(n,)): y koordinate interpolacijskih točk

Izhod:
    - Z (Zlepek): zlepek.
"""
def interpoliraj(x, y):

    # Inicializacija zlepka
    Z = Zlepek(x, y)

    # Inicializacija sistema enačb
    A = []
    b = []

    # Nastavitev sistema enačb
    for i in range(len(x) - 1):
        # Priprava i-te in (i+1)-te interpolacijske točke
        x1 = x[i]
        x2 = x[i + 1]
        y1 = y[i]
        y2 = y[i + 1]

        # Koeficienti S(x_i) = y_i
        A.append(Z.coefs(x1, i))
        b.append(y1)

        # Koeficienti S(x_{i+1}) = y_{i+1}
        A.append(Z.coefs(x2, i))
        b.append(y2)

        # Koeficienti S'(x_{i+1}) - S'(x_i) = 0 in S''x_{i+1}) - S''(x_i) = 0; za vmesne točke
        if i > 0:
            A.append(Z.coefs_prime(x1, i))
            b.append(0)

            A.append(Z.coefs_double_prime(x1, i))
            b.append(0)
        
        # Koeficienti S''(x_0) = 0 in S''(x_{n-1}) = 0 za robni točki - pogoj naravnega zlepka
        if i == 0:
            A.append(Z.coefs_natural(x1, i))
            b.append(0)
        if i == len(x) - 2:
            A.append(Z.coefs_natural(x2, i))
            b.append(0)

    # Pretvorba v Numpy array
    A = np.array(A)
    b = np.array(b)

    # Rešitev sistema enačb
    x = np.linalg.solve(A, b)

    # Ustvarjanje polinomov
    for i in range(len(x) // 4):
        Z.polinomi.append(Polinom(x[4 * i], x[4 * i + 1], x[4 * i + 2], x[4 * i + 3]))

    return Z

"""
plot(Z): izriše zlepek Z in njegove interpolacijske točke.

Vhod:
    - Z (Zlepek): zlepek.
    - func (lambda): funkcija, iz katere so bile generirane točke. 
                     Na grafu je predstavljena s črtkano črto.

Izhod: /
"""
def plot(Z, func=None):
    # Priprava interpolacijskih točk
    x = Z.interpolacijske_tocke[0]
    y = Z.interpolacijske_tocke[1]

    for i in range(len(Z.polinomi)):
        # Priprava i-tega polinoma
        p = Z.polinomi[i]

        # Priprava 100 točk med x1 in x2 za izris polinoma
        x1 = x[i]
        x2 = x[i + 1]
        x_p= np.linspace(x1, x2, 100)
        y_p = p.v(x_p)

        # Določitev barve polinoma. Sodo število = modra, liho število = rdeča
        col = i % 2 == 0 and 'b' or 'r'

        # Izris polinoma
        plt.plot(x_p, y_p, col)

    # Izris interpolacijskih točk
    plt.plot(x, y, 'ko')

    # Izris funkcije func, če je podana
    if func is not None:
        xf = np.linspace(x[0], x[-1], 100)
        yf = func(xf)
        plt.plot(xf, yf, 'k--')

    plt.show()

def main():
    x = np.array([-2, -1, 0, 1, 2])
    y = np.array([4, 1, 0, 1, 4])
    Z = interpoliraj(x, y)

    plot(Z, lambda x: x ** 2)

if __name__ == "__main__":
    main()