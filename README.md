# 🚀 Analisador de Conectividade de Grafos

**Trabalho APA 2 - Algoritmos e Programação Avançada**  
Implementação e comparação de algoritmos para verificação de conectividade e cálculo de fecho transitivo em grafos orientados e não orientados.

## 📋 Visão Geral

Este projeto implementa dois tipos de análise:

### 🔹 Grafos NÃO ORIENTADOS
- **Algoritmo Básico**: Implementação educacional com estruturas simples
- **Algoritmo Otimizado**: Implementação com foco em performance

### 🔹 Grafos ORIENTADOS (4 Passos Específicos)
Seguindo metodologia específica:
1. **Simetrização do grafo** - Adição de arcos simétricos
2. **Construção da lista de sucessores** - Estrutura auxiliar
3. **Cálculo do fecho transitivo direto** - Usando DFS
4. **Verificação de conectividade** - Teste se fecho = X

## 🏗️ Estrutura do Projeto

```
Trabalho_APA_2/
├── src/
│   └── algorithms/
│       ├── basic_connectivity.py           # Algoritmo básico (não orientado)
│       ├── optimized_connectivity.py       # Algoritmo otimizado (não orientado)
│       ├── directed_basic_connectivity.py  # Algoritmo básico (orientado)
│       └── directed_optimized_connectivity.py  # Algoritmo otimizado (orientado)
├── tests/
│   ├── test_connectivity.py                # Testes para grafos não orientados
│   └── test_directed_connectivity.py       # Testes para grafos orientados
├── examples/
│   ├── exemplo_conexo.txt                  # Exemplo de grafo conexo
│   ├── exemplo_desconexo.txt               # Exemplo de grafo desconexo
│   ├── exemplo_complexo.txt                # Exemplo complexo
│   ├── exemplo_enunciado.txt               # Exemplo do enunciado
│   ├── grafo_orientado_simples.txt         # Exemplo orientado simples
│   └── grafo_orientado_desconexo.txt       # Exemplo orientado desconexo
└── main.py                                 # Interface principal
```

## 🚀 Como Usar

### 1. Executar o programa principal
```bash
python3 main.py
```

### 2. Menu interativo
- **📁 Analisar arquivo de grafo**: Carrega arquivo e executa análise
- **ℹ️ Sobre os algoritmos**: Informações detalhadas
- **📖 Formatos suportados**: Guia de formatação de arquivos

### 3. Escolha do tipo de grafo
- **Grafo NÃO ORIENTADO**: Arestas bidirecionais (algoritmo tradicional)
- **Grafo ORIENTADO**: Arcos unidirecionais (algoritmo de 4 passos)

## 📖 Formatos de Arquivo Suportados

### Formato Colchetes
```
[A,B]
[B,C]
[C,D]
```

### Formato Hífen
```
A-B
B-C
C-D
```

### Formato Vírgula
```
A,B
B,C
C,D
```

## 🔧 Algoritmos Implementados

### Grafos Não Orientados

#### 🔵 Algoritmo Básico (`GrafoBasico`)
- Estruturas de dados simples (dict + list)
- Implementação educacional clara
- DFS tradicional para fecho transitivo

#### �� Algoritmo Otimizado (`GrafoOtimizado`)
- Estruturas otimizadas (frozenset, defaultdict)
- Cache de resultados
- Early termination
- Estatísticas detalhadas

### Grafos Orientados

#### 🔵 Algoritmo Básico (`GrafoOrientadoBasico`)
**4 Passos Específicos:**
1. `simetrizar_grafo()` - Adiciona arcos simétricos
2. `construir_lista_sucessores()` - Monta estrutura auxiliar
3. `dfs_fecho_transitivo_direto()` - Calcula fecho via DFS
4. `eh_conexo()` - Verifica se |fecho| = |X|

#### 🟢 Algoritmo Otimizado (`GrafoOrientadoOtimizado`)
**Mesmos 4 passos com otimizações:**
- Sets para operações O(1)
- Cache de resultados de fecho transitivo
- Early termination quando todos os vértices são visitados
- Cache de conectividade por componente

## 🧪 Testes

### Executar todos os testes
```bash
python3 -m unittest discover tests -v
```

### Executar testes específicos
```bash
# Testes para grafos não orientados
python3 -m unittest tests.test_connectivity -v

# Testes para grafos orientados  
python3 -m unittest tests.test_directed_connectivity -v
```

### Cobertura dos Testes
- **25 testes** implementados
- Consistência entre algoritmos básicos e otimizados
- Casos extremos (grafos vazios, um vértice)
- Grafos conexos e desconexos
- Validação do algoritmo de 4 passos para grafos orientados

## 🎯 Algoritmo Específico para Grafos Orientados

### Metodologia dos 4 Passos

1. **🔄 PASSO 1: Simetrização**
   - Para cada arco (u,v), adiciona (v,u) se não existir
   - Transforma o grafo orientado em não orientado

2. **🔄 PASSO 2: Lista de Sucessores**
   - Constrói estrutura auxiliar para navegação
   - Mapeia cada vértice para seus sucessores

3. **🔄 PASSO 3: Fecho Transitivo Direto**
   - Utiliza DFS a partir do vértice escolhido
   - Identifica todos os vértices alcançáveis

4. **🔄 PASSO 4: Verificação de Conectividade**
   - Compara |fecho| com |X| (conjunto de todos os vértices)
   - Grafo é conexo ⟺ |fecho| = |X|

### Otimizações Implementadas
- **Early Termination**: Para quando todos os vértices são visitados
- **Cache de Resultados**: Evita recálculos desnecessários
- **Estruturas Eficientes**: Sets para operações O(1)
- **Cache de Conectividade**: Reutiliza resultados para componentes conexos

## 📈 Performance

### Métricas Coletadas
- Tempo de execução (precisão de microssegundos)
- Comparação relativa entre algoritmos
- Detecção de speedup do algoritmo otimizado
- Cobertura de vértices alcançáveis

### Resultados Típicos
- Algoritmo otimizado: **1.1x a 1.5x mais rápido**
- Early termination: Redução significativa em grafos conexos
- Cache: Evita recálculos em análises múltiplas

## 🔍 Exemplo de Uso

```python
# Grafo orientado básico
vertices = ['A', 'B', 'C']
grafo = GrafoOrientadoBasico(vertices)
grafo.adicionar_arco('A', 'B')
grafo.adicionar_arco('B', 'C')
grafo.adicionar_arco('C', 'A')

# Verifica conectividade (executa os 4 passos)
conexo = grafo.eh_conexo('A')  # True para ciclo completo
```

## �� Características do Projeto

### ✅ Qualidade de Código
- Docstrings detalhadas
- Tratamento de erros
- Código limpo e modular
- Separação de responsabilidades

### ✅ Testes Abrangentes
- Testes unitários completos
- Validação de consistência
- Casos extremos cobertos
- Integração contínua

### ✅ Interface Profissional
- Design interativo atrativo
- Feedback visual rico
- Informações educacionais
- Experiência do usuário otimizada

---

**Desenvolvido para APA 2 - Algoritmos e Programação Avançada**  
Implementação completa de algoritmos de conectividade para grafos orientados e não orientados com foco em performance e qualidade.
