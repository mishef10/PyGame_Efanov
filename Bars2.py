import pygame
class Block:
    def __init__(self, coords, width, height, color):
        self.x = coords[0]
        self.y = coords[1]
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface((width, height))
        self.draw()
        self.rect = self.image.get_rect()
        self.rect.x = coords[0]
        self.rect.y = coords[1]

    def draw(self):
        pygame.draw.rect(self.image, self.color, ((0,0),(self.width,self.height)))

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                self.collidePoint()

    def collidePoint(self):
        if self.x>e.pos[0]<self.x+self.width and self.y>e.pos[1]<self.y+self.height:
            print("True")
        else:
            print("False")

    def moveON(self):
         for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    self.x=self.x+e.rel[0]
                    self.y=self.y+e.rel[1]

    def render(self,screen):
        screen.blit(self.image,self.rect)

pygame.init() #инициализация
display = pygame.display.set_mode((400,400)) #создание окна
block1=Block((10,10),100,100,(0,100,0))
# block2=Block((80,80),30,30,(44,44,44))
x=0
while x!=1:

    for e in pygame.event.get():

        # print(e)

        if e.type == pygame.QUIT:
            x=1
        if e.type == pygame.MOUSEBUTTONDOWN:
            block1.events(e)

    display.fill((55,00,99))
    block1.render(display)
    # block2.render(display)
    block1.collidePoint()

    pygame.display.flip()
