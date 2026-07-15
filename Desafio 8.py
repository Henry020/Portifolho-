medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
hm = medida / 10
dh = medida / 10
km = medida / 1000
print('A medida {}m equivale a {}cm\n {}mm\n {}dm\n {}hm\n {}dh \n {}km'.format(medida, cm, mm, dm, dm, hm, dh, km))
