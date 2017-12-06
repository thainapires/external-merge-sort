#ARQUIVO PARA INTERCALACAO DOS BLOCOS ATRAVES DO MERGE SORT

import struct
import sys
import os
import time

#Entrada do usuario
if len(sys.argv) != 2:
	tamanhoDoBloco = int(input("Entre com o numero de linhas de cada bloco: "))
else:
	tamanhoDoBloco = int(sys.argv[1])

inicio = time.time()

'''Definicao da estrutura do arquivo, assim como calculo da quantidade de blocos, armazenando em uma lista onde cada indice indica a quantidade
de linhas que o bloco do determinado indice possui'''

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
colunaDoCEP = 5
qtdLinhasTotal = os.path.getsize("cep.dat")/registroCEP.size
tamBlocos = []
qtdBlocos = qtdLinhasTotal / tamanhoDoBloco
resto = qtdLinhasTotal - (tamanhoDoBloco * qtdBlocos)
tamBlocos = [tamanhoDoBloco] * qtdBlocos
if resto > 0:
	tamBlocos.append(resto)

#Funcao para comparacao de tuplas
def cmp ( ta, tb ):
	if ta[colunaDoCEP] == tb[colunaDoCEP]: return 0
	if ta[colunaDoCEP] > tb[colunaDoCEP]: return 1
	return -1
        
#Funcao que faz a juncao dos blocos de dois em dois
def intercalar (blocoAtual, tamBlocosAt, blocoAtualum, tamBlocosAtu):

        ftemp.seek(0,os.SEEK_END)

        inicio = blocoAtual*tamBlocosAt
        fAux.seek(inicio*registroCEP.size)
        r1 = fAux.read(registroCEP.size)
        r1un = registroCEP.unpack(r1)
        
        inicio2 = blocoAtualum*tamBlocosAt
        fAux.seek(inicio2*registroCEP.size)
        r2 = fAux.read(registroCEP.size)
        r2un = registroCEP.unpack(r2)

        i = blocoAtual*tamBlocosAt
        j = blocoAtualum*tamBlocosAt
        
        while(i < inicio+tamBlocosAt and j < inicio2+tamBlocosAtu):
                if(cmp(r1un, r2un) < 0):
                        r1 = registroCEP.pack(r1un[0], r1un[1], r1un[2], r1un[3], r1un[4], r1un[5], r1un[6])
                        ftemp.write(r1)
                        i = i + 1
                        fAux.seek(i * registroCEP.size)
                        r1 = fAux.read(registroCEP.size)
                        r1un = registroCEP.unpack(r1)
                else:
                        r2 = registroCEP.pack(r2un[0], r2un[1], r2un[2], r2un[3], r2un[4], r2un[5], r2un[6])
                        ftemp.write(r2)
                        j = j + 1
                        fAux.seek(j * registroCEP.size)
                        r2 = fAux.read(registroCEP.size)
                        try:
                                r2un = registroCEP.unpack(r2)
                        except:
                                break

        while( i < inicio+tamBlocosAt):
                r1 = registroCEP.pack(r1un[0], r1un[1], r1un[2], r1un[3], r1un[4], r1un[5], r1un[6])
                ftemp.write(r1)
                i = i + 1
                fAux.seek(i* registroCEP.size)
                if i != inicio+tamBlocosAt:
                        r1 = fAux.read(registroCEP.size)
                        r1un = registroCEP.unpack(r1)


        while( j < inicio2+tamBlocosAtu):
                r2 = registroCEP.pack(r2un[0], r2un[1], r2un[2], r2un[3], r2un[4], r2un[5], r2un[6])
                ftemp.write(r2)
                j = j + 1
                fAux.seek(j* registroCEP.size)
                if j != inicio2+tamBlocosAtu:
                        r2 = fAux.read(registroCEP.size)
                        r2un = registroCEP.unpack(r2)

tamBlocosAux=[] #lista auxiliar para ajudar na alteracao da lista que contem as quantidades de linhas de cada bloco  
cont = 0 
#enquanto o tamanho da lista nao for igual a um, eh porque ainda faltam blocos a juntar
while len(tamBlocos) != 1: 
        tamBlocosAux = []
        numeroBlocos = len(tamBlocos)
        blocoAtual = 0
        ftemp = open("cepTemp.dat", "wb+")
        fAux = open("cep_ordenado.dat", "rb+")
        fAux.seek(0,0)
        #enquanto o bloco atual nao chegar ao numeroBlocos -1 eh porque ainda nao terminou de juntar os blocos da lista
        while blocoAtual < numeroBlocos:
        		#caso o bloco nao tenha outro com o qual juntar, escreve ele no final do arquivo e acrescenta na lista 
                if blocoAtual+1 == len(tamBlocos):
                        tamBlocosAux.append(tamBlocos[blocoAtual])
                        inicioBloco = blocoAtual * tamBlocos[0]
                        finalBloco = inicioBloco + tamBlocos[blocoAtual]
                        #i = inicioBloco
                        fAux.seek(inicioBloco*registroCEP.size)
                        cont = 0
                        while( inicioBloco < finalBloco):
                                cont +=1
                                r1 = fAux.read(registroCEP.size)
                                ftemp.write(r1)
                                inicioBloco += 1
                        blocoAtual += 2
                #caso contrario, junta com o bloco seguinte
                else:
                        intercalar(blocoAtual, tamBlocos[blocoAtual], blocoAtual+1, tamBlocos[blocoAtual+1])
                        tamBlocosAux.append(tamBlocos[blocoAtual] + tamBlocos[blocoAtual+1])
                        blocoAtual += 2
        #fecha os arquivos para deletar o menos atualizado e renomear o mais atualizado                   
        fAux.close()
        ftemp.close()
        os.remove("cep_ordenado.dat")
        os.rename('cepTemp.dat', 'cep_ordenado.dat')
        tamBlocos = tamBlocosAux


final = time.time()
print "Tempo: ",final-inicio
