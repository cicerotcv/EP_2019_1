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
            "item":{},
            "opcoes ocultas":{}
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
                    "speech": {
                        "conversar":"Olá, {0}, adoraria conversar, mas tenho que ver se ".format(nome)+ 
                                    "algum aluno está dormindo na biblioteca.",
                        "luta":{"derrota":"Brian diz: Você não achou que fosse ganhar de mim, não é?",
                                "vitoria":"Brian diz: '''Nunca tive chance. Não era nem uma batalha. "+
                                    "Tanto por profecias. Você é muito forte... {}...'''".format(nome)}},
                    "status":[]},
            
            "professor": {
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
                                "vitoria":"Brian diz: Nunca tive chance. Não era nem uma batalha. "+
                                    "Tanto por profecias. Você é muito forte... Saitama..."}},
                    "status":[]},
            
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
                                "vitoria":"Brian diz: Nunca tive chance. Não era nem uma batalha. "+
                                    "Tanto por profecias. Você é muito forte... Saitama..."}},
                    "status":[]},

            "Bibliotecaria": {
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
                                "vitoria":"Brian diz: Nunca tive chance. Não era nem uma batalha. "+
                                    "Tanto por profecias. Você é muito forte... Saitama..."}},
                    "status":[]},
        
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
                                "vitoria":"Brian diz: Nunca tive chance. Não era nem uma batalha. "+
                                    "Tanto por profecias. Você é muito forte... Saitama..."}},
                    "status":[]},
        
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
                                "vitoria":"Brian diz: Nunca tive chance. Não era nem uma batalha. "+
                                    "Tanto por profecias. Você é muito forte... Saitama..."}},
                    "status":[]}}
            
    return personagens

#Função de Luta:
def carregar_luta(inimigo, player):
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
    status = [100,10000,100] #Características do personagem
    bolsa = []
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
            opcoes_ocultas = cenario_atual['opcoes ocultas']
            voltar = cena
        elif cena in personagens:
            cenario_atual = cena
            titulo = personagens[cena]["descricao"]
            descricao = "Você está falando com {0}".format(titulo)
            opcoes = personagens[cena]['opcoes']
            opcoes_ocultas = personagens[cena]['opcoes ocultas']
            personagem = cena
        print("{0}\n{1}\n{2}\n".format(titulo,"-"*len(titulo),descricao))
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print('O que você vai fazer?')
            print()
            if cenarios[cena]['item'] in bolsa:
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
            elif start in personagens:
                print(personagens[start]["saudacao"])
            elif start == "voltar":
                start = voltar
            elif start == 'combate':
                resposta,game_over = carregar_luta(personagens[personagem],status)
                print(resposta)

            elif start == "investigar":
                verifica,item = carregar_inventario(cena)
                if verifica == True:
                    bolsa.append(item)
                    print("----------------------------------")
                    print("Parabéns! \n")
                    print("Você acaba de ganhar o item {0} \n {0} está agora guardada na sua bolsa".format(item))
                    enter = input("Aperte enter para voltar para o(a) {0}".format(voltar))
                    start = voltar
                else:
                    print("----------------------------------")
                    print("não há nada para encontrar")
                    enter = input("Aperte enter para voltar para o(a) {0}".format(voltar))
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