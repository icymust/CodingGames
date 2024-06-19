import pygame, controls
from gun import Gun # импортируем пушку 
from pygame.sprite import Group
from stats import Stats
from scores import Scores


# для запуска игры
def run():
    
    pygame.init() #инициализация
    screen = pygame.display.set_mode((700, 800)) #  размер окна для игры, ширина 700 , высота 800 пикселей
    pygame.display.set_caption("Space Defender") # название для игры
    bg_color = (0, 0, 0) #background color цвет заднего фона черный
    gun = Gun(screen) #присваеваем ган 
    bullets = Group()
    enemies = Group()
    controls.create_army(screen, enemies)
    stats = Stats() #сохранение статистики текущей игры
    sc = Scores(screen, stats) #вывод статистики
    
    
    # бесконечный цикл в котором будем все обрабатывать 
    while True:    
        
        controls.events(screen, gun, bullets) # вызываем функцию 
        if stats.run_game:
            gun.update_gun() # вызываем функцию по изменению движения
            controls.update(bg_color, screen, stats, sc, gun, enemies, bullets)
            controls.update_bullets(screen, stats, sc, enemies, bullets)
            controls.update_enemies(stats, screen, sc, gun, enemies, bullets)
        


run()