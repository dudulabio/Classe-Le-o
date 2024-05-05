from animal import Animal

class Leao(Animal):
        # Construtor da classe filha
    def __init__(self, juba, tamanho: float, cor: str):
       super().__init__(tamanho, cor)
       self.__juba = juba
       self.__cacando = False
       self.__comendo = False
       self.__descansando = False
       self.__passeando = False

    def juba_condition(self):
        return self.__juba

    def imprimir(self):
         print(f'Juba: {self.__juba}')
         print(f'Tamanho: {self._tamanho}')
         print(f'Cor: {self._cor}')
         print(f'Caçando: {self.__cacando}')
         print(f'Comendo: {self.__comendo}')
         print(f'Descansando: {self.__descansando}')
         print(f'Passeando: {self.__passeando}')

    def comer(self):
       self.__comendo = True
       self.__cacando = False

    def cacando(self):
       self.__cacando = True
       self.__comendo = False
       self.__descansando = False
       self.__passeando = False
