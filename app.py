import os

def start():
    #apresentar o ChatBot
    print('Olá, bem vindo ao Chat Bot do biga!')
    #Pedir o nome
    nome = input('Digite seu nome: ')
    #Pedir email
    email = input('Digite seu e-mail: ')
    while True:
        #Oferecer o menu de opções
        resposta = input(
            f'Selecione alguma opção:{os.linesep}[1] - Como foi desenvolvido esse Chat Bot? {os.linesep}[2] - Qual a finalidade deste bot?{os.linesep}[3] - Foi muito dificil desenvolver este bot? {os.linesep}[4] - Quem é o biga? ')
        #Processar Resposta
        processar_resposta(resposta, nome)


def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}Olá {nome}, este Chat Bot foi desenvolvido em python, em uma aula que eu fiz no youtube do Dev Aprender!{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}Opa {nome}! a maior finalidade deste bot é o aprendizado e o meu crescimento como desenvolvedor, já que estou habituado em trabalhar com Java, desenvovler em python é um novo desafio!{os.linesep}')
    elif  resposta == '3':
        print(f'{os.linesep}Então {nome}, eu já tenho como base a logica de programação, então não foi difícil para mim desenvolver esse Bot, mas se eu não tivesse essa base, iria ser muito mais difícil!{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}Fala {nome}!! O Biga é um desenvolvedor que ingressou na área de programação há um ano, atualmente ele trabalha com Java e está se arriscando a desenvolver em outras linguagens, muito focado em crescer na vida e se tornar um ótimo profissional...{os.linesep}')
    else:
        print('Digite apenas 1, 2, 3 ou 4.')



if __name__ == '__main__':
    start()

