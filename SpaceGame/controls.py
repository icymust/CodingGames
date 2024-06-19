import pygame, sys # для обработки событий и закрытие игрового окна
from bullet import Bullet
from enemy import Enemy
import time

def events(screen, gun, bullets):
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
                #нопка стрелять
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen, gun)
                    bullets.add(new_bullet)
                    
            elif event.type == pygame.KEYUP: # если кнопка отжата , то присваеваем  фалс
                # вправо
                if event.key == pygame.K_RIGHT:
                    gun.mright = False
                # Влево
                elif event.key == pygame.K_LEFT:
                    gun.mleft = False
                    
def update(bg_color, screen,stats, sc, gun, enemies, bullets):
    #обновление экрана
    screen.fill(bg_color) # вызываем фоновый цвет
    sc.show_score(  )
    for bullet in bullets.sprites(): # отрисовываем пулю
        bullet.draw_bullet()
    gun.output() # вывод на экран пушки
    enemies.draw(screen)
    pygame.display.flip() 
    
def update_bullets(screen, stats, sc,  enemies, bullets):
    #обновлять позиции пуль , и удалять не нужные
    bullets.update() # рисуем пули 
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0 :
            bullets.remove(bullet) # удаляет пули
    # проверка попадиний в пришельцев
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True) # если обьект попадает на обьект , то удаляются два обьеква ,True означает что удаляем обьект
    # если происходит колизия , означает что пуля убила врага и добавляем очков за это
    if collisions :
        for enemies in collisions.values():
            stats.score += 10 * len(enemies) #умнажаем на столько сколько было задето врагов
            sc.image_score()#вывод счета
            chech_high_score(stats, sc) #после каждого убийства проверяет , новый ли рекорд
            sc.image_guns_left()#вывод жизней
    #если победили всех пришельцев , то создаем новых
    if len(enemies) == 0 :
        bullets.empty()
        create_army(screen, enemies)
    
def gun_kill(stats, screen, sc, gun, enemies, bullets):
    #столкновение пушки и армии
    if stats.guns_left > 0:
        stats.guns_left -=1 # отнимаем одну жизнь 
        sc.image_guns_left()
        enemies.empty()
        bullets.empty()
        create_army(screen, enemies)
        gun.create_gun() 
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit
    
            
def update_enemies(stats, screen, sc, gun, enemies, bullets):
    #обновляет позицию врагов
    enemies.update()
    #проверяем если враги добрались до пушки
    if pygame.sprite.spritecollideany(gun, enemies):
        gun_kill(stats, screen, sc, gun, enemies, bullets)
    enemies_check(stats, screen, sc, gun, enemies, bullets)
        
def enemies_check(stats, screen, sc, gun, enemies, bullets):
    #проверка добрались ли враги до края экрана
    screen_rect = screen.get_rect()
    for enemy in enemies.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, enemies, bullets)
            break
            
def create_army(screen, enemies):
    #создание армии пришельцев
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width# ширина врага
    number_enemy_x = int((700 - 2 * enemy_width) / enemy_width) # считаем сколько может влезть в один ряд врагов
    enemy_height = enemy.rect.height
    number_enemy_y = int((800 - 100 - 2 * enemy_height) / enemy_height)
    
    for row_number in range(number_enemy_y-5):
        
        # цикл в котором будем перебирать по одному пришельцу
        for enemy_number in range(number_enemy_x):
            enemy = Enemy(screen)
            enemy.x = enemy_width + (enemy_width * enemy_number)
            enemy.y = enemy_height + (enemy_height * row_number)
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height +(enemy.rect.height * row_number)
            enemies.add(enemy)
            
def chech_high_score(stats, sc):
    # проверка нового рекдора 
    if stats.score > stats.high_score: #если новый счет больше рекорда
        stats.high_score = stats.score # записываем новый счет в рекодр
        sc.image_high_score() #вызывается всегда, для проверки каждого врага ,чтобы узнать новый ли рекорд 
        with open('SpaceGame/highscore.txt', 'w') as f: #открываем файл с рекордом с правами для записи
            f.write(str(stats.high_score)) #записываем туда новый рекорд