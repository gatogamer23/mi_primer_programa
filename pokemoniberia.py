pokemon_combate = input('Contra que Pokémon quieres combatir (Bulbasur / Charmander / Squirtle)')
vida_pikachu = 100
vida_enemigo = 0
dano_enemigo = 0
ataque_usado_2 = 'ha tenido un fallo en la seleccion del ataque'


if pokemon_combate == 'Bulbasur':
    vida_enemigo = 100
    dano_enemigo = 20
    ataque_usado_2 = 'Placaje'
elif pokemon_combate == 'Charmander':
    vida_enemigo = 100
    dano_enemigo = 30
    ataque_usado_2 = 'Arañazo'
elif pokemon_combate == 'Squirtle':
    vida_enemigo = 100
    dano_enemigo = 20
    ataque_usado_2 = 'Aguita de chico gamer'


while vida_pikachu >= 0 and vida_enemigo >= 0:
    ataque_usado = input('Que ataque quieres usar(Bola Voltio / Chispazo')
    if ataque_usado == 'Chispazo':
        vida_enemigo -= 12
    elif ataque_usado == 'Bola Voltio':
        vida_enemigo -= 20
    elif ataque_usado == 'Attack Z':
        vida_enemigo -= 360000

    print('Has usado {} contra {} y tiene {} de vida!'.format(ataque_usado, pokemon_combate, vida_enemigo))

    if pokemon_combate == 'Squirtle':
        vida_pikachu -= dano_enemigo
    elif pokemon_combate == 'Charmander':
        vida_pikachu -= dano_enemigo
    elif pokemon_combate == 'Bulbasur':
        vida_pikachu -= dano_enemigo



    print('{} ha usado {} y tienes ahora {} de vida'.format(pokemon_combate, ataque_usado_2, vida_pikachu))
if vida_enemigo<=0:
    print('Has Ganado!')
elif vida_pikachu<=0:
    print('Has Pardido :c')




