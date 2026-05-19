import pygame
pygame.init

#Frame creator
pygame.display.set_caption("Les Jeux de la peur")
screen=pygame.display.set_mode((1080,720))

background=pygame.image.load("BG.png")
running=True

#While pour maintenir la fenetre

while running:
    #display bg
    screen.blit(background, (0,0))
    #refresh screen
    pygame.display.flip()

    for event in pygame.event.get():     #pygame event return une list de chaque event, la variale event c'est le dernier event
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
            print("Succesfully closed")