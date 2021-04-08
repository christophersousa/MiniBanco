
from pilha import PilhaEncadeada
from lista import ListaEncadeada
from fila import FilaEncadeada


class Banco:
    def __init__(self, banco):
        self.__banco = banco
        self.__contF = FilaEncadeada()
        self.__contP = PilhaEncadeada()
        self.__contL = ListaEncadeada()
    
    #metodo de acesso
    @property
    def banco(self):
        return self.__banco
    
    #metodo de alteração
    @banco.setter
    def banco(self, novo_banco):
        self.__banco = novo_banco
    
    #metodos de adição de contas
    
    #lista
    def adicionar_conta_LIncio(self, ident, cpf, saldo):
        self.__contL.adicInic(ident, cpf, saldo)
    
    def adicionar_conta_LFim(self, ident, cpf, saldo):
        self.__contL.adicFim(ident, cpf, saldo)
    
    def adicionar_conta_LMeio(self, i, ident, cpf, saldo):
        self.__contL.adicMeio(i, ident, cpf, saldo)

    #Fila
    def adicionar_conta_F(self, ident, cpf, saldo):
        self.__contF.inserir(ident, cpf, saldo)
    
    #Pilha
    def adicionar_conta_P(self, ident, cpf, saldo):
        self.__contP.inserir(ident, cpf, saldo)

    #metodos de remoção

    def remover_conta_L(self, ident):
        self.__contL.remover(ident)
    
    def remover_conta_F(self):
        self.__contF.remover()
    
    def remover_conta_P(self):
        self.__contP.remover()
    
    #Interação com as contas listas
    def total_valor_contas(self):
        total = 0
        for i in range(self.__contL.tamanho ):
            cont = self.buscar_valor(i)
            total += cont.saldo
        return total

    def adicionar_valor_conta(self, id, valor):
        conta = self.buscar_conta(id)
        return conta.creditar(valor)
    
    def retirar_valor_conta(self, id, valor):
        conta = self.buscar_conta(id)
        return conta.debitar(valor)

    #metodo de busca
    def buscar_conta(self, ident):
        return self.__contL.buscar(ident)
    
    def buscar_valor(self, posicao):
        return self.__contL.__getitem__(posicao)

    #Metodos para ordenar a lista
    def ordena_contasCrescente(self):
        return self.__contL.ordenCresc()
    
    def ordena_contasDecrescente(self):
        return self.__contL.ordenDecres()

    #Impressão de contas
    def imprimir_contasL(self):
        self.__contL.imprimir()
    
    def imprimir_contaP(self):
        return self.__contP.imprimir()
    
    def imprimir_contaF(self):
        return self.__contF.imprimir()
    
    #metodos de acessar o tamanho
    def mostrar_tam_contasL(self):
        return self.__contL.tamanho

    def mostrar_tam_contasF(self):
        return self.__contF.tamanho()
        

    def mostrar_tam_contasP(self):
        return self.__contP.tamanho()
    
    #metodos de mostrar elementos
    def mostrar_elementP(self):
        return self.__contP.topo
    
    def mostrar_elementF(self):
        return self.__contF.inicio

    #Modificar Conta
    def modificarP(self, ident, cpf, saldo):
        return self.__contP.modificar(ident, cpf, saldo)
    
    def modificarF(self, ident, cpf, saldo):
        return self.__contF.modificar(ident, cpf, saldo)


    
    

   


        