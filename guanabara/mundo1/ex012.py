# -*- coding: utf-8 -*-

#012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual o valor do produto? R$'))

desconto = preco - (preco * 95 / 100)
total = preco - desconto

print('O produto custa R${:.2f}. 5% de desconto é: R${:.2f}. O valor a pagar é R${:.2f}'.format(preco, desconto, total))