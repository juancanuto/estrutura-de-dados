#Juan Canuto Hassam

import unittest

def menor(seq, tam):
    '''
    :param seq: uma sequencia
    :param tam: tamanho do vetor pra comparar
    :return: (menor)

     Retorna o menor de uma sequencia

    '''
    if tam < 2:
        return seq[0]
    else:
        resultado = menor(seq, tam - 1)
        if resultado < seq[tam - 1]:
            return resultado
        else:
            return seq[tam - 1]
def maior(seq, tam):
    '''
    :param seq: uma sequencia
    :param tam: usado para comparar
    :return: (maior)

     Retorna o maior valor da sequencia.
     
    '''
    if tam < 2:
        return seq[0]
    else:
        resultado = maior(seq, tam - 1)
        if resultado > seq[tam - 1]:
            return resultado
        else:
            return seq[tam - 1]
def min_max(seq):
    '''
    :param seq: uma sequencia
    :return: (min, max)

     Verifica se o vetor esta vazio , senão estiver ele chama as 2 funções Maior
     e Menor e retorna o resultado delas.

     O algoritmo roda em em O(n) creio eu , é diretamente ligado ao tamanho do
     vetor.
    '''

    if seq == []:
        return None ,None
    else:
        return menor(seq, len(seq)), maior(seq, len(seq))



class MinMaxTestes(unittest.TestCase):
    def test_lista_vazia(self):
        self.assertTupleEqual((None, None), min_max([]))

    def test_lista_len_1(self):
        self.assertTupleEqual((1, 1), min_max([1]))

    def test_lista_consecutivos(self):
        self.assertTupleEqual((0, 500), min_max(list(range(501))))


if __name__ == '__main__':
    unittest.main()
