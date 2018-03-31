# 015 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.

dias = int(input("Quantos dias alugado? "))
km = float(input("Quantos quilômetros rodados? "))
diaria = dias * 60
trajeto = km * 0.15

total = diaria + trajeto

print("O total a pagar pelo carro é: R${:.2f}".format(total))