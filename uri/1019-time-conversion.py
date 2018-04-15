n = int(input())

h = n / 3600
print(h)
m = (h - (h * 3600)) / 60
print(m)
s = n - (h * 3600) - (m * 60)
print(s)

# print("{}:{}:{}".format(h, m, s))
# print("%1.0f:%1.0f:%1.0f" %(h, m, s))

'''
| 556 | 0:9:16 |
'''
