from cavalo import Cavalo

#criando um novo cavalo
cavalo_arabe = Cavalo(
  'Savant', 170.0, 'Preto'
)
cavalo_arabe.imprimir()
print() #pulando a linha
cavalo_arabe.fugir()
cavalo_arabe.imprimir()


from leao import Leao

#criando um novo Leao

leao_africano = Leao(
  True,250.0, "Marrom"
)
print()
leao_africano.imprimir()
leao_africano.cacando()