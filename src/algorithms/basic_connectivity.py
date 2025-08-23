"""
Verificação de Conectividade em Grafos - Versão Básica
APA 2 - Algoritmos e Programação Avançada

Esta implementação utiliza uma abordagem mais direta e didática,
adequada para compreensão inicial do problema.
"""

class GrafoBasico:
    """
    Representação básica de um grafo não-orientado usando lista de adjacências.
    """
    
    def __init__(self, vertices):
        """
        Inicializa o grafo com um conjunto de vértices.
        
        Args:
            vertices (list): Lista de vértices do grafo
        """
        self.vertices = set(vertices)  # Conjunto de vértices
        self.adj_list = {}  # Lista de adjacências
        
        # Inicializa lista de adjacências vazia para cada vértice
        for vertice in vertices:
            self.adj_list[vertice] = []
    
    def adicionar_aresta(self, v1, v2):
        """
        Adiciona uma aresta entre dois vértices.
        Como o grafo é não-orientado, adiciona a conexão nos dois sentidos.
        
        Args:
            v1: Primeiro vértice
            v2: Segundo vértice
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
        else:
            raise ValueError(f"Vértice não encontrado: {v1} ou {v2}")
    
    def construir_grafo(self, arestas):
        """
        Constrói o grafo a partir de uma lista de arestas.
        
        Args:
            arestas (list): Lista de tuplas representando as arestas
        """
        for v1, v2 in arestas:
            self.adicionar_aresta(v1, v2)
    
    def dfs_fecho_transitivo(self, vertice_inicial):
        """
        Calcula o fecho transitivo de um vértice usando busca em profundidade (DFS).
        
        Args:
            vertice_inicial: Vértice de onde iniciar a busca
            
        Returns:
            set: Conjunto de vértices alcançáveis a partir do vértice inicial
        """
        visitados = set()
        pilha = [vertice_inicial]
        
        while pilha:
            vertice_atual = pilha.pop()
            
            if vertice_atual not in visitados:
                visitados.add(vertice_atual)
                
                # Adiciona todos os vizinhos não visitados à pilha
                for vizinho in self.adj_list[vertice_atual]:
                    if vizinho not in visitados:
                        pilha.append(vizinho)
        
        return visitados
    
    def eh_conexo(self):
        """
        Verifica se o grafo é conexo.
        
        Returns:
            bool: True se o grafo é conexo, False caso contrário
        """
        if not self.vertices:
            return True  # Grafo vazio é considerado conexo
        
        # Escolhe qualquer vértice para iniciar a busca
        vertice_inicial = next(iter(self.vertices))
        
        # Calcula o fecho transitivo
        fecho = self.dfs_fecho_transitivo(vertice_inicial)
        
        # O grafo é conexo se o fecho contém todos os vértices
        return fecho == self.vertices
    
    def imprimir_grafo(self):
        """
        Imprime a representação do grafo.
        """
        print("Lista de Adjacências:")
        for vertice in sorted(self.vertices):
            vizinhos = sorted(self.adj_list[vertice])
            print(f"{vertice}: {vizinhos}")


def teste_exemplo():
    """
    Testa o algoritmo com o exemplo fornecido no enunciado.
    """
    print("=== TESTE COM EXEMPLO DO ENUNCIADO ===")
    
    # Conjunto de vértices
    vertices = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
    
    # Conjunto de arestas
    arestas = [
        ('x1', 'x2'), ('x2', 'x3'), ('x3', 'x1'),  # Primeiro componente
        ('x4', 'x5'), ('x5', 'x6'), ('x6', 'x4')   # Segundo componente
    ]
    
    grafo = GrafoBasico(vertices)
    grafo.construir_grafo(arestas)
    
    print(f"Vértices: {sorted(vertices)}")
    print(f"Arestas: {arestas}")
    print()
    
    grafo.imprimir_grafo()
    print()
    
    # Testa conectividade
    eh_conexo = grafo.eh_conexo()
    print(f"O grafo é conexo? {eh_conexo}")
    
    # Mostra o fecho transitivo de x1
    fecho_x1 = grafo.dfs_fecho_transitivo('x1')
    print(f"Fecho transitivo de x1: {sorted(fecho_x1)}")
    print()


def teste_grafo_conexo():
    """
    Testa com um grafo conexo.
    """
    print("=== TESTE COM GRAFO CONEXO ===")
    
    vertices = ['A', 'B', 'C', 'D']
    arestas = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')]
    
    grafo = GrafoBasico(vertices)
    grafo.construir_grafo(arestas)
    
    print(f"Vértices: {sorted(vertices)}")
    print(f"Arestas: {arestas}")
    print()
    
    grafo.imprimir_grafo()
    print()
    
    eh_conexo = grafo.eh_conexo()
    print(f"O grafo é conexo? {eh_conexo}")
    
    fecho_A = grafo.dfs_fecho_transitivo('A')
    print(f"Fecho transitivo de A: {sorted(fecho_A)}")
    print()


def teste_grafo_desconexo():
    """
    Testa com um grafo desconexo simples.
    """
    print("=== TESTE COM GRAFO DESCONEXO SIMPLES ===")
    
    vertices = ['1', '2', '3', '4']
    arestas = [('1', '2'), ('3', '4')]  # Dois componentes separados
    
    grafo = GrafoBasico(vertices)
    grafo.construir_grafo(arestas)
    
    print(f"Vértices: {sorted(vertices)}")
    print(f"Arestas: {arestas}")
    print()
    
    grafo.imprimir_grafo()
    print()
    
    eh_conexo = grafo.eh_conexo()
    print(f"O grafo é conexo? {eh_conexo}")
    
    fecho_1 = grafo.dfs_fecho_transitivo('1')
    print(f"Fecho transitivo de 1: {sorted(fecho_1)}")
    print()


if __name__ == "__main__":
    print("VERIFICAÇÃO DE CONECTIVIDADE EM GRAFOS - VERSÃO BÁSICA")
    print("=" * 55)
    print()
    
    # Executa todos os testes
    teste_exemplo()
    teste_grafo_conexo()
    teste_grafo_desconexo()
    
    print("=" * 55)
    print("Complexidade de Tempo: O(V + E)")
    print("Complexidade de Espaço: O(V)")
    print("V = número de vértices, E = número de arestas")
