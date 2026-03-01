#conversão de celsius para fahrenheit 

#declação de variáveis

celsius: float = 0.0
fahrenheit: float = 0.0

#início

celsius: float = float(input("Digite a temperatura em Celsius: "))
fahrenheit: float = ((celsius * 9) + 160) / 5
print("A temperatura em Fahrenheit é: ", fahrenheit)

#Fim