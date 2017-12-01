#ARQUIVO PARA INTERCALACAO DOS BLOCOS ATRAVES DO MERGE SORT

import struct
import sys
import os
import cprofile

def profiling():
        tamanhoDoBloco = 10000

        registroCEP = struct.Struct("72s72s72s72s2s8s2s")
        colunaDoCEP = 5
        #qtdLinhasTotal = 100
        qtdLinhasTotal = os.path.getsize("cep.dat")/registroCEP.size
        tamBlocos = []
        qtdBlocos = qtdLinhasTotal / tamanhoDoBloco
        resto = qtdLinhasTotal - (tamanhoDoBloco * qtdBlocos)
        tamBlocos = [tamanhoDoBloco] * qtdBlocos
        if resto > 0:
                tamBlocos.append(resto)

        def cmp ( ta, tb ):
                if ta[colunaDoCEP] == tb[colunaDoCEP]: return 0
                if ta[colunaDoCEP] > tb[colunaDoCEP]: return 1
                return -1
          

        def intercalar (blocoAtual, tamBlocosAt, blocoAtualum, tamBlocosAtu,NomeArquivo):

                fArq = open("temp.dat","wb+")

                in1 = 0
                in2 = 0

                r1 = fAtual.read(registroCEP.size)
                r2 = fUM.read(registroCEP.size)

                r1un = registroCEP.unpack(r1)
                r2un = registroCEP.unpack(r2)


                while(in1 < tamBlocosAt and in2 < tamBlocosAtu):
                        if(cmp(r1un, r2un) < 0):
                                fArq.write(r1)
                                in1+=1
                                try:
                                        r1 = fAtual.read(registroCEP.size)
                                        r1un = registroCEP.unpack(r1)
                                except:
                                        break
                        else:
                                fArq.write(r2)
                                in2+=1
                                try:
                                        r2 = fUM.read(registroCEP.size)
                                        r2un = registroCEP.unpack(r2)
                                except:
                                        break
                                

                while (in1 < tamBlocosAt):
                        fArq.write(r1)
                        in1+=1
                        try:
                                r1 = fAtual.read(registroCEP.size)
                        except:
                                break

                while (in2 < tamBlocosAtu):
                        fArq.write(r2)
                        in2+=1
                        try:
                                r2 = fUM.read(registroCEP.size)
                        except:
                                break

                
                fArq.close()
                fAtual.close()
                fUM.close()
                os.remove(str(blocoAtual)+".dat")
                os.remove(str(blocoAtual+1) +".dat")
                os.rename('temp.dat', str(NomeArquivo)+".dat")

        tamBlocosAux=[]
        cont = 0
        while len(tamBlocos) != 1:
                tamBlocosAux = []
                numeroBlocos = len(tamBlocos)
                blocoAtual = 0
                contadorDeBlocos = 0
                while blocoAtual < numeroBlocos:
                        if blocoAtual+1 == len(tamBlocos):
                                tamBlocosAux.append(tamBlocos[blocoAtual])
                                if blocoAtual-2 != 0:
                                        os.rename(str(blocoAtual)+".dat", str(len(tamBlocosAux)-1)+".dat")
                                else:
                                        os.rename(str(blocoAtual)+".dat", str(len(tamBlocosAux)-1)+".dat")
                                        
                                blocoAtual += 2
                                break
                        else:
                                fAtual = open(str(blocoAtual) + ".dat","rb+")
                                fUM = open(str(blocoAtual+1) + ".dat","rb+")
                                intercalar(blocoAtual, tamBlocos[blocoAtual], blocoAtual+1, tamBlocos[blocoAtual+1],contadorDeBlocos)
                                tamBlocosAux.append(tamBlocos[blocoAtual] + tamBlocos[blocoAtual+1])
                                blocoAtual += 2
                                contadorDeBlocos += 1
                tamBlocos = tamBlocosAux

        os.rename('0.dat', "cep_ordenado.dat")

cProfile.run("profiling()")
