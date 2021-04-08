from conta import Conta

class ListaExceptionL(Exception): 
    def __init__(self, mensagem): 
        super().__init__(mensagem)


class ListaEncadeada:
    def __init__(self):
        self.__inicio = None
        self.__tamanho = 0

    @property
    def inicio(self):
        return self.__inicio

    @property
    def tamanho(self):
        return self.__tamanho

    # Para verificar se a "Lista" esta vazia.
    def __vazia(self):
        if self.__inicio == None:
            raise ListaExceptionL('A lista está vazia.')

    # Adiciona novo "objeto" no inicio da "Lista".
    def adicInic(self, ident, cpf, saldo): 

        no = Conta(ident, cpf, saldo)
        if self.__inicio == None:
            no.prox = self.inicio
            self.__inicio = no
            self.__tamanho += 1

        else:
            print('Lista já tem o primeiro objeto')
    
    # Adiciona novo "objeto" no final da "Lista".
    def adicFim(self, ident, cpf, saldo): 
        
        if self.__vazia():
            return True
        
        p = self.inicio
        while p.prox != None:
            p = p.prox
        no = Conta(ident, cpf, saldo)
        p.prox = no
        self.__tamanho += 1

    # Adiciona novo "objeto" em qualquer posicao da "Lista".
    def adicMeio(self, indice, ident, cpf, saldo):

        if self.__vazia(): 
            return True
        
        no =  Conta(ident, cpf, saldo)
        q = 0
        p = self.__inicio
        cont = 1
        
        while cont < indice and p != None:
            q = p
            p = p.prox
            cont += 1
        if indice == 0 or p.prox == None:
            raise ValueError('Posição indicada não é permitida.')
        no.prox = p.prox
        p.prox = no
        p = q
        self.__tamanho += 1

    def buscar(self, idconta):
        if self.__vazia(): 
            return True
        
        p = self.__inicio
        while p != None:
            
            if p.identificador == idconta:
                return p
            p = p.prox
            print('*'*45) 
        raise ValueError(f'{idconta} não está na Lista.')           
            
    # Para remover um "objeto" da "Lista".
    def remover(self, id):

        if self.__vazia(): 
            return True

        elif self.__inicio.identificador == id:
            self.__inicio = self.__inicio.prox
            self.__tamanho -= 1
            print(f'Remoção realizada com sucesso.')

        else:
            q = self.__inicio
            p = self.__inicio.prox
            while p != None:
                if p.identificador == id:
                    q.prox = p.prox
                    p.prox = None
                q = p
                p = p.prox
            self.__tamanho -= 1
            print(f'Remoção realizada com sucesso. no main2')


    def ordenCresc(self):
        if self.__vazia():
            return True

        if self.__tamanho > 1:            
            for i in range(self.__tamanho -1):
                    q = self.__inicio
                    p = q.prox
                    aux = None
                    while p != None:
                        if q.identificador > p.identificador:
                            if aux == None:
                                aux = q.prox
                                p = p.prox
                                aux.prox = q
                                q.prox = p
                                self.__inicio = aux
                            else:   
                                aux2 = p
                                p = p.prox
                                aux.prox = q.prox
                                aux = aux2
                                aux2.prox = q
                                q.prox = p
                        else:           
                            aux = q
                            q = p
                            p = p.prox
                    i += 1             
        else:
            raise ValueError ('O tamanho da lista é insuficiênte')        
           
    # Para ordenar a "Lista" em ordem "Decrescente".
    def ordenDecres(self):
        if self.__vazia():
            return True

        if self.__tamanho > 1:            
            for i in range(self.__tamanho -1):
                    q = self.__inicio
                    p = q.prox
                    aux = None
                    while p != None:
                        if q.identificador < p.identificador:
                            if aux == None:
                                aux = q.prox
                                p = p.prox
                                aux.prox = q
                                q.prox = p
                                self.__inicio = aux
                            else:   
                                aux2 = p
                                p = p.prox
                                aux.prox = q.prox
                                aux = aux2
                                aux2.prox = q
                                q.prox = p
                        else:           
                            aux = q
                            q = p
                            p = p.prox
                    i += 1             
        else:
            raise ValueError ('O tamanho da lista é insuficiênte')
            
    # Retorna o tamanho da lista com a função "len()", de igual modo se chamar ".tamanho".
    def __len__(self): 
        return self.__tamanho

    # Mostra um "objeto" de uma determinada posição.
    def __getitem__(self, indice): 
        p = self.__inicio
       
        for indice in range(indice):
            if p != None:
                p = p.prox
            else:
                raise IndexError('Incide indicado fora do range.')
        
        if p != None:
            return p
        
        raise IndexError('Incide indicado fora do range.')

    # Para modificar um "elemnto" na lista.
    def __setitem__(self, indice, dado):
        p = self.__inicio
       
        for indice in range(indice):
            if p != None:
                p = p.prox
            else:
                raise IndexError('Incide indicado fora do range.')

        if p != None:
            p.dado = dado
        else:
            raise IndexError('Incide indicado fora do range.')

    def __str__(self):
        saida = ''
        p = self.__inicio
        while p != None:
            saida = saida + '\n =>'+ str(p) 
            p = p.prox
        return saida
    
    def imprimir(self):
        print(self.__str__())




