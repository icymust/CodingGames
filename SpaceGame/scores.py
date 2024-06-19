import pygame.font
from gun import Gun
from pygame.sprite import Group

class Scores():
    #вывод игровой информации
    def __init__(self, screen, stats):
        #инифиализируем подсчет очков
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (34, 177, 76) # color text
        self.font = pygame.font.SysFont(None, 36) # шрифт и размер
        self.image_score()
        self.image_high_score()
        self.image_guns_left()
        
    def image_score(self):
        #преобразовывет текст счета в графичиское изображение
        #рендерим текст , приобразуем в строчку счета, цвет текста и фона 
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect() # делаем из него прямоугольник
        self.score_rect.right = self.screen_rect.right - 40 #выводим текст справо 40 пикселей
        self.score_rect.top = 20 #отступаем от верха 20 пикселей
    
    def image_high_score(self):
        #преобразует рекод в графическое изображение
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20
        
    def image_guns_left(self):
        #количество жизни для вывода
        self.guns = Group() #группируем все пушки которые есть
        for gun_number in range(self.stats.guns_left): # выводим пушки
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width # распологаем их вверху экрана по корденате Х
            gun.rect.y = 20
            self.guns.add(gun)
    
    def show_score(self):
        #вывод всего на экран
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect) 
        self.guns.draw(self.screen)
        
    