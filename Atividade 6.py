# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio = float(input("Digite o raio do círculo:\n"))
pi = 3.1415
area = (raio * raio) * pi
resultado = round(area, 2)
print(f"O valor do raio do círculo é: {resultado}")
