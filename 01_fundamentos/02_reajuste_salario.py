# Reajuste de salário
salario = float(input("Informe o seu salário atual: "))
percentual = float(input("Digite o percentual de aumento: "))

valor_do_aumento = (salario * percentual / 100)
novo_salario = salario + valor_do_aumento

print(f"O aumento será de: R${valor_do_aumento:.2f}")
print(f"O seu novo salário será: R${novo_salario:.2f}")
