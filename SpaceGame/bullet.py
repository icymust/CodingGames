import pygame

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, screen, gun):
        # Создание пули в позиции пушки
        super(Bullet, self).__init__()
        self.screen = screen # обьект экрана, загрузили экран
        self.rect = pygame.Rect(0, 0, 2, 12) # рисуеп прямоугольник маленький, 0 и 0 кординаты где она будет, 2 и 12 ширина и высота пули в пикселях
        self.color = 34, 177, 76 # color bullet
        self.speed = 4 # bullet speed
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top 
        self.y = float(self.rect.y)
        
    def update(self):
        #перемещение пули вверх
        self.y -= self.speed 
        self.rect.y = self.y
        
    def draw_bullet(self):
        #рисуем пулю на экране
        pygame.draw.rect(self.screen, self.color, self.rect)
        