""" Dois veículos (um carro e um caminhão) saem respectivamente de cidades
opostas pela mesma rodovia. O carro de Ribeirão Preto em direção a Franca,
a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a
Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem
na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?

IMPORTANTE:

a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.

b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para
passar em cada um deles e o carro possui tag de pedágio (Sem Parar)

c) Explique como chegou no resultado.

Obs.: Considerando movimento retilineo uniforme dos 2 veiculos!
"""

t = 0
vel_carro = 110
vel_caminhao = 80

#  Equacao horaria do carro saindo de Ribeirao Preto
funcao_horaria_carro = 0 + 110 * t

#  Equacao horaria do caminhao saindo de Franca
funcao_horaria_caminhao = 100 - 80 * t

#  Calculando a velocidade do caminhao com as paradas de pedagio
tempo_viagem_caminhao = 100/vel_caminhao
tempo_pedagio_caminhao = 10/60
vel_caminhao_com_pedagio = 100 / (tempo_viagem_caminhao + tempo_pedagio_caminhao)


#  Achando a distancia que os dois veiculos se cruzam
distancia = (vel_carro * 100)/(vel_carro + vel_caminhao_com_pedagio)

print(f"Os dois veiculos vao ser cruzar à {distancia:.2f} km de Ribeirao Preto,"
      f" portanto estarao igualmente proximos da cidade.")
