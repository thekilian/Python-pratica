# 014 - Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

c = float(input("Digite temperatura em Celsius: "))
f = c * 9 / 5 + 32
print("{}°C em Fahrenheit é: {}°F".format(c, f))