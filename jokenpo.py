from random import randint
from time import sleep
import sys
# python -m jokenpo


def inicio():
    print('*-' * 30)
    print(f'{" JOGO DO JOKENPO ":=^60}')
    print('*-' * 30)


def print_jogadas(jogador, computador):
    possibilidades = ['Pedra', 'Papel', 'Tesoura']
    print(f'O jogador jogou {possibilidades[jogador]}')
    print(f'O computador jogou {possibilidades[computador]}')


def jo_ken_po():
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!\n')
    sleep(0.5)


def new_game():
    question = input('Deseja jogar novamente? "S" para SIM e "N" para NÃO:\n').upper()

    if question == "S":
        start()

    else:
        print('Encerrando programa, até mais')
        sys.exit()


def start():
    global count

    if count == 0:
        print('\nBem-vindo ao jogo do Jokenpo!')

    count += 1

    jogador = int(input('\nEscolha um:\n[0] Pedra\n[1] Papel\n[2] Tesoura\n\n '))
    jo_ken_po()

    print_jogadas(jogador, computador)

    if jogador == computador:
        print('Empatamos!')

    elif jogador == 0:
        if computador == 1:
            print('O computador venceu!')

        elif computador == 2:
            print('Você venceu!')

    elif jogador == 1:
        if computador == 0:
            print('Você venceu!')

        elif computador == 2:
            print('O computador venceu!')

    elif jogador == 2:
        if computador == 0:
            print('O computador venceu!')

        elif computador == 1:
            print('Você venceu!')

    new_game()


invalid_input = True

computador = randint(0, 2)
jogador = -1
count = 0

inicio()

while invalid_input:
    start()
