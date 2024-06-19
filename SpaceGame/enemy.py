import pygame

class Enemy(pygame.sprite.Sprite):
    # класс одного пришельца
    def __init__(self, screen):
        #инициализируем и задаем начальную позицию
        super(Enemy, self).__init__()
        self.screen = screen # место где отрисовываем
        self.image = pygame.image.load('SpaceGame/images/enemy.png')
        self.rect = self.image.get_rect() #приоброзовали в прямоугольник 
        self.rect.x = self.rect.width # по Х отслеживаем ширину
        self.rect.y = self.rect.height # по Y отсживаем высоту
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def draw(self): 
        #вывод пришельца на экран
        self.screen.blit(self.image, self.rect) # выводит 
        
    def update(self):
        # перемещает врагов на пушку
        self.y += 0.1
        self.rect.y = self.y