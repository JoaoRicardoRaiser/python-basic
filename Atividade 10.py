#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
graus_celsius=float(input("Digite a temperatura em graus Celsius:\n"))
graus_farenheint= (graus_celsius * 9/5) + 32
resultado= round(graus_farenheint,1)
print(f"O valor em graus Farenheint é:{resultado}°")

