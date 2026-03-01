#Troca de valores

#Declaração de variáveis

x: int=0
y: int=0

#início

x = int(input("Declare o valor X:"))
y =  int(input("Declare o valor Y:"))

x,y = y,x 

print ("O valor X é:", x )
print ("O valor Y é:", y ) 

#Fim