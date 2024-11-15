import threading
from queue import Queue
import random
import time
from threading import Thread

class Table:
    def __init__(self, number):
        self.number = int(number)
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        time.sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    table.guest = guest
                    break
            else:
                print(f'{guest.name} в очереди')
                self.queue.put(guest)


    def discuss_guests(self):
        while not self.queue.empty() or any([table.guest for table in self.tables]):
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        ego = table.guest
                        print(f'{ego.name} покушал(-а) и ушёл(ушла)\nСтол номер {table.number} свободен')
                        table.guest = None
                if not self.queue.empty() and table.guest is None:
                    go = self.queue.get()
                    table.guest = go
                    print(f'{go.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    go.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
