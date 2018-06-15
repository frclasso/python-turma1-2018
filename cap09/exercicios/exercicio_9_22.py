#!/usr/bin/env python3

# -*-coding:utf-8 -*-
"""Ao ler ou gravar uma nova lista, verifique se a agenda atual já foi gravada.
Você pode usar uma variável para controlar quando a lista foi alterada
(novo,altera, apaga) e reinicializar esse valor quando ela for lida ou gravada.
"""

agenda = []

# Variável para marcar uma alteração na agenda
alterada = False


def pede_nome():
    return input("Nome: ")


def pede_telefone():
    return input("Telefone: ")


def mostra_dados(nome, telefone):
    print("Nome: {} Telefone: {}".format(nome, telefone))


def pede_nome_arquivo():
    return input("Nome do arquivo: ")


def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None


def novo():
     global agenda, alterada
     nome = pede_nome()
     telefone = pede_telefone()
     agenda.append([nome, telefone])
     alterada = True


def confirma(operacao):
    while True:
        opcao = input("Confirma {} (S/N)? ".format(operacao).upper())
        if opcao in "SN":
            return opcao
        else:
            print("Resposta inválida. Escolha S ou N.")


def apaga():
    global agenda, alterada
    nome = pede_nome()
    p = pesquisa(nome)
    if p != None:
        if confirma("apagamento") == "S":
            del agenda[p]
            alterada = True
    else:
        print("Nome não encontrado.")


def altera():
    global alterada
    p = pesquisa(pede_nome())
    if p != None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Encontrado:")
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        if confirma("alteração") == "S":
            agenda[p] = [nome, telefone]
            alterada = True
    else:
        print("Nome não encontrado.")


def lista():
    print("\nAgenda\n\n------")
    # Usamos a função enumerate para obter a posição na agenda
    for posicao, e in enumerate(agenda):
        # Imprimimos a posição, sem saltar linha
        print("Posição: {} ".format(posicao, end=""))
        mostra_dados(e[0], e[1])
    print("------\n")

def le():
    global agenda, alterada
    if alterada:
        print("Você não salvou a lista desde a última alteração. Deseja gravá-la agora?")
        if confirma("gravação") == "S":
            grava()
    print("Ler\n---")
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, "r", encoding = "utf-8")
    agenda = []
    for l in arquivo.readlines():
        nome, telefone = l.strip().split("#")
        agenda.append([nome, telefone])
    arquivo.close()
    alterada = False

def ordena():
    # Você pode ordenar a lista como mostrado no livro
    # com o método de bolhas (bubble sort)
    # Ou combinar o método sort do Python com lambdas para
    # definir a chave da lista
    # agenda.sort(key=lambda e: return e[0])
    fim = len(agenda)
    while fim > 1:
        i=0
        trocou = False
        while i < (fim - 1):
            if agenda[i]>agenda[i + 1]:
                agenda[i], agenda[i+1] = agenda[i+1], agenda[i]
                # temp = agenda[i + 1]
                # agenda[i + 1] = agenda[i]
                # agenda[i] = temp
                trocou = True
            i+=1
        if not trocou:
             break
        for posicao, e in enumerate(agenda):
            # Imprimimos a posição, sem saltar linha
            print("Posição: {} ".format(posicao, end=""))
            mostra_dados(e[0], e[1])
        print("------\n")


def grava():
    global alterada
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")
        if confirma("gravação") == "N":
            return
    print("Gravar\n------")
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, "w", encoding = "utf-8")
    for e in agenda:
        arquivo.write("%s#%s\n" % (e[0], e[1]))
    arquivo.close()
    alterada = False


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                   return(valor)
        except ValueError:
               print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))


def menu():
    print("""
   1 - Novo
   2 - Altera
   3 - Apaga
   4 - Lista
   5 - Grava
   6 - Lê
   7 - Ordena por nome

   0 - Sai
""")
    print("\nNomes na agenda: {} Alterada: {}\n".format(len(agenda), alterada))
    return valida_faixa_inteiro("Escolha uma opção: ",0,7)


while True:
     opcao = menu()
     if opcao == 0:
         break
     elif opcao == 1:
         novo()
     elif opcao == 2:
         altera()
     elif opcao == 3:
         apaga()
     elif opcao == 4:
         lista()
     elif opcao == 5:
         grava()
     elif opcao == 6:
         le()
     elif opcao == 7:
         ordena()
