#ARQUIVO DE ORDENACAO DE BLOCOS COM TAMANHOS ESCOLHIDOS PELO USUARIO

import struct
import sys
import os
import cProfile
import time

def profiling():

        inicio = time.time()
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

        f = open("cep.dat","rb+")
        #fAux = open("cepOrdenado.dat","wb+")s

        #Funcao para comparacao de tuplas
        def cmp ( ta, tb ):
                if ta[colunaDoCEP] == tb[colunaDoCEP]: return 0
                if ta[colunaDoCEP] > tb[colunaDoCEP]: return 1
                return -1

        cont2 = 0 #variavel para conseguir se locomover no arquivo

        contarBlocos = 0
        for i in tamBlocos:	
                blocoOrdenado = []
                leituras = i #variavel para controlar o numero de leituras com a quantidade de linhas de cada bloco
                while leituras != 0:
                        registroPacked = f.read(registroCEP.size)
                        registroUnpacked = registroCEP.unpack(registroPacked)
                        blocoOrdenado.append(registroUnpacked)
                        leituras = leituras - 1
                blocoOrdenado.sort(cmp)
                fBloco = open(str(contarBlocos)+".dat", "wb+")
                for j in range(i): 
                        line_pack = registroCEP.pack(blocoOrdenado[j][0], blocoOrdenado[j][1], blocoOrdenado[j][2], blocoOrdenado[j][3], blocoOrdenado[j][4], blocoOrdenado[j][5], blocoOrdenado[j][6])
                        fBloco.write(line_pack)
                        
                fBloco.close()
                blocoOrdenado = []
                contarBlocos= contarBlocos + 1
                
                
        print "Fim do programa"

        f.close()
        final = time.time()
        print "Tempo: ",final - inicio

cProfile.run("profiling()")
