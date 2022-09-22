# Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a
# temperatura em graus Celsius. C = 5 * ((F-32) / 9).


f = float(input("Informe a temperatura em °F: "))
c = 5 * ((f-32) / 9)
print(f"A temperatura {f:.0f}°F, corresponde a {c:.0f}°C")