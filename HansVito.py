from sklearn import tree

mangga = 0
semangka = 1
matang = 0
mengkal = 1

tipe = [[15, 1],[20, 1],[30, 0],[50, 0]]
sc = [0, 0, 1, 1]
gerakan= tree.DecisionTreeClassifier()
gerakan= gerakan.fit(tipe, sc)

print('Klasifikasi kang buah pancoran')
a = input('Berapa kilogram berat buahnya? : ')
b = input('\nTingkat Kematangan buah nya \nMatang atau Mengkal : ')

jawab = int(a)
if b.lower() == 'matang':
    tk = 0
elif b.lower() == 'mengkal':
    tk = 1
else:
    print('Unknown')

c = gerakan.predict([[jawab, tk]])
if c == 0:
    d = 'mangga'
else:
    d = 'semangka'

print('Jadi di klasifikasinya ialah : {}'.format(d))