import pygame

pygame.init()

screen = pygame.display.set_mode((800,600),0)

AMARELO = (255,255,0)
PRETO = (0,0,0)

class Pacman:
    def __init__(self):
        self.centro_x = 400
        self.centro_y = 300
        self.temanho = 50
        self.velocidade_x = 1
        self.velocidade_y = 1
        self.raio = int(self.temanho / 2)

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
    
if __name__ == "__main__":
    pacman = Pacman()

    while True:
        #Calcular as regras
        pacman.calcular_regras()
        #Pintar tela
        screen.fill(PRETO)
        pacman.pintar(screen)

        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()