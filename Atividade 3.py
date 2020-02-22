# Faça um Programa que peça dois números e imprima a soma.

# numero1 =float(input("Digite um número:\n"))
# numero2 = float(input("Digite outro número:\n"))
# print(f"A soma dos seus números foi:\n{numero1+numero2}")


print("Digite um número: ")
numero1 = float(input())

print("Digite outro número: ")
numero2 = float(input())

soma = numero1 + numero2
print("A soma dos seus números foi: ", soma)
print("A soma dos seus números foi: {} ".format(soma))
print(f"A soma dos seus números foi: {soma}")
