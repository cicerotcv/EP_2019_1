# -*- coding: utf-8 -*-
# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Cicero Tiago Carneiro Valentim, cicerotcv@al.insper.edu.br
# - aluno B: Luiz Felipe Lazzaron, luizfl@al.insper.edu.br

#Função Cenários
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "setimo andar": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca",
                "guarda": "Seu Brian"
            }
        },
        "setimo andar": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual
# Função personagens
def carregar_personagens():
    personagens = {"guarda":{
                    "conversa":"Brian, o guarda parceiro",
                    "descricao":"Hey aluno, tudo bem? O que você quer?",
                    "opcoes": {
                        "lutar",
                        "conversar",
                        
    }}}
    return personagens

#Função Principal
def main():
    # Introdução
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    
    name = input("Olá, visitante! Qual seu nome? \n>>>>> ")
    print("Olá, {0}! Espero que faça um bom jogo!\n{1}\n".format(name,(35+len(name))*'-'))

    cenarios, nome_cenario_atual = carregar_cenarios()
    personagens = carregar_personagens()
    game_over = False

    while not game_over:
        #Loading Inicial
        cenario_atual = cenarios[nome_cenario_atual]
        titulo = cenario_atual["titulo"]
        descricao = cenario_atual["descricao"]
        
        print(titulo,'\n{0}\n\n{1}\n'.format("-"*len(titulo),descricao))

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            print('O que você vai fazer?')
            print()
            for opcao in opcoes:
                print('{0}:{1}'.format(opcao,opcoes[opcao]))
            escolha = input()
            if escolha in opcoes:
                nome_cenario_atual = escolha
            elif escolha == 'monstro':
                print(nome_inimigo_atual)
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()