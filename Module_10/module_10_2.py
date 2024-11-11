import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)
        self.enemy = 100
        self.time_day = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemy >0:
            self.enemy -=self.power
            self.time_day +=1
            time.sleep(1)
            print(f'{self.name} сражается {self.time_day} день(дня)..., осталось {self.enemy} воинов\n')
        print(f'{self.name} одержал победу спустя {self.time_day} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')

