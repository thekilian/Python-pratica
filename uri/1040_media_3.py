'''
Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.

**Input**
A entrada contém quatro números de ponto flutuante correspendentes as notas dos alunos.

**Output**
Todas as respostas devem ser apresentadas com uma casa decimal. As mensagens devem ser impressas conforme a descrição do problema. Não esqueça de imprimir o enter após o final de cada linha, caso contrário obterá "Presentation Error".

| Input Sample    | Output Samples           |
| --------------- | ------------------------ |
| 2.0 4.0 7.5 8.0 | Media: 5.4               |
| 6.4             | Aluno em exame.          |
|                 | Nota do exame: 6.4       |
|                 | Aluno aprovado.          |
|                 | Media final: 5.9         |

| 2.0 6.5 4.0 9.0 | Media: 4.8               |
|                 | Aluno reprovado.         |

| 9.0 4.0 8.5 9.0 | Media: 7.3               |
|                 | Aluno aprovado.          |
'''

'''
# Fórmula Média Ponderada

Mp = [(N1 x P1) + (N2 x P2) + (N3 x P3) + ... (Nx x Px)] ÷ (P1 + P2 + P3 + ... Px)
Sendo que:

- Mp é a média ponderada (o resultado que você quer descobrir)
- N é cada valor do conjunto
- P é o peso correspondente de cada valor do conjunto.
'''

notas = input().split()

n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])

#outra forma de pegar os dados do input:
#n1, n2, n3, n4 = notas

p1 = 2
p2 = 3
p3 = 4
p4 = 1

media = ((n1 * p1) + (n2 * p2) + (n3 * p3) + (n4 * p4)) / (p1 + p2 + p3 + p4)
print("Media: {:.1f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif media >= 5.0 and media <= 6.9:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: {:.1f}".format(exame))
    new_media = (exame + media) / 2
    if new_media >= 5.0:
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(new_media))
    elif new_media <= 4.9:
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(new_media))