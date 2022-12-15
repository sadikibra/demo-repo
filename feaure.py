listaSalas = [1,2,3,4,5]
lotacao = int(input("introduza o numero da sala a qual deseja ver a lotação"))
listaLotacao = [120,320,170,300,436]
if lotacao < 1 or lotacao > 5:
    print("Introduza de 1 a 5 o numero da sala.")
else:
    print("A sala numero", lotacao,"tem este número de lugares disponiveis",listaLotacao[lotacao-1])
