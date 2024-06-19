class Stats():
    # отслеживание статистики
    
    def __init__(self):
        # инициализирует статистику 
        self.reset_stats()
        self.run_game = True # нужен для того чтобы, если жизни закончатся , то меняется на фалс и игра заканчивается
        with open('SpaceGame/highscore.txt', 'r') as f: #открываем файл с рекордом для чтения
            self.high_score = int(f.readline()) # записываем рекорд из вне кода
        
    def reset_stats(self):
        # статистика изменяющиеся во время игры
        self.guns_left = 2 #количество жизней пушки
        self.score = 0 #счетчик убитых врагов