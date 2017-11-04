# External Merge Sort

Algoritmo composto de duas fases que realiza a ordenação de arquivos grandes. Esse algoritmo minimiza o número de acessos e melhora a performance da ordenação.

# Fases

## Primeira fase
Fase de ordenação em memória. O arquivo é dividido em blocos de X linhas escolhidas pelo usuário
- Trazer para memória um bloco
- Ordenar o bloco 
- Escrever resultado da ordenação em outro(s) arquivo(s)
- Repetir o procedimento até que todos os X blocos sejam processados.

## Segunda fase
Fase de fusão (merge) dos blocos criados na fase anterior.
- Intercalar de dois em dois blocos
- Repetir o procedimento até que resulte em um único bloco do tamanho do arquivo e que esteja ordenado.

## Especificações de onde o algoritmo foi rodado
- Processador: Intel Core i5-72000U CPU @2.50GHz 2.70 GHz
- Memória RAM: 8,00GB
- Sistema operacional: Windows 10 64 bits

*Obs: Repositório destinado a matéria de Organização e estrutura de arquivos*

*Aluna: Thainá Pires*




