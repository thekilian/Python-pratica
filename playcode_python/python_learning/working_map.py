# working with map()

list_ = ['1', '2', '3']
[float(i) for i in list_]

list(map(float,list_))

def pow(a):
    return int(a)**2

list(map(pow,list_))