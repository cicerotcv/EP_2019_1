# -*- coding: utf-8 -*-
# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Cicero Tiago Carneiro Valentim, cicerotcv@al.insper.edu.br
# - aluno B: Luiz Felipe Lazzaron, luizfl@al.insper.edu.br
def creditos(entrada):
    lista = [
        "\nEste código foi desenvolvido em conjunto por Cicero Tiago e Luiz Felipe.",
        "Sinceramente, esperamos que tenha uma experiencia satisfatória, {}.".format(entrada),
        "Não foi fácil encontrar essa forma mais 'enxuta' de escrever os códigos e de relacionar os comandos.",
        "(sim, acredite! O código estava ficando tão (e desnecessariamente) grande e complexo que "
        "tínhamos a impressão de que a qualquer momento ele assumiria o controle do computador e se iniciaria a 'Era das Máquinas'.\n\n"]
    for elemento in lista:
        print(elemento)

def instrucoes():
    lista = [
        "Instruções:",
        "1) Se você não quiser ser eliminado instantaneamente, digite exatamente como sugerem as sugestões",
        "2) Se quiser desistir do jogo, pode digitar 'prefiro pegar DP' a qualquer momento.\n"
        "3) As instruções 1 e 2 são muito importantes"]
    for i in lista:
        print(i)

#Função Cenários
def carregar_cenarios(nome):
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
def carregar_personagens(nome):
    personagens = {
            "guarda":{
                    "descricao":"Brian, o guarda parceiro",
                    "saudacao":"Hey aluno, tudo bem? O que você quer?",
                    "opcoes": {
                            "combate":"lutar com o Brian.",
                            "conversar": "conversar com o Brian.",
                            "voltar":"voltar para o saguão."}, # ainda não foi implementado
                    "imortal": True,
                    "speech": "Olá, {0}, adoraria conversar, mas tenho que ver se ".format(nome)+ 
                        "algum aluno está dormindo na biblioteca.",
                    "status":{}},
            
            "professor": {
                    "descricao": "o monstro do Python",
                    "saudacao": "Voce foi pedir para o professor adiar o EP."
                             "O professor revelou que é um monstro disfarçado "
                             "e devorou sua alma.",
                    "opcoes": {},
                    "imortal":True,
                    "status":{}},
            
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
                "opcoes":{}}}
            
    return personagens

#Função de Luta:
def carregar_luta(immortality,skills_npc, skills_player):
    if immortality == True:
        game_over = True
        text = "Você foi punido por código de ética!"
    else:
        if skills_player[1] == skills_npc[1]:
            skills_player[0] = skills_player[0] / 2
            text = "Vocês empataram. Você perdeu metade da sua vida por conta do desgaste."
            game_over = False
        elif skills_player[1] > skills_npc[1]:
            text = "Você venceu a luta!"
            game_over = False
        else:
            skills_player[0] = skills_player[0] - (skills_npc[1] - skills_player[1])
            if skills_player[0] <= 0:
                game_over = True
                text = "você foi derrotado, fim de jogo para você!"
            else:
                game_over = False
    return text,game_over

#Função Principal
def main():
    
    name = input("Olá, visitante! Qual seu nome? \n>>>>> ")
    
    comecar = False
    while not comecar:
        key = input("Olá, {0}! Aperte enter para começar, digite 'creditos' para exibir "
                    "o comentario dos autores ou 'instrucoes' "
                    "para mostrar as instrucoes.\n{1} ".format(name,(5*">")))
        if key == "creditos":
            creditos(name)
        elif key == "instrucoes":
            instrucoes()
        else:
            comecar = True
            print("\n\n=-=-=-=-=-= VAMOS COMEÇAR =-=-=-=-=-=\n\n")
        
        
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

    #Loading
    status = [100,10000,100]#Características do personagem
    cenarios, condicao = carregar_cenarios(name)
    personagens = carregar_personagens(name)
    game_over = False
    start = condicao

    #Rodada do Jogo
    while not game_over:
        #Loading Inicial
        cena = start
        if cena in cenarios:
            cenario_atual = cenarios[cena]
            titulo = cenario_atual["titulo"]
            descricao = cenario_atual["descricao"]
            opcoes = cenario_atual['opcoes']
            voltar = cena
        elif cena in personagens:
            cenario_atual = cena
            titulo = personagens[cena]["descricao"]
            descricao = "Você está falando com {0}".format(titulo)
            opcoes = personagens[cena]['opcoes']
            personagem = cena
            
        print("{0}\n{1}\n{2}\n".format(titulo,"-"*len(titulo),descricao))
        
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print('O que você vai fazer?')
            print()
            for opcao in opcoes:
                print('{0}: {1}'.format(opcao,opcoes[opcao]))
            
            
            start = input(">>>>> ")  # palavra mágica do jogo
            
            
            if start == "prefiro pegar DP": 
                break

            elif start in personagens:
                print(personagens[start]["saudacao"])
            elif start == "voltar":
                start = voltar
                
            elif start == 'combate':
                resposta,game_over = carregar_luta(personagens[personagem]['imortal'],personagens[personagem]['status'],status)
                print(resposta)
            elif start in cenarios:
                cena = start
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()