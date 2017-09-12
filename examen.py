# coding=utf-8

def analisis_lista(lista, k):
    menores = [x for x in lista if x < k]
    mayores = [x for x in lista if x > k]
    iguales = [x for x in lista if x == k]
    multiplos = [x for x in lista if x % k == 0]
    return [[menores, mayores, iguales], multiplos]
