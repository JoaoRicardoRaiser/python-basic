#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
graus_farenheint=int(input("Digite a temperatura em graus Farenheit:\n"))
graus_celsius= (5 * (graus_farenheint -32) / 9)
resultado =round(graus_celsius,1)
print(f"A temperatura em graus Celsius será de: {resultado}°")