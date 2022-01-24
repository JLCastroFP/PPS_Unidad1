import unittest
from src.lista import *

class listaTest(unittest.TestCase):
    def setUp(self):
        print("Empezando Test...")
    
    def tearDown(self):
        print("Test ejecutado...")
    
    def test_Ord(self):
        self.assertEqual(ordenarLista(lista), [1, 2, 3, 6, 11, 14, 15, 19])
    
    def test_OrdRev(self):
        self.assertEqual(ordenarListaRev(lista), [19, 15, 14, 11, 6, 3, 2, 1])

    def test_range(self):
        self.assertEqual(estaEnRango(10,1,15), 'Está en rango')
        self.assertEqual(estaEnRango(10,1,5), 'No está en rango')

    def test_lists(self):
        self.assertEqual(estaEnLista(10, lista), 'No está en la lista')
        self.assertEqual(estaEnLista(11, lista), 'Está en la lista')

if __name__ == '__main__':
    unittest.main()