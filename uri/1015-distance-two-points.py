p1 = input().split(" ")
p2 = input().split(" ")

x1 = float(p1[0])
y1 = float(p1[1])
x2 = float(p2[0])
y2 = float(p2[1])

sub = ((x2 - x1)*(x2 - x1)) + ((y2 - y1)*(y2 - y1))
distance = sub ** (1/2)

print("%1.4f" %(distance))