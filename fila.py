from conta import Conta

class FilaExceptionF(Exception):
  def __init__(self,mensagem):
    super().__init__(mensagem)
  


class FilaEncadeada:
  def __init__(self):
    self.__inicio = None
    self.__tamanho = 0

  @property
  def inicio(self):
      if self.vazia():
        return True

      return self.__inicio

  def vazia(self):
    if self.__inicio == None:
      raise FilaExceptionF('A fila está vazia')
  
  def tamanho(self):
    return self.__tamanho
  
  def inserir(self, ident, cpf, saldo):
      novo = Conta (ident,cpf, saldo)
  
      if self.__inicio == None:
        self.__inicio = novo
        

      else:
        aux = self.__inicio
        while aux.prox != None:
            aux = aux.prox

        aux.prox = novo
        


      self.__tamanho += 1 
  
  def remover(self):
      if self.vazia():
        return True

      self.__inicio = self.__inicio.prox
      self.__tamanho -= 1  
  
  def __str__(self):
    saida = 'Fila: ['
    p = self.__inicio

    while p != None:
      saida += f'{p}'
      p = p.prox

      if p != None:
        saida += ', '
    
    saida += ']'
    return saida

  def imprimir(self):
    print(self.__str__())

  def modificar(self, ident,cpf, saldo):
      if self.vazia():
        return True
      self.__inicio = Conta(ident,cpf, saldo)
      return True
  
  '''def modificar(self, ident,cpf, saldo):
      if self.vazia():
        return True
      p = self.__inicio.prox

      self.__inicio = Conta(ident,cpf, saldo)

      self.__inicio.prox = p
      return True'''

