import struct
import sys
import os
import time

#ARQUIVO DE ORDENACAO DE BLOCOS COM TAMANHOS ESCOLHIDOS PELO USUARIO

if len(sys.argv) != 2:
	tamBloco = int(input("Entre com o numero de linhas de cada bloco: "))
else:
	tamBloco = int(sys.argv[1])

inicio = time.time()

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
cepColumn = 5
print "Tamanho de cada linha do arquivo: %d" % registroCEP.size

f = open("cep.dat","rb+")
fAux = open("cepBlocos.dat","wb+")

tam = os.path.getsize("cep.dat")/registroCEP.size
tamBlocos = []
qtdBlocos = tam / tamBloco
resto = tam - (tamBloco * qtdBlocos)
tamBlocos = [tamBloco] * qtdBlocos
if resto > 0:
	tamBlocos.append(resto)

#Funcao para comparacao de tuplas
def cmp ( ta, tb ):
	if ta[cepColumn] == tb[cepColumn]: return 0
	if ta[cepColumn] > tb[cepColumn]: return 1
	return -1

cont2 = 0 #variavel para conseguir se locomover no arquivo

for i in tamBlocos:	
	listOrdena = []
	cont = i #variavel para controlar o numero de leituras com a quantidade de linhas de cada bloco
	while cont != 0:
		line = f.read(registroCEP.size)
		line_t = registroCEP.unpack(line)
		listOrdena.append(line_t)
		cont = cont - 1
	listOrdena.sort(cmp)
	for j in range(i): 
		line_pack = registroCEP.pack(listOrdena[j][0], listOrdena[j][1], listOrdena[j][2], listOrdena[j][3], listOrdena[j][4], listOrdena[j][5], listOrdena[j][6])
		fAux.write(line_pack) #escreve no mesmo arquivo
	listOrdena = []
	
print "Fim do programa"

f.close()
fAux.close()

final = time.time() - inicio
print "Tempo: ",final
