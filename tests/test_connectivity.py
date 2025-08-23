"""
Testes Unitários para Verificação de Conectividade em Grafos
APA 2 - Algoritmos e Programação Avançada

Este arquivo contém testes unitários para validar ambas as implementações.
"""

import unittest
import sys
import os

# Adiciona o diretório src ao path para importar os módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from algorithms.basic_connectivity import GrafoBasico
from algorithms.optimized_connectivity import GrafoOtimizado


class TestGrafoBasico(unittest.TestCase):
    """
    Testes para a implementação básica.
    """
    
    def setUp(self):
        """
        Configuração inicial para os testes.
        """
        self.vertices_exemplo = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
        self.arestas_exemplo = [
            ('x1', 'x2'), ('x2', 'x3'), ('x3', 'x1'),  # Componente 1
            ('x4', 'x5'), ('x5', 'x6'), ('x6', 'x4')   # Componente 2
        ]
    
    def test_grafo_vazio(self):
        """
        Testa grafo vazio.
        """
        grafo = GrafoBasico([])
        self.assertTrue(grafo.eh_conexo())
    
    def test_grafo_um_vertice(self):
        """
        Testa grafo com um único vértice.
        """
        grafo = GrafoBasico(['A'])
        self.assertTrue(grafo.eh_conexo())
    
    def test_exemplo_enunciado(self):
        """
        Testa o exemplo fornecido no enunciado (deve ser desconexo).
        """
        grafo = GrafoBasico(self.vertices_exemplo)
        grafo.construir_grafo(self.arestas_exemplo)
        self.assertFalse(grafo.eh_conexo())
    
    def test_grafo_conexo_simples(self):
        """
        Testa um grafo conexo simples.
        """
        vertices = ['A', 'B', 'C']
        arestas = [('A', 'B'), ('B', 'C')]
        grafo = GrafoBasico(vertices)
        grafo.construir_grafo(arestas)
        self.assertTrue(grafo.eh_conexo())
    
    def test_grafo_completo(self):
        """
        Testa um grafo completo K4.
        """
        vertices = ['A', 'B', 'C', 'D']
        arestas = [('A', 'B'), ('A', 'C'), ('A', 'D'), 
                   ('B', 'C'), ('B', 'D'), ('C', 'D')]
        grafo = GrafoBasico(vertices)
        grafo.construir_grafo(arestas)
        self.assertTrue(grafo.eh_conexo())
    
    def test_fecho_transitivo(self):
        """
        Testa o cálculo do fecho transitivo.
        """
        grafo = GrafoBasico(self.vertices_exemplo)
        grafo.construir_grafo(self.arestas_exemplo)
        
        # Fecho de x1 deve incluir apenas {x1, x2, x3}
        fecho_x1 = grafo.dfs_fecho_transitivo('x1')
        self.assertEqual(fecho_x1, {'x1', 'x2', 'x3'})
        
        # Fecho de x4 deve incluir apenas {x4, x5, x6}
        fecho_x4 = grafo.dfs_fecho_transitivo('x4')
        self.assertEqual(fecho_x4, {'x4', 'x5', 'x6'})
    
    def test_adicionar_aresta_invalida(self):
        """
        Testa adição de aresta com vértice inexistente.
        """
        grafo = GrafoBasico(['A', 'B'])
        with self.assertRaises(ValueError):
            grafo.adicionar_aresta('A', 'C')  # C não existe
    
    def test_grafo_linear(self):
        """
        Testa grafo em forma de linha.
        """
        vertices = ['1', '2', '3', '4', '5']
        arestas = [('1', '2'), ('2', '3'), ('3', '4'), ('4', '5')]
        grafo = GrafoBasico(vertices)
        grafo.construir_grafo(arestas)
        self.assertTrue(grafo.eh_conexo())


class TestGrafoOtimizado(unittest.TestCase):
    """
    Testes para a implementação otimizada.
    """
    
    def setUp(self):
        """
        Configuração inicial para os testes.
        """
        self.vertices_exemplo = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
        self.arestas_exemplo = [
            ('x1', 'x2'), ('x2', 'x3'), ('x3', 'x1'),  # Componente 1
            ('x4', 'x5'), ('x5', 'x6'), ('x6', 'x4')   # Componente 2
        ]
    
    def test_grafo_vazio(self):
        """
        Testa grafo vazio.
        """
        grafo = GrafoOtimizado([])
        self.assertTrue(grafo.eh_conexo_otimizado())
    
    def test_grafo_um_vertice(self):
        """
        Testa grafo com um único vértice.
        """
        grafo = GrafoOtimizado(['A'])
        self.assertTrue(grafo.eh_conexo_otimizado())
    
    def test_exemplo_enunciado(self):
        """
        Testa o exemplo fornecido no enunciado.
        """
        grafo = GrafoOtimizado(self.vertices_exemplo)
        grafo.construir_grafo(self.arestas_exemplo)
        self.assertFalse(grafo.eh_conexo_otimizado())
    
    def test_comparacao_dfs_bfs(self):
        """
        Testa se DFS e BFS dão o mesmo resultado.
        """
        grafo = GrafoOtimizado(self.vertices_exemplo)
        grafo.construir_grafo(self.arestas_exemplo)
        
        resultado_dfs = grafo.eh_conexo_otimizado()
        resultado_bfs = grafo.eh_conexo_bfs()
        
        self.assertEqual(resultado_dfs, resultado_bfs)
    
    def test_componentes_conexos(self):
        """
        Testa identificação de componentes conexos.
        """
        grafo = GrafoOtimizado(self.vertices_exemplo)
        grafo.construir_grafo(self.arestas_exemplo)
        
        componentes = grafo.componentes_conexos()
        self.assertEqual(len(componentes), 2)  # Dois componentes
        
        # Verifica se os componentes estão corretos
        comp_sizes = sorted([len(comp) for comp in componentes])
        self.assertEqual(comp_sizes, [3, 3])  # Ambos têm 3 vértices
    
    def test_cache_funcionamento(self):
        """
        Testa se o cache está funcionando corretamente.
        """
        grafo = GrafoOtimizado(['A', 'B'])
        grafo.adicionar_aresta('A', 'B')
        
        # Primeira chamada
        resultado1 = grafo.eh_conexo_otimizado()
        
        # Segunda chamada (deve usar cache)
        resultado2 = grafo.eh_conexo_otimizado()
        
        self.assertEqual(resultado1, resultado2)
        
        # Adiciona nova aresta (deve invalidar cache)
        grafo.adicionar_aresta('B', 'A')  # Aresta redundante
        resultado3 = grafo.eh_conexo_otimizado()
        
        self.assertEqual(resultado1, resultado3)
    
    def test_estatisticas(self):
        """
        Testa cálculo de estatísticas do grafo.
        """
        vertices = ['A', 'B', 'C']
        arestas = [('A', 'B'), ('B', 'C'), ('C', 'A')]  # Triângulo
        
        grafo = GrafoOtimizado(vertices)
        grafo.construir_grafo(arestas)
        
        stats = grafo.estatisticas()
        
        self.assertEqual(stats['num_vertices'], 3)
        self.assertEqual(stats['num_arestas'], 3)
        self.assertEqual(stats['grau_medio'], 2.0)
        self.assertEqual(stats['grau_maximo'], 2)
        self.assertEqual(stats['grau_minimo'], 2)
        self.assertEqual(stats['densidade'], 1.0)  # Grafo completo
    
    def test_auto_loop_ignorado(self):
        """
        Testa se auto-loops são ignorados corretamente.
        """
        grafo = GrafoOtimizado(['A'])
        grafo.adicionar_aresta('A', 'A')  # Auto-loop
        
        # Não deve adicionar adjacência para si mesmo
        self.assertEqual(len(grafo.adj_set['A']), 0)
    
    def test_dfs_com_limite(self):
        """
        Testa DFS com limite de vértices.
        """
        vertices = ['A', 'B', 'C', 'D', 'E']
        arestas = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')]
        
        grafo = GrafoOtimizado(vertices)
        grafo.construir_grafo(arestas)
        
        # Limita a 3 vértices
        visitados = grafo.dfs_iterativa_com_limite('A', 3)
        self.assertLessEqual(len(visitados), 3)


class TestConsistencia(unittest.TestCase):
    """
    Testes para verificar consistência entre as duas implementações.
    """
    
    def test_consistencia_exemplo_enunciado(self):
        """
        Verifica se ambas implementações dão o mesmo resultado para o exemplo.
        """
        vertices = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
        arestas = [
            ('x1', 'x2'), ('x2', 'x3'), ('x3', 'x1'),
            ('x4', 'x5'), ('x5', 'x6'), ('x6', 'x4')
        ]
        
        grafo_basico = GrafoBasico(vertices)
        grafo_basico.construir_grafo(arestas)
        resultado_basico = grafo_basico.eh_conexo()
        
        grafo_otimizado = GrafoOtimizado(vertices)
        grafo_otimizado.construir_grafo(arestas)
        resultado_otimizado = grafo_otimizado.eh_conexo_otimizado()
        
        self.assertEqual(resultado_basico, resultado_otimizado)
    
    def test_consistencia_grafos_conexos(self):
        """
        Testa consistência em vários grafos conexos.
        """
        casos_teste = [
            # Caso 1: Linha
            (['A', 'B', 'C'], [('A', 'B'), ('B', 'C')]),
            # Caso 2: Triângulo
            (['1', '2', '3'], [('1', '2'), ('2', '3'), ('3', '1')]),
            # Caso 3: Estrela
            (['X', 'Y', 'Z', 'W'], [('X', 'Y'), ('X', 'Z'), ('X', 'W')]),
        ]
        
        for vertices, arestas in casos_teste:
            with self.subTest(vertices=vertices, arestas=arestas):
                grafo_basico = GrafoBasico(vertices)
                grafo_basico.construir_grafo(arestas)
                resultado_basico = grafo_basico.eh_conexo()
                
                grafo_otimizado = GrafoOtimizado(vertices)
                grafo_otimizado.construir_grafo(arestas)
                resultado_otimizado = grafo_otimizado.eh_conexo_otimizado()
                
                self.assertEqual(resultado_basico, resultado_otimizado)
    
    def test_consistencia_fechos_transitivos(self):
        """
        Verifica se os fechos transitivos são consistentes.
        """
        vertices = ['A', 'B', 'C', 'D']
        arestas = [('A', 'B'), ('C', 'D')]  # Dois componentes
        
        grafo_basico = GrafoBasico(vertices)
        grafo_basico.construir_grafo(arestas)
        fecho_basico = grafo_basico.dfs_fecho_transitivo('A')
        
        grafo_otimizado = GrafoOtimizado(vertices)
        grafo_otimizado.construir_grafo(arestas)
        fecho_otimizado = grafo_otimizado.dfs_fecho_transitivo_otimizado('A')
        
        self.assertEqual(fecho_basico, fecho_otimizado)


def executar_testes():
    """
    Executa todos os testes unitários.
    """
    # Cria suite de testes
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Adiciona testes das diferentes classes
    suite.addTests(loader.loadTestsFromTestCase(TestGrafoBasico))
    suite.addTests(loader.loadTestsFromTestCase(TestGrafoOtimizado))
    suite.addTests(loader.loadTestsFromTestCase(TestConsistencia))
    
    # Executa os testes
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Retorna se todos passaram
    return result.wasSuccessful()


if __name__ == "__main__":
    print("EXECUTANDO TESTES UNITÁRIOS")
    print("=" * 50)
    
    sucesso = executar_testes()
    
    print("\n" + "=" * 50)
    if sucesso:
        print("✅ TODOS OS TESTES PASSARAM!")
        print("As implementações estão funcionando corretamente.")
    else:
        print("❌ ALGUNS TESTES FALHARAM!")
        print("Verifique as implementações.")
    
    print("\nCobertura dos testes:")
    print("- Grafos vazios e com um vértice")
    print("- Exemplo do enunciado")
    print("- Grafos conexos e desconexos")
    print("- Casos extremos e validação de entrada")
    print("- Consistência entre implementações")
    print("- Funcionalidades específicas da versão otimizada")
