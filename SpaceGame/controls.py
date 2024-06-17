import pygame, sys # для обработки событий и закрытие игрового окна

def events(gun):
    #обработка событий
    
    for event in pygame.event.get(): #собираем / получаем  / перебираем все события
            if event.type == pygame.QUIT: # если крестик , то выход
                sys.exit()   
                
            elif event.type == pygame.KEYDOWN: # если кнопка нажата , то меняем на тру
                # вправо
                if event.key == pygame.K_RIGHT: # кнопка стрелка в право 
                    gun.mright = True # если кнопка нажата ,то тру для движения 
                # Влево
                elif event.key == pygame.K_LEFT: # кнопка влево 
                    gun.mleft = True
                    
            elif event.type == pygame.KEYUP: # если кнопка отжата , то присваеваем  фалс
                # вправо
                if event.key == pygame.K_RIGHT:
                    gun.mright = False
                # Влево
                elif event.key == pygame.K_LEFT:
                    gun.mleft = False
                    
def update(bg_color, screen, gun):
    #обновление экрана
    screen.fill(bg_color) # вызываем фоновый цвет
    gun.output() # вывод на экран пушки
    pygame.display.flip() 