import unittest
from pruebas import Pruebas

class TestMethodsCalculadora(unittest.TestCase):

    def setUp(self):
        self.Pruebas = Pruebas
        self.var1 = 1
        self.var2 = 5

    def test_suma(self):
        self.assertEqual(self.Pruebas.suma(self.var1, self.var2), 6)

    def test_resta(self):
        self.assertEqual(Pruebas.resta(self.var1, self.var2), -4)

    def test_randomnum_superior(self):
        self.assertGreaterEqual(Pruebas.randomnum(), 0)

    def test_randomnum_inferior(self):
        self.assertLessEqual(Pruebas.randomnum(), 100)

    def test_multiplicacion(self):
        self.assertEqual(Pruebas.multiplicacion(10), 120)

    def test_multiplicacion_sin_entrada(self):
        with self.assertRaises(TypeError):
            Pruebas.multiplicacion()

if __name__ == "__main__":
    unittest.main(verbosity=2)