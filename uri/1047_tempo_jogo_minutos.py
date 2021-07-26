'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo. Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

| Input Sample | Output Samples                        |
| ------------ | ------------------------------------- |
| 7 8 9 10     | O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)  |
| ------------ | ------------------------------------- |
| 7 7 7 7      | O JOGO DUROU 24 HORA(S) E 0 MINUTO(S) | 
| ------------ | ------------------------------------- |
| 7 10 8 9     | O JOGO DUROU 0 HORA(S) E 59 MINUTO(S) |
'''

hora = input().split()

hora_inicio = int(hora[0])
minuto_inicio = int(hora[1])
hora_fim = int(hora[2])
minuto_fim = int(hora[3])

if hora_inicio < hora_fim:
    result_hora = hora_fim - hora_inicio
else:
    result_hora = (24 - hora_inicio) + hora_fim

if minuto_inicio < minuto_fim:
    result_minuto = minuto_fim - minuto_inicio
else:
    result_minuto = (60 - minuto_inicio) + minuto_fim
    
print("O JOGO DUROU {} HORA(S) E {} MINUTOS(S)".format(result_hora, result_minuto))