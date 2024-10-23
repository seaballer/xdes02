from abc import ABC, abstractmethod
from datetime import date

IMPOSTO_PF = 0.09
IMPOSTO_PJ = 0.06

class Venda(ABC):

    def __init__(self, nroNF: int, dtEmissao: date) -> None:
        self.__nroNF = nroNF
        self.__dtEmissao = dtEmissao
        self.__itens = []
    
    @property
    def nroNF(self) -> int:
        return self.__nroNF
    
    @property
    def dtEmissao(self) -> date:
        return self.__dtEmissao
    
    @property
    def itens(self) -> list:
        return self.__itens
    
    def adicionaItem(self, pCodProd: int, pQuant: int, precoUnit: float) -> None:
        self.__itens.append(ItemVenda(pCodProd, pQuant, precoUnit))

    def calculaTotalVendido(self) -> float:
        total = 0.0

        for item in self.__itens:
            total += item.quant * item.precoUnit
        
        return total

    @abstractmethod
    def geraNF(self) -> str:
        pass

    @abstractmethod
    def calculaImposto(self) -> float:
        pass

class ItemVenda:

    def __init__(self, codProd: int, quant: int, precoUnit: float) -> None:
        self.__codProd = codProd
        self.__quant = quant
        self.__precoUnit = precoUnit
    
    @property
    def codProd(self) -> int:
        return self.__codProd
    
    @property
    def quant(self) -> int:
        return self.__quant
    
    @property
    def precoUnit(self) -> float:
        return self.__precoUnit
    
class VendaPF(Venda):

    def __init__(self, nroNF: int, dtEmissao: date, cpf: str, nome: str) -> None:
        super().__init__(nroNF, dtEmissao)
        self.__cpf = cpf
        self.__nome = nome
    
    @property
    def cpf(self) -> str:
        return self.__cpf
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    def geraNF(self):
        print('NOME: {} CPF: {}'.format(self.__nome, self.__cpf))
        for item in self.itens:
            print('NUMERO {}    QUANTIDADE {}  VALOR: R${:.2f}'.format(item.codProd, item.quant, item.precoUnit))
        print()
        print('VALOR TOTAL VENDIDO: R$ {:.2f}'.format(item.calculaTotalVendido()))
    
    def calculaImposto(self):
        return self.calculaTotalVendido() * IMPOSTO_PF

class VendaPJ(Venda):

    def __init__(self, nroNF: int, dtEmissao: int, cnpj: str, nomeFantasia: str) -> None:
        super().__init__(nroNF, dtEmissao)
        self.__cnpj = cnpj
        self.__nomeFantasia = nomeFantasia

    @property
    def cnpj(self) -> str:
        return self.__cnpj
    
    @property
    def nomeFantasia(self) -> str:
        return self.__nomeFantasia
    
    def geraNF(self):
        print('NOME: {} CNPJ: {}'.format(self.__nomeFantasia, self.__cnpj))
        for item in self.itens:
            print('NUMERO {}    QUANTIDADE {}  VALOR: R${:.2f}'.format(item.codProd, item.quant, item.precoUnit))
        print()
        print('VALOR TOTAL VENDIDO: R$ {:.2f}'.format(item.calculaTotalVendido()))

    def calculaImposto(self):
        return self.calculaTotalVendido() * IMPOSTO_PJ

if __name__ == "__main__":     

    totalFaturado = 0     
    totalImposto = 0     
    vendas = []     

    vendapf = VendaPF(1000, date.today(), '123456789', 'Joao')     
    vendapf.adicionaItem(100, 10, 10)     
    vendapf.adicionaItem(100, 10, 20)     
    vendapf.adicionaItem(100, 10, 30)     
    vendas.append(vendapf)     

    vendapj = VendaPJ(1001, date.today(), '987654321', 'Silva Ltda')     
    vendapj.adicionaItem(200, 100, 10)     
    vendapj.adicionaItem(201, 100, 20)     
    vendas.append(vendapj)     

    for venda in vendas:         
        totalFaturado += venda.calculaTotalVendido()         
        totalImposto += venda.calculaImposto()
        
    print('Total faturado: {}'.format(totalFaturado))     
    print('Total pago em impostos: {}'.format(totalImposto))    
