#CONWAY'S GAME OF LIFE DO PRIMEIRO ANO
from time import sleep
import matplotlib.pyplot as plt
def printJogo(jogo,x):
    for i in range(x):
        print(jogo[i])
def adjacentes(jogo,x,y,limiteX,limiteY):
    tot=0
    for i in range(-1,2):
        for j in range(-1,2):
            if (not(x+i==x and y+j==y) and i+x>=0 and i+x<limiteX and j+y>=0 and j+y<limiteY):
                tot+=int(jogo[x+i][y+j])
    return tot
def criarGrafico(jogo,x,y):
    fig, ax = plt.subplots()
    jogoInvertido = jogo.copy()
    jogoInvertido.reverse()
    ax.pcolormesh(range(x+1), range(y+1), jogoInvertido)
    plt.show()
x=int(input("Largura da tabela "))
y=int(input("Altura da tabela "))
seg=float(input("Tempo entre cada atualização (em segundos) "))
jogoAtual=[]
jogoSeguinte=[]
for i in range(x):
    jogoAtual.append([])
    jogoSeguinte.append([])
print("0 para celula morta, 1 para celula viva, sem separar por espaços")
strIn=str()
'''
for i in range(x):
    for j in range(y): 
        print("Linha número",i,"Coluna número",j)
        jogoAtual[i].append(int(input()))
        jogoSeguinte[i].append("")
'''


for i in range(x):
    print ("Linha número",i+1,end="")
    strIn=str(input())
    for j in range(y):
        jogoAtual[i].append(0)
        jogoAtual[i][j]=int(strIn[j])
        jogoSeguinte[i].append(0)

while(True):
    printJogo(jogoAtual,x)
    criarGrafico(jogoAtual,x,y)
    print("\n")
    for i in range(x):
        for j in range(y):
            if (jogoAtual[i][j]==0):
                if (adjacentes(jogoAtual,i,j,x,y)==3):
                    jogoSeguinte[i][j]=1
                else:
                    jogoSeguinte[i][j]=0
            else:
                if (adjacentes(jogoAtual,i,j,x,y)==2 or adjacentes(jogoAtual,i,j,x,y)==3):
                    jogoSeguinte[i][j]=1
                else:
                    jogoSeguinte[i][j]=0
    jogoAtual=jogoSeguinte.copy()
    jogoSeguinte=[]
    for i in range(x):
        jogoSeguinte.append([])
        for j in range(y):
            jogoSeguinte[i].append("")
    sleep(seg)
