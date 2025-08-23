"""
Verificação de Conectividade em Grafos Orientados - Versão Otimizada (LLM)
APA 2 - Algoritmos e Programação Avançada

Implementação otimizada para grafos orientados, incluindo:
- Simetrização eficiente dos arcos
- Uso de sets para operações rápidas
- DFS iterativa otimizada
- Verificação de conectividade
"""

class GrafoOrientadoOtimizado:
    """
    Grafo orientado otimizado com simetrização e verificação de conectividade.
    """
    def __init__(self, vertices, arcos):
        self.vertices = set(vertices)
        self.arcos = set(arcos)
        self.arcos_simetrizados = self._simetrizar_grafo()
        self.lista_sucessores = self._construir_lista_sucessores()

    def _simetrizar_grafo(self):
        arcos_sim = set(self.arcos)
        for u, v in self.arcos:
            arcos_sim.add((v, u))
        return arcos_sim

    def _construir_lista_sucessores(self):
        lista = {v: set() for v in self.vertices}
        for u, v in self.arcos_simetrizados:
            lista[u].add(v)
        return lista

    def dfs_fecho_transitivo_otimizado(self, vertice_inicial):
        visitados = set()
        pilha = [vertice_inicial]
        while pilha:
            atual = pilha.pop()
            if atual not in visitados:
                visitados.add(atual)
                # Early termination
                if len(visitados) == len(self.vertices):
                    break
                for vizinho in self.lista_sucessores[atual]:
                    if vizinho not in visitados:
                        pilha.append(vizinho)
        return visitados

    def eh_conexo_otimizado(self):
        if not self.vertices:
            return True
        vertice_inicial = max(self.vertices, key=lambda v: len(self.lista_sucessores[v]))
        fecho = self.dfs_fecho_transitivo_otimizado(vertice_inicial)
        return fecho == self.vertices

    def imprimir_grafo(self):
        print("Lista de Sucessores (Orientado/Otimizado):")
        for vertice in sorted(self.vertices):
            vizinhos = sorted(self.lista_sucessores[vertice])
            print(f"{vertice}: {vizinhos}")


def teste_exemplo_orientado_otimizado():
    print("=== TESTE OTIMIZADO COM GRAFO ORIENTADO ===")
    vertices = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
    arcos = [
        ('x1', 'x2'), ('x2', 'x3'), ('x3', 'x1'),
        ('x4', 'x5'), ('x5', 'x6'), ('x2', 'x4')
    ]
    grafo = GrafoOrientadoOtimizado(vertices, arcos)
    print(f"Vértices: {sorted(vertices)}")
    print(f"Arcos (originais): {arcos}")
    print(f"Arcos (simetrizados): {sorted(grafo.arcos_simetrizados)}")
    print()
    grafo.imprimir_grafo()
    print()
    eh_conexo = grafo.eh_conexo_otimizado()
    print(f"O grafo orientado é conexo? {eh_conexo}")
    fecho = grafo.dfs_fecho_transitivo_otimizado(vertices[0])
    print(f"Fecho transitivo de {vertices[0]}: {sorted(fecho)}")
    print()


if __name__ == "__main__":
    print("VERIFICAÇÃO DE CONECTIVIDADE EM GRAFOS ORIENTADOS - VERSÃO OTIMIZADA (LLM)")
    print("=" * 60)
    print()
    teste_exemplo_orientado_otimizado()
    print("=" * 60)
    print("Complexidade de Tempo: O(V + E)")
    print("Complexidade de Espaço: O(V)")
    print("V = número de vértices, E = número de arcos")
