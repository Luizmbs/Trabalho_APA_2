# Trabalho APA 2 - Verificação de Conectividade em Grafos

## Descrição do Problema

Dado um grafo formado por um conjunto de vértices e um conjunto de ligações, desenvolver um algoritmo que verifique se o mesmo é conexo.

**Exemplo do Enunciado:**
- Conjunto de vértices: X = {x1, x2, x3, x4, x5, x6}
- Conjunto de arestas: U = {[x1,x2], [x2,x3], [x3,x1], [x4,x5], [x5,x6], [x6,x4]}
- **Resultado**: Falso (grafo possui 2 componentes conexos distintos)

## Implementações Desenvolvidas

### 1. Implementação Básica (`src/algorithms/basic_connectivity.py`)
- **Objetivo**: Implementação didática e direta
- **Características**: Código limpo e fácil compreensão
- **Estruturas**: `dict` + `list` para adjacências, DFS simples

### 2. Implementação Otimizada (`src/algorithms/optimized_connectivity.py`)
- **Objetivo**: Máximo desempenho e funcionalidades avançadas
- **Otimizações**: 
  - `frozenset` + `defaultdict(set)` para estruturas eficientes
  - Early termination na DFS
  - Cache de resultados
  - Heurística de escolha do vértice inicial
- **Funcionalidades Extra**:
  - Análise de componentes conexos
  - Estatísticas do grafo (densidade, graus, etc.)
  - Implementações alternativas (BFS, DFS com limite)

### 3. Programa Principal (`main.py`) 🌟 NOVO!
- **Objetivo**: Interface completa para análise de conectividade
- **Funcionalidades**:
  - Carregamento automático de arquivos da pasta `examples/`
  - Interface interativa para escolha de vértice
  - Análise comparativa automática entre ambos algoritmos
  - Apresentação detalhada dos resultados
  - Suporte a múltiplos formatos de entrada

## Estrutura do Algoritmo (Conforme Especificação)

1. **Construir Lista de Adjacência**: Representação eficiente do grafo a partir dos dados de entrada
2. **Computar Fecho Transitivo**: Usar DFS para encontrar todos os vértices alcançáveis de um vértice escolhido
3. **Verificar Conectividade**: Se o fecho contém todos os vértices de X, o grafo é conexo

## Como Executar

### 🌟 Programa Principal (Recomendado)
```bash
# Executa o programa principal interativo
python main.py
# ou
make run
```

O programa principal oferece:
- 📁 Seleção de arquivos de exemplo
- 🎯 Escolha interativa do vértice inicial  
- 🔍 Análise com ambos os algoritmos
- 📊 Resultados comparativos detalhados

### Execução Direta dos Algoritmos
```bash
# Implementação básica
python src/algorithms/basic_connectivity.py
make basic

# Implementação otimizada  
python src/algorithms/optimized_connectivity.py
make optimized

# Testes unitários
python tests/test_connectivity.py
make test

# Comparação entre algoritmos
python tests/comparison.py
make compare
```

### Usando Makefile (Comandos Completos)
```bash
# Ver todos os comandos disponíveis
make help

# Configurar ambiente
make setup

# Execução completa de tudo
make all

# Validação completa (recomendado para avaliação)
make professor
```

## Formatos de Arquivo Suportados

### Formato 1: Estilo do Enunciado
```
VERTICES: x1 x2 x3 x4 x5 x6
ARESTAS: [x1,x2] [x2,x3] [x3,x1] [x4,x5] [x5,x6] [x6,x4]
```

### Formato 2: Com Vírgulas e Traços
```
VERTICES: A,B,C,D,E
ARESTAS: A-B B-C C-D D-E E-A
```

### Formato 3: Formato Simples
```
VERTICES: 1 2 3 4 5 6
ARESTAS: 1,2 2,3 4,5 5,6
```

### Arquivos de Exemplo Inclusos (pasta `examples/`)
- `exemplo_enunciado.txt`: O exemplo exato do enunciado
- `exemplo_conexo.txt`: Um grafo conexo para comparação
- `exemplo_desconexo.txt`: Um grafo claramente desconexo
- `exemplo_complexo.txt`: Grafo mais complexo em formato de estrela

## Estrutura do Projeto

```
Trabalho_APA_2/
├── README.md                           # Este arquivo
├── DOCUMENTACAO_TECNICA.md             # Documentação técnica detalhada
├── Makefile                            # Comandos automatizados
├── main.py                             # 🌟 PROGRAMA PRINCIPAL 🌟
├── src/                                # Código fonte
│   ├── __init__.py
│   └── algorithms/                     # Implementações dos algoritmos
│       ├── __init__.py
│       ├── basic_connectivity.py       # Implementação básica
│       └── optimized_connectivity.py   # Implementação otimizada
├── tests/                              # Testes e comparações
│   ├── __init__.py
│   ├── test_connectivity.py           # Testes unitários
│   └── comparison.py                  # Comparação entre implementações
├── examples/                           # Arquivos de exemplo
│   ├── exemplo_enunciado.txt          # Exemplo do enunciado
│   ├── exemplo_conexo.txt             # Exemplo grafo conexo
│   ├── exemplo_desconexo.txt          # Exemplo grafo desconexo
│   └── exemplo_complexo.txt           # Exemplo mais complexo
└── .venv/                             # Ambiente virtual Python
```

## Exemplo de Saída

### Para o Exemplo do Enunciado:
```
Vértices: ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
Arestas: [('x1', 'x2'), ('x2', 'x3'), ('x3', 'x1'), ('x4', 'x5'), ('x5', 'x6'), ('x6', 'x4')]

O grafo é conexo? False

Fecho transitivo de x1: ['x1', 'x2', 'x3']
Componentes conexos: 2
  - Componente 1: ['x1', 'x2', 'x3']  
  - Componente 2: ['x4', 'x5', 'x6']
```

## Análise de Complexidade

### Ambas Implementações
- **Tempo**: O(V + E) onde V = número de vértices, E = número de arestas
- **Espaço**: O(V + E) para representação + O(V) para algoritmo

### Otimizações Práticas (Versão Otimizada)
- **Early Termination**: Para quando todos vértices são visitados
- **Estruturas Eficientes**: O(1) para lookup vs O(n) em listas
- **Cache**: O(1) para consultas repetidas
- **Heurísticas**: Escolha inteligente do vértice inicial

## Validação e Testes

✅ **20 Testes Unitários** cobrindo:
- Casos extremos (grafo vazio, um vértice)
- Exemplo do enunciado
- Grafos conexos e desconexos
- Consistência entre implementações
- Funcionalidades específicas da versão otimizada

✅ **Casos de Teste Validados**:
- Exemplo do enunciado: ❌ Falso (correto)
- Grafo linear: ✅ Verdadeiro
- Grafo completo: ✅ Verdadeiro
- Múltiplos componentes: ❌ Falso (correto)

## Performance Comparativa

| Aspecto | Versão Básica | Versão Otimizada |
|---------|---------------|------------------|
| Legibilidade | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Performance Pequenos Grafos | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| Performance Grandes Grafos | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Funcionalidades | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Extensibilidade | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

## Conclusão

O projeto implementa com sucesso duas versões do algoritmo de verificação de conectividade:

1. **Básica**: Ideal para aprendizado e compreensão do algoritmo
2. **Otimizada**: Ideal para uso prático e análise avançada

Ambas mantêm a complexidade teórica O(V + E), mas a versão otimizada oferece melhor desempenho prático e funcionalidades adicionais para análise de grafos.
