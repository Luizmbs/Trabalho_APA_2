#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste das funcionalidades de impressão de listas
Demonstra tanto listas de adjacências quanto listas de sucessores
"""

import os
import sys

# Adiciona o diretório src ao path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from algorithms.basic_connectivity import GrafoBasico
from algorithms.optimized_connectivity import GrafoOtimizado
from algorithms.directed_basic_connectivity import GrafoOrientadoBasico
from algorithms.directed_optimized_connectivity import GrafoOrientadoOtimizado

def teste_grafo_nao_orientado():
    """Testa impressão de lista de adjacências para grafo não orientado"""
    print("="*60)
    print("TESTE: GRAFO NÃO ORIENTADO - LISTA DE ADJACÊNCIAS")
    print("="*60)
    
    # Dados do exemplo
    vertices = ['A', 'B', 'C', 'D', 'E']
    arestas = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A')]
    
    # Criar grafo
    grafo = GrafoBasico(vertices)
    for v1, v2 in arestas:
        grafo.adicionar_aresta(v1, v2)
    
    # Imprimir lista de adjacências
    print(f"📋 LISTA DE ADJACÊNCIAS:")
    print("-" * 30)
    for vertice in sorted(vertices):
        adjacentes = sorted(grafo.adj_list.get(vertice, []))
        print(f"   {vertice}: {adjacentes}")
    
    return grafo

def teste_grafo_orientado():
    """Testa impressão de lista de sucessores para grafo orientado"""
    print("\n" + "="*60)
    print("TESTE: GRAFO ORIENTADO - LISTA DE SUCESSORES")
    print("="*60)
    
    # Dados do exemplo
    vertices = ['A', 'B', 'C']
    arestas = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    
    # Criar grafo orientado
    grafo = GrafoOrientadoBasico(vertices)
    grafo.construir_lista_sucessores(arestas)
    
    # Imprimir lista de sucessores
    print(f"📋 LISTA DE SUCESSORES APÓS SIMETRIZAÇÃO:")
    print("-" * 30)
    for vertice in sorted(vertices):
        sucessores = sorted(grafo.sucessores.get(vertice, []))
        print(f"   {vertice}: {sucessores}")
    
    return grafo

def teste_fecho_transitivo():
    """Teste de fecho transitivo para mostrar como funciona"""
    print("\n" + "="*60)
    print("TESTE: CÁLCULO DO FECHO TRANSITIVO")
    print("="*60)
    
    # Grafo não orientado
    print("\n🔹 GRAFO NÃO ORIENTADO - Fecho transitivo de 'A':")
    grafo_nao_orientado = teste_grafo_nao_orientado()
    fecho = grafo_nao_orientado.dfs_fecho_transitivo('A')
    print(f"   Fecho de A: {sorted(fecho)}")
    
    # Grafo orientado
    print("\n🔹 GRAFO ORIENTADO - Fecho transitivo direto de 'A':")
    grafo_orientado = teste_grafo_orientado()
    fecho_direto = grafo_orientado.dfs_fecho_transitivo_direto('A')
    print(f"   Fecho direto de A: {sorted(fecho_direto)}")

def main():
    """Função principal do teste"""
    print("🧪 TESTE DAS LISTAS DE ADJACÊNCIAS E SUCESSORES")
    print("="*60)
    
    try:
        # Teste individual de cada tipo
        grafo_nao_orientado = teste_grafo_nao_orientado()
        grafo_orientado = teste_grafo_orientado()
        
        # Teste de fecho transitivo
        teste_fecho_transitivo()
        
        print("\n" + "="*60)
        print("✅ TODOS OS TESTES EXECUTADOS COM SUCESSO!")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ ERRO NO TESTE: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
