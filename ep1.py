# -*- coding: utf-8 -*-
# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Cicero Tiago Carneiro Valentim, cicerotcv@al.insper.edu.br
# - aluno B: Luiz Felipe Lazzaron, luizfl@al.insper.edu.br
def creditos(entrada):
    lista = [
        "\nEste código foi desenvolvido em conjunto por Cicero Tiago e Luiz Felipe.",
        "Sinceramente, esperamos que tenha uma experiencia satisfatória, {}".format(entrada),
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
                        "algum aluno está dormindo na biblioteca."},
            "professor": {
                    "descricao": "o monstro do Python",
                    "saudacao": "Voce foi pedir para o professor adiar o EP."
                             "O professor revelou que é um monstro disfarçado "
                             "e devorou sua alma.",
                    "opcoes": {},
                    "imortal":True}
            }
    return personagens

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


    cenarios, condicao = carregar_cenarios(name)
    personagens = carregar_personagens(name)
    game_over = False


    while not game_over:
        #Loading Inicial
        if condicao in cenarios:
            cenario_atual = cenarios[condicao]
            titulo = cenario_atual["titulo"]
            descricao = cenario_atual["descricao"]
            opcoes = cenario_atual['opcoes']
        else:
            cenario_atual = escolha
            titulo = personagens[escolha]["descricao"]
            descricao = "Você está falando com {0}".format(titulo)
            opcoes = personagens[escolha]['opcoes']
            
            
        print("{0}\n{1}\n{2}\n".format(titulo,"-"*len(titulo),descricao))
        
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            print('O que você vai fazer?')
            print()
            for opcao in opcoes:
                print('{0}: {1}'.format(opcao,opcoes[opcao]))
            
            
            escolha = input(">>>>> ")  # palavra mágica do jogo
            
            
            if escolha == "prefiro pegar DP": 
                break
            
            elif escolha in opcoes:
                condicao = escolha
            
            elif escolha in personagens:
                print(personagens[escolha]["saudacao"])
            elif escolha == "voltar":
                escolha = condicao
                
            elif escolha == 'combate':
                print(condicao)
            
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()