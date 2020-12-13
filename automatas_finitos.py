def acepta(transiciones: dict, estado_inicial: int, conjunto_aceptacion: list, q: str):
    estado = estado_inicial
    for c in q:
        estado = transiciones[estado][c]
    return estado in conjunto_aceptacion

alfabeto = ['a', 'b']

automata_finito = {
    0: {alfabeto[0]: 1, alfabeto[1]: 0},
    1: {alfabeto[0]: 2, alfabeto[1]: 2},
    2: {alfabeto[0]: 3, alfabeto[1]: 0},
    3: {alfabeto[0]: 3, alfabeto[1]: 3}
}

estado_inicial = 0
conjunto_de_aceptacion = [3]

print(acepta(automata_finito, estado_inicial, conjunto_de_aceptacion, f'babaaaaaaaaaaaa'))