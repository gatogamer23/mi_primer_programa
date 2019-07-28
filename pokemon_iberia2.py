pokemon_combate = input('Contra que Pokémon quieres combatir (Bulbasur / Charmander / Squirtlle)')
vida_pikachu = 100
vida_enemigo = 0
dano_enemigo = 0
ataque_usado_2 = 'ninguno'


if pokemon_combate == 'Bulbasur':
    vida_enemigo = 100
    dano_enemigo = 20
    ataque_usado_2 == 'Placaje'
elif pokemon_combate == 'Charmander':
    vida_enemigo = 100
    dano_enemigo = 30
    ataque_usado_2 == 'Arañazo'
elif pokemon_combate == 'Squirtle':
    vida_enemigo = 100
    dano_enemigo = 20
    ataque_usado_2 == 'Aguita de chico gamer'


while vida_pikachu >= 0 and vida_enemigo >= 0:
    ataque_usado = input('Que ataque quieres usar(Bola Voltio / Chispazo')
    if ataque_usado == 'Chispazo':
        vida_enemigo - 12
    if ataque_usado == 'Bola Voltio':
        vida_enemigo - 20
