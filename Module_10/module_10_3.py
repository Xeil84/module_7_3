import random
import threading
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            self.r_dep = random.randint(50,500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += self.r_dep
            time.sleep(0.0001)
            print(f'Пополнение: {self.r_dep}. Баланс: {self.balance}')

    def take(self):
        for i in range(100):
            self.r_cash = random.randint(50,500)
            print(f'Запрос на {self.r_cash}')
            if self.r_cash <= self.balance:
                self.balance -= self.r_cash
                print(f"Снятие: {self.r_cash}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')










