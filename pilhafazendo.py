__author__ = 'Juan'

import unittest
def vazia(self):
        return not bool(self.tam)

class PilhaVaziaErro(Exception):
    try:
         self.tam == 0
    except Exception:
        print ("Lista Vazia")

class Noh():
    def __init__(self, valor, esquerdo=None, direito=None):
        self.valor = valor
        self.esquerdo = esquerdo
        self.direito = direito

class Pilha(): ##pilha
    def __init__(self):
        self.tam = 0
        self.primeiro = None
        self.topo = None

    def empilhar(self, valor):
        noh = Noh(valor)
        if self.tam == 0:
            self.primeiro = noh
            self.topo = noh
        else:
            ultimo = self.primeiro
            while ultimo.direito is not None:
                ultimo = ultimo.direito
            self.topo = noh
            ultimo.direito = noh
            noh.esquerdo = ultimo

        self.tam += 1


    def desempilhar(self):

        if self.tam == 0:
            raise PilhaVaziaErro()

        ultimo = self.topo
        if self.tam == 1:
            self.topo = None
            self.primeiro = None
        else:
            penultimo = ultimo.esquerdo
            penultimo.direito = None
            self.topo = penultimo
        self.tam -= 1
        return ultimo.valor

    def vazia(self):
        return not bool(self.tam)

    def top(self):
        ultimo = self.topo
        return ultimo.valor


class PilhaTestes(unittest.TestCase):
    def test_top_lista_vazia(self): #top
        pilha = Pilha()
        self.assertTrue(pilha.vazia())
        self.assertRaises(PilhaVaziaErro, pilha.topo) #top

    def test_empilhar_um_elemento(self):
        pilha = Pilha()
        pilha.empilhar('A')
        self.assertFalse(pilha.vazia())
        self.assertEqual('A', pilha.top())

    def test_empilhar_dois_elementos(self):
        pilha = Pilha()
        pilha.empilhar('A')
        pilha.empilhar('B')
        self.assertFalse(pilha.vazia())
        self.assertEqual('B', pilha.top())

    def test_desempilhar_pilha_vazia(self):
        pilha = Pilha()
        self.assertRaises(PilhaVaziaErro, pilha.desempilhar)

    def test_desempilhar(self):
        pilha = Pilha()
        letras = 'ABCDE'
        for letra in letras:
            pilha.empilhar(letra)

        for letra_em_ordem_reversa in reversed(letras):
            letra_desempilhada = pilha.desempilhar()
            self.assertEqual(letra_em_ordem_reversa, letra_desempilhada)

if __name__ == '__main__':
    unittest.main()

       
          
     
    
