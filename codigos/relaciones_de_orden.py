from algebra_bool import *

def getDivisors(num):
    return [i for i in range(1, num+1) if num % i == 0]
    
def contenido(b, a):
    contained = True
    for i in b:
        contained &= i in a
    return contained

def maximos(b, a):
    maximos = []
    if contenido(b, a):
        for M in b:
            maximo = True
            for x in b:
                maximo &= M % x == 0
            if maximo:
                maximos.append(M)
    return maximos

def minimos(b, a):
    minimos = []
    if contenido(b, a):
        for m in b:
            minimo = True
            for x in b:
                minimo &= x % m == 0
            if minimo:
                minimos.append(m)
    return minimos

def cota_inferior(b, a):
    cota_inf = []
    if contenido(b, a):
        for c in a:
            cota = True
            for x in b:
                cota &= x % c == 0
            if cota:
                cota_inf.append(c)
    return cota_inf

def cota_superior(b, a):
    cota_sup = []
    if contenido(b, a):
        for c in a:
            cota = True
            for x in b:
                cota &= c % x == 0
            if cota:
                cota_sup.append(c)
    return cota_sup

def infimos(b, a):
    infimos = []
    if contenido(b, a):
        cota_inf = cota_inferior(b, a)
        for i in cota_inf:
            inf = True
            for c in cota_inf:
                inf &= i % c == 0
            if inf:
                infimos.append(i)
    return infimos

def supremos(b, a):
    supremos = []
    if contenido(b, a):
        cota_sup = cota_superior(b, a)
        for s in cota_sup:
            sup = True
            for c in cota_sup:
                sup &= c % s == 0
            if sup:
                supremos.append(s)
    return supremos

def minimal(b, a):
    minimal = []
    if contenido(b, a):
        for e in b:
            mini = True
            for x in b:
                mini &= (e % x != 0 or x == e)
            if mini:
                minimal.append(e)
    return minimal

def maximal(b, a):
    maximal = []
    if contenido(b, a):
        for e in b:
            maxi = True
            for x in b:
                maxi &= (x % e != 0 or x == e)
            if maxi:
                maximal.append(e)
    return maximal

'''
IMPORTANTE
Precondicion: se trata de una relacion de orden.
'''

# Ejemplo de uso

# Creo un conjunto de divisores
a = getDivisors(24)
# Declaro un subconjunto del conjunto de divisores
b = [2, 3, 6]

# Imprimo los detalles
print(f'a: {a}')
print(f'b: {b}')
print(f'max(b) = {maximos(b, a)}')
print(f'min(b) = {minimos(b, a)}')
print(f'c.inf(b) = {cota_inferior(b, a)}')
print(f'c.sup(b) = {cota_superior(b, a)}')
print(f'inf(b) = {infimos(b, a)}')
print(f'sup(b) = {supremos(b, a)}')
print(f'minimal(b) = {minimal(b, a)}')
print(f'maximal(b) = {maximal(b, a)}')