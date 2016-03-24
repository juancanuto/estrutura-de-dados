from aula4.pilha import Pilha
from aula5.fila import Fila
import unittest

class ErroLexico(Exception):
    pass

class ErroSintatico(Exception):
    pass

def analise_sintatica(fila):
    token = R"-+/*(){}[]"
    if fila.__len__():
        fila_sintatica = Fila()
        num = ''
        num2 = '.'
        for lex in range(fila.__len__()):
            if fila._deque[lex] in token:
                if num:
                    if num2 in num:
                        fila_sintatica.enfileirar(float(num))
                    else:
                        fila_sintatica.enfileirar(int(num))
                num = ''
                fila_sintatica.enfileirar(fila._deque[lex])
            else:
                num = num + fila._deque[lex]
        if num:
            if num2 in num:
                fila_sintatica.enfileirar(float(num))
            else:
                fila_sintatica.enfileirar(int(num))
        return fila_sintatica
    else:
        raise ErroSintatico

def analise_lexica(expressao):
    fila = Fila()
    token = R"0123456789.-+*/{}[]()"
    token2 = R".-+*/{}[]()"
    if expressao:
        num = ''
        for lex in expressao:
            if lex in token:
                if lex in token2:
                    if num:
                        fila.enfileirar(num)
                        num = ''
                    fila.enfileirar(lex)
                else:
                    num = num + lex
            else:
                raise ErroLexico()
        if num:
            fila.enfileirar(num)
    return fila
    
def avaliar(expressao):
    token2 = R".-+*/{}[]()"
    token3 = R"(){}[]"
    num3 = '+'
    if expressao:
        fila = analise_sintatica(analise_lexica(expressao))
        if fila.__len__() == 1:
            return fila.primeiro()
        else:
            pilha = Pilha()
            for lex in range(fila.__len__()):
                pilha.empilhar(fila._deque[lex])
                if pilha.__len__() >= 3 and str(pilha.topo()) not in token2:
                    num = pilha.topo()
                    pilha.desempilhar()
                    if pilha.topo() == num3:
                        pilha.desempilhar()
                        num = pilha.desempilhar() + num
                        pilha.empilhar(num)
                    elif pilha.topo() == '-':
                        pilha.desempilhar()
                        num = pilha.desempilhar() - num
                        pilha.empilhar(num)

                    elif pilha.topo() == '*':
                        pilha.desempilhar()
                        num = pilha.desempilhar() * num
                        pilha.empilhar(num)

                    elif pilha.topo() == '/':
                        pilha.desempilhar()
                        num = pilha.desempilhar() / num
                        pilha.empilhar(num)

                    else:
                        pilha.empilhar(num)
                elif str(pilha.topo()) in ')}]' and lex == fila.__len__() - 1:
                    pilha.desempilhar()
                    while len(pilha) > 1:
                        if str(pilha.topo()) not in token2:
                            num = pilha.topo()
                            pilha.desempilhar()
                            if pilha.topo() == num3:
                                pilha.desempilhar()
                                num = pilha.desempilhar() + num
                                pilha.empilhar(num)

                            elif pilha.topo() == '/':
                                pilha.desempilhar()
                                num = pilha.desempilhar() / num
                                pilha.empilhar(num)

                            elif pilha.topo() == '*':
                                pilha.desempilhar()
                                num = pilha.desempilhar() * num
                                pilha.empilhar(num)

                            elif pilha.topo() == '-':
                                pilha.desempilhar()
                                num = pilha.desempilhar() - num
                                pilha.empilhar(num)

                            elif str(pilha.topo()) in token3:
                                pilha.desempilhar()
                                pilha.empilhar(num)
                            else:
                                pilha.empilhar(num)
                        else:
                            pilha.desempilhar()
            return pilha.topo()
    raise ErroSintatico()

class AnaliseLexicaTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        fila = analise_lexica('')
        self.assertTrue(fila.vazia())

    def test_caracter_estranho(self):
        self.assertRaises(ErroLexico, analise_lexica, 'a')
        self.assertRaises(ErroLexico, analise_lexica, 'ab')

    def test_inteiro_com_um_algarismo(self):
        fila = analise_lexica('1')
        self.assertEqual('1', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_inteiro_com_vários_algarismos(self):
        fila = analise_lexica('1234567890')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_float(self):
        fila = analise_lexica('1234567890.34')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('34', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_parenteses(self):
        fila = analise_lexica('(1)')
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_chaves(self):
        fila = analise_lexica('{(1)}')
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_colchetes(self):
        fila = analise_lexica('[{(1.0)}]')
        self.assertEqual('[', fila.desenfileirar())
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertEqual(']', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_adicao(self):
        fila = analise_lexica('1+2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('+', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_subtracao(self):
        fila = analise_lexica('1-2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('-', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_multiplicacao(self):
        fila = analise_lexica('1*2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('*', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_divisao(self):
        fila = analise_lexica('1/2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('/', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_expresao_com_todos_simbolos(self):
        expressao = '1/{2.0+3*[7-(5-3)]}'
        fila = analise_lexica(expressao)
        self.assertListEqual(list(expressao), [e for e in fila])
        self.assertTrue(fila.vazia())


class AnaliseSintaticaTestes(unittest.TestCase):
    def test_fila_vazia(self):
        fila = Fila()
        self.assertRaises(ErroSintatico, analise_sintatica, fila)

    def test_int(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_float(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila.enfileirar('.')
        fila.enfileirar('4')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890.4, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_expressao_com_todos_elementos(self):
        fila = analise_lexica('1000/{222.125+3*[7-(5-3)]}')
        fila_sintatica = analise_sintatica(fila)
        self.assertListEqual([1000, '/', '{', 222.125, '+', 3, '*', '[', 7, '-', '(', 5, '-', 3, ')', ']', '}'],[e for e in fila_sintatica])


class AvaliacaoTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertRaises(ErroSintatico, avaliar, '')

    def test_inteiro(self):
        self.assert_avaliacao('1')

    def test_float(self):
        self.assert_avaliacao('2.1')

    def test_soma(self):
        self.assert_avaliacao('2+1')

    def test_subtracao_e_parenteses(self):
        self.assert_avaliacao('(2-1)')

    def test_expressao_com_todos_elementos(self):
        self.assertEqual(1.0, avaliar('2.0/[4*3+1-{15-(1+3)}]'))

    def assert_avaliacao(self, expressao):
        self.assertEqual(eval(expressao), avaliar(expressao))


if __name__ == '__main__':
    unittest.main()
