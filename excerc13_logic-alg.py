#Calcular quanto tempo dura uma quantidade de alimento em kilos considerando 50g por dia 

#declaração de variáveis

quant_alim: float=0.0

#início

quant_alim = float(input("Insira a quantidade do alimento em quilos:"))

print ("Esse alimento durará por", ((quant_alim*100)/50) , "dias")

#Fim