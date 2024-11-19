import threading
import time
from turtledemo.penrose import start
import multiprocessing as mp
import os

def read_info(name):
    all_data =[]
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break
    return all_data

filenames = [f'./file {number}.txt' for number in range(1, 5)]
# Многопроцессный
if __name__ == '__main__':
    start_t = time.time()
    with mp.Pool() as pool:
        pool.map(read_info, filenames)
        end_t = time.time()
    print(f'{end_t - start_t} (многопроцессный)')
#Линейный вызов
#start_t = time.time()
#for name in filenames:
#    result = read_info(name)
#end_t = time.time()
#print(f'{end_t - start_t} (линейный)')



