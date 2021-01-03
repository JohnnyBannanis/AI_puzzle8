from heapq import heappush,heappop
from collections import deque
import numpy as np
import math
import matplotlib.pyplot as plt
import time
import seaborn as sns
sns.set(style="darkgrid")


from puzzle import Puzzle
from astar import Astar
from idastar import IDAstar


def main_1():
    dim = 3
    goal = Puzzle(np.insert(np.arange(1,dim*dim),dim*dim-1,0).reshape(dim,dim))
    time1 = []
    time2 = []
    space1 = []
    space2 = []

    for i in range(15):
        while True:
            start = Puzzle(np.random.permutation(np.arange(dim*dim)).reshape((dim,dim)))
            if start.solvable() : break
        t_1 = time.time()
        p1 = Astar('manhattan',start,goal)
        h1 = p1.search()
        t_2 = time.time()
        t_f = t_2 - t_1 
        time1.append(t_f)
        space1.append(np.mean([j for i,j in h1]))

        t_11 = time.time()
        p2 = Astar('hamming',start,goal)
        h2 = p2.search()
        t_22 = time.time()
        t_ff = t_22 - t_11 
        time2.append(t_ff)
        space2.append(np.mean([j for i,j in h2]))

    a = plt.plot(time1,'blue')
    b = plt.plot(time2,'red')
    plt.legend(['Manhattan','Hamming'])
    plt.xlabel('puzzle')
    plt.ylabel('tiempo')
    plt.title('Tiempo A*')
    plt.show()    

    a = plt.plot(space1,'blue')
    b = plt.plot(space2,'red')
    plt.legend(['Manhattan','Hamming'])
    plt.xlabel('puzzle')
    plt.ylabel('espacio')
    plt.title('Espacio A*')
    plt.show()

    print(time1)
    print(space1)
    print(time2)
    print(space2)

main_1()
#main_21()
#main_22()