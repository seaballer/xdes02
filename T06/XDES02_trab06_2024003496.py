from datetime import date

class Conta():

    def __init__(self, nroConta:int, nome:str, limite:int, senha:str) -> None:
        self.__nroConta = nroConta
        self.__nome = nome
        self.__limite = limite
        self.__senha = senha
        self.__transacoes = []

    @property
    def nroConta(self) -> int:
        return self.__nroConta
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def limite(self) -> int:
        return self.__limite
    
    @property
    def senha(self) -> str:
        return self.__senha
    
    @property
    def transacoes(self) -> list:
        return self.__transacoes
    
    def adicionaDeposito(self, valor, data, nomeDepositante) -> None:
        self.__transacoes.append(Deposito(valor, data, nomeDepositante))
    
    def adicionaSaque(self, valor, data, senha) -> bool:
        if senha != self.__senha or self.calculaSaldo() < valor:
            return False
        
        self.__transacoes.append(Saque(valor, data, senha))
        return True

    def adicionaTransf(self, valor, data, senha, contaFavorecido) -> bool:
        if senha != self.__senha or self.calculaSaldo() < valor:
            return False
        
        self.__transacoes.append(Transferencia(valor, data, senha, 'D'))
        contaFavorecido.__transacoes.append(Transferencia(valor, data, senha, 'C'))
        return True
    
    def calculaSaldo(self):
        saldo = self.__limite

        for transacao in self.__transacoes:
            if type(transacao) is Deposito:
                saldo += transacao.valor
            elif type(transacao) is Saque:
                saldo -= transacao.valor
            elif type(transacao) is Transferencia:
                if transacao.tipoTransf == 'C':
                    saldo += transacao.valor
                else:  # transacao.tipoTransf == 'D'
                    saldo -= transacao.valor
        
        return saldo

class Transacao():

    def __init__(self, valor:int, data:str) -> None:
        self.__valor = valor
        self.__data = data

    @property
    def valor(self) -> int:
        return self.__valor
    
    @property
    def data(self) -> str:
        return self.__data

class Saque(Transacao):

    def __init__(self, valor:int, data:str, senha:str) -> None:
        super().__init__(valor, data)
        self.__senha = senha
    
    @property
    def senha(self):
        return self.__senha

class Deposito(Transacao):

    def __init__(self, valor:int, data:str, nomeDepositante:str):
        super().__init__(valor, data)
        self.__nomeDepositante = nomeDepositante
    
    @property
    def nomeDepositante(self):
        return self.__nomeDepositante

class Transferencia(Transacao):
    
    def __init__(self, valor:int, data:str, senha:str, tipoTransf:str):
        super().__init__(valor, data)
        self.__senha = senha
        self.__tipoTransf = tipoTransf

    @property
    def senha(self):
        return self.__senha
    
    @property
    def tipoTransf(self):
        return self.__tipoTransf

if __name__ == "__main__":
    c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')     
    c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')     
    if c1.adicionaSaque(2000, date.today(), 'senha1') == False:         
        print('Não foi possível realizar o saque no valor de 2000')     
    if c1.adicionaSaque(1000, date.today(), 'senha-errada') == False:  # deve falhar         
            print('Não foi possível realizar o saque no valor de 1000')          
    
    c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')     
    c2.adicionaDeposito(3000, date.today(), 'Maria da Cruz')     
    if c2.adicionaSaque(1500, date.today(), 'senha2') == False:        
        print('Não foi possível realizar o saque no valor de 1500')     
    if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False:  # deve falhar         
        print('Não foi possível realizar a transf no valor de 5000')     
    if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:         
        print('Não foi possível realizar a transf no valor de 800')
       
    print('--------')     
    print('Saldo de c1: {}'.format(c1.calculaSaldo()))  # deve imprimir 4800     
    print('Saldo de c2: {}'.format(c2.calculaSaldo()))  # deve imprimir 1700 
