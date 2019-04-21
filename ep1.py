# -*- coding: utf-8 -*-
# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Cicero Tiago Carneiro Valentim, cicerotcv@al.insper.edu.br
# - aluno B: Luiz Felipe Lazzaron, luizfl@al.insper.edu.br
from random import randint

name = input("\nOlá, visitante! Qual seu nome? \n>>>>> ")

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
        "2) Se quiser desistir do jogo, pode digitar 'prefiro pegar DP' a qualquer momento.",
        "3) As instruções 1 e 2 são muito importantes",
        "4) O jogo possui uma cheat de vida que pode ser usada a qualquer momento.",
        "5) A cheat mencionada acima é: 'essa EP merece A+ mesmo sem ter todas as features implementadas'."]
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
                "guarda": "Seu Brian",
                "investigar": "Busque no cenário se há alguma coisa"},
            "item":"carterinha do guarda",
            "opcoes ocultas":{"Porta para Escadas":"Somente pessoas autorizadas podem entrar aqui"}},
        
        "setimo andar": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor",
                "investigar": "Busque no cenário se há alguma coisa"},
            "item":"carterinha de Marcos da Costa",
            "opcoes ocultas":{},
        },
        
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "investigar": "Busque no cenário se há alguma coisa"},
            "item":{"Think Python"},
            "opcoes ocultas":{"Outra dimensão":"Você se senta para ler o livro Think Python e acaba dormindo"}
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
                            "voltar":"voltar para o saguão."}, 
                    "imortal": False,
                    "derrotado": False,
                    "speech": {
                        "conversar":"Olá, {0}, adoraria conversar, mas tenho que ver se ".format(nome)+ 
                                    "algum aluno está dormindo na biblioteca.",
                        "luta":{"derrota":"Brian diz: Você não achou que fosse ganhar de mim, não é?",
                                "vitoria":"Brian diz: Parece que eu nunca tive chance de te vencer... aarrrhgh!",
                                "imortal":"Você foi obliterado",
                                "derrotado":"O guarda já foi derrotado."}},
                    "status":[100,100,100], # [vida,ataque,defesa]
                    "item":{"Pizza no iFood"},
                    "opcoes ocultas":{"Alimentar":"Dar pizza ao guarda"}},
            
            "professor": {
                    "descricao": "o monstro do Python",
                    "saudacao": "",
                    "opcoes": {"combate":"tente a sorte"},
                    "imortal":False,
                    "derrotado": False,
                    "speech": {
                        "conversar":"Olá, {0}, adoraria conversar, mas tenho que ver se ".format(nome)+ 
                                    "algum aluno está dormindo na biblioteca.",
                        "luta":{"derrota":"Brian diz: Você não achou que fosse ganhar de mim, não é?",
                                "vitoria":"texto de vitória",
                                 "":"Voce foi pedir para o professor adiar o EP. "+
                                    "O professor revelou que é um monstro disfarçado "+
                                    "e devorou sua alma."}},
                    "status":[100,100,100],
                    "item":{},
                    "opcoes ocultas":{}},
            
            "Ganiel Duzzo": {
                    "descricao": "o monstro do Python",
                    "saudacao": "Voce foi pedir para o professor adiar o EP."
                             "O professor revelou que é um monstro disfarçado "
                             "e devorou sua alma.",
                    "opcoes": {"combate":"tente a sorte"},
                    "imortal":False,
                    "speech": {
                        "conversar":"Olá, {0}, adoraria conversar, mas tenho que ver se ".format(nome)+ 
                                    "algum aluno está dormindo na biblioteca.",
                        "luta":{"derrota":"Brian diz: Você não achou que fosse ganhar de mim, não é?",
                                "vitoria":"Brian diz: texto de vitória"}},
                    "status":[],
                    "item":{},
                    "opcoes ocultas":{}},
            "Bibliotecaria": {
                    "descricao": "o monstro do Python",
                    "saudacao": "Voce foi pedir para o professor adiar o EP."
                             "O professor revelou que é um monstro disfarçado "
                             "e devorou sua alma.",
                    "opcoes": {"combate":"tente a sorte"},
                    "imortal":True,
                    "speech": {
                        "conversar":"Olá, {0}, adoraria conversar, mas tenho que ver se ".format(nome)+ 
                                    "algum aluno está dormindo na biblioteca.",
                        "luta":{"derrota":"Brian diz: Você não achou que fosse ganhar de mim, não é?",
                                "vitoria":"texto de vitória"}},
                    "status":[],
                    "item":{},
                    "opcoes ocultas":{}},
            "Hagemoto": {
                    "descricao": "o monstro do Python",
                    "saudacao": "Voce foi pedir para o professor adiar o EP."
                             "O professor revelou que é um monstro disfarçado "
                             "e devorou sua alma.",
                    "opcoes": {"combate":"tente a sorte"},
                    "imortal":False,
                    "speech": {
                        "conversar":"Olá, {0}, adoraria conversar, mas tenho que ver se ".format(nome)+ 
                                    "algum aluno está dormindo na biblioteca.",
                        "luta":{"derrota":"Brian diz: Você não achou que fosse ganhar de mim, não é?",
                                "vitoria":"texto de vitória"}},
                    "status":[],
                    "item":{},
                    "opcoes ocultas":{}},
            "Aluno dormindo no chão":{
                    "descricao": "o monstro do Python",
                    "saudacao": "Voce foi pedir para o professor adiar o EP."
                             "O professor revelou que é um monstro disfarçado "
                             "e devorou sua alma.",
                    "opcoes": {"combate":"tente a sorte"},
                    "imortal":False,
                    "speech": {
                        "conversar":"Olá, {0}, adoraria conversar, mas tenho que ver se ".format(nome)+ 
                                    "algum aluno está dormindo na biblioteca.",
                        "luta":{"derrota":"Brian diz: Você não achou que fosse ganhar de mim, não é?",
                                "vitoria":"texto de vitória"}},
                    "status":[]}}
            
    return personagens

#Função de Luta:
def carregar_luta(characters,inimigo, player,):
    # characters: dicionario com todos os personagens carregado -> usar 'personagens' na chamada da função
    # inimigo: nome do inimigo -> usar 'personagem' na chamada da função
    # player: status do jogador: status -> usar 'player_status' na chamada da função [vida,ataque,defesa]''
    game_over = False
    enemy = characters[inimigo] # valor de dicionario
    enemy_status = enemy["status"] # valor de lista [vida,ataque,defesa]

    if enemy["imortal"] == True:
        game_over = True
        text = enemy["speech"]["luta"]["imortal"]
    elif enemy["derrotado"] == True:
        game_over = False
        text = enemy["speech"]["luta"]["derrotado"]
    else:
        battle = True 
        battle_ini = ["\nEis que se inicia a batalha", "\nComeçou!", "\nPrepare-se!", "\nSe inicia um dos maiores duelos de todos os tempos"]
        texto_inicio = battle_ini[randint(0,len(battle_ini)-1)]
        print(texto_inicio+len(texto_inicio)*("-")+"\n")
        
        while battle:
            sorte = randint(0,100)
            azar = randint(-100,0)
        
            if (player[1] >= enemy_status[2]): # se o ataque do jogador for maior que a defesa do inimigo:
            
                # Turno do jogador:
                player_damage = round((player[1] - enemy_status[2] + (2*sorte) + azar)/100)*randint(0,10) # dano causado pelo jogador
                if player_damage < 0:
                    player_damage = 0
                
                enemy_status[0] -= round(player_damage) # atualizacao da vida do inimigo
                if enemy_status[0] < 0:
                    enemy_status[0] = 0
                    battle = False
                    text = enemy["speech"]["luta"]["vitoria"]
                print("\n{0} recebe {1} de dano. Vida atual:{2} pontos de vida.".format(inimigo, player_damage, enemy_status[0]))
                if not battle:
                    break
                
                # Turno do inimigo:
                enemy_damage = round((enemy_status[1] - player[2] + sorte + azar)/100)*randint(0,20) # dano causado pelo inimigo
                if enemy_damage < 0:
                    enemy_damage = 0
                player[0] -= round(enemy_damage) # atualização da vida do jogador
                
                if player[0] <= 0: # checar se o jogador morreu
                    player[0] = 0
                    battle = False
                    game_over = True
                    text = enemy["speech"]["luta"]["derrota"]
                print("\nVocê recebe {0} de dano. Vida atual: {1} pontos de vida.".format(enemy_damage,player[0]))


            elif (player[1] < enemy_status[2]): # se o ataque do jogador for menor que a defesa do inimigo:
                
                # Turno do jogador:
                player_damage = ((player[1] - enemy_status[2] + sorte + azar)/100)*randint(0,20) # dano causado pelo jogador
                if player_damage < 0:
                    player_damage = 0
                enemy_status[0] -= round(player_damage) # atualizacao da vida do inimigo
                
                if enemy_status[0] < 0:
                    enemy_status[0] = 0
                    battle = False
                    text = enemy["speech"]["luta"]["vitoria"]
                print("\n{0} recebe {1} de dano. Vida atual:{2} pontos de vida.".format(inimigo,player_damage,enemy_status[0]))
                if not battle:
                    break
                
                # Turno do inimigo:
                enemy_damage = ((enemy_status[1] - player[2] + sorte + azar)/100)*randint(0,10) # dano causado pelo inimigo
                if enemy_damage < 0:
                    enemy_damage = 0
                player[1] -= round(enemy_damage) # atualização da vida do jogador
                
                if player[0] <= 0:
                    player[0] = 0
                    battle = False
                    game_over = True
                    text = enemy["speech"]["luta"]["derrota"]
                print("\nVocê recebe {0} de dano. Vida atual: {1} pontos de vida.".format(enemy_damage,player[0]))



    return text, game_over

def carregar_inventario(lugar):
    cenas = {
                "guarda":"carterinha do guarda",
                "biblioteca": "iPhone XII",
                "setimo andar": "carterinha de Marcos da Costa"}
    if lugar in cenas:
       return True,cenas[lugar],
    else:
       return False, None
    
#Função Principal
def main():
    

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

    player_status = [100,100,100] #Características do personagem [hp,atk,def]
    cenarios, condicao = carregar_cenarios(name) # dicionarios
    personagens = carregar_personagens(name) # valor de dicionario
    bolsa = []
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
            opcoes_ocultas = cenario_atual['opcoes ocultas']
            voltar = cena
            tipo = cenarios
        elif cena in personagens:
            cenario_atual = cena
            titulo = personagens[cena]["descricao"]
            descricao = "Você está falando com {0}".format(titulo)
            opcoes = personagens[cena]['opcoes']
            opcoes_ocultas = personagens[cena]['opcoes ocultas']
            personagem = cena
            tipo = personagens
        print("{0}\n{1}\n{2}\n".format(titulo,"-"*len(titulo),descricao))
        
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print('O que você vai fazer?\n')
            if tipo[cena]['item'] in bolsa:
                for opcao in opcoes:
                    print('{0}: {1}'.format(opcao,opcoes[opcao]))
                for opcao_oculta in opcoes_ocultas:
                    print('{0}: {1}'.format(opcao_oculta,opcoes_ocultas[opcao_oculta]))
            else:
                for opcao in opcoes:
                    print('{0}: {1}'.format(opcao,opcoes[opcao]))
            start = input(">>>>> ")  # palavra mágica do jogo

            if start == "prefiro pegar DP": 
                break
            
            if start == "essa EP merece A+ mesmo sem ter todas as features implementadas":
                player_status[0] = 200
                start = cena
            
            if start in personagens:
                print(personagens[start]["saudacao"])
            
            elif start == "voltar":
                start = voltar
            
            elif start == 'combate':
                resposta,game_over = carregar_luta(personagens,personagem,player_status)
                print(resposta)
                if not game_over:  # jogador volta ao início
                    personagens[personagem]["derrotado"] = True
                    #cenarios[cena]["opcoes"][personagem] = "{} está inconsciente.".format(personagem)
                    start = voltar
            
            elif start == "investigar":
                verifica,item = carregar_inventario(cena)
                if verifica == True:
                    bolsa.append(item)
                    print("----------------------------------")
                    print("Parabéns! \n")
                    print("Você acaba de ganhar o item {0}\n {0} está agora guardada na sua bolsa".format(item))
                    verifica = False
                    input("Aperte enter para voltar para o(a) {0}".format(voltar))
                    start = voltar
                else:
                    print("----------------------------------")
                    print("não há nada para encontrar")
                    input("Aperte enter para voltar para o(a) {0}".format(voltar))
                    start = voltar
            
            elif start in cenarios:
                cena = start
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")

# Programa principal.
if __name__ == "__main__":
    main()