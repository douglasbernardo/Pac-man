import pygame

pygame.init()

screen = pygame.display.set_mode((800,600),0)

AMARELO = (255,255,0)
PRETO = (0,0,0)
AZUL = (0,0,255)

class Cenario:
    def __init__(self,tamanho):
        self.tamanho = tamanho
        self.matriz = [
            
            [2,2,2,2,2],
            [2,0,2,0,2],
            [2,0,2,0,2],
            [2,0,2,0,2],
            [2,2,2,2,2]

        ]
    
    def pintar_linha(self,tela,numero_linha,linha):
        for numero_coluna,coluna in enumerate(linha): #Devolve o valor e o indice da coluna
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho

            cor = PRETO
            if coluna == 2:
                cor = AZUL

            pygame.draw.rect(tela,cor,(x,y,self.tamanho,self.tamanho),0)




    def pintar(self,tela):
        for numero_linha,linha in enumerate(self.matriz):
            self.pintar_linha(tela,numero_linha,linha)






class Pacman:
    def __init__(self):
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = int(800/30)
        self.velocidade_x = 1
        self.velocidade_y = 1
        self.raio = int(self.tamanho / 2)

    def calcular_regras(self):
        self.centro_x += self.velocidade_x
        self.centro_y += self.velocidade_y
        if self.centro_x + self.raio > 800:
            self.velocidade_x -= 1
        
        if self.centro_x - self.raio < 0:
            self.velocidade_x += 1

        if self.centro_y + self.raio > 600:
            self.velocidade_y -= 1

        if self.centro_y - self.raio < 0:
            self.velocidade_y += 1

    def pintar(self,tela):
        #Desenho do Pac-Man
        pygame.draw.circle(tela,AMARELO,(self.centro_x,self.centro_y),self.raio,0)
        #Desenho da boca do Pac-Man
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)

        pontos = [canto_boca,labio_superior,labio_inferior]

        pygame.draw.polygon(tela,PRETO,pontos,0)
        #Desenho do olho do Pac-Man
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)

        olho_raio = int(self.raio * 0.15)

        pygame.draw.circle(tela,PRETO,(olho_x,olho_y),olho_raio,0)
    
    def processar_eventos(self,eventos):
        for e in eventos:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x += 1
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x -= 1
                elif e.key == pygame.K_UP:
                    self.velocidade_y -= 1
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y += 1
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.velocidade_x = 0
                elif e.key == pygame.K_LEFT:
                    self.velocidade_x = 0
                elif e.key == pygame.K_UP:
                    self.velocidade_y = 0
                elif e.key == pygame.K_DOWN:
                    self.velocidade_y = 0

if __name__ == "__main__":
    pacman = Pacman()
    cenario = Cenario(600 // 30)

    while True:
        #Calcular as regras
        pacman.calcular_regras()
        #Pintar tela
        screen.fill(PRETO)
        cenario.pintar(screen)
        pacman.pintar(screen)

        pygame.display.update()

        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
            
        pacman.processar_eventos(eventos)