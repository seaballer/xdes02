from abc import ABC, abstractmethod

# constantes
PI = 3.14

class Terreno(ABC):

    def __init__(self, localizacao, preco):
        self.__localizacao = localizacao
        self.__preco = preco

    @property
    def localizacao(self):
        return self.__localizacao
    
    @localizacao.setter
    def localizacao(self, valor):
        self.__localizacao = valor

    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        self.__preco = valor

    @abstractmethod
    def calcula_peso(self):
        pass

class TerrenoCircular(Terreno):

    def __init__(self, localizacao, preco, raio):
        super().__init__(localizacao, preco)
        self.__raio = raio
    
    @property
    def raio(self):
        return self.__raio
    
    def calcula_peso(self):
        return self.preco / (self.__raio * self.__raio * PI)
    
class TerrenoRetangular(Terreno):

    def __init__(self, localizacao, preco, ladoMenor, ladoMaior):
        super().__init__(localizacao, preco)
        self.__ladoMenor = ladoMenor
        self.__ladoMaior = ladoMaior

    @property
    def ladoMenor(self):
        return self.__ladoMenor
    
    @property
    def ladoMaior(self):
        return self.__ladoMaior
    
    def calcula_peso(self):
        return self.preco / (self.__ladoMaior * self.__ladoMenor)

if __name__ == '__main__':

    terrenos = []
    pesos = []
    
    tc1 = TerrenoCircular('BPS', 70000, 15)
    tr1 = TerrenoRetangular('Piranguinho', 75000, 20, 35)
    tc2 = TerrenoCircular('Maria da Fe', 110000, 20)

    terrenos.append(tc1)
    terrenos.append(tr1)
    terrenos.append(tc2)

    for terreno in terrenos:
        print('Terreno em {}'.format(terreno.localizacao))
        print('Preco: R${}'.format(terreno.preco))
        print('Peso: R${} por metro quadrado'.format(terreno.calcula_peso()))
        print()

        pesos.append(terreno.calcula_peso())
    
    i = pesos.index(min(pesos))

    print('Melhor custo por metro quadrado: {}'.format(terrenos[i].localizacao))
    print('Preco: R$ {}    Peso: R${} por metro quadrado'.format(terrenos[i].preco, pesos[i]))
