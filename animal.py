class Animal:
  #construtor da classe pai
  def __init__(self, tamanho: float, cor: str):
    self._tamanho = tamanho #protected
    self._cor = cor #protected

  def comer(self):
    pass