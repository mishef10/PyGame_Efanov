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
        self.drag = False

    def draw(self):
        pygame.draw.rect(self.image, self.color, ((0,0),(self.width,self.height)))

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # flag=True
                if self.collidePoint(event.pos[0], event.pos[1]) == True:
                    self.drag = True
                    print("Flag True")
        if event.type==pygame.MOUSEMOTION:
            if self.drag==True:
                self.moveON(event.rel[0],event.rel[0])


    def collidePoint(self,mouse_x, mouse_y):
        if self.x<mouse_x<self.x+self.width and self.y<mouse_y<self.y+self.height:
            flag2=True
            print("True")
            return True
        else:
            print("False")
            return False

    def moveON(self,move_x,move_y):
        self.rect.x+=move_x
        self.rect.y+=move_y

    def render(self,screen):
        screen.blit(self.image,self.rect)

pygame.init() #инициализация
display = pygame.display.set_mode((400,400)) #создание окна
block1=Block((50,60),100,100,(0,100,0))
# block2=Block((80,80),30,30,(44,44,44))
x=0
while x!=1:

    for e in pygame.event.get():

        # print(e)

        if e.type == pygame.QUIT:
            x=1
        if e.type == pygame.MOUSEBUTTONDOWN:
            block1.events(e)
        elif e.type == pygame.MOUSEMOTION:
            block1.events(e)

    display.fill((55,00,99))
    block1.render(display)
    # block2.render(display)


    pygame.display.flip()
