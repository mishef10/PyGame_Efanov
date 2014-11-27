import pygame
class Block:
    def __init__(self, coords, width, height, color):
        self.x = coords[0]
        self.y = coords[1]
        self.width = width
        self.height = height
        self.color = color
        self.color2 = (100,0,0)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x = coords[0]
        self.rect.y = coords[1]
        self.drag = False
        self.drop = False
        self.widthDrag = 10
        self.heightDrag = 10
        self.rectDragX = self.width-self.widthDrag
        self.rectDragY = self.height-self.heightDrag

        # print(self.rect.w, self.rect.h)
        self.colorDrag = (255,0,0)
        self.draw()

    def draw(self):
        pygame.draw.rect(self.image, self.color, ((0,0),(self.width,self.height)))
        pygame.draw.rect(self.image,self.colorDrag,((self.rectDragX,self.rectDragY),(self.widthDrag,self.heightDrag)))

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.pos[0],event.pos[1])
                print(self.rectDragX)
                print(self.rectDragY)
                print(self.widthDrag)
                print(self.heightDrag)
                if self.collidePoint(event.pos[0], event.pos[1]) == True:
                    self.drag = True
                    print("Flag True")
        if event.type == pygame.MOUSEBUTTONUP:
            self.drag = False
        if event.type==pygame.MOUSEMOTION:
            if self.drop==True:
                self.DragDrop(event.rel[0],event.rel[1])
            if self.drag==True:
                self.moveON(event.rel[0],event.rel[1])


    def collidePoint(self,mouse_x, mouse_y):
        # Метод принемает позицию мыши и возвращает значчение:
        # 'True'- мышь находится в прямоугольние,
        # 'False' - мышь не находистя в прямоугольнике
        if self.rectDragX<mouse_x<self.rectDragX+self.widthDrag and self.rectDragY<mouse_y<self.rectDragY+self.heightDrag:
            self.drop=True
            print("True")
            return False
        if self.rect.x<mouse_x<self.rect.x+self.width and self.rect.y<mouse_y<self.rect.y+self.height:
            color=self.color
            self.color=self.color2
            self.color2=color
            return True
        else:
            print("False")
            return False


    def moveON(self,move_x,move_y):
        self.rect.x+=move_x
        self.rect.y+=move_y

    def DragDrop(self,move_x,move_y):
        self.width=self.width+move_x
        self.height=self.height+move_y



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
        if e.type == pygame.MOUSEBUTTONUP:
            block1.events(e)
        if e.type == pygame.QUIT:
            x=1
        if e.type == pygame.MOUSEBUTTONDOWN:
            block1.events(e)
        elif e.type == pygame.MOUSEMOTION:
            block1.events(e)

    display.fill((55,00,99))
    block1.draw()
    block1.render(display)
    # block2.render(display)


    pygame.display.flip()
