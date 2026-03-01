#Calcular idade atual e em 17 anos

#declaração de variáveis

ano_atual: int=0
ano_nascim: int=0

#Início

ano_atual= int(input("Insira o ano atual:"))
ano_nascim = int(input("Insira o ano que nasceu:"))

print ("Você tem ", (ano_atual-ano_nascim), "anos," , "e em 17 anos terá" ,((ano_atual-ano_nascim) +17), "anos."  )

#Fim