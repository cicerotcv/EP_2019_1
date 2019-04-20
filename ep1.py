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
nome = input("Bem-vindo, jogador! Qual é o seu nome? ")

#Parâmetros do Jogador
forca = 100
agilidade = 100
vida = 100

#FUNÇÃO EXPLORAÇÃO
def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo.",
            "descricao": "Voce esta no saguao de entrada do insper. ",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a entrada da biblioteca",
                "conversar":"interagir com as pessoas do cenario",
                "investigar":"Procurar itens no cenario"},
            "monstros": [],
            "investigar": "Não há nada aqui.",
        
        "andar professor": {
            "titulo": "Andar do desespero.",
            "descricao": "Voce chegou ao andar da sala do seu professor.",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada.",
                "professor": "Falar com o professor."},
            "monstros": []},
        
        "professor": {
            "titulo": "O monstro do Python.",
            "descricao": "Voce foi pedir para o professor adiar o EP."
                         "O professor revelou que é um monstro disfarçado."
                         "e devorou sua alma.",
            "opcoes": {},
            "monstros": []
        },
        "biblioteca": {
            "titulo": "Entrada da Biblioteca",
            "descricao": "Bem-vindo a biblioteca. Aqui, existem muitas coisas para procurar, e algumas pessoas para conversar.",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "salas individuais": "Procurar colegas para ajudar na EP",
                "pesquisar no acervo": "Procurar livros que possam ajudar na EP",
                "investigar": "Procurar itens no cenario"},
            "monstros": []
            },
        
        "salas individuais": {
            "titulo":"Silêncio, por favor",
            "descricao":"Voce precisa encontrar amigos que te ajudem a resolver a EP. "
                        "Tome cuidado para não entrar em uma sala que está ocupada por um veterano",
            "opcoes": {
                "biblioteca":"Voltar para a entrada da biblioteca",
                "sala 01":"Entrar na sala 01",
                "sala 02":"Entrar na sala 02",
                "investigar": "Procurar itens no cenario"},
            "monstros": []
            },
        
        "sala 01": {
            "titulo":"Sala de estudos 1",
            "descricao":"Essa sala esta vazia.",
            "opcoes": {
                "salas individuais":"voltar para o corredor das salas individuais",
                "investigar":"Procurar itens no cenario"},
            "monstros": []
            },
        
        "sala 02": {
            "titulo":"Sala de estudos 2",
            "descricao":"Essa sala esta cheia de veteranos enfurecidos por conta reprovacao!",
            "opcoes": {
                "salas individuais":"voltar para o corredor das salas individuais",
                "conversar":"interagir com as pessoas do cenario",
                "investigar":"Procurar itens no cenario"},
            "monstros": []
            }
    }}
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def NPCs():
    inimigos = {
    "Professor": {
        "descricao": "O Monstro do Python",
        "classe": 1,
        "agressividade": True,
        "status":{"vida": 1000, "ataque":100, "defesa": 50},
        "opcoes":{
            "conversar":"Professor diz: Você não deveria tentar me enganar"}},

    "Veterano Enfurecido": {
        "descricao": "descrição do monstro 1 aqui.",
        "classe": 2,
        "agressividade": True,
        "status":{"vida": 100, "ataque":100, "defesa": 100},
        "opcoes":{
            "ignorar":"você irá ignorar o monstro.",
            "fugir": "você irá empurrar o monstro e correr para o cenário anterior."}}}

    outros = {
    "Ganiel Duzzo": {
        "descricao": "descrição do monstro 1 aqui.",
        "classe": 1,
        "agressividade": False,
        "status":{"vida": 100, "ataque":100, "defesa": 100},
        "opcoes":{
            "ignorar":"você irá ignorar a presença do personagem.",
            "fugir": "você irá empurrar o personagem e correr para o cenário anterior."}},

    "Bibliotecaria": {
        "descricao": "Encontra-se ociosa olhando atentamente para o acervo de livros.",
        "classe": 1,
        "agressividade": False,
        "status":{"vida": 100, "ataque":100, "defesa": 100},
        "opcoes":{
            "conversar":"Bibliotecaria diz: Estou muito ocupada agora."
            ""
            }},

    "Hagemoto": {
        "descricao": "Nada se sabe sobre ele.",
        "classe": 1,
        "agressividade": False,
        "status":{"vida": 9999, "ataque": 9999, "defesa": 9999},
        "opcoes":{
            "ignorar":"você irá ignorar o monstro",
            "interagir": "você irá falar com ele"}},

    "Aluno dormindo no chão":{
        "descricao": "Aluno dormindo próximo ao livro 'Think Python'.",
        "classe": 99999999,
        "agressividade": True,
        "status":{"vida": 1, "ataque":0, "defesa": 0},
        "opcoes":{}}
    }
    return inimigos,outros


def mochila(): {
    "Caderno":"anotações"
    }
    
def interagir():
        locais = {
        "inicio": {
                "observar":{
                        "pessoas":["não há ninguém aqui"],
                        "objetos":["não há nada aqui"]},
                "pegar":"não há nada para pegar",
                "andar":"Você pode ir para a 'biblioteca' ou para o 'andar do professor'",
                "conversar":{}},
        
        "biblioteca":{
                "observar":{
                        "pessoas":["aluno dormindo no chão próximo a um livro","Bibliotecaria"],
                        "objetos":"o livro Think Python"},
                "pegar":"livro Think Python"
                },
        
        "andar do professor": {
                "observar":{"pessoas":"não há ninguém aqui",
                            "objetos":["extintor de incêndio","pacote de balas de café"]},
                "pegar": {}
        }}
        return locais

# Função Principal
def main():
    #Introdução do Jogo
    print("Na hora do sufoco!")
    print("------------------")
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)\n")
    #Carregamento dos Cenários e do Início
    cenarios, nome_cenario_atual = carregar_cenarios()
    #Condição para o Game Over
    game_over = False 
    #Enquanto não for Game Over
    while not game_over:
        # Recebendo Inicio como cenario atual
        cenario_atual = cenarios[nome_cenario_atual]
      
        print(nome_cenario_atual,"\n{}\n".format("-"*len(nome_cenario_atual)))
        print(cenarios[nome_cenario_atual]["descricao"])
       
        opcoes = cenario_atual['opcoes']
        
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        
        else:
            print(cenario_atual['titulo'])
            print("")
            for opcao in opcoes:
                print('{0}: {1}'.format(opcao,opcoes[opcao]))
            escolha = input("O que você vai fazer? ")
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
