"""
Verificação de Conectividade em Grafos Não Orientados - Versão Otimizada (LLM)
APA 2 - Algoritmos e Programação Avançada

Esta implementação foi gerada por uma LLM (GitHub Copilot) e inclui otimizações de desempenho:
- Uso de sets para operações O(1)
- Early termination na DFS
- Estruturas de dados mais eficientes
- Otimizações de memória
"""

from collections import defaultdict, deque
import time


class GrafoNaoOrientadoOtimizadoLLM:
    """
    Representação otimizada de um grafo não-orientado.
    Utiliza estruturas de dados mais eficientes e técnicas de otimização.
    """
    
    def __init__(self, vertices):
        """
        Inicializa o grafo com um conjunto de vértices.
        
        Args:
            vertices (list): Lista de vértices do grafo
        """
        self.vertices = frozenset(vertices)  # frozenset é mais eficiente para conjuntos imutáveis
        self.num_vertices = len(vertices)
        
        # defaultdict evita verificações de existência de chaves
        self.adj_set = defaultdict(set)  # Usa sets para adjacências (O(1) lookup)
        
        # Cache para resultados de conectividade
        self._cache_conectividade = None
    
    def adicionar_aresta(self, v1, v2):
        """
        Adiciona uma aresta entre dois vértices.
        
        Args:
            v1: Primeiro vértice
            v2: Segundo vértice
        """
        if v1 not in self.vertices or v2 not in self.vertices:
            raise ValueError(f"Vértice não encontrado: {v1} ou {v2}")
        
        # Evita auto-loops desnecessários
        if v1 != v2:
            self.adj_set[v1].add(v2)
            self.adj_set[v2].add(v1)
        
        # Invalida cache quando estrutura muda
        self._cache_conectividade = None
    
    def construir_grafo(self, arestas):
        """
        Constrói o grafo a partir de uma lista de arestas.
        Otimizado para inserção em lote.
        
        Args:
            arestas (list): Lista de tuplas representando as arestas
        """
        for v1, v2 in arestas:
            self.adicionar_aresta(v1, v2)
    
    def dfs_fecho_transitivo_otimizado(self, vertice_inicial):
        """
        Calcula o fecho transitivo usando DFS otimizada.
        Implementa early termination e usa estruturas eficientes.
        
        Args:
            vertice_inicial: Vértice de onde iniciar a busca
            
        Returns:
            set: Conjunto de vértices alcançáveis
        """
        if vertice_inicial not in self.vertices:
            return set()
        
        visitados = set()
        pilha = [vertice_inicial]
        
        while pilha:
            vertice_atual = pilha.pop()
            
            if vertice_atual not in visitados:
                visitados.add(vertice_atual)
                
                # Early termination: se já visitamos todos os vértices
                if len(visitados) == self.num_vertices:
                    break
                
                # Adiciona vizinhos não visitados (operação O(1) com sets)
                for vizinho in self.adj_set[vertice_atual]:
                    if vizinho not in visitados:
                        pilha.append(vizinho)
        
        return visitados
    
    def dfs_iterativa_com_limite(self, vertice_inicial, limite_vertices=None):
        """
        DFS iterativa com limite opcional de vértices.
        Útil quando só queremos saber se alcançamos um número mínimo.
        
        Args:
            vertice_inicial: Vértice inicial
            limite_vertices (int): Para quando atingir este número de vértices
            
        Returns:
            set: Conjunto de vértices visitados
        """
        if limite_vertices is None:
            limite_vertices = self.num_vertices
            
        visitados = set()
        pilha = [vertice_inicial]
        
        while pilha and len(visitados) < limite_vertices:
            vertice_atual = pilha.pop()
            
            if vertice_atual not in visitados:
                visitados.add(vertice_atual)
                
                # Adiciona vizinhos
                pilha.extend(viz for viz in self.adj_set[vertice_atual] 
                           if viz not in visitados)
        
        return visitados
    
    def eh_conexo_otimizado(self):
        """
        Verifica conectividade de forma otimizada.
        Usa cache e early termination.
        
        Returns:
            bool: True se conexo, False caso contrário
        """
        # Usa cache se disponível
        if self._cache_conectividade is not None:
            return self._cache_conectividade
        
        if self.num_vertices <= 1:
            self._cache_conectividade = True
            return True
        
        # Escolhe vértice com maior grau para começar (heurística)
        vertice_inicial = max(self.vertices, 
                            key=lambda v: len(self.adj_set[v]))
        
        # Usa DFS otimizada
        fecho = self.dfs_fecho_transitivo_otimizado(vertice_inicial)
        
        # Cache do resultado
        resultado = len(fecho) == self.num_vertices
        self._cache_conectividade = resultado
        
        return resultado
    
    def eh_conexo_bfs(self):
        """
        Alternativa usando BFS (Breadth-First Search).
        Pode ser mais eficiente em alguns tipos de grafos.
        
        Returns:
            bool: True se conexo, False caso contrário
        """
        if self.num_vertices <= 1:
            return True
        
        # Escolhe qualquer vértice
        vertice_inicial = next(iter(self.vertices))
        
        visitados = set()
        fila = deque([vertice_inicial])
        
        while fila:
            vertice_atual = fila.popleft()
            
            if vertice_atual not in visitados:
                visitados.add(vertice_atual)
                
                # Early termination
                if len(visitados) == self.num_vertices:
                    return True
                
                # Adiciona vizinhos não visitados
                for vizinho in self.adj_set[vertice_atual]:
                    if vizinho not in visitados:
                        fila.append(vizinho)
        
        return len(visitados) == self.num_vertices
    
    def componentes_conexos(self):
        """
        Encontra todos os componentes conexos do grafo.
        Método adicional para análise mais detalhada.
        
        Returns:
            list: Lista de sets, cada um representando um componente conexo
        """
        visitados_global = set()
        componentes = []
        
        for vertice in self.vertices:
            if vertice not in visitados_global:
                # Encontra componente deste vértice
                componente = self.dfs_fecho_transitivo_otimizado(vertice)
                componentes.append(componente)
                visitados_global.update(componente)
        
        return componentes
    
    def estatisticas(self):
        """
        Retorna estatísticas do grafo.
        
        Returns:
            dict: Dicionário com estatísticas
        """
        num_arestas = sum(len(adj) for adj in self.adj_set.values()) // 2
        graus = [len(self.adj_set[v]) for v in self.vertices]
        
        return {
            'num_vertices': self.num_vertices,
            'num_arestas': num_arestas,
            'grau_medio': sum(graus) / len(graus) if graus else 0,
            'grau_maximo': max(graus) if graus else 0,
            'grau_minimo': min(graus) if graus else 0,
            'densidade': (2 * num_arestas) / (self.num_vertices * (self.num_vertices - 1)) if self.num_vertices > 1 else 0
        }
    
    def imprimir_grafo(self):
        """
        Imprime representação otimizada do grafo.
        """
        print("Lista de Adjacências (Sets):")
        for vertice in sorted(self.vertices):
            vizinhos = sorted(self.adj_set[vertice])
            print(f"{vertice}: {vizinhos}")


def benchmark_comparativo():
    """
    Compara o desempenho entre versões básica e otimizada.
    """
    print("=== BENCHMARK COMPARATIVO ===")
    
    # Cria grafo grande para teste de performance
    vertices_grandes = [f"v{i}" for i in range(1000)]
    arestas_grandes = [(f"v{i}", f"v{(i+1)%1000}") for i in range(1000)]  # Grafo circular
    
    # Teste versão otimizada
    start_time = time.time()
    grafo_otim = GrafoNaoOrientadoOtimizadoLLM(vertices_grandes)
    grafo_otim.construir_grafo(arestas_grandes)
    resultado_otim = grafo_otim.eh_conexo_otimizado()
    tempo_otim = time.time() - start_time
    
    print(f"Versão Otimizada:")
    print(f"  Tempo: {tempo_otim:.4f}s")
    print(f"  Resultado: {resultado_otim}")
    print(f"  Estatísticas: {grafo_otim.estatisticas()}")


def teste_exemplo_otimizado():
    """
    Testa a versão otimizada com o exemplo do enunciado.
    """
    print("=== TESTE OTIMIZADO COM EXEMPLO DO ENUNCIADO ===")
    
    vertices = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
    arestas = [
        ('x1', 'x2'), ('x2', 'x3'), ('x3', 'x1'),  # Componente 1
        ('x4', 'x5'), ('x5', 'x6'), ('x6', 'x4')   # Componente 2
    ]
    
    grafo = GrafoNaoOrientadoOtimizadoLLM(vertices)
    grafo.construir_grafo(arestas)
    
    print(f"Vértices: {sorted(vertices)}")
    print(f"Arestas: {arestas}")
    print()
    
    grafo.imprimir_grafo()
    print()
    
    # Testa conectividade com diferentes métodos
    print("Métodos de verificação:")
    eh_conexo_dfs = grafo.eh_conexo_otimizado()
    eh_conexo_bfs = grafo.eh_conexo_bfs()
    
    print(f"  DFS Otimizada: {eh_conexo_dfs}")
    print(f"  BFS: {eh_conexo_bfs}")
    print()
    
    # Mostra componentes conexos
    componentes = grafo.componentes_conexos()
    print(f"Componentes conexos encontrados: {len(componentes)}")
    for i, comp in enumerate(componentes, 1):
        print(f"  Componente {i}: {sorted(comp)}")
    print()
    
    # Estatísticas
    stats = grafo.estatisticas()
    print("Estatísticas do grafo:")
    for chave, valor in stats.items():
        print(f"  {chave}: {valor}")
    print()


def teste_casos_extremos():
    """
    Testa casos extremos para validar robustez.
    """
    print("=== TESTES DE CASOS EXTREMOS ===")
    
    # Grafo com um único vértice
    print("1. Grafo com um vértice:")
    grafo_um = GrafoNaoOrientadoOtimizadoLLM(['A'])
    print(f"   Conexo: {grafo_um.eh_conexo_otimizado()}")
    
    # Grafo vazio
    print("2. Grafo vazio:")
    grafo_vazio = GrafoNaoOrientadoOtimizadoLLM([])
    print(f"   Conexo: {grafo_vazio.eh_conexo_otimizado()}")
    
    # Grafo completo pequeno
    print("3. Grafo completo K4:")
    vertices_k4 = ['A', 'B', 'C', 'D']
    arestas_k4 = [('A', 'B'), ('A', 'C'), ('A', 'D'), 
                  ('B', 'C'), ('B', 'D'), ('C', 'D')]
    grafo_k4 = GrafoNaoOrientadoOtimizadoLLM(vertices_k4)
    grafo_k4.construir_grafo(arestas_k4)
    print(f"   Conexo: {grafo_k4.eh_conexo_otimizado()}")
    print(f"   Densidade: {grafo_k4.estatisticas()['densidade']:.2f}")
    
    print()


if __name__ == "__main__":
    print("VERIFICAÇÃO DE CONECTIVIDADE EM GRAFOS NÃO ORIENTADOS - VERSÃO OTIMIZADA (LLM)")
    print("=" * 60)
    print()
    # Executa testes
    teste_exemplo_otimizado()
    teste_casos_extremos()
    benchmark_comparativo()
    print("=" * 60)
    print("OTIMIZAÇÕES IMPLEMENTADAS (LLM):")
    print("- Uso de frozenset e defaultdict para eficiência")
    print("- Sets para adjacências (lookup O(1))")
    print("- Early termination na DFS")
    print("- Cache de resultados")
    print("- Heurística de escolha do vértice inicial")
    print("- Implementação alternativa com BFS")
    print("- Análise de componentes conexos")
    print("- Estruturas de dados otimizadas para memória")
