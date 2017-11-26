values = input().split(" ")

a = int(values[0])
b = int(values[1])
c = int(values[2])

ab = (a + b + abs(a - b))/2
bc = (b + c + abs(b - c))/2
maior = (ab + bc + abs(ab - bc))/2

print("%1.0f eh o maior" %(maior))