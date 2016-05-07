from collections import Counter

cache={0:[0]}

def soma_quadrados(n):
    if n == 0:
        return [0]

    square=[]
    maximo = 1

    while(maximo * maximo <= n):
        square.append(maximo * maximo)
        maximo+= 1

    while len(square)> 0:
        numero = n

        quad = square.copy()
        x = quad.pop()
        vt =[]

        while(numero > 0):
            if numero in cache.keys() and numero is not n:
                vt = vt+cache[numero]

                numero= 0

            else:
                if len(quad) > 0:

                    if numero - x < 0:
                       x = quad.pop()

                    else:
                        numero-= x
                        vt.append(x)
                        if(numero < quad[-1]):
                            x = quad.pop()
                else:
                    numero-= x
                    vt.append(x)

        if n not in cache.keys():
            cache[n]= vt.copy()

        elif len(vt) < len(cache[n]):
            cache[n]= vt.copy()
        square.pop()

    return cache[n]




import unittest


class SomaQuadradosPerfeitosTestes(unittest.TestCase):
    def teste_0(self):
        self.assert_possui_mesmo_elementos([0], soma_quadrados(0))

    def teste_01(self):
        self.assert_possui_mesmo_elementos([1], soma_quadrados(1))

    def teste_02(self):
        self.assert_possui_mesmo_elementos([1, 1], soma_quadrados(2))

    def teste_03(self):
        self.assert_possui_mesmo_elementos([1, 1, 1], soma_quadrados(3))

    def teste_04(self):
        self.assert_possui_mesmo_elementos([4], soma_quadrados(4))

    def teste_05(self):
        self.assert_possui_mesmo_elementos([4, 1], soma_quadrados(5))

    def teste_11(self):
        self.assert_possui_mesmo_elementos([9, 1, 1], soma_quadrados(11))

    def teste_12(self):
        self.assert_possui_mesmo_elementos([4, 4, 4], soma_quadrados(12))


    def assert_possui_mesmo_elementos(self, esperado, resultado):
        self.assertEqual(Counter(esperado), Counter(resultado))
