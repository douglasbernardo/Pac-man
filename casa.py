import pygame
pygame.init()
tela = pygame.display.set_mode((640, 480), 0)

while True:
    
    pygame.draw.line(tela, (255, 255, 0), (320, 0), (600, 240), 5)
    pygame.draw.line(tela, (255, 255, 0), (320, 0), (40, 240), 5)
    pygame.draw.rect(tela, (255, 255, 0), ((40, 240), (560, 200)), 5)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()