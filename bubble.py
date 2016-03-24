import unittest

def bubble_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        for x in range(0,len(seq)):
            for i in range(0,len(seq)-1):
                if seq[i]>seq[i+1]:
                    seq[i+1], seq[i] = seq[i], seq[i+1]
    return seq
'''
Complexidade: O(n²) para tempo de execução.
'''


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], bubble_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], bubble_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], bubble_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()