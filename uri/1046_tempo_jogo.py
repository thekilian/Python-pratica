'''
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

| Input Sample | Output Samples          |
| ------------ | ----------------------- |
| 16 2         | O JOGO DUROU 10 HORA(S) |
| ------------ | ----------------------- |
| 0 0          | O JOGO DUROU 24 HORA(S) |
| ------------ | ----------------------- |
| 2 16         | O JOGO DUROU 14 HORA(S) |
'''

hora = input().split()

inicio = int(hora[0])
fim = int(hora[1])

'''
result = fim - inicio

if result == 0:
    print("O JOGO DUROU 24 HORA(S)")

else:
    print("O JOGO DUROU {} HORA(S)".format(result))
'''

if inicio < fim:
    result = fim - inicio
else:
    result = (24 - inicio) + fim
    
print("O JOGO DUROU {} HORA(S)".format(result))