import unittest
from calculadora_media import calcular_media 

class TestCalculoMedia(unittest.TestCase):
    def test_media_basica(self):
        # Teste para valores comuns
        self.assertEqual(calcular_media(6, 8, 10), 8)

    def test_media_zero(self):
        # Teste para caso em que todas as notas são zero
        self.assertEqual(calcular_media(0, 0, 0), 0)
        
    def test_media_valores_maximos(self):
        # Teste para valores máximos (assumindo uma escala de 0 a 10)
        self.assertEqual(calcular_media(10, 10, 10), 10)

    def test_media_valores_decimais(self):
        # Teste para notas com valores decimais
        self.assertAlmostEqual(calcular_media(6.5, 7.5, 8.0), 7.333333, places=5)

if __name__ == '__main__':
    unittest.main()
