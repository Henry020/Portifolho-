import math

an = float(input('Qual o angulo que vocer quer?'))
seno = math.sin(math.radians(an))
co = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('o angulo de {} tem o seno de {:.2f}'.format(an, seno))
print('o angulo de {} tem o cosseno {:.2f}'.format(an, co))
print('o angulo de {} tem a tangente {:.2f}'.format(an, tan))