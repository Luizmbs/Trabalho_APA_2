import unittest
from src.algorithms.directed_basic_connectivity import GrafoOrientadoBasico
from src.algorithms.directed_optimized_connectivity import GrafoOrientadoOtimizado

class TestGrafoOrientado(unittest.TestCase):
    """Testes para algoritmos de grafos orientados."""
    
    def test_algoritmo_4_passos_basico(self):
        """Testa o algoritmo completo de 4 passos - versão básica."""
        vertices = ['A', 'B', 'C']
        grafo = GrafoOrientadoBasico(vertices)
        grafo.adicionar_arco('A', 'B')
        grafo.adicionar_arco('B', 'C')
        grafo.adicionar_arco('C', 'A')  # Ciclo completo
        
        # Deve ser conexo
        eh_conexo = grafo.eh_conexo('A')
        self.assertTrue(eh_conexo)
        
        # Teste com grafo desconexo
        vertices2 = ['A', 'B', 'C', 'D']
        grafo2 = GrafoOrientadoBasico(vertices2)
        grafo2.adicionar_arco('A', 'B')
        grafo2.adicionar_arco('C', 'D')
        
        # Não deve ser conexo
        eh_conexo2 = grafo2.eh_conexo('A')
        self.assertFalse(eh_conexo2)
    
    def test_algoritmo_4_passos_otimizado(self):
        """Testa o algoritmo completo de 4 passos - versão otimizada."""
        vertices = ['A', 'B', 'C']
        grafo = GrafoOrientadoOtimizado(vertices)
        grafo.adicionar_arco('A', 'B')
        grafo.adicionar_arco('B', 'C')
        grafo.adicionar_arco('C', 'A')  # Ciclo completo
        
        # Deve ser conexo
        eh_conexo = grafo.eh_conexo_otimizado('A')
        self.assertTrue(eh_conexo)
        
        # Teste com grafo desconexo
        vertices2 = ['A', 'B', 'C', 'D']
        grafo2 = GrafoOrientadoOtimizado(vertices2)
        grafo2.adicionar_arco('A', 'B')
        grafo2.adicionar_arco('C', 'D')
        
        # Não deve ser conexo
        eh_conexo2 = grafo2.eh_conexo_otimizado('A')
        self.assertFalse(eh_conexo2)
    
    def test_consistencia_algoritmos(self):
        """Testa consistência entre algoritmos básico e otimizado."""
        # Cenário 1: Grafo conexo
        vertices = ['A', 'B', 'C', 'D']
        
        grafo_basico = GrafoOrientadoBasico(vertices)
        grafo_basico.adicionar_arco('A', 'B')
        grafo_basico.adicionar_arco('B', 'C')
        grafo_basico.adicionar_arco('C', 'D')
        grafo_basico.adicionar_arco('D', 'A')  # Forma um ciclo
        
        grafo_otimizado = GrafoOrientadoOtimizado(vertices)
        grafo_otimizado.adicionar_arco('A', 'B')
        grafo_otimizado.adicionar_arco('B', 'C')
        grafo_otimizado.adicionar_arco('C', 'D')
        grafo_otimizado.adicionar_arco('D', 'A')  # Forma um ciclo
        
        # Ambos devem dar o mesmo resultado para conectividade
        for vertice in vertices:
            conexo_basico = grafo_basico.eh_conexo(vertice)
            conexo_otimizado = grafo_otimizado.eh_conexo_otimizado(vertice)
            self.assertEqual(conexo_basico, conexo_otimizado, 
                           f"Inconsistência para vértice {vertice}")
    
    def test_grafo_desconexo(self):
        """Testa detecção de grafo desconexo."""
        vertices = ['A', 'B', 'C', 'D', 'E']
        
        # Dois componentes separados: A-B-C e D-E
        grafo_basico = GrafoOrientadoBasico(vertices)
        grafo_basico.adicionar_arco('A', 'B')
        grafo_basico.adicionar_arco('B', 'C')
        grafo_basico.adicionar_arco('C', 'A')  # Ciclo A-B-C
        grafo_basico.adicionar_arco('D', 'E')  # Componente separado
        
        grafo_otimizado = GrafoOrientadoOtimizado(vertices)
        grafo_otimizado.adicionar_arco('A', 'B')
        grafo_otimizado.adicionar_arco('B', 'C')
        grafo_otimizado.adicionar_arco('C', 'A')
        grafo_otimizado.adicionar_arco('D', 'E')
        
        # A conecta ao componente A-B-C, mas não a D-E
        conexo_basico_A = grafo_basico.eh_conexo('A')
        conexo_otimizado_A = grafo_otimizado.eh_conexo_otimizado('A')
        
        self.assertEqual(conexo_basico_A, conexo_otimizado_A)
        self.assertFalse(conexo_basico_A)  # Não conecta todo o grafo
        
        # D também não conecta todo o grafo
        conexo_basico_D = grafo_basico.eh_conexo('D')
        conexo_otimizado_D = grafo_otimizado.eh_conexo_otimizado('D')
        
        self.assertEqual(conexo_basico_D, conexo_otimizado_D)
        self.assertFalse(conexo_basico_D)
    
    def test_grafo_trivial(self):
        """Testa casos triviais."""
        # Grafo com um vértice
        vertices = ['A']
        grafo_basico = GrafoOrientadoBasico(vertices)
        grafo_otimizado = GrafoOrientadoOtimizado(vertices)
        
        # Um vértice sozinho é "conexo" consigo mesmo
        self.assertTrue(grafo_basico.eh_conexo('A'))
        self.assertTrue(grafo_otimizado.eh_conexo_otimizado('A'))
        
        # Dois vértices sem arcos
        vertices2 = ['A', 'B']
        grafo_basico2 = GrafoOrientadoBasico(vertices2)
        grafo_otimizado2 = GrafoOrientadoOtimizado(vertices2)
        
        # Sem arcos, não é conexo
        self.assertFalse(grafo_basico2.eh_conexo('A'))
        self.assertFalse(grafo_otimizado2.eh_conexo_otimizado('A'))

if __name__ == '__main__':
    unittest.main()
