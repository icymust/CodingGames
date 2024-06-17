import pygame

#описание всего что связано с пушкой
class Gun():

    def __init__ (self, screen):
        ### инициализация пушки ###
        
        self.screen = screen # получаем экран 
        self.image = pygame.image.load('SpaceGame/images/img_gun.png') # загружаем фотографию пушки
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self. screen_rect.bottom
        
        # делаем фалс для такого чтобы когда кнопка отжата , то будет фалс
        self.mright = False 
        self.mleft = False
        
    # функция которая будет выводить нашу пушку  
    def output(self):
        # рисование пушки
        self.screen.blit(self.image, self.rect)
        
    def update_gun(self):
        # обновление позиции пушки
        if self.mright and self.rect.right < self.screen_rect.right: # если правая край пушки меньще конец экрана , то можем двигать
            self.center += 1.5
        elif self.mleft and self.rect.left > self.screen_rect.left:
            self.center -= 1.5
            
        self.rect.centerx = self.center
            