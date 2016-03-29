__author__ = 'Juan'

import unittest

''' O(n²)'''

def insertion_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        for i in range(1, len(seq)):
            s = seq[i]
            j = i
            while j > 0 and seq[j - 1] > s:
                seq[j] = seq[j - 1]
                j -= 1
            seq[j] = s
        return seq


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], insertion_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], insertion_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], insertion_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insertion_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
