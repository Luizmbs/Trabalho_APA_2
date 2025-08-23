"""
Comparação entre Implementações Básica e Otimizada
APA 2 - Algoritmos e Programação Avançada

Este arquivo compara as duas implementações lado a lado,
demonstrando as diferenças de performance e funcionalidades.
"""

import time
import sys
import os

# Adiciona o diretório src ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from algorithms.basic_connectivity import GrafoBasico
from algorithms.optimized_connectivity import GrafoOtimizado


def comparar_implementacoes(vertices, arestas, nome_teste):
    """
    Compara as duas implementações com o mesmo conjunto de dados.
    
    Args:
        vertices (list): Lista de vértices
        arestas (list): Lista de arestas
        nome_teste (str): Nome do teste para identificação
    """
    print(f"=== {nome_teste.upper()} ===")
    print(f"Vértices: {len(vertices)}, Arestas: {len(arestas)}")
    print()
    
    # Teste implementação básica
    print("IMPLEMENTAÇÃO BÁSICA:")
    start_time = time.time()
    
    grafo_basico = GrafoBasico(vertices)
    grafo_basico.construir_grafo(arestas)
    resultado_basico = grafo_basico.eh_conexo()
    
    tempo_basico = time.time() - start_time
    
    print(f"  Resultado: {resultado_basico}")
    print(f"  Tempo de execução: {tempo_basico:.6f}s")
    
    # Mostra fecho transitivo do primeiro vértice (se existir)
    if vertices:
        primeiro_vertice = vertices[0]
        fecho_basico = grafo_basico.dfs_fecho_transitivo(primeiro_vertice)
        print(f"  Fecho de '{primeiro_vertice}': {len(fecho_basico)} vértices")
    
    print()
    
    # Teste implementação otimizada
    print("IMPLEMENTAÇÃO OTIMIZADA:")
    start_time = time.time()
    
    grafo_otimizado = GrafoOtimizado(vertices)
    grafo_otimizado.construir_grafo(arestas)
    resultado_otimizado = grafo_otimizado.eh_conexo_otimizado()
    
    tempo_otimizado = time.time() - start_time
    
    print(f"  Resultado: {resultado_otimizado}")
    print(f"  Tempo de execução: {tempo_otimizado:.6f}s")
    
    # Informações adicionais da versão otimizada
    if vertices:
        primeiro_vertice = vertices[0]
        fecho_otimizado = grafo_otimizado.dfs_fecho_transitivo_otimizado(primeiro_vertice)
        print(f"  Fecho de '{primeiro_vertice}': {len(fecho_otimizado)} vértices")
    
    componentes = grafo_otimizado.componentes_conexos()
    print(f"  Componentes conexos: {len(componentes)}")
    
    stats = grafo_otimizado.estatisticas()
    print(f"  Densidade do grafo: {stats['densidade']:.4f}")
    
    print()
    
    # Comparação de performance
    if tempo_basico > 0:
        speedup = tempo_basico / tempo_otimizado if tempo_otimizado > 0 else float('inf')
        print(f"COMPARAÇÃO DE PERFORMANCE:")
        print(f"  Speedup: {speedup:.2f}x")
        print(f"  Diferença: {((tempo_basico - tempo_otimizado) / tempo_basico * 100):.2f}%")
    
    # Validação de consistência
    if resultado_basico != resultado_otimizado:
        print("⚠️  ATENÇÃO: Resultados diferentes entre implementações!")
    else:
        print("✅ Resultados consistentes entre implementações")
    
    print("-" * 50)
    print()


def teste_exemplo_enunciado():
    """
    Testa com o exemplo fornecido no enunciado.
    """
    vertices = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
    arestas = [
        ('x1', 'x2'), ('x2', 'x3'), ('x3', 'x1'),  # Primeiro componente
        ('x4', 'x5'), ('x5', 'x6'), ('x6', 'x4')   # Segundo componente
    ]
    
    comparar_implementacoes(vertices, arestas, "Exemplo do Enunciado (Desconexo)")


def teste_grafo_conexo_pequeno():
    """
    Testa com um grafo conexo pequeno.
    """
    vertices = ['A', 'B', 'C', 'D', 'E']
    arestas = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A')]
    
    comparar_implementacoes(vertices, arestas, "Grafo Conexo Pequeno")


def teste_grafo_linear():
    """
    Testa com um grafo em forma de linha (pior caso para alguns algoritmos).
    """
    n = 20
    vertices = [f"v{i}" for i in range(n)]
    arestas = [(f"v{i}", f"v{i+1}") for i in range(n-1)]
    
    comparar_implementacoes(vertices, arestas, "Grafo Linear (Caminho)")


def teste_grafo_denso():
    """
    Testa com um grafo mais denso.
    """
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    # Grafo quase completo
    arestas = []
    for i, v1 in enumerate(vertices):
        for v2 in vertices[i+1:]:
            arestas.append((v1, v2))
    
    # Remove algumas arestas para não ser completo
    arestas = arestas[:-3]
    
    comparar_implementacoes(vertices, arestas, "Grafo Denso")


def teste_performance_grande():
    """
    Teste de performance com grafo maior.
    """
    print("=== TESTE DE PERFORMANCE COM GRAFO GRANDE ===")
    
    # Grafo circular grande
    n = 1000
    vertices = [f"v{i}" for i in range(n)]
    arestas = [(f"v{i}", f"v{(i+1)%n}") for i in range(n)]
    
    # Adiciona algumas conexões extras para tornar mais interessante
    for i in range(0, n, 10):
        arestas.append((f"v{i}", f"v{(i+5)%n}"))
    
    comparar_implementacoes(vertices, arestas, f"Grafo Circular Grande (n={n})")


def teste_multiplos_componentes():
    """
    Testa grafo com múltiplos componentes.
    """
    # Cria 4 componentes separados
    vertices = []
    arestas = []
    
    # Componente 1: triângulo
    comp1 = ['A1', 'A2', 'A3']
    vertices.extend(comp1)
    arestas.extend([('A1', 'A2'), ('A2', 'A3'), ('A3', 'A1')])
    
    # Componente 2: linha
    comp2 = ['B1', 'B2', 'B3', 'B4']
    vertices.extend(comp2)
    arestas.extend([('B1', 'B2'), ('B2', 'B3'), ('B3', 'B4')])
    
    # Componente 3: estrela
    comp3 = ['C1', 'C2', 'C3', 'C4', 'C5']
    vertices.extend(comp3)
    arestas.extend([('C1', 'C2'), ('C1', 'C3'), ('C1', 'C4'), ('C1', 'C5')])
    
    # Componente 4: vértice isolado
    comp4 = ['D1']
    vertices.extend(comp4)
    
    comparar_implementacoes(vertices, arestas, "Múltiplos Componentes")


def analise_detalhada_otimizacoes():
    """
    Análise detalhada das otimizações implementadas.
    """
    print("=== ANÁLISE DETALHADA DAS OTIMIZAÇÕES ===")
    print()
    
    print("1. ESTRUTURAS DE DADOS:")
    print("   Básica: list para adjacências, set para vértices")
    print("   Otimizada: set para adjacências (O(1) lookup), frozenset para vértices")
    print()
    
    print("2. ALGORITMO DE BUSCA:")
    print("   Básica: DFS simples com pilha")
    print("   Otimizada: DFS com early termination + alternativa BFS")
    print()
    
    print("3. OTIMIZAÇÕES DE MEMÓRIA:")
    print("   Básica: Estruturas padrão do Python")
    print("   Otimizada: defaultdict, cache de resultados, frozenset")
    print()
    
    print("4. FUNCIONALIDADES ADICIONAIS:")
    print("   Básica: Apenas verificação de conectividade")
    print("   Otimizada: Componentes, estatísticas, múltiplos algoritmos")
    print()
    
    print("5. HEURÍSTICAS:")
    print("   Básica: Escolha arbitrária do vértice inicial")
    print("   Otimizada: Escolha do vértice com maior grau")
    print()


def main():
    """
    Função principal que executa todos os testes comparativos.
    """
    print("COMPARAÇÃO: IMPLEMENTAÇÃO BÁSICA vs OTIMIZADA")
    print("=" * 70)
    print()
    
    # Executa todos os testes
    teste_exemplo_enunciado()
    teste_grafo_conexo_pequeno()
    teste_grafo_linear()
    teste_grafo_denso()
    teste_multiplos_componentes()
    
    # Teste de performance (opcional - pode ser lento)
    resposta = input("Executar teste de performance com grafo grande? (s/n): ")
    if resposta.lower() == 's':
        teste_performance_grande()
    
    # Análise das otimizações
    analise_detalhada_otimizacoes()
    
    print("=" * 70)
    print("CONCLUSÕES:")
    print("- A versão otimizada mantém a mesma complexidade O(V + E)")
    print("- Melhora significativa em casos práticos devido às otimizações")
    print("- Estruturas de dados mais eficientes reduzem overhead")
    print("- Early termination reduz trabalho desnecessário")
    print("- Funcionalidades adicionais facilitam análise e debugging")


if __name__ == "__main__":
    main()
