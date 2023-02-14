from random import choice
from time import sleep

escolhas = ['Pedra', 'Papel', 'Tesoura']

jogada_pc = choice(escolhas)

while True:
    jogada_player = str(input('Pedra / Papel / Tesoura: ')).capitalize()
    if jogada_player == jogada_pc:
        sleep(0.5)
        print(f'Você escolheu {jogada_player} e o pc {jogada_pc}.')
        print('Empate!')
        jogada_pc = choice(escolhas)
    elif (jogada_player == 'Pedra' and jogada_pc == 'Tesoura') or (jogada_player == 'Papel' and jogada_pc == 'Pedra')\
            or (jogada_player == 'Tesoura' and jogada_pc == 'Papel'):
        sleep(0.5)
        print(f'Você escolheu {jogada_player} e o pc {jogada_pc}.')
        print('Você ganhou!')
        break
    elif (jogada_player == 'Pedra' and jogada_pc == 'Papel') or (jogada_player == 'Papel' and jogada_pc == 'Tesoura')\
            or (jogada_player == 'Tesoura' and jogada_pc == 'Pedra'):
        sleep(0.5)
        print(f'Você escolheu {jogada_player} e o pc {jogada_pc}.')
        print('Você perdeu!')
        break
