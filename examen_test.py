# coding=utf-8

import unittest
from examen import analisis_lista


class ExamenTest(unittest.TestCase):
    # Test fixtures

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Pruebas del análisis de las listas

    def test_1(self):
        self.assertEqual(analisis_lista([1, 2, 3, 4, 5, 6, 7], 4),
                         [[[1, 2, 3], [5, 6, 7], [4]], [4]])

    def test_2(self):
        self.assertEqual(analisis_lista([1, 2, 3, 4, 5, 6, 7], -1),
                         [[[], [1, 2, 3, 4, 5, 6, 7], []],
                          [1, 2, 3, 4, 5, 6, 7]])

    def test_3(self):
        self.assertEqual(analisis_lista([1, 2, 3, 4, 5, 6, 7], 8),
                         [[[1, 2, 3, 4, 5, 6, 7], [], []], []])

    def test_4(self):
        self.assertEqual(analisis_lista([2, 3, 2, 3, 2, 3, 2], 2),
                         [[[], [3, 3, 3], [2, 2, 2, 2]], [2, 2, 2, 2]])

    def test_5(self):
        self.assertEqual(analisis_lista([2, 3, 2, 3, 2, 3, 2], 3),
                         [[[2, 2, 2, 2], [], [3, 3, 3]], [3, 3, 3]])


# Ejecuta las pruebas implementadas

if __name__ == '__main__':
    unittest.main()
