#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analisador de Conectividade de Grafos
Trabalho APA 2 - Algoritmos Básico e Otimizado
"""

import os
import sys
import re
import time
from pathlib import Path

# Adiciona o diretório src ao path para imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from algorithms.basic_connectivity import GrafoBasico
from algorithms.optimized_connectivity import GrafoOtimizado
from algorithms.directed_basic_connectivity import GrafoOrientadoBasico
from algorithms.directed_optimized_connectivity import GrafoOrientadoOtimizado


class GrafoReader:
    """Classe para leitura e processamento de arquivos de grafo."""
    
    def __init__(self, caminho_exemplos="examples"):
        self.caminho_exemplos = Path(caminho_exemplos)
    
    def listar_arquivos(self):
        """Lista todos os arquivos .txt no diretório examples."""
        try:
            if not self.caminho_exemplos.exists():
                print(f"❌ Diretório '{self.caminho_exemplos}' não encontrado.")
                return []
            
            arquivos = list(self.caminho_exemplos.glob("*.txt"))
            return sorted([arquivo.name for arquivo in arquivos])
        
        except Exception as e:
            print(f"❌ Erro ao listar arquivos: {e}")
            return []
    
    def ler_arquivo(self, nome_arquivo):
        """Lê um arquivo e retorna suas linhas."""
        try:
            caminho = self.caminho_exemplos / nome_arquivo
            
            if not caminho.exists():
                raise FileNotFoundError(f"Arquivo '{nome_arquivo}' não encontrado")
            
            with open(caminho, 'r', encoding='utf-8') as arquivo:
                linhas = [linha.strip() for linha in arquivo.readlines()]
                linhas = [linha for linha in linhas if linha and not linha.startswith('#')]
            
            return linhas
        
        except Exception as e:
            print(f"❌ Erro ao ler arquivo '{nome_arquivo}': {e}")
            return None
    
    def _processar_arestas(self, linhas):
        """Processa as linhas e extrai as arestas."""
        arestas = []
        vertices = set()
        
        for linha in linhas:
            linha = linha.strip()
            if not linha or linha.startswith('#'):
                continue
            
            # Pula linhas que começam com VERTICES:
            if linha.startswith('VERTICES:'):
                continue
            
            # Se começa com ARESTAS:, processa múltiplas arestas na linha
            if linha.startswith('ARESTAS:'):
                linha = linha.replace('ARESTAS:', '').strip()
            
            # Procura múltiplas arestas no formato [x1,x2] na mesma linha
            padrao_multiplos = r'\[([^,]+),([^\]]+)\]'
            matches = re.findall(padrao_multiplos, linha)
            if matches:
                for v1, v2 in matches:
                    v1, v2 = v1.strip(), v2.strip()
                    arestas.append((v1, v2))
                    vertices.update([v1, v2])
                continue
            
            # Formato [x1,x2] único
            match = re.match(padrao_multiplos, linha)
            if match:
                v1 = match.group(1).strip()
                v2 = match.group(2).strip()
                arestas.append((v1, v2))
                vertices.update([v1, v2])
                continue
            
            # Formato A-B
            if '-' in linha and not linha.replace('-', '').replace(' ', '').isdigit():
                partes = linha.split('-', 1)
                if len(partes) == 2:
                    v1 = partes[0].strip()
                    v2 = partes[1].strip()
                    arestas.append((v1, v2))
                    vertices.update([v1, v2])
                    continue
            
            # Formato 1,2
            if ',' in linha:
                partes = linha.split(',', 1)
                if len(partes) == 2:
                    v1 = partes[0].strip()
                    v2 = partes[1].strip()
                    arestas.append((v1, v2))
                    vertices.update([v1, v2])
                    continue
            
            # Formato espaço separado
            partes = linha.split()
            if len(partes) == 2:
                v1, v2 = partes
                arestas.append((v1, v2))
                vertices.update([v1, v2])
                continue
            
            print(f"⚠️  Linha ignorada: {linha}")
        
        return arestas, vertices
    
    def processar_arquivo(self, nome_arquivo):
        """Processa um arquivo e retorna as arestas e vértices."""
        linhas = self.ler_arquivo(nome_arquivo)
        if linhas is None:
            return None, None
        
        if not linhas:
            print(f"❌ Arquivo '{nome_arquivo}' está vazio.")
            return None, None
        
        try:
            arestas, vertices = self._processar_arestas(linhas)
            
            if not arestas:
                print(f"❌ Nenhuma aresta válida encontrada em '{nome_arquivo}'.")
                return None, None
            
            print(f"✅ Processado '{nome_arquivo}': {len(arestas)} arestas, {len(vertices)} vértices")
            return list(arestas), list(vertices)
        
        except Exception as e:
            print(f"❌ Erro ao processar '{nome_arquivo}': {e}")
            return None, None


def exibir_header():
    print("=" * 60)
    print("🚀 ANALISADOR DE CONECTIVIDADE DE GRAFOS")
    print("=" * 60)
    print("📚 Trabalho APA 2 - Algoritmos Básico vs. Otimizado")
    print("🔍 Análise de conectividade e fecho transitivo")
    print("=" * 60)


def exibir_menu():
    print("\n" + "=" * 60)
    print("📋 MENU PRINCIPAL")
    print("=" * 60)
    print("1. 📁 Analisar arquivo de grafo")
    print("2. ℹ️  Sobre os algoritmos")
    print("3. 📖 Formatos de arquivo suportados")
    print("0. 👋 Sair")
    print("=" * 60)


def escolher_vertice(vertices_disponiveis):
    """Permite ao usuário escolher um vértice."""
    print("\n🎯 ESCOLHA DO VÉRTICE INICIAL:")
    print("=" * 40)
    vertices_ordenados = sorted(vertices_disponiveis)
    
    for i, vertice in enumerate(vertices_ordenados, 1):
        print(f"  {i:2d}. {vertice}")
    
    print("   0. Voltar")
    
    while True:
        try:
            escolha = input(f"\nEscolha um vértice (0-{len(vertices_ordenados)}): ").strip()
            
            if escolha == '0':
                return None
            
            if escolha.isdigit():
                num = int(escolha)
                if 1 <= num <= len(vertices_ordenados):
                    return vertices_ordenados[num-1]
                else:
                    print(f"❌ Número inválido. Digite entre 0 e {len(vertices_ordenados)}")
                    continue
            else:
                # Verifica se digitou o nome diretamente
                if escolha in vertices_disponiveis:
                    return escolha
                else:
                    print(f"❌ Vértice '{escolha}' não encontrado.")
                    continue
                    
        except KeyboardInterrupt:
            print("\n\n👋 Operação cancelada.")
            return None
        except Exception as e:
            print(f"❌ Erro: {e}")
            continue


def escolher_tipo_grafo():
    """Permite ao usuário escolher se o grafo é orientado ou não orientado."""
    print("\n🔄 ESCOLHA DO TIPO DE GRAFO:")
    print("=" * 40)
    print("  1. Grafo NÃO ORIENTADO")
    print("     • Arestas bidirecionais")
    print("     • Algoritmo padrão de conectividade")
    print()
    print("  2. Grafo ORIENTADO") 
    print("     • Arcos unidirecionais")
    print("     • Simetrização + fecho transitivo direto")
    print()
    print("  0. Voltar")
    
    while True:
        try:
            escolha = input("\nEscolha o tipo (0-2): ").strip()
            
            if escolha == '0':
                return None
            elif escolha == '1':
                return False  # Não orientado
            elif escolha == '2':
                return True   # Orientado
            else:
                print("❌ Opção inválida. Digite 0, 1 ou 2.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Operação cancelada.")
            return None
        except Exception as e:
            print(f"❌ Erro: {e}")


def executar_analise_fecho_transitivo(arestas, vertices, vertice_inicial, orientado=False):
    """Executa a análise do fecho transitivo usando ambos os algoritmos."""
    
    if orientado:
        # GRAFOS ORIENTADOS - Segue os 4 passos específicos
        print(f"\n🔄 ANÁLISE DE GRAFO ORIENTADO - 4 PASSOS DO ALGORITMO")
        print("=" * 60)
        
        # Cria instâncias dos algoritmos para grafos orientados
        grafo_basico = GrafoOrientadoBasico(vertices)
        grafo_otimizado = GrafoOrientadoOtimizado(vertices)
        
        print(f"🎯 Analisando {len(arestas)} arcos orientados com {len(vertices)} vértices")
        print()
        
        # ========== ALGORITMO BÁSICO ==========
        print("🔵 EXECUTANDO ALGORITMO BÁSICO PARA GRAFOS ORIENTADOS:")
        print("-" * 50)
        inicio_basico = time.time()
        
        # Constrói o grafo seguindo os 4 passos
        grafo_basico.construir_lista_sucessores(arestas)
        print()
        
        # Calcula conectividade (inclui os passos 3 e 4)
        conectado_basico = grafo_basico.eh_conexo(vertice_inicial)
        
        # Obtém o fecho transitivo direto
        fecho_basico = grafo_basico.dfs_fecho_transitivo_direto(vertice_inicial)
        
        tempo_basico = time.time() - inicio_basico
        print()
        
        # ========== ALGORITMO OTIMIZADO ==========
        print("🟢 EXECUTANDO ALGORITMO OTIMIZADO PARA GRAFOS ORIENTADOS:")
        print("-" * 50)
        inicio_otimizado = time.time()
        
        # Constrói o grafo seguindo os 4 passos otimizados
        grafo_otimizado.construir_lista_sucessores_otimizada(arestas)
        print()
        
        # Calcula conectividade (inclui os passos 3 e 4 otimizados)
        conectado_otimizado = grafo_otimizado.eh_conexo_otimizado(vertice_inicial)
        
        # Obtém o fecho transitivo direto
        fecho_otimizado = grafo_otimizado.dfs_fecho_transitivo_direto_otimizado(vertice_inicial)
        
        tempo_otimizado = time.time() - inicio_otimizado
        print()
        
    else:
        # GRAFOS NÃO ORIENTADOS - Algoritmo tradicional
        print(f"\n🔄 ANÁLISE DE GRAFO NÃO ORIENTADO")
        print("=" * 60)
        
        # Cria instâncias dos grafos tradicionais
        grafo_basico = GrafoBasico(vertices)
        grafo_otimizado = GrafoOtimizado(vertices)
        
        print(f"🎯 Analisando {len(arestas)} arestas com {len(vertices)} vértices")
        
        # Adiciona as arestas aos grafos
        for v1, v2 in arestas:
            grafo_basico.adicionar_aresta(v1, v2)
            grafo_otimizado.adicionar_aresta(v1, v2)
        
        print(f"✅ Grafos construídos com {len(vertices)} vértices")
        
        # Executa algoritmo básico
        print(f"\n⏳ Executando Algoritmo BÁSICO para vértice '{vertice_inicial}'...")
        inicio_basico = time.time()
        fecho_basico = grafo_basico.dfs_fecho_transitivo(vertice_inicial)
        conectado_basico = grafo_basico.eh_conexo()
        tempo_basico = time.time() - inicio_basico
        
        # Executa algoritmo otimizado  
        print(f"⏳ Executando Algoritmo OTIMIZADO para vértice '{vertice_inicial}'...")
        inicio_otimizado = time.time()
        fecho_otimizado = grafo_otimizado.dfs_fecho_transitivo_otimizado(vertice_inicial)
        conectado_otimizado = grafo_otimizado.eh_conexo_otimizado()
        tempo_otimizado = time.time() - inicio_otimizado
    
    # Exibe resultados
    print("\n" + "=" * 60)
    print("� RESULTADOS DA ANÁLISE DO FECHO TRANSITIVO")
    print("=" * 60)
    
    print(f"🎯 Vértice inicial: {vertice_inicial}")
    print(f"📈 Total de vértices no grafo: {len(vertices)}")
    
    print("\n🔵 ALGORITMO BÁSICO:")
    print(f"   📍 Vértices alcançáveis: {sorted(fecho_basico)}")
    print(f"   📊 Quantidade: {len(fecho_basico)}")
    print(f"   ⏱️  Tempo de execução: {tempo_basico:.6f} segundos")
    
    print("\n� ALGORITMO OTIMIZADO:")
    print(f"   📍 Vértices alcançáveis: {sorted(fecho_otimizado)}")
    print(f"   📊 Quantidade: {len(fecho_otimizado)}")
    print(f"   ⏱️  Tempo de execução: {tempo_otimizado:.6f} segundos")
    
    # Verificação de consistência
    print("\n🔍 VERIFICAÇÃO DE CONSISTÊNCIA:")
    if fecho_basico == fecho_otimizado:
        print("✅ Os dois algoritmos produziram o MESMO resultado!")
        
        # Cálculo de cobertura
        cobertura = (len(fecho_basico) / len(vertices)) * 100
        print(f"📊 Cobertura: {cobertura:.1f}% dos vértices do grafo")
        
        if len(fecho_basico) == len(vertices):
            print("🌟 Este vértice alcança TODOS os vértices do grafo!")
        elif len(fecho_basico) == 1:
            print("⚠️  Este vértice só alcança a si mesmo (isolado)")
        else:
            vertices_nao_alcancaveis = set(vertices) - fecho_basico
            print(f"❌ Vértices NÃO alcançáveis: {sorted(vertices_nao_alcancaveis)}")
    else:
        print("❌ ATENÇÃO: Os algoritmos produziram resultados DIFERENTES!")
        print(f"   Básico: {sorted(fecho_basico)}")
        print(f"   Otimizado: {sorted(fecho_otimizado)}")
    
    # Comparação de performance
    print("\n⚡ COMPARAÇÃO DE PERFORMANCE:")
    if tempo_basico > 0 and tempo_otimizado > 0:
        if tempo_otimizado < tempo_basico:
            speedup = tempo_basico / tempo_otimizado
            print(f"🚀 Algoritmo otimizado foi {speedup:.2f}x mais rápido")
        elif tempo_basico < tempo_otimizado:
            slowdown = tempo_otimizado / tempo_basico
            print(f"🐌 Algoritmo básico foi {slowdown:.2f}x mais rápido")
        else:
            print("⚖️  Ambos algoritmos tiveram performance similar")
        
        diferenca = abs(tempo_basico - tempo_otimizado)
        print(f"   📏 Diferença: {diferenca:.6f} segundos")
    
    return {
        'basico': {
            'fecho': fecho_basico, 
            'tempo': tempo_basico,
            'conectado': conectado_basico
        },
        'otimizado': {
            'fecho': fecho_otimizado, 
            'tempo': tempo_otimizado,
            'conectado': conectado_otimizado
        },
        'orientado': orientado
    }


def analisar_arquivo():
    """Fluxo principal para análise de um arquivo."""
    # Escolhe arquivo
    nome_arquivo = escolher_arquivo()
    if nome_arquivo is None:
        return
    
    # Processa arquivo
    reader = GrafoReader()
    arestas, vertices = reader.processar_arquivo(nome_arquivo)
    if arestas is None:
        input("\nPressione ENTER para continuar...")
        return
    
    # Escolhe tipo de grafo
    orientado = escolher_tipo_grafo()
    if orientado is None:
        return
    
    # Mostra informações do grafo
    tipo_str = "ORIENTADO" if orientado else "NÃO ORIENTADO"
    print(f"\n📋 INFORMAÇÕES DO GRAFO:")
    print(f"   📁 Arquivo: {nome_arquivo}")
    print(f"   � Tipo: {tipo_str}")
    if orientado:
        print(f"   �🔗 Arcos: {len(arestas)}")
    else:
        print(f"   🔗 Arestas: {len(arestas)}")
    print(f"   🎯 Vértices: {len(vertices)}")
    print(f"   📍 Lista de vértices: {sorted(vertices)}")
    
    if orientado:
        print(f"\n🔄 ARCOS DO GRAFO ORIENTADO:")
        for i, (v1, v2) in enumerate(arestas, 1):
            print(f"   {i:2d}. {v1} → {v2}")
    
    # Escolhe vértice
    vertice_escolhido = escolher_vertice(vertices)
    if vertice_escolhido is None:
        return
    
    # Executa análise do fecho transitivo
    resultados = executar_analise_fecho_transitivo(arestas, vertices, vertice_escolhido, orientado)
    
    print("\n" + "=" * 60)
    print("✅ ANÁLISE CONCLUÍDA COM SUCESSO!")
    print("=" * 60)
    
    if orientado:
        print("🔄 Algoritmo específico para grafos orientados executado:")
        print("   1. ✅ Simetrização do grafo")
        print("   2. ✅ Construção da lista de sucessores")
        print("   3. ✅ Cálculo do fecho transitivo direto")
        print("   4. ✅ Verificação de conectividade (fecho = X)")
    
    input("\nPressione ENTER para voltar ao menu principal...")
    print(f"   🎯 Vértices: {len(vertices)}")
    print(f"   📍 Lista de vértices: {sorted(vertices)}")
    
    # Escolhe vértice
    vertice_escolhido = escolher_vertice(vertices)
    if vertice_escolhido is None:
        return
    
    # Executa análise do fecho transitivo
    resultados = executar_analise_fecho_transitivo(arestas, vertices, vertice_escolhido)
    
    print("\n" + "=" * 60)
    print("✅ ANÁLISE CONCLUÍDA COM SUCESSO!")
    print("=" * 60)
    
    input("\nPressione ENTER para voltar ao menu principal...")


def exibir_sobre():
    """Exibe informações sobre os algoritmos."""
    print("\n" + "=" * 60)
    print("ℹ️  SOBRE OS ALGORITMOS")
    print("=" * 60)
    print("� ALGORITMO BÁSICO:")
    print("   • Implementação educacional com estruturas simples")
    print("   • Usa dicionários e listas padrão do Python")
    print("   • Fácil compreensão e depuração")
    print("   • Adequado para aprendizado")
    print()
    print("🔹 ALGORITMO OTIMIZADO:")
    print("   • Implementação com foco em performance")
    print("   • Usa frozensets e defaultdict(set)")
    print("   • Otimizações: cache, early termination")
    print("   • Estruturas de dados mais eficientes")
    print()
    print("🎯 AMBOS CALCULAM:")
    print("   • Fecho transitivo de um vértice")
    print("   • Conectividade do grafo")
    print("   • Usam busca em profundidade (DFS)")


def exibir_formatos():
    """Exibe os formatos de arquivo suportados."""
    print("\n" + "=" * 60)
    print("📖 FORMATOS DE ARQUIVO SUPORTADOS")
    print("=" * 60)
    print("🔹 Formato colchetes: [A,B] ou [1,2]")
    print("🔹 Formato hífen: A-B ou 1-2") 
    print("🔹 Formato vírgula: A,B ou 1,2")
    print("🔹 Formato espaço: A B ou 1 2")
    print("🔹 Múltiplas arestas: [A,B] [C,D] [E,F]")
    print()
    print("📝 REGRAS:")
    print("   • Uma ou mais arestas por linha")
    print("   • Linhas vazias são ignoradas")
    print("   • Comentários começam com #")
    print("   • Linhas com VERTICES: são ignoradas")
    print("   • Espaços extras são removidos automaticamente")


def escolher_arquivo():
    """Permite ao usuário escolher um arquivo."""
    reader = GrafoReader()
    arquivos = reader.listar_arquivos()
    
    if not arquivos:
        print("\n❌ Nenhum arquivo .txt encontrado no diretório 'examples'.")
        input("\nPressione ENTER para continuar...")
        return None
    
    print("\n📁 ARQUIVOS DISPONÍVEIS:")
    print("=" * 40)
    
    for i, arquivo in enumerate(arquivos, 1):
        print(f"  {i:2d}. {arquivo}")
    
    print("   0. Voltar")
    
    while True:
        try:
            escolha = input(f"\nEscolha um arquivo (0-{len(arquivos)}): ").strip()
            
            if escolha == '0':
                return None
            
            if escolha.isdigit():
                num = int(escolha)
                if 1 <= num <= len(arquivos):
                    return arquivos[num-1]
                else:
                    print(f"❌ Número inválido. Digite entre 0 e {len(arquivos)}")
            else:
                print("❌ Digite apenas números.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Operação cancelada.")
            return None
        except Exception as e:
            print(f"❌ Erro: {e}")


def main():
    """Função principal."""
    try:
        while True:
            exibir_header()
            exibir_menu()
            
            try:
                opcao = input("\nEscolha uma opção: ").strip()
                
                if opcao == '0':
                    print("\n👋 Até logo!")
                    break
                elif opcao == '1':
                    analisar_arquivo()
                elif opcao == '2':
                    exibir_sobre()
                    input("\nPressione ENTER para continuar...")
                elif opcao == '3':
                    exibir_formatos()
                    input("\nPressione ENTER para continuar...")
                else:
                    print("\n❌ Opção inválida. Digite 0, 1, 2 ou 3.")
                    input("Pressione ENTER para continuar...")
            
            except KeyboardInterrupt:
                print("\n\n👋 Programa encerrado pelo usuário.")
                break
            except Exception as e:
                print(f"\n❌ Erro inesperado: {e}")
                input("Pressione ENTER para continuar...")
    
    except Exception as e:
        print(f"❌ Erro crítico: {e}")
    
    finally:
        print("\n🔚 Programa finalizado.")


if __name__ == "__main__":
    main()
