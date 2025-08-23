"""
Módulo de algoritmos para verificação de conectividade em grafos.

Este módulo contém implementações básicas e otimizadas para verificar
se um grafo é conexo usando algoritmos de busca em profundidade (DFS).
"""

from .basic_connectivity import GrafoBasico
from .optimized_connectivity_llm import GrafoOtimizado

__version__ = "1.0.0"
__author__ = "APA 2 - Trabalho de Algoritmos"

__all__ = [
    'GrafoBasico',
    'GrafoOtimizado'
]
