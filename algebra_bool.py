from tabulate import tabulate

def mcd(x, y):
    return x if y == 0 else mcd(y, x % y)

def mcm(x, y):
    return (x * y) // mcd(x, y)

class BooleanSet:

    def __init__(self):
        self.set = []

    def append(self, value):
        self.set.append(value)
    
    def isSubset(self, other):
        foo = True
        for i in self.set:
            foo &= i in other.set
        
        return len(self.set) <= len(other.set) and foo

    def __le__(self, other):
        foo = True
        for i in self.set:
            foo &= i in other.set
        
        return len(self.set) <= len(other.set) and foo

    def __lt__(self, other):
        foo = True
        for i in self.set:
            foo &= i in other.set
        
        return len(self.set) < len(other.set) and foo
    
    def __repr__(self):
        return f'{sorted(self.set)}'

class BooleanNumber:
    def __init__(self, number: int):
        self.number = number
    
    def __add__(self, other):
        return BooleanNumber(mcm(self.number, other.number))
    
    def __mul__(self, other):
        return BooleanNumber(mcd(self.number, other.number))

    def __div__(self, other):
        return BooleanNumber(self.number / other.number)
    
    def __truediv__(self, other):
        return BooleanNumber(self.number // other.number)
    
    def __lt__(self, other):
        return self.number < other.number
    
    def __le__(self, other):
        return self.number <= other.number
    
    def __repr__(self):
        return f'{self.number}'
    
    def __eq__(self, other):
        return self.number == other.number

    def __mod__(self, other):
        return self.number % other.number

def drawTable(booleanSet, operation: str) -> None:
    '''
    Dibuja una tabla ordenada de un conjunto de numeros y las operaciones entre ellos
    Pre: se creo un conjunto de numeros booleanos.
    Pos: se dibuja una tabla con la operacion obtenida (+, *) de ese conjunto.
    '''
    firstRow = [operation] + sorted(booleanSet.set)
    table = [firstRow]
    for i in booleanSet.set:
        row = []
        row.append(i)
        for j in booleanSet.set:
            if operation == '+':
                row.append(i + j)
            elif operation == '*':
                row.append(i * j)
        table.append(row)
    print(tabulate(table, tablefmt='fancy_grid', stralign='center'))


def booleanDivisorsSet(num: int):
    '''
    Obtiene un conjunto de divisores de cierto numero
    Pre: -
    Post: conjunto de divisores de un numero "x".
    '''
    divSet = BooleanSet()
    for i in range(1, num+1):
        if num % i == 0:
            divSet.append(BooleanNumber(i))

    return divSet

def getBooleanSet(booleanSet):
    '''
    Devuelve un conjunto, de otro conjunto, dada una condicion especifica
    Pre: se creo un conjunto de numeros booleanos (ej: de divisores)
    Post: se devuelve un conjunto de numeros que cumplen con una condicion dada.
    '''
    a = BooleanSet()
    for x in booleanSet.set:
        '''
        CONDICION A MODIFICAR SEGUN ENUNCIADO
        '''
        if ((BooleanNumber(14) * x) + BooleanNumber(1)) < (BooleanNumber(35) * x):
            a.append(x)

    return a


# Ejemplo de uso
def main():
    # Obtiene los divisores de 70
    booleanSet = booleanDivisorsSet(70)
    # 
    a = getBooleanSet(booleanSet)
    print(f'D = {booleanSet}')
    print(f'A = {a}')
    print(f'{"A es una subalgebra de D" if a.isSubset(booleanSet) else "A no es una subalgebra de D"}')
    '''
    # DESCOMENTAR SOLO SI SE QUIERE VER LA TABLA
    drawTable(booleanSet, '+')
    drawTable(booleanSet, '*')
    '''

if __name__ == "__main__":
    main()