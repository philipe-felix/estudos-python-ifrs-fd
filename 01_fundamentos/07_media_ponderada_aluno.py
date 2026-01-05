# Média ponderada

nota_1 = float(input("Digite a sua primeira prova: "))
peso_prova1 = float(input("Digite o peso da primeira prova: "))
nota_2 = float(input("Digite a sua segunda prova: "))
peso_prova2 = float(input("Digite o peso da segunda prova: "))
nota_3 = float(input("Digite a sua terceira prova: "))
peso_prova3 = float(input("Digite o peso da terceira prova: "))

soma_notas_pesos = (nota_1 * peso_prova1) + (nota_2 * peso_prova2) + (nota_3 * peso_prova3)

soma_pesos = peso_prova1 + peso_prova2 + peso_prova3

media_final = soma_notas_pesos / soma_pesos

print(f"{media_final:.2f}")