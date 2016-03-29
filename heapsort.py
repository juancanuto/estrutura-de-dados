import unittest

def heapsort(seq):
  for inicio in range(int(len(seq)-2/2), -1, -1):
    descer(seq, inicio, len(seq)-1)

  for final in range(len(seq)-1, 0, -1):
    seq[final], seq[0] = seq[0], seq[final]
    descer(seq, 0, final - 1)
  return seq

def descer(seq, inicio, final):
  pivo = inicio
  while True:
    metade = pivo * 2 + 1
    if metade > final: break
    if metade + 1 <= final and seq[metade] < seq[metade + 1]:
      metade += 1
    if seq[pivo] < seq[metade]:
      seq[pivo], seq[metade] = seq[metade], seq[pivo]
      pivo = metade
    else:
      break


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], heapsort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], heapsort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], heapsort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], heapsort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()