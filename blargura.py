import unittest
class Noh:
    def __init__(self, valor, pai = None):
        self.pai = pai
        self.valor = valor
        self.irmao = None
        self.filho = None

        if pai:
            pai.filhos.append(self)
        self.filhos = []

    
    def adicionar(self, filho):
        self.filhos.append(filho)
        filho.pai = self

class Arvore:
    def __init__(self, raiz = None):
        self.raiz = raiz

    def altura(self):
        if self.raiz:
            x = 1
            while self.raiz.filhos:
                self.raiz = self.raiz.filhos[0]
                x = x + 1
            return x
        return 0

    def __iter__(self):
        if self.raiz is None:
            return self.raiz
        pilha = []
        pilha.append(self.raiz)

        while pilha:
            noh = pilha.pop(0)
            if noh.pai is None:
                yield noh.valor
            for x in noh.filhos:
                x.pai = None
                pilha.append(x)

class NohTestes(unittest.case.TestCase):
    def teste_init_com_defaults(self):
        noh = Noh(5)
        self.assertEqual(5, noh.valor)
        self.assertIsNone(noh.pai)
        self.assertListEqual([], noh.filhos)

    def teste_init_com_pai_justaposto(self):
        pai = Noh(5)
        filho = Noh(4, pai)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filhos[0])

    def teste_init_com_pai_nomeado(self):
        pai = Noh(5)
        filho = Noh(4, pai=pai)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filhos[0])

    def teste_adicionar_um_filho(self):
        pai = Noh(5)
        filho = Noh(4)
        pai.adicionar(filho)
        self.assertIs(pai, filho.pai)
        self.assertIs(filho, pai.filhos[0])

    def teste_adicionar_dois_filhos(self):
        pai = Noh(5)
        filho = Noh(4)
        filho2 = Noh(3)
        pai.adicionar(filho)
        pai.adicionar(filho2)
        self.assertIs(pai, filho.pai)
        self.assertIs(pai, filho2.pai)
        self.assertListEqual([filho, filho2], pai.filhos)

    def teste_adicionar_tres_filhos(self):
        pai = Noh(5)
        filho = Noh(4)
        filho2 = Noh(3)
        filho3 = Noh(2)
        pai.adicionar(filho)
        pai.adicionar(filho2)
        pai.adicionar(filho3)
        self.assertIs(pai, filho.pai)
        self.assertIs(pai, filho2.pai)
        self.assertIs(pai, filho3.pai)
        self.assertListEqual([filho, filho2, filho3], pai.filhos)


class ArvoreTestes(unittest.case.TestCase):
    def teste_init(self):
        arvore = Arvore()
        self.assertIsNone(arvore.raiz)

    def teste_arvore_com_raiz(self):
        noh = Noh(1)
        arvore = Arvore(noh)
        self.assertIs(noh, arvore.raiz)

    def teste_altura_arvore(self):
        self.assertEqual(0, Arvore().altura())
        self.assertEqual(1, Arvore(Noh(1)).altura())
        arvore_binaria = self.gerar_arvore_binaria()
        self.assertEqual(4, arvore_binaria.altura())

    def test_travesia_em_largura(self):
        travessia_arvore_vazia = [i for i in Arvore()]
        self.assertListEqual([], travessia_arvore_vazia)
        travessia_arvore_unitaria = [i for i in Arvore(Noh(1))]
        self.assertListEqual([1], travessia_arvore_unitaria)
        arvore_binaria = self.gerar_arvore_binaria()
        travessia_arvore_binaria = [i for i in arvore_binaria]
        self.assertListEqual([5, 2, 8, 1, 4, 7, 9, 0, 3, 6], travessia_arvore_binaria)

    def gerar_arvore_binaria(self):
        nohs = [Noh(i) for i in range(10)]
        raiz = nohs[5]
        raiz.adicionar(nohs[2])
        raiz.adicionar(nohs[8])

        nohs[2].adicionar(nohs[1])
        nohs[2].adicionar(nohs[4])

        nohs[1].adicionar(nohs[0])

        nohs[4].adicionar(nohs[3])

        nohs[8].adicionar(nohs[7])
        nohs[8].adicionar(nohs[9])

        nohs[7].adicionar(nohs[6])

        return Arvore(raiz)
