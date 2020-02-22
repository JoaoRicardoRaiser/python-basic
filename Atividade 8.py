# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor_por_hora = float(input("Digite o seu salário por hora\n"))
horas_trabalhadas_no_mes = float(input("Digite o número de horas trabalhadas no mês:\n"))
salario = valor_por_hora * horas_trabalhadas_no_mes
print(f"O seu salário mensal é: {salario}")
