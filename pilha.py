from conta import Conta

class PilhaExceptionP(Exception):
  def __init__(self,mensagem):
    super().__init__(mensagem)
  

class PilhaEncadeada:
  def __init__(self):
    self.__topo = None
    self.__tamanho = 0

  @property
  def topo(self):
      if self.vazia():
        return True
      return self.__topo

  def vazia(self):
    if self.__topo == None:
      raise PilhaExceptionP('A pilha está vazia')
  
  def tamanho(self):
    return self.__tamanho
  
  def inserir(self, ident, cpf, saldo):
    novo = Conta(ident, cpf, saldo)
    novo.prox = self.__topo
    self.__topo = novo

    self.__tamanho += 1  

  def remover(self):
      if self.vazia():
        return True

      self.__topo = self.__topo.prox
      self.__tamanho -= 1  
  
  def __str__(self):
    saida = 'Pilha: ['
    p = self.__topo

    while p != None:
      saida += f'{p}'
      p = p.prox

      if p != None:
        saida += ', '
    
    saida += ']'
    return saida

  def imprimir(self):
    print(self.__str__())

  def modificar(self, ident, cpf, saldo):
      if self.vazia():
        return True
      self.__topo = Conta(ident, cpf, saldo)
      return True
  
  '''def modificar(self, ident, cpf, saldo):
      if self.vazia():
        return True
      p = self.__topo.prox
      self.__topo = Conta(ident, cpf, saldo)
      self.__topo.prox = p
      return True'''
    
