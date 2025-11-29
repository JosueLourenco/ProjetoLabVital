import networkx as nx
# noinspection PyUnresolvedReferences
import matplotlib.pyplot as plt
import Graph as gra

g = nx.Graph()
opcao = 0
while True:
    print("Opção 1 - Criar aresta\n"
          "Opção 2 - Criar vértice\n"
          "Opção 3 - Desenhar gráfico\n"
          "Opção 4 - Sair\n")
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida, tente novamente.")

    if opcao == 1:
        gra.aresta(g)

    elif opcao == 2:
            gra.vertice(g)

    elif opcao == 3:
        gra.layout(g)

    elif opcao == 4:
        print("Programa finalizado!")
        break

    else:
        print("Opção inexistente, tente novamente")


