import random
import string
import os

def mostrar_letras_restantes(tentativas):
    alfabeto = string.ascii_lowercase
    return ''.join([char + ' ' for char in alfabeto if char not in tentativas])

def desenho(vidas):
    draw = ''
    for i in range(6):
        if i == 0:
            draw += '  _____  \n'
        elif i == 1:
            draw += '  |   |  \n'
        elif i == 2:
            if vidas == 6:
                draw += '  |      \n'
            else:
                draw += '  |   o  \n'
        elif i == 3:
            if vidas == 4:
                draw += r'  |   |   ' + '\n'
            elif vidas == 3:
                draw += r'  |   |\  ' + '\n'
            elif vidas <= 2:
                draw += r'  |  /|\  ' + '\n'
            else:
                draw += r'  |       ' + '\n'
        elif i == 4:
            if vidas == 1:
                draw += r'  |    \ ' + '\n'
            elif vidas == 0:
                draw += r'  |  / \ ' + '\n'
            else:
                draw += r'  |     ' + '\n'
        else:
            draw += '__|__     '
    return draw

def escpalavra():
    palavras = ["cavalo", 'pampa', 'aeronautica', 'comunista', "praia", 'marijuana', "computador", "montanha", "viagem", "sorriso", "felicidade", "amizade", "livro", "aventura", 'rajeh', 'macumba', 'windows', 'python', 'laranja', 'ornintorrinco', 'horas', 'sessenta', 'seissentos', 'palindromo', 'teste um arroba', 'socorram-me subi em um onibus em marrocos', 'funcional', 'macaco', 'gambiarra', 'homossexualidade', 'astronauta', 'feminista', 'monitor', 'obrigado por jogar!']
    return random.choice(palavras)

def print_letras(palavra, tent):
    pal = ''
    for char in palavra:
        if char in tent and char.isalpha():
            pal += char + ' '
        elif not char.isalpha():
            pal += char + ' '
        else:
            pal += '_ '
    return pal

print('jogo da forca :)')
vida = 6
palavra_secreta = escpalavra()
tentativas = []

while vida > 0:
    os.system('cls')
    print(desenho(vida))
    print(print_letras(palavra_secreta, tentativas))
    print(mostrar_letras_restantes(tentativas))
    tent = input('Digite uma letra: ')
    if tent in tentativas:
        print('Essa letra já foi escolhida uma vez')
    else:
        tentativas.append(tent)
    if tent not in palavra_secreta:
        vida -= 1

    if vida == 0:
        os.system('cls')
        print(desenho(vida))
        print('fim de jogo :(')

    if '_' not in print_letras(palavra_secreta, tentativas):
        print('Tu venceu :)')
        break
print('A palavra era "', palavra_secreta,'"')