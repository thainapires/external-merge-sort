# Repositório destinado a matéria de Organização e estrutura de arquivos

*Aluna: Thainá Pires*

## Objetivo do trabalho

Criação do algoritmo external merge sort de duas formas diferentes:

- 1ª forma: Fazendo a divisão do arquivo principal em subarquivos e depois juntando
- 2ª forma: Fazendo a divisão dos blocos escrevendo no mesmo arquivo

Além de fazer o benchmark de sua performance.

# External Merge Sort

Algoritmo composto de duas fases que realiza a ordenação de arquivos grandes. Esse algoritmo minimiza o número de acessos e melhora a performance da ordenação.

## Fases

### Primeira fase
Fase de ordenação em memória. O arquivo é dividido em blocos de X linhas escolhidas pelo usuário
- Trazer para memória um bloco
- Ordenar o bloco 
- Escrever resultado da ordenação em outro(s) arquivo(s)
- Repetir o procedimento até que todos os X blocos sejam processados.

### Segunda fase
Fase de fusão (merge) dos blocos criados na fase anterior.
- Intercalar de dois em dois blocos
- Repetir o procedimento até que resulte em um único bloco do tamanho do arquivo e que esteja ordenado.

# Especificações de onde o algoritmo foi rodado
- Processador: Intel Core i5-72000U CPU @2.50GHz 2.70 GHz
- Memória RAM: 8,00GB
- Sistema operacional: Windows 10 64 bits

*Link para baixar o arquivo dos CEPs: https://drive.google.com/file/d/1hoTpOwcF3lWd-Pcsf6Nf2TXnjCgRyt9I/view?usp=sharing



