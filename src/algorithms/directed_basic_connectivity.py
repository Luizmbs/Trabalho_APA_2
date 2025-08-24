"""
Verificação de Conectividade em Grafos Orientados - Versão Básica
APA 2 - Algoritmos e Programação Avançada

Esta implementação segue os passos específicos para grafos orientados:
1. Simetrizar o grafo adicionando arcos simétricos
2. Construir lista de sucessores
3. Computar fecho transitivo direto usando DFS
4. Verificar se fecho = X (todos os vértices) para determinar conectividade
"""

class GrafoOrientadoBasico:
    """
    Representação básica de um grafo orientado.
    Implementa simetrização e fecho transitivo direto.
    """
    
    def __init__(self, vertices):
        """
        Inicializa o grafo orientado com um conjunto de vértices.
        
        Args:
            vertices (list): Lista de vértices do grafo
        """
        self.vertices = set(vertices)  # Conjunto X de vértices
        self.arcos_originais = []  # Arcos do grafo orientado original
        self.sucessores = {}  # Lista de sucessores (após simetrização)
        
        # Inicializa lista de sucessores vazia para cada vértice
        for vertice in vertices:
            self.sucessores[vertice] = []
    
    def adicionar_arco(self, origem, destino):
        """
        Adiciona um arco orientado ao grafo.
        
        Args:
            origem: Vértice de origem
            destino: Vértice de destino
        """
        if origem in self.vertices and destino in self.vertices:
            # Armazena arco original
            if (origem, destino) not in self.arcos_originais:
                self.arcos_originais.append((origem, destino))
            
            # Adiciona à lista de sucessores (ainda não simetrizado)
            if destino not in self.sucessores[origem]:
                self.sucessores[origem].append(destino)
        else:
            raise ValueError(f"Vértice não encontrado: {origem} ou {destino}")
    
    def simetrizar_grafo(self):
        """
        PASSO 1: Simetrizar o grafo adicionando todos os arcos simétricos.
        Para cada arco (u,v), adiciona o arco simétrico (v,u).
        """
        print("🔄 PASSO 1: Simetrizando o grafo...")
        
        arcos_simetricos_adicionados = []
        
        # Para cada arco original, adiciona o arco simétrico
        for origem, destino in self.arcos_originais:
            # Verifica se o arco simétrico já existe
            arco_simetrico = (destino, origem)
            if arco_simetrico not in self.arcos_originais:
                # Adiciona o arco simétrico
                if origem not in self.sucessores[destino]:
                    self.sucessores[destino].append(origem)
                    arcos_simetricos_adicionados.append(arco_simetrico)
        
        print(f"   📊 Arcos originais: {len(self.arcos_originais)}")
        print(f"   ➕ Arcos simétricos adicionados: {len(arcos_simetricos_adicionados)}")
        print(f"   🔗 Total de arcos após simetrização: {len(self.arcos_originais) + len(arcos_simetricos_adicionados)}")
        
        return arcos_simetricos_adicionados
    
    def construir_lista_sucessores(self, arestas_orientadas):
        """
        PASSO 2: Construir a lista de sucessores a partir dos dados de entrada.
        
        Args:
            arestas_orientadas (list): Lista de tuplas representando arcos orientados
        """
        print("🔄 PASSO 2: Construindo lista de sucessores...")
        
        for origem, destino in arestas_orientadas:
            self.adicionar_arco(origem, destino)
        
        # Após adicionar todos os arcos, simetriza o grafo
        arcos_simetricos = self.simetrizar_grafo()
        
        print(f"   ✅ Lista de sucessores construída para {len(self.vertices)} vértices")
        
        return arcos_simetricos
    
    def dfs_fecho_transitivo_direto(self, vertice_inicial):
        """
        PASSO 3: Calcula o fecho transitivo direto usando DFS.
        Não visita os arcos, apenas os vértices.
        
        Args:
            vertice_inicial: Vértice de onde iniciar a busca
            
        Returns:
            set: Conjunto de vértices alcançáveis (fecho transitivo direto)
        """
        if vertice_inicial not in self.vertices:
            return set()
        
        print(f"🔄 PASSO 3: Computando fecho transitivo direto de '{vertice_inicial}'...")
        
        visitados = set()
        pilha = [vertice_inicial]
        
        while pilha:
            vertice_atual = pilha.pop()
            
            if vertice_atual not in visitados:
                visitados.add(vertice_atual)
                
                # Adiciona sucessores não visitados à pilha
                # (não visita os arcos, apenas navega pelos vértices)
                for sucessor in self.sucessores[vertice_atual]:
                    if sucessor not in visitados:
                        pilha.append(sucessor)
        
        print(f"   📍 Vértices alcançáveis: {sorted(visitados)}")
        print(f"   📊 Tamanho do fecho: {len(visitados)}")
        
        return visitados
    
    def eh_conexo(self, vertice_inicial=None):
        """
        PASSO 4: Verifica se o grafo é conexo.
        O grafo é conexo se o fecho transitivo = X (conjunto de todos os vértices).
        
        Args:
            vertice_inicial: Vértice para iniciar a busca (opcional)
            
        Returns:
            bool: True se conexo, False se desconexo
        """
        if not self.vertices:
            return True  # Grafo vazio é considerado conexo
        
        if vertice_inicial is None:
            # Escolhe qualquer vértice para iniciar
            vertice_inicial = next(iter(self.vertices))
        
        print(f"🔄 PASSO 4: Verificando conectividade a partir de '{vertice_inicial}'...")
        
        # Calcula o fecho transitivo direto
        fecho = self.dfs_fecho_transitivo_direto(vertice_inicial)
        
        # Verifica se fecho = X (todos os vértices)
        conjunto_X = self.vertices
        eh_conexo = fecho == conjunto_X
        
        print(f"   🎯 Conjunto X (todos os vértices): {sorted(conjunto_X)}")
        print(f"   📊 Tamanho de X: {len(conjunto_X)}")
        print(f"   📊 Tamanho do fecho: {len(fecho)}")
        print(f"   {'✅' if eh_conexo else '❌'} Fecho = X? {eh_conexo}")
        
        return eh_conexo
    
    def obter_vertices(self):
        """Retorna o conjunto de vértices."""
        return list(self.vertices)
    
    def imprimir_grafo(self):
        """
        Imprime a representação do grafo orientado simetrizado.
        """
        print("📋 REPRESENTAÇÃO DO GRAFO ORIENTADO (após simetrização):")
        print("Lista de Sucessores:")
        for vertice in sorted(self.vertices):
            sucessores = sorted(self.sucessores[vertice])
            print(f"  {vertice} → {sucessores}")
    
    def imprimir_estatisticas(self):
        """
        Imprime estatísticas detalhadas do grafo.
        """
        print("\n📊 ESTATÍSTICAS DO GRAFO ORIENTADO:")
        print(f"   🎯 Número de vértices: {len(self.vertices)}")
        print(f"   🔗 Arcos originais: {len(self.arcos_originais)}")
        
        total_sucessores = sum(len(self.sucessores[v]) for v in self.vertices)
        print(f"   ➕ Total de arcos após simetrização: {total_sucessores}")
        
        grau_medio = total_sucessores / len(self.vertices) if self.vertices else 0
        print(f"   📈 Grau médio (após simetrização): {grau_medio:.2f}")


def teste_exemplo_orientado():
    """
    Testa o algoritmo com um exemplo de grafo orientado.
    """
    print("=" * 60)
    print("🧪 TESTE - GRAFO ORIENTADO BÁSICO")
    print("=" * 60)
    
    # Exemplo de grafo orientado
    vertices = ['A', 'B', 'C', 'D']
    arcos = [('A', 'B'), ('B', 'C'), ('C', 'D')]  # Grafo linear orientado
    
    print(f"🎯 Vértices: {sorted(vertices)}")
    print(f"🔗 Arcos orientados: {arcos}")
    print()
    
    grafo = GrafoOrientadoBasico(vertices)
    
    # Executa os 4 passos do algoritmo
    grafo.construir_lista_sucessores(arcos)
    print()
    
    grafo.imprimir_grafo()
    print()
    
    # Testa conectividade
    eh_conexo = grafo.eh_conexo('A')
    print()
    
    print("🏆 RESULTADO FINAL:")
    print(f"   O grafo orientado é {'CONEXO' if eh_conexo else 'DESCONEXO'}")
    
    grafo.imprimir_estatisticas()
    print()


def teste_grafo_orientado_conexo():
    """
    Testa com um grafo orientado que se torna conexo após simetrização.
    """
    print("=" * 60)
    print("🧪 TESTE - GRAFO ORIENTADO QUE SE TORNA CONEXO")
    print("=" * 60)
    
    vertices = ['X', 'Y', 'Z']
    arcos = [('X', 'Y'), ('Y', 'Z'), ('Z', 'X')]  # Ciclo orientado
    
    print(f"🎯 Vértices: {sorted(vertices)}")
    print(f"🔗 Arcos orientados: {arcos}")
    print()
    
    grafo = GrafoOrientadoBasico(vertices)
    grafo.construir_lista_sucessores(arcos)
    print()
    
    grafo.imprimir_grafo()
    print()
    
    eh_conexo = grafo.eh_conexo('X')
    print()
    
    print("🏆 RESULTADO FINAL:")
    print(f"   O grafo orientado é {'CONEXO' if eh_conexo else 'DESCONEXO'}")
    
    grafo.imprimir_estatisticas()
    print()


if __name__ == "__main__":
    print("VERIFICAÇÃO DE CONECTIVIDADE EM GRAFOS ORIENTADOS - VERSÃO BÁSICA")
    print("=" * 70)
    print()
    print("ALGORITMO PARA GRAFOS ORIENTADOS:")
    print("1. Simetrizar o grafo (adicionar arcos simétricos)")
    print("2. Construir lista de sucessores")
    print("3. Computar fecho transitivo direto usando DFS")
    print("4. Verificar se fecho = X para determinar conectividade")
    print()
    
    # Executa testes
    teste_exemplo_orientado()
    teste_grafo_orientado_conexo()
    
    print("=" * 70)
    print("✅ PASSOS DO ALGORITMO IMPLEMENTADOS CONFORME ESPECIFICAÇÃO")
