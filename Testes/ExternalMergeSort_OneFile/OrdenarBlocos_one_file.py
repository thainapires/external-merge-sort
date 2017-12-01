#ARQUIVO DE ORDENACAO DE BLOCOS COM TAMANHO ESCOLHIDO PELO USUARIO

import struct
import sys
import os
import cProfile


def profiling():
        tamanhoDoBloco = 10000

        registroCEP = struct.Struct("72s72s72s72s2s8s2s")
        colunaDoCEP = 5
        qtdLinhasTotal = os.path.getsize("cep.dat")/registroCEP.size
        #qtdLinhasTotal = 100
        tamBlocos = []
        qtdBlocos = qtdLinhasTotal / tamanhoDoBloco
        resto = qtdLinhasTotal - (tamanhoDoBloco * qtdBlocos)
        tamBlocos = [tamanhoDoBloco] * qtdBlocos
        if resto > 0:
                tamBlocos.append(resto)

        #Abrindo arquivo do CEP e criando o arquivo que os blocos odenados serao escritos	
        f = open("cep.dat","rb+")
        fAux = open("cep_ordenado.dat","wb+")

        #Funcao para comparacao de tuplas
        def cmp ( ta, tb ):
                if ta[colunaDoCEP] == tb[colunaDoCEP]: return 0
                if ta[colunaDoCEP] > tb[colunaDoCEP]: return 1
                return -1

        cont2 = 0 #variavel para conseguir se locomover no arquivo

        #Ordenacao em si
        for i in tamBlocos:	
                blocoOrdenado = []
                leituras = i #variavel para controlar o numero de leituras com a quantidade de linhas de cada bloco
                #Enquanto a variavel leituras nao for igual a zero, eh porque o bloco ainda nao acabou de ser lido e adicionado na lista
                while leituras != 0: 
                        registroPacked = f.read(registroCEP.size)
                        registroUnpacked = registroCEP.unpack(registroPacked)
                        blocoOrdenado.append(registroUnpacked)
                        leituras = leituras - 1 #decrementar leituras
                blocoOrdenado.sort(cmp) #Fazendo a ordenacao na memoria com a funcao sort nativa de python
                #Escrevendo o bloco ordenadado no arquivo
                for j in range(i): 
                        line_pack = registroCEP.pack(blocoOrdenado[j][0], blocoOrdenado[j][1], blocoOrdenado[j][2], blocoOrdenado[j][3], blocoOrdenado[j][4], blocoOrdenado[j][5], blocoOrdenado[j][6])
                        fAux.write(line_pack)
                blocoOrdenado = [] #necessario zerar a lista para que o processo comece novamente
                
        print "Fim do programa"

        f.close()
        fAux.close()

cProfile.run("profiling()")
