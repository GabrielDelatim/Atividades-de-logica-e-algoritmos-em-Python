#Calcular salário

#Declaração de variáveis

horas_trabalhadas: int=0
dependentes: int=0
valor_hora: float=0.0
percent_descont: float=0.0

#Início

horas_trabalhadas = int(input("Insira a quantidade de horas trabalhadas:"))
valor_hora = float(input("Insira o valor da hora de trabalho:"))
percent_descont= float(input("Insira o percentual de desconto:"))
dependentes = int(input("Insira a quantidade de dependentes:"))

print ("\n Salário Bruto:", horas_trabalhadas*valor_hora,
       "\n Salário Líquido:", (horas_trabalhadas*valor_hora-(horas_trabalhadas*valor_hora)*(percent_descont/100)),
      "\n Salário Líquido mais acrescimo por dependendente:", ((horas_trabalhadas*valor_hora-(horas_trabalhadas*valor_hora)*(percent_descont/100))+ (dependentes*100)), "\n" )


#Fim
