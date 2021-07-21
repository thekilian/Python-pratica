'''
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

| Input Sample | Output Samples     |
| ------------ | ------------------ |
| 6 24         | Sao Multiplos      |
| ------------ | ------------------ |
| 6 25         | Nao sao Multiplos  |
'''

a, b = input().split()

a = int(a)
b = int(b)

if a % b == 0 or b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")