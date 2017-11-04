import struct
import sys
import os
import time

#ARQUIVO PARA INTERCALACAO DOS BLOCOS ATRAVES DO MERGE SORT

inicio = time.time()

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
cepColumn = 5
print "Tamanho da Estrutura: %d" % registroCEP.size
tam = os.path.getsize("cepBlocos.dat")/registroCEP.size
tamBloco = 1000
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
def intercalar (blocoAtual, tamBlocosAt, blocoAtualum, tamBlocosAtu):
       
        ftemp.seek(0,os.SEEK_END)

        inicio = blocoAtual*tamBlocosAt
        f.seek(inicio*registroCEP.size)
        r1 = f.read(registroCEP.size)
        r1un = registroCEP.unpack(r1)
        
        inicio2 = blocoAtualum*tamBlocosAt
        f.seek(inicio2*registroCEP.size)
        r2 = f.read(registroCEP.size)
        r2un = registroCEP.unpack(r2)

        i = blocoAtual*tamBlocosAt
        j = blocoAtualum*tamBlocosAt
        
        while(i < inicio+tamBlocosAt and j < inicio2+tamBlocosAtu):
                if(cmp(r1un, r2un) < 0):
                        r1 = registroCEP.pack(r1un[0], r1un[1], r1un[2], r1un[3], r1un[4], r1un[5], r1un[6])
                        ftemp.write(r1)
                        i = i + 1
                        f.seek(i * registroCEP.size)
                        r1 = f.read(registroCEP.size)
                        r1un = registroCEP.unpack(r1)
                else:
                        r2 = registroCEP.pack(r2un[0], r2un[1], r2un[2], r2un[3], r2un[4], r2un[5], r2un[6])
                        ftemp.write(r2)
                        j = j + 1
                        f.seek(j * registroCEP.size)
                        r2 = f.read(registroCEP.size)
                        try:
                                r2un = registroCEP.unpack(r2)
                        except:
                                break

        while( i < inicio+tamBlocosAt):
                r1 = registroCEP.pack(r1un[0], r1un[1], r1un[2], r1un[3], r1un[4], r1un[5], r1un[6])
                ftemp.write(r1)
                i = i + 1
                f.seek(i* registroCEP.size)
                if i != inicio+tamBlocosAt:
                        r1 = f.read(registroCEP.size)
                        r1un = registroCEP.unpack(r1)


        while( j < inicio2+tamBlocosAtu):
                r2 = registroCEP.pack(r2un[0], r2un[1], r2un[2], r2un[3], r2un[4], r2un[5], r2un[6])
                ftemp.write(r2)
                j = j + 1
                f.seek(j* registroCEP.size)
                if j != inicio2+tamBlocosAtu:
                        r2 = f.read(registroCEP.size)
                        r2un = registroCEP.unpack(r2)

vetoraux=[]
cont = 0
while len(tamBlocos) != 1:
        vetoraux = []
        numeroBlocos = len(tamBlocos)
        blocoAtual = 0
        f = open("cepBlocos.dat","rb+")
        ftemp = open("cepTemp.dat", "wb+")
        f.seek(0,0)
        while blocoAtual < numeroBlocos:
                aux = blocoAtual
                if blocoAtual+1 == len(tamBlocos):
                        vetoraux.append(tamBlocos[blocoAtual])

                        inicioBloco = blocoAtual * tamBlocos[0]
                        finalBloco = inicioBloco + tamBlocos[blocoAtual]
                        i = inicioBloco

                        f.seek(inicioBloco*registroCEP.size)
                        cont = 0
                        while( inicioBloco < finalBloco):
                                cont +=1
                                r1 = f.read(registroCEP.size)
                                ftemp.write(r1)
                                inicioBloco += 1

                        blocoAtual += 2
                else:
                        intercalar(blocoAtual, tamBlocos[blocoAtual], blocoAtual+1, tamBlocos[blocoAtual+1])
                        vetoraux.append(tamBlocos[blocoAtual] + tamBlocos[blocoAtual+1])
                        blocoAtual += 2
                        
        f.close()
        ftemp.close()
        os.remove("cepBlocos.dat")
        os.rename('cepTemp.dat', 'cepBlocos.dat')
        tamBlocos = vetoraux

final = time.time()- inicio
print 'fim em: ',final
print tamBlocos


