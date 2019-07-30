frase = input('Escribe aquí tu frase:')

vocales = {'a','e','i','o','u'}
n_vocales = 0
n_consonantes = 0

for letra in frase:
    for letra in vocales:
        n_vocales += 1
    else:
        n_consonantes += 1


print('Hay {} vocales y {} consononantes'.format(n_vocales, n_consonantes))
