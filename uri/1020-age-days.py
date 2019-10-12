'''
year = 365 days
month = 30 days
'''

days = int(input())

a = days // 365
m = (days - (a * 365)) // 30
d = days - (a * 365) - (m * 30)

print(f"{a} ano(s)\n{m} mes(es)\n{d} dia(s)")

#print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(a, m, d))