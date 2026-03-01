#raízes reais de uma equação do segundo grau
import math
#declaração de variáveis

a: float = 0.0
b: float = 0.0
c: float = 0.0
delta: float = 0.0
raiz1: float = 0.0
raiz2: float = 0.0

#início

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print ("A equação não possui raízes reais")

raiz1 = -(b) - (math.sqrt (delta)) / a*2
raiz2 = -(b) + (math.sqrt (delta)) / a*2

print ("As raizes da equação são" , raiz1 ,"e", raiz2 )


#Fim
