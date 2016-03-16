import unittest
from aula4.pilha import Pilha
'''  Analise de complexidade: O(n)'''

def esta_balanceada(expressao):

    pilha = Pilha()
    abrir='{[('
    fechar='}])'

    if expressao and expressao[0] in fechar:
        return False
    for x in expressao:
        if x in abrir:
            pilha.empilhar(x)
            #print (x)
        elif x in fechar:
            if x == '}' and pilha.desempilhar() != '{' or x == ')' and pilha.desempilhar() != '(' or x == ']' and pilha.desempilhar() != '['  :
                return False
    if pilha.vazia():
        return True

class BalancearTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertTrue(esta_balanceada(''))

    def test_parenteses(self):
        self.assertTrue(esta_balanceada('()'))

    def test_chaves(self):
        self.assertTrue(esta_balanceada('{}'))

    def test_colchetes(self):
        self.assertTrue(esta_balanceada('[]'))

    def test_todos_caracteres(self):
        self.assertTrue(esta_balanceada('({[]})'))
        self.assertTrue(esta_balanceada('[({})]'))
        self.assertTrue(esta_balanceada('{[()]}'))

    def test_chave_nao_fechada(self):
        self.assertFalse(esta_balanceada('{'))

    def test_colchete_nao_fechado(self):
        self.assertFalse(esta_balanceada('['))

    def test_parentese_nao_fechado(self):
        self.assertFalse(esta_balanceada('('))

    def test_chave_nao_aberta(self):
        self.assertFalse(esta_balanceada('}{'))

    def test_colchete_nao_aberto(self):
        self.assertFalse(esta_balanceada(']['))

    def test_parentese_nao_aberto(self):
        self.assertFalse(esta_balanceada(')('))

    def test_falta_de_caracter_de_fechamento(self):
        self.assertFalse(esta_balanceada('({[]}'))

    def test_falta_de_caracter_de_abertura(self):
        self.assertFalse(esta_balanceada('({]})'))

    def test_expressao_matematica_valida(self):
        self.assertTrue(esta_balanceada('({[1+3]*5}/7)+9'))

    def test_char_errado_fechar(self):
        self.assertFalse(esta_balanceada('[)'))

if __name__ == '__main__':
    unittest.main()
