import unittest

from zlepek import *

class TestZlepek(unittest.TestCase):

    def test_polinom(self):
        p = Polinom(1, 2, 3, 4)
        self.assertEqual(p.v(0), 1)
        self.assertEqual(p.v(1), 10)
        self.assertEqual(p.v(2), 49)
        self.assertEqual(p.v(3), 142)

    def test_zlepek_coefs(self):
        x = np.array([0, 1, 2])
        y = np.array([3, 4, 5])

        Z = interpoliraj(x, y)

        coefs1 = Z.coefs(2, 0)
        coefs2 = Z.coefs(2, 1)
        self.assertEqual(coefs1, [1, 2, 4, 8, 0, 0, 0, 0])
        self.assertEqual(coefs2, [0, 0, 0, 0, 1, 2, 4, 8])

        coefs_prime = Z.coefs_prime(2, 1)
        self.assertEqual(coefs_prime, [0, 1, 4, 12, 0, -1, -4, -12])

        coefs_double_prime = Z.coefs_double_prime(2, 1)
        self.assertEqual(coefs_double_prime, [0, 0, 2, 12, 0, 0, -2, -12])
    
        coefs_natural_1 = Z.coefs_natural(2, 0)
        coefs_natural_2 = Z.coefs_natural(2, 1)
        self.assertEqual(coefs_natural_1, [0, 0, 2, 12, 0, 0, 0, 0])
        self.assertEqual(coefs_natural_2, [0, 0, 0, 0, 0, 0, 2, 12])
        
    def test_zlepek_v(self):
        x = np.array([0, 1, 2])
        y = np.array([3, 4, 5])

        Z = interpoliraj(x, y)

        self.assertEqual(Z.v(0), 3)
        self.assertEqual(Z.v(0.5), 3.5)
        self.assertEqual(Z.v(1), 4)
        self.assertEqual(Z.v(1.5), 4.5)
        self.assertEqual(Z.v(2), 5)

    def test_zlepek_line(self):
        x = np.array([0, 1])
        y = np.array([0, 1])

        Z = interpoliraj(x, y)

        self.assertEqual(len(Z.polinomi), 1)
        self.assertEqual(Z.polinomi[0].a_0, 0)
        self.assertEqual(Z.polinomi[0].a_1, 1)
        self.assertEqual(Z.polinomi[0].a_2, 0)
        self.assertEqual(Z.polinomi[0].a_3, 0)

    def test_zlepek_tri(self):
        x = np.array([-1, 0, 1])
        y = np.array([1, 0, 1])
        
        Z = interpoliraj(x, y)

        self.assertEqual(len(Z.polinomi), 2)
        self.assertEqual(Z.polinomi[0].a_0, 0)
        self.assertEqual(Z.polinomi[0].a_1, 0)
        self.assertEqual(Z.polinomi[0].a_2, 1.5)
        self.assertEqual(Z.polinomi[0].a_3, 0.5)

        self.assertEqual(Z.polinomi[1].a_0, 0)
        self.assertEqual(Z.polinomi[1].a_1, 0)
        self.assertEqual(Z.polinomi[1].a_2, 1.5)
        self.assertEqual(Z.polinomi[1].a_3, -0.5)


    def test_zlepek_parabola(self):
        eps = 0.1

        x = np.array([-2, -1, 0, 1, 2])
        y = x ** 2

        Z = interpoliraj(x, y)

        self.assertEqual(len(Z.polinomi), 4)
        
        x_linspace = np.linspace(-2, 2, 100)
        y_linspace = x_linspace ** 2
        y_interpolated = np.array([Z.v(x) for x in x_linspace])
        self.assertTrue(np.all(np.abs(y_linspace - y_interpolated) < eps))

    def test_zlepek_sin(self):
        eps = 0.1

        x = np.array([k * np.pi / 2 for k in range(50)])
        y = np.sin(x)

        Z = interpoliraj(x, y)

        self.assertEqual(len(Z.polinomi), 49)
        
        x_linspace = np.linspace(0, np.pi, 100)
        y_linspace = np.sin(x_linspace)
        y_interpolated = np.array([Z.v(x) for x in x_linspace])
        self.assertTrue(np.all(np.abs(y_linspace - y_interpolated) < eps))


if __name__ == '__main__':
    unittest.main()