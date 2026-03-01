#Calcular angulo de triângulo recebendo dois dos ângulos

#declaração de variáveis

primeiro_angulo: int=0.0
segundo_angulo: int=0.0

#Início

primeiro_angulo = int(input("Insira o valor do primeiro ângulo:"))
segundo_angulo = int(input("Insira o valor do segundo ângulo:"))

print ("O valor do terceiro ângulo é ", (180 - (primeiro_angulo+segundo_angulo)))

#Fim