# -*- coding: utf-8 -*-
# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Cicero Tiago Carneiro Valentim, cicerotcv@al.insper.edu.br
# - aluno B: Luiz Felipe Lazzaron, luizfl@al.insper.edu.br

"""
Em nosso código, temos várias funções de jogo:
    - Função exploração ==> função em que o personagem caminha sobre os cenário
        ==> carregar_cenarios()
    - Função combate ==> função em que o personagem luta com monstros
        ==> carregar_combate():
    - Função investigação ==> função em que o personagem investiga o ambiente,
        achando itens ==> carregar_investigação()
    - Função inventário ==> função em que o personagem procura em sua mochila
        itens que ele foi conseguindo por meio da investigação
        ==> carregar_inventario()
"""

#Parâmetros do Jogador
forca = 1000
agilidade = 1000
vida = 1000

#FUNÇÃO EXPLORAÇÃO
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a entrada da biblioteca",
                "conversar":"interagir com as pessoas do cenario",
                "investigar":"Procurar itens no cenario"
            }
        },
        "andar professor": {
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
            "titulo": "Entrada da Biblioteca",
            "descricao": "Bem-vindo a biblioteca. Aqui, existem muitas coisas para procurar, e algumas pessoas para conversar.",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "salas individuais": "Procurar colegas para ajudar na EP",
                "pesquisar no acervo": "Procurar livros que possam ajudar na EP",
                "investigar": "Procurar itens no cenario"
            }
        },
        "salas individuais": {
            "titulo":"Silêncio, por favor",
            "descricao":"Voce precisa encontrar amigos que te ajudem a resolver a EP"
                        "Tome cuidado para não entrar em uma sala que está ocupada por um veterano",
            "opcoes": {
                "biblioteca":"Voltar para a entrada da biblioteca",
                "sala 01":"Entrar na sala 01",
                "sala 02":"Entrar na sala 02",
                "investigar": "Procurar itens no cenario"        
            }
        },
        "sala 01": {
            "titulo":"Sala de estudos 1",
            "descricao":"Essa sala esta vazia.",
            "opcoes": {
                "salas individuais":"voltar para o corredor das salas individuais",
                "investigar":"Procurar itens no cenario"
            }
        },
        "sala 02": {
            "titulo":"Sala de estudos 2",
            "descricao":"Essa sala esta cheia de veteranos enfurecidos por conta reprovacao!",
            "opcoes": {
                "salas individuais":"voltar para o corredor das salas individuais",
                "conversar":"interagir com as pessoas do cenario",
                "investigar":"Procurar itens no cenario"}
            "monstros": {"monstro1": {
                            "descricao": "descrição do monstro 1 aqui",
                            "dificuldade": 1,
                            "status":{"vida":100, "agilidade":100,"força":100},
                            "opcoes":{
                                    "atacar":"você irá atacar o monstro",
                                    "fugir": "você irá empurrar o monstro e correr para o cenário anterior"}}
                    }
        
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


    
def monstros():
    monstros = {
    "monstro1": {
        "descricao": "descrição do monstro 1 aqui",
        "dificuldade": 1,
        "status":{"vida":100, "agilidade":100},
        "opcoes":{
            "ignorar":"você irá ignorar o monstro",
            "fugir": "você irá empurrar o monstro e correr para o cenário anterior"}},
    
    "monstro2": {
        "descricao": "descrição do monstro 1 aqui",
        "dificuldade": 1,
        "status":{"vida":100, "agilidade":100},
        "opcoes":{
            "ignorar":"você irá ignorar o monstro",
            "fugir": "você irá empurrar o monstro e correr para o cenário anterior"}},
    
    "monstro3": {
        "descricao": "descrição do monstro 1 aqui",
        "dificuldade": 1,
        "status":{"vida":100, "agilidade":100},
        "opcoes":{
            "ignorar":"você irá ignorar o monstro",
            "fugir": "você irá empurrar o monstro e correr para o cenário anterior"}},
    
    "monstro4": {
        "descricao": "descrição do monstro 1 aqui",
        "dificuldade": 1,
        "status":{"vida":100, "agilidade":100},
        "opcoes":{
            "ignorar":"você irá ignorar o monstro",
            "fugir": "você irá empurrar o monstro e correr para o cenário anterior"}}
                }

# Função Principal
def main():
    #Introdução do Jogo
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
    #Carregamento dos Cenários e do Início
    cenarios, nome_cenario_atual = carregar_cenarios()
    #Condição para o Game Over
    game_over = False
    #Enquanto não for Game Over
    while not game_over:
        # Recebendo Inicio como cenario atual
        cenario_atual = cenarios[nome_cenario_atual]
        
        
        
        
        
        
        print(nome_cenario_atual,"\n{}".format("-"*len(nome_cenario_atual)))
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        
        else:
            print(cenario_atual['titulo'])
            print(cenario_atual['descricao'])
            print("")
            for opcao in opcoes:
                print('{0}:{1}'.format(opcao,opcoes[opcao]))
            escolha = input()
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
