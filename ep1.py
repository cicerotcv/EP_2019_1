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
        "tínhamos a impressão de que a qualquer momento ele assumiria o controle do computador e se iniciaria a 'Era das Máquinas'.\n\n",
        "\n>>>> ReadyPlayerOne <<<<"]
    for elemento in lista:
        print(elemento)

def instrucoes():
    lista = [
        "Instruções:",
        "1) Se você não quiser ser eliminado instantaneamente, digite exatamente como sugerem as sugestões",
        "2) Se quiser desistir do jogo, pode digitar 'churrasco' a qualquer momento.",
        "3) As instruções 1 e 2 são muito importantes",
        "4) O jogo possui uma cheat de vida que pode ser usada a qualquer momento fora de combate.",
        "5) A cheat mencionada acima é... Bom... Você fica até o final dos créditos em filmes da Marvel?",
        "6) Você pode digitar 'mochila' a qualquer momento para checar seu inventario",
        "7) Nenhuma NPC será violentamente ferido nesse jogo e não há nenhum incentivo à violência."]
    for i in lista:
        print(i)

#Função Cenários
def carregar_cenarios(nome):
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper\n"+
                        "Por algum motivo, os elevadores só podem te levar para o setimo andar",
            "opcoes": {
                "setimo andar": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca",
                "guarda": "falar com o guarda",
                "investigar": "Busque no cenário se há alguma coisa"},
            "item":"notebook de algum bolsista", #item necessário para desbloquear opções ocultas
            # Item disponivel: nenhum
            "opcoes ocultas":{"veterano enfurecido":"surge um veterano enfurecido em modo de combate."}},
        
        "escadas": {
            "titulo": "Escadas infinitas",
            "descricao": "Você está nas escadas infinitas\n"+
                    "Você percebe que existem alguns livros jogados no chão",
            "opcoes": {
                "inicio": "voltar para o saguao de entrada",
                "setimo andar": "subir escadas até o sétimo andar",
                "investigar": "Busque nas escadarias se há alguma coisa útil"},
            "item":"canudos",
            # item disponivel: livro Think Python 
            "opcoes ocultas":{"refeitorio":"vá para o refeitório usando escadas.",
                              "sala de estudos": "vá até a sala de estudos"},
        },
        
        "setimo andar": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor.\n"+
                        "Você não deixa de notar a grande quantidade de extintores de incendio no andar",
            "opcoes": {
                "inicio": "tomar o elevador para o saguao de entrada",
                "sala vazia": "entrar em uma sala aparentemente vazia",
                "professor": "falar com o professor",
                "Ganiel Duzzo": "falar com Ganiel Duzzo",
                "investigar": "Busque no corredor se há alguma coisa"},
            "item":"carteirinha de Marcos da Costa",
            # item disponível: extintor de incendio
            "opcoes ocultas":{"sala secreta":"vá para a sala secreta do Marcos",
                              "escadas":"acesso às escadas"},
        },
        "sala vazia":{
            "titulo": "Sala aparentemente vazia",
            "descricao": "Parece que não temos nada aqui.",
            "opcoes": {
                "setimo andar": "Voltar para o setimo andar",
                "investigar": "Veja se há alguma coisa na sala vazia"},
            "item":"chave triangular",
            # item disponivel: canudos
            "opcoes ocultas":{"porta estranha":"você nota um orifício triangular"}
        },
        "porta estranha":{
            "titulo": "Você chegou em lugar nenhum.",
            "descricao": "Aqui você pode descansar e fazer sua EP.",
            "opcoes": {
                "sala vazia": "Voltar para a sala vazia",
                "investigar": "digite 'investigar' e receba sua merecida recompensa."},
            "item":"clipes metalicos",
            # item disponivel: EP feita
            "opcoes ocultas":{"porta estranha":"você nota um orifício triangular"}
        },
            
        "refeitorio": {
            "titulo": "Refugio da felicidade",
            "descricao": "Voce esta no refeitorio.\n"+
                    "Voce percebe sinais de fumaça no ambiente",
            "opcoes": {
                "setimo andar": "Voltar para o setimo andar",
                "investigar": "Busque no refeitório se há alguma coisa"},
            "item":"extintor de incendio",
            # item disponivel: pizza do InsperFoods
            "opcoes ocultas":{"sala secreta":"a porta que estava em chamas leva a uma sala secreta",
                              "escadas":"ir para as escadas"}
        },
        
        "sala de estudos":{
            "titulo": "Sala de Estudos",
            "descricao": "Aqui você encotra inumeros lugares vazios para estudo.\n"+
                        "Você não deixa de notar uma mochila no ambiente",
            "opcoes": {
                "inicio": "Voltar para o inicio",
                "investigar": "Busque algo útil na mochila."},
            "item":"extintor de incendio",
            # item disponível: notebook de algum bolsista
            "opcoes ocultas":{"refeitorio":"vá para o refeitório usando o elevador."}
        },

        "sala secreta":{
            "titulo": "Sala secreta de Marcos da Costa",
            "descricao": "Você vê uma mesa com várias palitos de picolé em cima.",
            "opcoes": {
                "setimo andar": "Voltar para o saguao de entrada.",
                "investigar": "pegue uma das chaves da mesa."},
            "item":"joia do espaco",
            # item disponivel: palitos de picole
            "opcoes ocultas":{"inicio":"se teletransporte para o inicio",
                              "refeitorio":"va para o refeitorio",
                              "outra dimensao":"vá para outra dimensão",
                              "setimo andar":"vá para o sétimo andar",
                              "sala de estudos":"vá para a sala de estudos",
                              "escadas":"ir para as escadas"}
        },
            
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "investigar": "Busque no cenário se há alguma coisa",
                "bibliotecaria": "falar com a bibliotecaria"},
            "item":"Think Python",
            # item disponivel: iPhone XII
            "opcoes ocultas":{"outra dimensao":"Você se senta para ler o livro Think Python e acaba dormindo"}
        },
            
        "outra dimensao": {
            "titulo": "Limbo",
            "descricao": "Você está no Limbo e vê uma figura caminhando em sua direção.",
            "opcoes": {
                "biblioteca": "voltar para a biblioteca",
                "investigar": "Busque no cenário se há alguma coisa"},
            "item":"Think Python",
            # Item disponível: joia do espaco
            "opcoes ocultas":{"Hagemoto":"falar com Hagemoto."}
        }
        }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

# Função personagens
def carregar_personagens(nome):
    personagens = {
            "guarda":{
                    "descricao":"Brian, o guarda parceiro",
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
                    "item":"pizza do InsperFoods",
                    "opcoes ocultas":{"sala de estudos":"dê pizza ao guarda para acessar"}},
            
            "professor": {
                    "descricao": "O monstro do Python",
                    "opcoes": {"combate":"tente a sorte",
                               "conversar":"conversar com o professor",
                               "voltar":"voltar para os corredores do sétimo andar"},
                    "imortal":False,
                    "derrotado": False,
                    "speech": {
                        "conversar":"Olá, {0} hehehehe\nAdoraria conversar, mas tenho que ".format(nome)+ 
                                    "receber inúmeras EPs\nhehehe.",
                        "luta":{"derrota":"A-a-chei que fosse i-i-impossísvel.",
                                "vitoria":"Como eu poderia ter sido esmagado \npor alguém como você??? Aerrrgh!".format(nome),
                                 }},
                    "status":[500,100,100],
                    "item":"coragem", # conseguido na sala vazia
                    "opcoes ocultas":{"prefiro pegar DP":"desistir"}},
            
            "Ganiel Duzzo": {
                    "descricao": "o monstro do Design",
                    "opcoes": {
                            "combate":"lutar com o Ganiel.",
                            "conversar": "conversar com Ganiel.",
                            "voltar":"voltar para o setimo andar."},
                    "imortal":False,
                    "derrotado":False,
                    "speech": {
                        "conversar":"Olá. Não esqueça de passar no FabLab terça, Ok?!",
                        "luta":{"derrota":"Ganiel Duzzo diz: O que te fez pensar que conseguiria? hahahaha",
                                "vitoria":"Ganiel Duzzo diz: Não e-e-entendo como v-v-você... Aaaergh"}},
                    "status":[100,100,100],
                    "item":{},
                    "opcoes ocultas":{}},
            
            "bibliotecaria": {
                    "descricao": "o monstro dos livros",
                    "opcoes": {"combate":"tente a sorte",
                               "conversar":"converse com ela."},
                    "imortal":False,
                    "derrotado":False,
                    "speech": {
                        "conversar":"Olá, {0}, você sabia que é saudável digitar".format(nome)+ 
                                    "'ReadyPlayerOne'?",
                        "luta":{"derrota":"Bibliotecaria diz: Você não achou que fosse ganhar de mim, não é?",
                                "vitoria":"Bibliotecaria diz: Foi pura sorte"}},
                    "status":[100,100,100],
                    "item":"carteirinha do guarda",
                    "opcoes ocultas":{'escadas':'vá para as escadas secretas dentro da biblioteca.'}},
            
            "Hagemoto": {
                    "descricao": "?????????",
                    "opcoes": {"combate":"tente a sorte",
                               "conversar":"falar com Hagemoto"},
                    "imortal":False,
                    "derrotado":False,
                    "speech": {
                        "conversar":"Olá, {0}, adoraria conversar, mas tenho que ver se ".format(nome)+ 
                                    "algum aluno está dormindo na biblioteca.",
                        "luta":{"derrota":"Brian diz: Você não achou que fosse ganhar de mim, não é?",
                                "vitoria":"texto de vitória"}},
                    "status":[300,100,100],
                    "item":"canudos",
                    "opcoes ocultas":{"sala vazia":"ser teletransportado para a biblioteca"}},
            
            "veterano enfurecido":{
                    "descricao": "Ele te acusa de ter roubado o notebook dele.",
                    "saudacao": "E aí, suco de fruta, quero meu notebook de volta!",
                    "opcoes": {"combate":"mostrar quem é que manda"},
                    "imortal":False,
                    "derrotado": False,
                    "speech": {
                        "conversar":"Não quero conversar!",
                        "luta":{"derrota":"Vetaro diz: você já era, panaca!",
                                "vitoria":"E-e-e-eu não quis insinuar que-e Eeeargh!"}},
                    "status":[100,100,100],
                    "item":"notebook de algum bolsista",
                    "opcoes ocultas":{"conversar":"tentar conversar com ele"}}}
            
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
                player_damage = round((player[1] - enemy_status[2] + (2*sorte) + azar)/100)*randint(1,50) # dano causado pelo jogador
                if player_damage < 0:
                    player_damage = 0
                
                enemy_status[0] -= round(player_damage) # atualizacao da vida do inimigo
                if enemy_status[0] < 0:
                    enemy_status[0] = 0
                    battle = False
                    text = enemy["speech"]["luta"]["vitoria"]
                print("\n{0} recebe {1} de dano. Vida atual: {2} pontos de vida.".format(inimigo, player_damage, enemy_status[0]))
                if not battle:
                    break
                
                # Turno do inimigo:
                enemy_damage = round((enemy_status[1] - player[2] + (2*sorte) + azar)/100)*randint(1,50) # dano causado pelo inimigo
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
                player_damage = ((player[1] - enemy_status[2] + sorte + azar)/100)*randint(1,50) # dano causado pelo jogador
                if player_damage < 0:
                    player_damage = 0
                enemy_status[0] -= round(player_damage) # atualizacao da vida do inimigo
                
                if enemy_status[0] < 0:
                    enemy_status[0] = 0
                    battle = False
                    text = enemy["speech"]["luta"]["vitoria"]
                print("\n{0} recebe {1} de dano. Vida atual: {2} pontos de vida.".format(inimigo,player_damage,enemy_status[0]))
                if not battle:
                    break
                
                # Turno do inimigo:
                enemy_damage = ((enemy_status[1] - player[2] + sorte + azar)/100)*randint(1,50) # dano causado pelo inimigo
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

# Função que define os itens presentes nos cenários
def carregar_inventario(lugar):
    cenas = {
                "guarda":"carteirinha do guarda",
                "escadas":"Think Python",
                "Hagemoto":"carteirinha de Marcos da Costa",
                "setimo andar": "extintor de incendio",
                "refeitorio": "pizza do InsperFoods",
                "outra dimensao":"joia do espaco",
                "Ganiel Duzzo":"chave triangular",
                "sala de estudos":"notebook de algum bolsista",
                "biblioteca": "iPhone XII",
                "veterano enfurecido":"pedacos de papel",
                "porta estranha":"EP feita",
                "sala vazia":"canudos",
                "bibliotecaria":"clipes metalicos",
                "sala secreta":"palitos de picole"}
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
        "na entrada do Insper e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    #Loading

    player_status = [500,100,100] #Características do personagem [hp,atk,def]
    cenarios, start = carregar_cenarios(name) # dicionarios
    
    personagens = carregar_personagens(name) # valor de dicionario
    
    itens_cenarios = {} # itens dos cenarios // valor de dicionario
    verificacao = {}
    for i in cenarios:
        itens_cenarios[i] = carregar_inventario(i)[1]
        verificacao[i] = carregar_inventario(i)[0]
    bolsa = ["coragem"] # lista do inventário
    
    itens_personagens = {}
    for i in personagens:
        itens_personagens[i] = carregar_inventario(i)[1]
    
    game_over = False
    EP_feita = False
    #Rodada do Jogo
    while not game_over:
        
        cena = start
        if cena in cenarios:
            cenario_atual = cenarios[cena] # valor de dicionario
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
        
        print("\n{1}\n>> {0} <<\n{1}\n{2}\n".format(titulo,"-"*(len(titulo)+6),descricao))
        
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
            # Entregar EP:
            if start == "Entregar EP" and "Ep feita" in bolsa:
                EP_feita = True
                game_over = True
                break            
            
            if start == "churrasco" or start == "prefiro pegar DP":
                print("\033[31mVocê foi obliterado \033[0;0m")
                break
            
            if start == "ReadyPlayerOne":
                print("+ 500 de vida")
                player_status[0] += 500
                start = cena
            if start in personagens:
                if personagens[start]["derrotado"]:
                    print("\n\033[31m{} está incosciente e vocês não podem mais interagir.\033[0;0m".format(personagem))
                    start = voltar
            # voltar
            elif start == "voltar":
                start = voltar
            
            # abrir mochila
            elif start == "mochila":
                if len(bolsa) != 0:
                    print("Você possui {} objeto(s)) na mochila:".format(len(bolsa)))
                    for objeto in bolsa:
                        print('\033[31m'+objeto+'\033[0;0m')
                else:
                    print("\n{0}\n>> sua mochila está vazia <<\n{0}".format(28*'-'))
                start = voltar
            
            # iniciar combate
            elif start == 'combate':
                resposta,game_over = carregar_luta(personagens,personagem,player_status)
                print()
                print(resposta)
                if not game_over:  # jogador retorna ao cenario
                    personagens[cena]["derrotado"] = True
                    if itens_personagens[cena] != None:
                        bolsa.append(itens_personagens[cena])
                        del itens_personagens[cena]
                        print("\n\033[31mParabéns, voce ganhou um prêmio:\033[0;0m")
                        print("\033[31mvocê obteve: {}\033[0;0m".format(bolsa[len(bolsa)-1]))
                    cenarios[voltar]["opcoes"][personagem] = "{} está inconsciente.".format(personagem)
                    if personagens["professor"]["derrotado"]:
                        break
                    start = voltar
            
            # obter itens do cenário
            elif start == "investigar":
                verifica,item = verificacao[cena],itens_cenarios[cena]
                if verifica == True:
                    bolsa.append(item)
                    print("--------")
                    print("Parabéns!")
                    print("Você acaba de ganhar o item: \033[31m{0}\033[0;0m".format(item))
                    if cena in itens_cenarios:
                        del itens_cenarios[cena]
                        del cenarios[cena]["opcoes"]["investigar"]
                    input("Pressione enter para voltar.\n")
                    start = voltar
                else:
                    print("--------------------------")
                    print("não há nada aqui")
                    input("Aperte enter para voltar.\n")
                    start = voltar
            # conversar:
            elif start == "conversar":
                print("\n\033[32m"+personagens[cena]["speech"]["conversar"]+'\033[0;0m\n')
                start = cena
                
            elif start in cenarios:
                cena = start
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
    if EP_feita:
        print('Parabéns, você conseguiu quebrar a maldição e vencer o jogo!')
    elif personagens["professor"]["derrotado"]:
        print("Parabéns! Você venceu o jogo derrotando o professor.")
    else:
        print("Você perdeu")

# Programa principal.
if __name__ == "__main__":
    main()