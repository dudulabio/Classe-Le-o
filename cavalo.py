from animal import Animal

class Cavalo(Animal):
  #construtor da classe filha
  def __init__(self, raca: str, tamanho: float, cor: str):
    '''
    (13) chama-se primeiro o construtor da classe pai
    pois existe herança.
    (13) o método super() é usado para chamar o 
    (13) construtor da classe pai
    tamanho e cor são da classe pai
    '''   
    super().__init__(tamanho, cor)
    self.__raca = raca #priv
    self.__fugindo = False #priv
    self.__comendo = False #priv
    self.__descansando = False #priv
    self.__passeando = False #priv

  def imprimir(self):
    print(f'Raça: {self.__raca}')
    print(f'Tamanho: {self._tamanho}')
    print(f'Cor: {self._cor}')
    print(f'Fugindo: {self.__fugindo}')
    print(f'Comendo: {self.__comendo}')
    print(f'Descansando: {self.__descansando}')
    print(f'Passeando: {self.__passeando}')

  def comer(self):
    self.__comendo = True
    self.__fugindo = False

  def fugir(self):
    self.__fugindo = True
    self.__comendo = False
    self.__descansando = False
    self.__passeando = False