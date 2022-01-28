import unittest
from src.binario import binarioDecimal, esBinario

class binarioTest(unittest.TestCase):
    def setUp(self):
        print("Empezando Test...")
    
    def tearDown(self):
        print("Test ejecutado...")
    
    def test_value(self):
        self.assertTrue(esBinario("1001"))
        self.assertFalse(esBinario("123"))
    
    def test_letter(self):
        self.assertFalse(esBinario("Hola"))
    
    def test_negative(self):
        self.assertFalse(esBinario("-1001"))

    def test_convert(self):
        self.assertEqual(binarioDecimal("111"), 7)
        self.assertEqual(binarioDecimal("1001"), 9)
        self.assertEqual(binarioDecimal("123"), 'El número no es binario')

if __name__ == '__main__':
    unittest.main()