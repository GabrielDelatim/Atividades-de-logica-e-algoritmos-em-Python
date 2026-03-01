#Calcular quantidade de litros gastos em uma viagem de automóvel que faz 12km/l

#Declaração de variáveis

Tempo_Percus: int=0
Veloc_Media: int=0

#Início

Tempo_Percus = int(input("Insira o tempo do percurso em horas:"))
Veloc_Media = int(input("Insira a velocidade média em Km's por hora:"))

print ("A quantidade de litros gastos nesse percurso é ", (Tempo_Percus*Veloc_Media)/12 )

#Fim