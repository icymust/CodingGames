import pygame, controls
from gun import Gun # импортируем пушку 

# для запуска игры
def run():
    
    pygame.init() #инициализация
    screen = pygame.display.set_mode((700, 800)) #  размер окна для игры
    pygame.display.set_caption("Space Defender") # название для игры
    bg_color = (0, 0, 0) #background color цвет заднего фона черный
    gun = Gun(screen) #присваеваем ган 
    
    # бесконечный цикл в котором будем все обрабатывать 
    while True:    
        
        controls.events(gun) # вызываем функцию 
        gun.update_gun() # вызываем функцию по изменению движения
        controls.update(bg_color, screen, gun)
    

run()