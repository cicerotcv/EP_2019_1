# -*- coding: utf-8 -*-
#FUNÇÃO COMBATE
def carregar_combate():
    monstro =  nome_cenario_atual['monstros']
    print(monstro['descricao'])   
    print(monstro['dificuldade'])  
    print(monstro['status'])  
    print(monstro['opcoes'])
    escolha = input()
    if escolha == 'atacar':
        if monstro['status']["força"] > forca:
            vida = vida - (monstro['status']["força"] - forca)
        else:
            print("você derrotou {0}!".format(monstro))
    if escolha == "fugir":
        if monstro['status']["força"] > forca:
            vida = vida - (monstro['status']["força"] - forca)
        else:
            print("você derrotou {0}!".format(monstro))
    return resultado