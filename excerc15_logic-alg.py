#Calculo da hipotenusa de um triângulo retângulo

import math

#declaração de variáveis

primeiro_cateto: int = 0
segundo_cateto: int = 0

#Início

primeiro_cateto = int(input("Insira o valor do primeiro cateto:"))
segundo_cateto = int(input("Insira o valor do segundo cateto:"))

print ("O valor da hipotenusa é ", math.sqrt((primeiro_cateto**2)+(segundo_cateto**2)))

#Fim

