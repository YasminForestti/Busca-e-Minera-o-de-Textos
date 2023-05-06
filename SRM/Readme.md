# COS738 - IMPLEMENTAÇÃO DE UM SISTEMA DE RECUPERAÇÃO EM MEMÓRIA SEGUNDO O MODELO VETORIAL

Implementação de um sistema de recuperação em memória segundo o modelo vetorial.

## Módulos:
--
1. Processador de consultas
1.1. PC.py - Processador de consultas.
2. Indexador
2.1. lista_invertida.py - Gerador de lista invertida.
2.2. modelo.py - Cria o modelo vetorial.
3. Buscador
3.1. buscador.py - Buscador, responsável pelos resultados finais.


## Arquivos gerados pelo sistema
--
1. consultas.csv - Criado pelo processador, lista todas as consultas processadas.
2. esperados.csv - Criado pelo processador, lista número do documento e seu número de votos.
3. gli.csv - Criado pelo gerador, cada linha correponde a uma palavra e à lista dos índices dos documentos em que a palavra aparece. O índice do documento aparece na lista o mesmo número de vezes que a palavra aparece no documento.
4. modelo.csv - Criado pelo indexador, especificado no arquivo modelo.txt.
5. resultados.csv - Criado pelo buscador, para cada consulta listamos o rank e o índice dos seus 5 documentos mais similares e o grau de similaridade para cada documento.

## Como executar
--
Os módulos devem ser executados na ordem 1.1 -> 2.1 -> 2.2 -> 3.1.