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



# ===================== GRAFO ORIENTADO =====================
class GrafoOrientado:
    """
    Representação de grafo orientado com simetrização e verificação de conectividade.
    """
    def __init__(self, vertices, arcos):
        """
        Inicializa o grafo orientado.
        Args:
            vertices (list ou set): Lista ou conjunto de vértices
            arcos (list ou set): Lista ou conjunto de arcos (tuplas)
        """
        self.vertices = set(vertices)
        self.arcos = set(arcos)
        self.arcos_simetrizados = self.simetrizar_grafo()
        self.lista_sucessores = self.construir_lista_sucessores()

    def simetrizar_grafo(self):
        """
        Adiciona arcos simétricos para cada arco do grafo.
        Returns:
            set: Conjunto de arcos simetrizados
        """
        arcos_sim = set(self.arcos)
        for u, v in self.arcos:
            arcos_sim.add((v, u))
        return arcos_sim

    def construir_lista_sucessores(self):
        """
        Constrói a lista de sucessores a partir dos arcos simetrizados.
        Returns:
            dict: Lista de sucessores
        """
        lista = {v: [] for v in self.vertices}
        for u, v in self.arcos_simetrizados:
            lista[u].append(v)
        return lista

    def dfs_fecho_transitivo(self, vertice_inicial):
        """
        Busca em profundidade para encontrar o fecho transitivo direto.
        Args:
            vertice_inicial: Vértice inicial
        Returns:
            set: Conjunto de vértices alcançados
        """
        visitados = set()
        pilha = [vertice_inicial]
        while pilha:
            atual = pilha.pop()
            if atual not in visitados:
                visitados.add(atual)
                for vizinho in self.lista_sucessores[atual]:
                    if vizinho not in visitados:
                        pilha.append(vizinho)
        return visitados

    def eh_conexo(self):
        """
        Verifica se o grafo orientado é conexo após simetrização.
        Returns:
            bool: True se conexo, False caso contrário
        """
        if not self.vertices:
            return True
        vertice_inicial = next(iter(self.vertices))
        fecho = self.dfs_fecho_transitivo(vertice_inicial)
        return fecho == self.vertices

    def imprimir_grafo(self):
        """
        Imprime a lista de sucessores do grafo orientado.
        """
        print("Lista de Sucessores (Orientado):")
        for vertice in sorted(self.vertices):
            vizinhos = sorted(self.lista_sucessores[vertice])
            print(f"{vertice}: {vizinhos}")


def teste_exemplo_orientado():
    """
    Testa o algoritmo orientado com o exemplo do enunciado.
    """
    print("=== TESTE COM GRAFO ORIENTADO ===")
    vertices = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
    arcos = [
        ('x1', 'x2'), ('x2', 'x3'), ('x3', 'x1'),
        ('x4', 'x5'), ('x5', 'x6'), ('x2', 'x4')
    ]
    grafo = GrafoOrientado(vertices, arcos)
    print(f"Vértices: {sorted(vertices)}")
    print(f"Arcos (originais): {arcos}")
    print(f"Arcos (simetrizados): {sorted(grafo.arcos_simetrizados)}")
    print()
    grafo.imprimir_grafo()
    print()
    eh_conexo = grafo.eh_conexo()
    print(f"O grafo orientado é conexo? {eh_conexo}")
    fecho = grafo.dfs_fecho_transitivo(vertices[0])
    print(f"Fecho transitivo de {vertices[0]}: {sorted(fecho)}")
    print()


if __name__ == "__main__":
    print("VERIFICAÇÃO DE CONECTIVIDADE EM GRAFOS - VERSÃO BÁSICA E ORIENTADA")
    print("=" * 55)
    print()
    # Testes não orientado
    teste_exemplo()
    teste_grafo_conexo()
    teste_grafo_desconexo()
    # Teste orientado
    teste_exemplo_orientado()
    print("=" * 55)
    print("Complexidade de Tempo: O(V + E)")
    print("Complexidade de Espaço: O(V)")
    print("V = número de vértices, E = número de arestas")
