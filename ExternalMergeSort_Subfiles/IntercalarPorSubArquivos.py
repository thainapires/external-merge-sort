import struct
import sys
import os
import time

#ARQUIVO PARA INTERCALACAO DOS BLOCOS ATRAVES DO MERGE SORT

inicio = time.time()

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
cepColumn = 5
print "Tamanho da Estrutura: %d" % registroCEP.size
tam = 100
#tam = os.path.getsize("cep.dat")/registroCEP.size
tamBloco = 10
tamBlocos = []
qtdBlocos = tam / tamBloco
resto = tam - (tamBloco * qtdBlocos)
tamBlocos = [tamBloco] * qtdBlocos
if resto > 0:
	tamBlocos.append(resto)

def cmp ( ta, tb ):
	if ta[cepColumn] == tb[cepColumn]: return 0
	if ta[cepColumn] > tb[cepColumn]: return 1
	return -1
  
blocoAtual = 0

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

vetoraux=[]
cont = 0
while len(tamBlocos) != 1:
        vetoraux = []
        numeroBlocos = len(tamBlocos)
        blocoAtual = 0
        contadorDeBlocos = 0
        while blocoAtual < numeroBlocos:
                if blocoAtual+1 == len(tamBlocos):
                        vetoraux.append(tamBlocos[blocoAtual])
                        if blocoAtual-2 != 0:
                                os.rename(str(blocoAtual)+".dat", str(len(vetoraux)-1)+".dat")
                        else:
                                os.rename(str(blocoAtual)+".dat", str(len(vetoraux)-1)+".dat")
                                
                        blocoAtual += 2
                        break
                else:
                        fAtual = open(str(blocoAtual) + ".dat","rb+")
                        fUM = open(str(blocoAtual+1) + ".dat","rb+")
                        intercalar(blocoAtual, tamBlocos[blocoAtual], blocoAtual+1, tamBlocos[blocoAtual+1],contadorDeBlocos)
                        vetoraux.append(tamBlocos[blocoAtual] + tamBlocos[blocoAtual+1])
                        blocoAtual += 2
                        contadorDeBlocos += 1
        tamBlocos = vetoraux

os.rename('0.dat', "cep_ordenado.dat")

final = time.time()- inicio
print 'fim em: ',final
print tamBlocos
