import unittest

def quicksort(seq):
    if len(seq) <= 1:
        return seq
    else:
        pivo = seq[0]
        iguais  = [x for x in seq if x == pivo]
        menores = [x for x in seq if x <  pivo]
        maiores = [x for x in seq if x >  pivo]
        seq = quicksort(menores) + iguais + quicksort(maiores)
        return seq

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], quicksort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], quicksort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], quicksort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], quicksort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
