# Repositório destinado ao trabalho final da matéria de Organização e estrutura de arquivos

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
Fase de ordenação em memória. O arquivo é dividido em N blocos de X linhas escolhidas pelo usuário.
- Trazer para memória um bloco
- Ordenar o bloco 
- Escrever resultado da ordenação em outro(s) arquivo(s)
- Repetir o procedimento até que todos os N blocos sejam processados.

### Segunda fase
Fase de junção (merge) dos blocos criados na fase anterior.
- Intercalar de dois em dois blocos
- Repetir o procedimento até que resulte em um único bloco do tamanho do arquivo e que esteja ordenado.

# Especificações de onde o algoritmo foi rodado
- Processador: Intel Core i5-3470 CPU @3.20GHz x4
- Memória RAM: 7,7GiB
- Sistema operacional: Ubuntu 16.04 LTS 64 bits

# Usage

- 1: Baixar o algoritmo ([Opção 1](https://github.com/thainaspires/External-Merge-Sort/tree/master/ExternalMergeSort_OneFile) | [Opção 2](https://github.com/thainaspires/External-Merge-Sort/tree/master/ExternalMergeSort_Subfiles))

- 2: Baixar o arquivo de CEPs que não está ordenado ([Link](https://drive.google.com/file/d/1hoTpOwcF3lWd-Pcsf6Nf2TXnjCgRyt9I/view?usp=sharing)) e coloca-lo na mesma pasta que os arquivos de ordenação e intercalação.

- 3: Executar o código de ordenação colocando como argumento o número de linhas que quer em cada bloco, como no exemplo:
```
$ python OrdenarBlocos_one_file.py 10000
```
- 4: Executar o código de intercalaçao colocando como argumento o mesmo número de linhas colocados no código de ordenação, como no exemplo:
```
$ python IntercalarBlocos_one_file.py 10000
```
Ao final do processo, será obtido um arquivo chamado cep_ordenado.dat que conterá todos os CEPs ordenados.

*Obs: Também é possível executar o código rodando em uma IDE pois será pedido a quantidade de linhas que o usuário quer escolher assim que o algoritmo rodar*




