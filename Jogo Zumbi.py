from tkinter import *
from time import sleep as s
from random import randint as r


XI = 224
YI = 418
velocidade_pulo = 6
pode_pular = True
personagem = [[]]
ataque = [[]]
piso = [[]]
zumbi = [[]]
contPiso = 0
lop1 = True
XZ = 50
contSpawnZumbi = 0
vida = 3
vivo = True
pontos = 0



def VerificarVidaEDano():
    global vida
    global pers
    global vivo
    global XZ
    global XI
    global nvida

    if XZ >= XI - 15 and XZ <= XI + 16 and vivo == True:
        vida -= 1
        nvida.destroy()
        nvida = Label(tela, text='VIDA = {}'.format(vida))
        nvida['bg'] = 'black'
        nvida['fg'] = 'white'
        nvida.place(x=15, y=15)
        
    if vida <= 0:
        pers['bg'] = 'cyan'
        pers['fg'] = 'cyan'
        pers.place(x=XI, y=YI)
        vivo = False
        
def AtaqueZumbi():
    global zumbi
    global pers
    global zombiatack
    global XZ
    global VidaZumbi
    global vida
    global XI
    
    VidaZumbi = 3
    zombiatack = Label(tela, text=zumbi)
    zombiatack['bg'] = 'cyan'
    zombiatack['fg'] = 'cyan'
    zombiatack.place(x=XZ, y=418)


        
    tela.update()
    
def ZumbiMovimento():
    global XI
    global zombiatack
    global XZ
    global VidaZumbi
    global vivo
    global pontos
    global npontos

    if vivo == True:
        if XZ > XI:
            XZ -= 2
        if XZ < XI:
            XZ += 2
        zombiatack.place(x=XZ, y=418)
        if VidaZumbi <= 0:
            if r(1, 2) == 1:
                XZ = -18
                zombiatack.place(x=XZ, y=418)
            else:
                XZ = 466
                zombiatack.place(x=XZ, y=418)
            pontos += 1
            npontos.destroy()
            npontos = Label(tela, text='PONTUAÇÃO = {}'.format(pontos))
            npontos['bg'] = 'black'
            npontos['fg'] = 'white'
            npontos.place(x=15, y=35)
            VidaZumbi = 3
    tela.update()
    s(0.026)
#===========FAZER-PULO==========#
def Ir_up(key):
    global XI
    global YI
    global velocidade_pulo
    global pers
    global pode_pular
    global zombiatack
    global XZ
    global frame
    global vivo
    
    
    if pode_pular == True:
        pode_pular = False
        velocidade_pulo = 16
        for c in range(0, 12):
            YI -= 6
            pers.place(x=XI, y=YI)
            if vivo == True:
                if XZ > XI:
                    XZ -= 1
                if XZ < XI:
                    XZ += 1
                zombiatack.place(x=XZ, y=418)
            s(0.026)
            tela.update()
        for c in range(0, 12):
            YI += 6
            pers.place(x=XI, y=YI)
            if vivo == True:
                if XZ > XI:
                    XZ -= 1
                if XZ < XI:
                    XZ += 1
                zombiatack.place(x=XZ, y=418)
            s(0.026)
            tela.update()
        velocidade_pulo = 6
        pode_pular = True

#==========FAZER-RECARGA========#
'''
def Ir_down(key):
    global XI
    global YI
    global pers

    YI += 6
    if YI > 437:
        YI = 437
    pers.place(x=XI, y=YI)
'''
#===========MOVIMENTO============#
def Ir_left(key):
    global XI
    global YI
    global pers
    global velocidade_pulo

    XI -= velocidade_pulo
    if XI < 0:
        XI = 0
    pers.place(x=XI, y=YI)


def Ir_right(key):
    global XI
    global YI
    global pers
    global velocidade_pulo

    XI += velocidade_pulo
    if XI > 432:
        XI = 433
    pers.place(x=XI, y=YI)

'''
def Atacar_cima(Key):
    global XI
    global YI
    global pers
    global ataque1

    ataque1.place(x=XI + 1, y=YI - 19)
    tela.update()    
    ataque1.place(x=-30, y=-30)


def Atacar_baixo(Key):
    global XI
    global YI
    global pers
    global ataque1

    ataque1.place(x=XI + 1, y=YI + 19)
    tela.update()
    ataque1.place(x=-30, y=-30)
'''

def Atacar_esquerda(Key):
    global XI
    global YI
    global pers
    global ataque1
    global VidaZumbi
    global XZ

    ataque1.place(x=XI - 16, y=YI)
    if XZ >= XI - 35 and XZ < XI:
        VidaZumbi -= 1
    
    tela.update()
    s(0.026)
    ataque1.place(x=-30, y=-30)


def Atacar_direita(Key):
    global XI
    global YI
    global pers
    global ataque1
    global VidaZumbi
    global XZ

    ataque1.place(x=XI + 16, y=YI)
    if XZ <= XI + 35 and XZ > XI:
        VidaZumbi -= 1
    tela.update()
    s(0.026)
    ataque1.place(x=-30, y=-30)
    
def main():
    global XI
    global YI
    global pers
    global ataque1
    global contPiso
    global frame
    global nvida
    global vida
    global npontos
    global pontos

    pers = Label(tela, text=personagem)
    pers['bg'] = 'blue'
    pers['fg'] = 'blue'
    pers.place(x=XI, y=YI)
    
    ataque1 = Label(tela, text=ataque)
    ataque1['fg'] = 'red'
    ataque1['bg'] = 'red'

    nvida = Label(tela, text='VIDA = {}'.format(vida))
    nvida['bg'] = 'black'
    nvida['fg'] = 'white'
    nvida.place(x=15, y=15)
    
    npontos = Label(tela, text='PONTUAÇÃO = {}'.format(pontos))
    npontos['bg'] = 'black'
    npontos['fg'] = 'white'
    npontos.place(x=15, y=35)

    frame = Frame(tela)
    frame.bind("<d>", Ir_right)
    frame.bind("<a>", Ir_left)
    frame.bind("<w>", Ir_up)
    #frame.bind("<s>", Ir_down)
    
    #frame.bind("<i>", Atacar_cima)
    #frame.bind("<k>", Atacar_baixo)
    frame.bind("<j>", Atacar_esquerda)
    frame.bind("<l>", Atacar_direita)
    frame.focus_set()
    frame.place(x=-30, y=-30)
    
    for z in range(0, 28):
        terra = Label(tela, text=piso)
        terra['bg'] = 'green'
        terra['fg'] = 'green'
        terra.place(x=contPiso, y=437)
        contPiso += 16



tela = Tk()
tela.geometry('448x456+150+150')
tela.title('JogoQuadrado')
tela['bg'] = 'black'

while __name__=="__main__":

    if lop1 == True:
        main()
        AtaqueZumbi()
        lop1 = False
    try:
        ZumbiMovimento()
        VerificarVidaEDano()
        tela.update()
    except:
        break
    s(0.026)
    
try:
    tela.mainloop()
except:
    pass
