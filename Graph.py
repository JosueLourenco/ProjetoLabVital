import networkx as nx
# noinspection PyUnresolvedReferences
import matplotlib.pyplot as plt

class Grafo:
 def aresta(self,x):
  while True:
      op1 = input("Digite A e B (espaço para finalizar): ").strip()
      if op1 == "" or op1 == " ":
          print("Opção finalizada!")
          break
      partes = op1.split()
      if len(partes) != 2:
          print("Você deve digitar *dois* caracteres")
      else:
          a,b = partes
          x.add_edge(a, b)
          print("aresta adicionada!")

 def layout(self,x):
    print("Digite o Layout desejado: \n"
              "Random - 1\n"
              "Spring - 2\n"
              "Shell  - 3\n")

    op = int(input("- "))
    while True:
        match op:
            case 1:
                nx.draw_random(x, with_labels = True)
                plt.show()
                break
            case 2:
                nx.draw_spring(x, with_labels=True)
                plt.show()
                break
            case 3:
                nx.draw_shell(x, with_labels=True)
                plt.show()
                break
            case _:
                print("formato inválido, digite novamente")
                break

 def vertice(self,x):
    while True:
        a = input("Digite A (espaço para finalizar): ").strip()
        if a == "" or a == " ":
            print("Opção finalizada!")
            break
        elif len(str(a)) > 2:
            print("A deve ter no máximo 2 caracteres")
        else:
            x.add_node(a)
            print("vértice adicionado!")
