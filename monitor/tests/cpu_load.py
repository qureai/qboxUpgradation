"""
Max out CPU for a certain amount of time, pass time as CLI arg in seconds
"""

from multiprocessing import Pool, cpu_count
from time import sleep
import sys 
def f(y):
    while True:
        y *= 2

def cpu_load(load_secs):
    procs = cpu_count()
    with Pool(processes=procs) as p:
        p.map(f, range(procs))
    sleep(load_secs)
    p.terminate()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("pass the time for load in seconds as argument.")
    else:
        secs = sys.argv[1]
        cpu_load(secs)
