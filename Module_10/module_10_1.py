import threading
import time
from time import sleep



def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf8') as file:
        for i in range(word_count):
            time.sleep(0.1)
            start_t = time.time()
            file.write(f"Какое-то слово № {i+1}\n")
    print(f"Завершилась запись в файл {file_name}")
start_t = time.time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end_t = time.time()
print(f'Работа потоков{round(end_t-start_t,6)}')


start_t = time.time()
thread= threading.Thread(target=write_words, args=(10, "example5.txt"))
thread.start()
thread= threading.Thread(target=write_words, args=(30, "example6.txt"))
thread.start()
thread= threading.Thread(target=write_words, args=(200, "example7.txt"))
thread.start()
thread= threading.Thread(target=write_words, args=(100, "example8.txt"))
thread.start()
thread.join()
thread.join()
thread.join()
thread.join()
end_t = time.time()
print(f'Работа потоков {round(end_t-start_t,6)}')
