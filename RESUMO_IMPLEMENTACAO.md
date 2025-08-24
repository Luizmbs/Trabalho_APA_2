✅ FUNCIONALIDADES IMPLEMENTADAS COM SUCESSO!

🔹 GRAFOS NÃO ORIENTADOS:
   ✅ Lista de adjacências impressa corretamente
   ✅ Usa o atributo correto: grafo_basico.adj_list
   ✅ Formato: vértice: [lista_de_adjacentes_ordenada]

🔹 GRAFOS ORIENTADOS:
   ✅ Lista de sucessores impressa corretamente
   ✅ Usa o atributo correto: grafo_basico.sucessores
   ✅ Mostra sucessores APÓS a simetrização
   ✅ Formato: vértice: [lista_de_sucessores_ordenada]

📋 EXEMPLO DE SAÍDA:

GRAFO NÃO ORIENTADO:
   A: ['B', 'E']
   B: ['A', 'C']
   C: ['B', 'D']
   D: ['C', 'E']
   E: ['A', 'D']

GRAFO ORIENTADO:
   A: ['B', 'C']
   B: ['A', 'C']
   C: ['A', 'B']

🎯 LOCALIZAÇÃO DAS MUDANÇAS:
   - main.py: linha ~325 (grafos não orientados)
   - main.py: linha ~274 (grafos orientados)
   - Correção: adj_list (não adjacencias)
   - Correção: sucessores (não lista_sucessores)

🔧 ARQUIVOS MODIFICADOS:
   - main.py: Adicionada impressão das listas
   - teste_listas.py: Arquivo de teste criado
   - Removido código duplicado no main.py

✨ FUNCIONAMENTO:
   1. Usuário escolhe o tipo de grafo
   2. Programa constrói o grafo
   3. Imprime a lista apropriada (adjacências ou sucessores)
   4. Continua com a análise do fecho transitivo
