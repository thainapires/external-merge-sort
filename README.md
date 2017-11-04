# External Merge Sort
Repositório destinado ao trabalho final da disciplina de Organização e estrutura de arquivos.

#O que é o External Merge Sort?
É um algoritmo que serve para ajudar na ordenação de arquivos que são muito grandes para serem ordenados como um todo na memória. Esse 
algoritmo minimiza o número de acessos ao disco e melhora a performance de ordenação. 

#Fases do algoritmo
1)Fase de ordenação: divide o arquivo em blocos com tamanho de linhas X desejado pelo usuário. O código de ordenação rodará uma determinada 
quantidade de vezes até que o arquivo esteja ordenado a cada X linhas.
Exemplo:
->Arquivo: 1000 linhas
->Quantidade de linhas por bloco escolhida pelo usuário: 100
->A quantidade de blocos será: 1000/100 = 10 blocos de 100 linhas cada

Em cada rodada desta fase, o algoritmo lê a quantidade de linhas que o usuário escolheu e faz a ordenação em disco. Logo após, escreve estas
mesmas linhas em outro arquivo.

2)Fase de fusão: nesta fase os blocos vão sendo juntados de dois em dois até que vire um bloco ordenado.

#Especificações de onde foi rodado o algoritmo
Processador: Intel Core i5-72000U CPU @2.50GHz 2.70 GHz
Memória RAM: 8,00GB
SO: Windows 10 64 bits
