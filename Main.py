import networkx as nx
# noinspection PyUnresolvedReferences
import matplotlib.pyplot as plt
from Graph import Grafo

gra = Grafo()
g = nx.Graph() # Cria o grafo
opcao = 0
while True: # Menu de opções
    print("Opção 1 - Arestas\n"
          "Opção 2 - Vertices\n"
          "Opção 3 - Desenhar gráfico\n"
          "Opção 4 - Sair\n")
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida, tente novamente.")

    match opcao:
        case 1:
            while True:
                print("Opção 1 - Criar aresta\n"
                      "Opção 2 - Listar arestas\n"
                      "Opção 3 - Voltar\n")
                try:
                    oparesta = int(input("Digite a opção desejada: "))
                except ValueError:
                    print("Opção inválida, tente novamente.")
                if oparesta == 1:
                    gra.aresta(g)  # Adiciona a aresta
                elif oparesta == 2:
                    print("Arestas: ",list(g.edges)) # Coloca todas as arestas em uma lista
                elif oparesta == 3:
                    break
                else:
                    print("Opção inexistente, tente novamente")

        case 2:
            while True:
                print("Opção 1 - Criar vértice\n"
                      "Opção 2 - Listar vértices\n"
                      "Opção 3 - Voltar\n")
                try:
                    opvertice = int(input("Digite a opção desejada: "))
                except ValueError:
                    print("Opção inválida, tente novamente.")
                if opvertice == 1:
                    gra.vertice(g)  # Adiciona o vértice
                elif opvertice == 2:
                    print("Vértices: ", list(g.nodes)) # Coloca todos os vértices em uma lista
                elif opvertice == 3:
                    break
                else:
                    print("Opção inexistente, tente novamente")

        case 3:
            gra.layout(g) # Escolhe o layout entre: Shell, Spring e Random

        case 4:
            print("Programa finalizado!!!")
            break

        case _:
            print("Opção inexistente, tente novamente.")