n = int(input())

h = n / 3600

m = ((h * 3600) - h) / 60

s = (h * 3600) - (m * 60)

print("{:2.0f}:{:2.0f}:{:2.0f}".format(h, m, s))
