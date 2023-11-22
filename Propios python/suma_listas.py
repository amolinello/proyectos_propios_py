# Suma de dos listas del mismo tamaño y entrega promedio
from itertools import zip_longest

def suma_lista_igual(list_a, list_b):
    resultado = [a+b for a,b in zip(list_a, list_b)]
    return resultado

def suma_lista_dif(list_a, list_b):
    resultado = [a+b for a,b in zip_longest(list_a, list_b, fillvalue=0) ]
    return resultado

if __name__ == '__main__':
    lista_a = [1, 2, 3, 4]
    lista_b = [5, 6, 7, 8]
    print(f'Resultado suma de dos listas del mismo tamaño: {suma_lista_igual(lista_a, lista_b)}')

    lista_c = [1, 2, 3, 4, 3, 4]
    print(f'Resultado suma de dos listas de distinto tamaño 1: {suma_lista_dif(lista_c, lista_b)}')

    lista_d = [1]
    print(f'Resultado suma de dos listas de distinto tamaño 2: {suma_lista_dif(lista_d, lista_b)}')