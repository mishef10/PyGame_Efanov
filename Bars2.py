import pygame
class Block:
    def __init__(self, coords, width, height, color):
        self.x = coords[0]
        self.y = coords[1]
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = coords[0]
        self.rect.y = coords[1]
    def render(self,screen):
        screen.blit(self.image,self.rect)
pygame.init() #инициализация
display = pygame.display.set_mode((400,400)) #создание окна
block1=Block((5,5),30,30,(44,44,44))
block2=Block((80,80),30,30,(44,44,44))
block3=Block((150,150),30,30,(34,23,66))
x=0
while x!=1:
    display.fill((55,00,99))
    for e in pygame.event.get():
        # print(e)
        if e.type == 12:
            x=1
    if e.type == pygame.MOUSEBUTTONDOWN:
        pass

    block1.render(display)
    block2.render(display)
    block3.render(display)

    pygame.display.flip()
