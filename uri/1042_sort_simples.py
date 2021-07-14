'''
| Input Sample | Output Samples |
| ------------ | -------------- |
| 7 21 -14     | -14            |
|              | 7              |
|              | 21             |
|              |                |
|              | 7              |
|              | 21             |
|              | -14            |
| ------------ | -------------- |
| -14 21 7     | -14            |
|              | 7              |
|              | 21             |
|              |                |
|              | -14            |
|              | 21             |
|              | 7              |
'''

valores = input().split( )

n1 = int(valores[0])
n2 = int(valores[1])
n3 = int(valores[2])

result = n1, n2, n3
ordem = sorted(result)

print("{}\n{}\n{}".format(ordem[0], ordem[1], ordem[2]))
print()
print("{}\n{}\n{}".format(n1, n2, n3))