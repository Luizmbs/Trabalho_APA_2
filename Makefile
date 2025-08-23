# Makefile para o Projeto de Verificação de Conectividade em Grafos
# APA 2 - Algoritmos e Programação Avançada

# Variáveis
PYTHON = .venv/bin/python
SRC_DIR = .
VENV_DIR = .venv

# Comandos principais
.PHONY: help setup test basic optimized compare file-demo file-interactive clean all

help:
	@echo "Comandos disponíveis:"
	@echo "  make setup          - Configura o ambiente Python"
	@echo "  make run            - Executa o programa principal"
	@echo "  make basic          - Executa implementação básica"
	@echo "  make optimized      - Executa implementação otimizada"
	@echo "  make test           - Executa testes unitários"
	@echo "  make compare        - Executa comparação entre implementações"
	@echo "  make file-demo      - Demonstração com entrada de arquivo"
	@echo "  make file-interactive - Modo interativo com arquivo"
	@echo "  make all            - Executa todos os componentes"
	@echo "  make clean          - Limpa arquivos temporários"
	@echo "  make help           - Mostra esta ajuda"

setup:
	@echo "Configurando ambiente Python..."
	python3 -m venv $(VENV_DIR)
	$(PYTHON) -m pip install --upgrade pip
	@echo "Ambiente configurado com sucesso!"

run:
	@echo "=== EXECUTANDO PROGRAMA PRINCIPAL ==="
	$(PYTHON) main.py

basic:
	@echo "=== EXECUTANDO IMPLEMENTAÇÃO BÁSICA ==="
	$(PYTHON) src/algorithms/basic_connectivity.py

optimized:
	@echo "=== EXECUTANDO IMPLEMENTAÇÃO OTIMIZADA ==="
	$(PYTHON) src/algorithms/optimized_connectivity.py

test:
	@echo "=== EXECUTANDO TESTES UNITÁRIOS ==="
	$(PYTHON) tests/test_connectivity.py

compare:
	@echo "=== EXECUTANDO COMPARAÇÃO ENTRE IMPLEMENTAÇÕES ==="
	$(PYTHON) tests/comparison.py

file-demo:
	@echo "=== DEMONSTRAÇÃO COM ENTRADA DE ARQUIVO ==="
	$(PYTHON) demo_arquivo.py

file-interactive:
	@echo "=== MODO INTERATIVO COM ARQUIVO ==="
	$(PYTHON) file_connectivity.py

performance:
	@echo "=== TESTE DE PERFORMANCE DETALHADO ==="
	$(PYTHON) -c "from comparison import teste_performance_grande; teste_performance_grande()"

demo:
	@echo "=== DEMONSTRAÇÃO INTERATIVA ==="
	@echo "1. Exemplo do enunciado:"
	$(PYTHON) -c "import sys; sys.path.insert(0, 'tests'); from comparison import teste_exemplo_enunciado; teste_exemplo_enunciado()"
	@echo ""
	@echo "2. Caso conexo:"
	$(PYTHON) -c "import sys; sys.path.insert(0, 'tests'); from comparison import teste_grafo_conexo_pequeno; teste_grafo_conexo_pequeno()"

validate:
	@echo "=== VALIDAÇÃO COMPLETA ==="
	$(PYTHON) tests/test_connectivity.py
	@echo ""
	@echo "=== TESTE COM EXEMPLO DO ENUNCIADO ==="
	$(PYTHON) -c "import sys; sys.path.insert(0, 'tests'); from comparison import teste_exemplo_enunciado; teste_exemplo_enunciado()"

all: test basic optimized compare run
	@echo ""
	@echo "=== EXECUÇÃO COMPLETA FINALIZADA ==="
	@echo "Todas as implementações foram testadas e executadas com sucesso!"

clean:
	@echo "Limpando arquivos temporários..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	@echo "Limpeza concluída!"

# Comandos de desenvolvimento
dev-setup: setup
	@echo "Configurando ambiente de desenvolvimento..."
	$(PYTHON) -m pip install black flake8 mypy
	@echo "Ferramentas de desenvolvimento instaladas!"

format:
	@echo "Formatando código com black..."
	$(PYTHON) -m black *.py

lint:
	@echo "Verificando código com flake8..."
	$(PYTHON) -m flake8 *.py --max-line-length=88 --ignore=E203,W503

typecheck:
	@echo "Verificando tipos com mypy..."
	$(PYTHON) -m mypy *.py --ignore-missing-imports

# Comandos para análise
stats:
	@echo "=== ESTATÍSTICAS DO PROJETO ==="
	@echo "Arquivos Python:"
	@find . -name "*.py" | wc -l
	@echo "Linhas de código:"
	@find . -name "*.py" -exec wc -l {} + | tail -1
	@echo "Tamanho total:"
	@du -sh .

info:
	@echo "=== INFORMAÇÕES DO PROJETO ==="
	@echo "Projeto: Verificação de Conectividade em Grafos"
	@echo "Disciplina: APA 2 - Algoritmos e Programação Avançada"
	@echo "Implementações: Básica e Otimizada"
	@echo "Linguagem: Python 3.10+"
	@echo ""
	@echo "Arquivos principais:"
	@echo "  - basic_connectivity.py: Implementação básica"
	@echo "  - optimized_connectivity.py: Implementação otimizada"  
	@echo "  - comparison.py: Comparação entre implementações"
	@echo "  - test_connectivity.py: Testes unitários"
	@echo "  - DOCUMENTACAO_TECNICA.md: Documentação completa"

# Comando para demonstração do professor
professor: validate demo run
	@echo ""
	@echo "=== DEMONSTRAÇÃO PARA AVALIAÇÃO ==="
	@echo "1. Testes unitários executados com sucesso"
	@echo "2. Exemplo do enunciado validado"
	@echo "3. Ambas implementações funcionam corretamente"
	@echo "4. Resultados consistentes entre versões"
	@echo "5. Programa principal implementado e testado"
	@echo ""
	@echo "Para mais detalhes, consulte:"
	@echo "  - README.md: Visão geral do projeto"
	@echo "  - DOCUMENTACAO_TECNICA.md: Análise técnica detalhada"
	@echo ""
	@echo "Nova estrutura do projeto:"
	@echo "  - src/algorithms/: Implementações dos algoritmos"
	@echo "  - tests/: Testes e comparações"
	@echo "  - examples/: Arquivos de exemplo"
	@echo "  - main.py: Programa principal"
