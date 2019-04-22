# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class triangle:
    pass

tr=triangle()
tr.xa=1
tr.ya=-1
tr.xb=3
tr.yb=2
tr.xc=1
tr.yc=-2

def s_triangle(xa,ya,xb,yb,xc,yc):
    s=1/2*((xa*(yb - yc) - xb*(ya - yc) + xc*(ya - yb)))
    return s

print('Площадь треугольника = ',s_triangle(tr.xa,tr.ya,tr.xb,tr.yb,tr.xc,tr.yc))

import math
def dlina(x1,y1,x2,y2):
    d=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return d

def perimetr():
    ab=dlina(tr.xa,tr.ya,tr.xb,tr.yb)
    bc=dlina(tr.xb,tr.yb,tr.xc,tr.yc)
    ca=dlina(tr.xc,tr.yc,tr.xa,tr.ya)
    p=ab+bc+ca
    return p
print('Периметр треугольника = ', perimetr())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class trap:
    pass

r_tr=trap()
r_tr.xa = -2
r_tr.ya = 2
r_tr.xb = 2
r_tr.yb = 2
r_tr.xc = 3
r_tr.yc = -1
r_tr.xd = -3
r_tr.yd = -1


def ravn_trap():
    if dlina(r_tr.xa,r_tr.ya,r_tr.xd,r_tr.yd) == dlina(r_tr.xb,r_tr.yb,r_tr.xc,r_tr.yc):
        print('Трапеция равнобочная ')

print(ravn_trap())

def dlina_storon():
    ad = dlina(r_tr.xa, r_tr.ya, r_tr.xd, r_tr.yd)
    ab = dlina(r_tr.xa, r_tr.ya, r_tr.xb, r_tr.yb)
    bc = dlina(r_tr.xb, r_tr.yb, r_tr.xc, r_tr.yc)
    cd = dlina(r_tr.xc, r_tr.yc, r_tr.xd, r_tr.yd)
    # print('ab = '{str(ab)}, 'bc = '{bc}, 'ad = ' {cd}, 'ad = ' {ad} )
    print('Длинa ab', ab)
    print('Длинa bc', bc)
    print('Длина ad', ad)
    print('Длина cd', cd)

print(dlina_storon())
