import pickle
p = open('banner.p','rb')
data = pickle.load(p)
print(data)
print('\n'.join([''.join([p[0] * p[1] for p in row]) for row in data]))