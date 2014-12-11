# -*- coding: utf-8 -*-
import pygame,os
class Button:
    def __init__(self,coords,weght,height):
        self.x=coords[0]
        self.y=coords[1]
        # self.image_normal = load_image(image_names[0],alpha_channel=True,dir_name=path)
        # self.image_on_over = load_image(image_names[1],alpha_channel=True,dir_name=path)
        # self.image_on_click = load_image(image_names[2],alpha_channel=True,dir_name=path)
        # self.images = [self.image_normal,self.image_on_over,self.image_on_click]

def load_image(name,alpha_cannel):
    fullname = os.path.join('Images', name)

    try:
        image = pygame.image.load(fullname) # Загружаем картинку и сохраняем поверхность (Surface)
    except (pygame.error): # Если картинки нет на месте
        print("Cannot load image:", name)
        return 0
    if(alpha_cannel):
        image = image.convert_alpha()
    else:
        image = image.convert()

if image:
    done = False
else:
    done = True

    return image
while not done: #главный цикл программы
    for e in pygame.event.get(): #цикл обработки очереди событий окна
        if e.type == pygame.QUIT: #Обработка события "Закрытие окна"
            done = True




    screen.fill(colors[i])
    screen.blit(image,(x,y))  #отрисовываем содержимое поверхности image на поверхность screen
    screen.blit(image2,(200,200))
    pygame.display.flip()       #показываем на экране все что нарисовали на основной поверхности
