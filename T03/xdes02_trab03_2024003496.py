from abc import ABC, abstractmethod

class EmpDomestica(ABC):

    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, valor):
        self.__telefone = valor

    @abstractmethod
    def getSalario(self):
        pass

class Horista(EmpDomestica):

    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorPorHora = valorPorHora

    @property
    def horasTrabalhadas(self):
        return self.__horasTrabalhadas
    
    @property
    def valorPorHora(self):
        return self.__valorPorHora
    
    def getSalario(self):
        return self.__horasTrabalhadas * self.__valorPorHora
    
class Diarista(EmpDomestica):

    def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
        super().__init__(nome, telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__valorPorDia = valorPorDia

    @property
    def diasTrabalhados(self):
        return self.__diasTrabalhados
    
    @property
    def valorPorDia(self):
        return self.__valorPorDia
    
    def getSalario(self):
        return self.__diasTrabalhados * self.__valorPorDia

class Mensalista(EmpDomestica):

    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__valorMensal = valorMensal

    @property
    def valorMensal(self):
        return self.__valorMensal
    
    def getSalario(self):
        return self.__valorMensal

if __name__ == '__main__':

    empregadas = []
    salarios = []

    EmpH = Horista('Hortênsia', '(12) 1234-5678', 160, 12)
    EmpD = Diarista('Damares', '(35) 5556-7778', 20, 65)
    EmpM = Mensalista('Marília', '(11) 98765-4321', 1200)

    empregadas.append(EmpH)
    empregadas.append(EmpD)
    empregadas.append(EmpM)

    print('Salário mensal da horista: R$ {}'.format(EmpH.getSalario()))
    print('Salário mensal da diarista: R$ {}'.format(EmpD.getSalario()))
    print('Salário mensal da mensalista: R$ {}'.format(EmpM.getSalario()))
    
    for empregada in empregadas:
        salarios.append(empregada.getSalario())

    i = salarios.index(min(salarios))

    print('Opção mais barata: {} (Telefone: {}), salário mensal de R$ {}'.format(empregadas[i].nome, empregadas[i].telefone, salarios[i]))
