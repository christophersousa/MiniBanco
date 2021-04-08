
class Conta:
    def __init__(self, ident, cpf, saldo):
        self.__id = ident
        self.__cpf = cpf
        self.__saldo = saldo
        self.__prox = None
    
    #Modo de Acesso 
    
    @property
    def identificador(self):
        return self.__id

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def prox(self):
        return self.__prox
    
    #Modo de alteração

    @identificador.setter
    def identificador(self, novo_id):
        self.__id = novo_id
    
    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    @saldo.setter
    def saldo(self, novo_saldo):

        self.__saldo = novo_saldo
    
    @prox.setter
    def prox(self, novo_prox):

        self.__prox = novo_prox
        
    
    #metodos

    def creditar(self, valor):
        self.__saldo += valor
        return True
    
    def debitar(self, valor):
        self.__saldo -= valor
        return True

    def __str__(self):
      return f'Id = {self.__id} CPF = {self.__cpf}  Saldo = {self.__saldo}'


