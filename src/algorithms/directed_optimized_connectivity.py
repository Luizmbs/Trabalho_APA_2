"""
Verificação de Conectividade em Grafos Orientados - Versão Otimizada
APA 2 - Algoritmos e Programação Avançada

Esta implementação otimizada segue os mesmos passos da versão básica:
1. Simetrizar o grafo adicionando arcos simétricos
2. Construir lista de sucessores
3. Computar fecho transitivo direto usando DFS otimizada
4. Verificar se fecho = X para determinar conectividade

Otimizações incluídas:
- Uso de sets para operações O(1)
- Early termination na DFS
- Estruturas de dados mais eficientes
- Cache de resultados
"""

from collections import defaultdict
import time


class GrafoOrientadoOtimizado:
    """
    Representação otimizada de um grafo orientado.
    Utiliza estruturas de dados eficientes e técnicas de otimização.
    """
    
    def __init__(self, vertices):
        """
        Inicializa o grafo orientado com um conjunto de vértices.
        
        Args:
            vertices (list): Lista de vértices do grafo
        """
        self.vertices = frozenset(vertices)  # frozenset é mais eficiente para conjuntos imutáveis
        self.num_vertices = len(vertices)
        
        # Arcos originais e sucessores usando sets para O(1) lookup
        self.arcos_originais = set()  # Set de arcos originais
        self.sucessores = defaultdict(set)  # defaultdict com sets para sucessores
        
        # Inicializa sucessores vazios
        for vertice in vertices:
            self.sucessores[vertice] = set()
        
        # Cache para resultados
        self._cache_conectividade = None
        self._cache_fecho = {}
    
    def adicionar_arco(self, origem, destino):
        """
        Adiciona um arco orientado ao grafo de forma otimizada.
        
        Args:
            origem: Vértice de origem
            destino: Vértice de destino
        """
        if origem not in self.vertices or destino not in self.vertices:
            raise ValueError(f"Vértice não encontrado: {origem} ou {destino}")
        
        # Evita arcos duplicados e auto-loops desnecessários
        if origem != destino:
            arco = (origem, destino)
            if arco not in self.arcos_originais:
                self.arcos_originais.add(arco)
                self.sucessores[origem].add(destino)
        
        # Invalida caches quando estrutura muda
        self._cache_conectividade = None
        self._cache_fecho.clear()
    
    def simetrizar_grafo_otimizado(self):
        """
        PASSO 1: Simetrizar o grafo de forma otimizada.
        Usa sets para operações eficientes.
        
        Returns:
            set: Conjunto de arcos simétricos adicionados
        """
        print("🚀 PASSO 1: Simetrizando o grafo (versão otimizada)...")
        
        arcos_simetricos = set()
        
        # Para cada arco original, adiciona o simétrico se não existir
        for origem, destino in self.arcos_originais.copy():  # copy() para evitar modificação durante iteração
            arco_simetrico = (destino, origem)
            
            if arco_simetrico not in self.arcos_originais:
                # Adiciona arco simétrico
                self.sucessores[destino].add(origem)
                arcos_simetricos.add(arco_simetrico)
        
        print(f"   📊 Arcos originais: {len(self.arcos_originais)}")
        print(f"   ➕ Arcos simétricos adicionados: {len(arcos_simetricos)}")
        
        # Atualiza conjunto de arcos originais com os simétricos
        self.arcos_originais.update(arcos_simetricos)
        
        print(f"   🔗 Total de arcos após simetrização: {len(self.arcos_originais)}")
        
        return arcos_simetricos
    
    def construir_lista_sucessores_otimizada(self, arestas_orientadas):
        """
        PASSO 2: Construir a lista de sucessores de forma otimizada.
        
        Args:
            arestas_orientadas (list): Lista de tuplas representando arcos orientados
        """
        print("🚀 PASSO 2: Construindo lista de sucessores (versão otimizada)...")
        
        # Inserção em lote para melhor performance
        for origem, destino in arestas_orientadas:
            self.adicionar_arco(origem, destino)
        
        # Simetriza o grafo
        arcos_simetricos = self.simetrizar_grafo_otimizado()
        
        print(f"   ✅ Lista de sucessores construída para {len(self.vertices)} vértices")
        
        return arcos_simetricos
    
    def dfs_fecho_transitivo_direto_otimizado(self, vertice_inicial):
        """
        PASSO 3: Calcula o fecho transitivo direto com otimizações.
        
        Otimizações:
        - Early termination quando atinge todos os vértices
        - Cache de resultados
        - Estruturas de dados eficientes
        
        Args:
            vertice_inicial: Vértice de onde iniciar a busca
            
        Returns:
            set: Conjunto de vértices alcançáveis
        """
        if vertice_inicial not in self.vertices:
            return set()
        
        # Verifica cache primeiro
        if vertice_inicial in self._cache_fecho:
            print(f"🚀 PASSO 3: Usando resultado em cache para '{vertice_inicial}'")
            return self._cache_fecho[vertice_inicial]
        
        print(f"🚀 PASSO 3: Computando fecho transitivo direto de '{vertice_inicial}' (otimizado)...")
        
        visitados = set()
        pilha = [vertice_inicial]
        
        while pilha:
            vertice_atual = pilha.pop()
            
            if vertice_atual not in visitados:
                visitados.add(vertice_atual)
                
                # Early termination: se já visitamos todos os vértices
                if len(visitados) == self.num_vertices:
                    print("   ⚡ Early termination: todos os vértices visitados!")
                    break
                
                # Adiciona sucessores não visitados (operação O(1) com sets)
                sucessores_nao_visitados = self.sucessores[vertice_atual] - visitados
                pilha.extend(sucessores_nao_visitados)
        
        # Armazena no cache
        self._cache_fecho[vertice_inicial] = visitados
        
        print(f"   📍 Vértices alcançáveis: {sorted(visitados)}")
        print(f"   📊 Tamanho do fecho: {len(visitados)}")
        
        return visitados
    
    def eh_conexo_otimizado(self, vertice_inicial=None):
        """
        PASSO 4: Verifica conectividade com otimizações.
        
        Args:
            vertice_inicial: Vértice para iniciar a busca (opcional)
            
        Returns:
            bool: True se conexo, False se desconexo
        """
        # Usa cache se disponível
        if self._cache_conectividade is not None:
            print("🚀 PASSO 4: Usando resultado de conectividade em cache")
            return self._cache_conectividade
        
        if self.num_vertices <= 1:
            self._cache_conectividade = True
            return True
        
        if vertice_inicial is None:
            # Heurística: escolhe vértice com maior número de sucessores
            vertice_inicial = max(self.vertices, 
                                key=lambda v: len(self.sucessores[v]))
            print(f"🚀 Heurística: escolhido vértice '{vertice_inicial}' (maior grau de saída)")
        
        print(f"🚀 PASSO 4: Verificando conectividade a partir de '{vertice_inicial}' (otimizado)...")
        
        # Calcula o fecho transitivo direto
        fecho = self.dfs_fecho_transitivo_direto_otimizado(vertice_inicial)
        
        # Verifica se fecho = X (todos os vértices)
        eh_conexo = len(fecho) == self.num_vertices
        
        # Cache do resultado
        self._cache_conectividade = eh_conexo
        
        print(f"   🎯 Conjunto X (todos os vértices): {len(self.vertices)} vértices")
        print(f"   📊 Tamanho do fecho: {len(fecho)}")
        print(f"   {'✅' if eh_conexo else '❌'} Fecho = X? {eh_conexo}")
        
        return eh_conexo
    
    def dfs_com_limite(self, vertice_inicial, limite=None):
        """
        DFS otimizada com limite de vértices.
        Útil para verificações parciais.
        
        Args:
            vertice_inicial: Vértice inicial
            limite: Número máximo de vértices a visitar
            
        Returns:
            set: Conjunto de vértices visitados
        """
        if limite is None:
            limite = self.num_vertices
        
        visitados = set()
        pilha = [vertice_inicial]
        
        while pilha and len(visitados) < limite:
            vertice_atual = pilha.pop()
            
            if vertice_atual not in visitados:
                visitados.add(vertice_atual)
                
                # Adiciona sucessores não visitados
                for sucessor in self.sucessores[vertice_atual]:
                    if sucessor not in visitados and len(visitados) < limite:
                        pilha.append(sucessor)
        
        return visitados
    
    def obter_vertices(self):
        """Retorna lista de vértices."""
        return list(self.vertices)
    
    def estatisticas_otimizadas(self):
        """
        Retorna estatísticas detalhadas do grafo orientado.
        
        Returns:
            dict: Dicionário com estatísticas
        """
        total_arcos = len(self.arcos_originais)
        graus_saida = [len(self.sucessores[v]) for v in self.vertices]
        
        # Calcula graus de entrada
        graus_entrada = {v: 0 for v in self.vertices}
        for sucessores_set in self.sucessores.values():
            for sucessor in sucessores_set:
                graus_entrada[sucessor] += 1
        
        graus_entrada_list = list(graus_entrada.values())
        
        return {
            'num_vertices': self.num_vertices,
            'num_arcos_originais': len([arco for arco in self.arcos_originais if arco[0] != arco[1]]) // 2,  # Conta apenas originais
            'num_arcos_total': total_arcos,
            'grau_saida_medio': sum(graus_saida) / len(graus_saida) if graus_saida else 0,
            'grau_saida_maximo': max(graus_saida) if graus_saida else 0,
            'grau_entrada_medio': sum(graus_entrada_list) / len(graus_entrada_list) if graus_entrada_list else 0,
            'grau_entrada_maximo': max(graus_entrada_list) if graus_entrada_list else 0,
            'densidade': total_arcos / (self.num_vertices * (self.num_vertices - 1)) if self.num_vertices > 1 else 0
        }
    
    def imprimir_grafo_otimizado(self):
        """
        Imprime representação otimizada do grafo orientado.
        """
        print("📋 REPRESENTAÇÃO DO GRAFO ORIENTADO OTIMIZADO (após simetrização):")
        print("Lista de Sucessores (Sets):")
        for vertice in sorted(self.vertices):
            sucessores = sorted(self.sucessores[vertice])
            print(f"  {vertice} → {sucessores}")
    
    def imprimir_estatisticas_detalhadas(self):
        """
        Imprime estatísticas detalhadas do grafo.
        """
        stats = self.estatisticas_otimizadas()
        
        print("\n📊 ESTATÍSTICAS DETALHADAS DO GRAFO ORIENTADO:")
        for chave, valor in stats.items():
            if isinstance(valor, float):
                print(f"   {chave}: {valor:.3f}")
            else:
                print(f"   {chave}: {valor}")


def benchmark_grafos_orientados():
    """
    Compara performance entre versões básica e otimizada para grafos orientados.
    """
    print("=" * 60)
    print("⚡ BENCHMARK - GRAFOS ORIENTADOS GRANDES")
    print("=" * 60)
    
    # Cria grafo orientado grande para teste
    vertices_grandes = [f"v{i}" for i in range(500)]
    arcos_grandes = [(f"v{i}", f"v{(i+1)%500}") for i in range(500)]  # Ciclo orientado
    
    # Adiciona mais conexões para tornar mais interessante
    arcos_grandes.extend([(f"v{i}", f"v{(i+250)%500}") for i in range(0, 500, 2)])
    
    print(f"🎯 Testando com {len(vertices_grandes)} vértices e {len(arcos_grandes)} arcos")
    
    # Teste versão otimizada
    start_time = time.time()
    grafo_otim = GrafoOrientadoOtimizado(vertices_grandes)
    grafo_otim.construir_lista_sucessores_otimizada(arcos_grandes)
    resultado_otim = grafo_otim.eh_conexo_otimizado()
    tempo_otim = time.time() - start_time
    
    print(f"\n🚀 Versão Otimizada:")
    print(f"  ⏱️  Tempo total: {tempo_otim:.4f}s")
    print(f"  🏆 Resultado: {'CONEXO' if resultado_otim else 'DESCONEXO'}")
    
    stats = grafo_otim.estatisticas_otimizadas()
    print(f"  📊 Arcos após simetrização: {stats['num_arcos_total']}")
    print(f"  📈 Densidade: {stats['densidade']:.3f}")


def teste_exemplo_orientado_otimizado():
    """
    Testa a versão otimizada com exemplos específicos.
    """
    print("=" * 60)
    print("🧪 TESTE - GRAFO ORIENTADO OTIMIZADO")
    print("=" * 60)
    
    vertices = ['P', 'Q', 'R', 'S']
    arcos = [('P', 'Q'), ('Q', 'R'), ('R', 'S'), ('S', 'P')]  # Ciclo orientado
    
    print(f"🎯 Vértices: {sorted(vertices)}")
    print(f"🔗 Arcos orientados: {arcos}")
    print()
    
    grafo = GrafoOrientadoOtimizado(vertices)
    grafo.construir_lista_sucessores_otimizada(arcos)
    print()
    
    grafo.imprimir_grafo_otimizado()
    print()
    
    # Testa conectividade
    eh_conexo = grafo.eh_conexo_otimizado()
    print()
    
    print("🏆 RESULTADO FINAL:")
    print(f"   O grafo orientado é {'CONEXO' if eh_conexo else 'DESCONEXO'}")
    
    grafo.imprimir_estatisticas_detalhadas()
    print()


if __name__ == "__main__":
    print("VERIFICAÇÃO DE CONECTIVIDADE EM GRAFOS ORIENTADOS - VERSÃO OTIMIZADA")
    print("=" * 75)
    print()
    print("ALGORITMO OTIMIZADO PARA GRAFOS ORIENTADOS:")
    print("1. Simetrizar o grafo (com sets e otimizações)")
    print("2. Construir lista de sucessores (defaultdict + sets)")
    print("3. Computar fecho transitivo direto (DFS com early termination)")
    print("4. Verificar conectividade (com cache e heurísticas)")
    print()
    
    # Executa testes
    teste_exemplo_orientado_otimizado()
    benchmark_grafos_orientados()
    
    print("=" * 75)
    print("✅ OTIMIZAÇÕES IMPLEMENTADAS:")
    print("   • Sets para operações O(1)")
    print("   • Early termination na DFS")  
    print("   • Cache de resultados")
    print("   • Heurística para escolha do vértice inicial")
    print("   • Estruturas de dados eficientes (frozenset, defaultdict)")
