from heapq import heappush,heappop
from collections import deque
import numpy as np
import time
import math


from puzzle import Puzzle

class IDAstar(object):
    def __init__(self,_heuristic,_start,_goal):
        self.heuristic = _heuristic
        self.start = _start
        self.goal = _goal
        self.path = []
    
    def start_node(self):
        return self.start_node
        
    def is_goal(self,node):
        return node == self.goal

    def get_children(self,node):
        child_list = set()
        dim = node.state.shape[0]
        i,j = map(np.int,np.where(node.state == 0))
        if (j > 0):
            child = node.state.copy()
            child[i,j] = node.state[i,j-1]
            child[i,j-1] = 0
            p = Puzzle(child)
            child_list.add(p)
        if (j < dim-1):
            child = node.state.copy()
            child[i,j] = node.state[i,j+1]
            child[i,j+1] = 0
            p = Puzzle(child)
            child_list.add(p)
        if (i > 0):
            child = node.state.copy()
            child[i,j] = node.state[i-1,j]
            child[i-1,j] = 0
            p = Puzzle(child)
            child_list.add(p)
        if (i < dim-1):
            child = node.state.copy()
            child[i,j] = node.state[i+1,j]
            child[i+1,j] = 0
            p = Puzzle(child)
            child_list.add(p)
        return child_list

    def heuristic_sel(self,nodo,costoAcumulado):
        if (self.heuristic=='hamming'):
            return (nodo).hamming(self.goal) + costoAcumulado
        elif (self.heuristic=='manhattan'):
            return (nodo).manhattan(self.goal) + costoAcumulado

    def trajectory(self):
        ruta = []
        for i,j in self.path:
            if (i,j) != (self.start,0):
                ruta.append(i)
        return ruta

    def print_trajectory(self):
        for i,j in self.path:
            if (i,j) != (self.start,0):
                print(i.pretty_print())

    def search(self):
        origen = self.start
        historia = [(0,0)]
        if (self.is_goal(origen)):
            self.path = [(origen,0)]
            return(historia)
        c = self.heuristic_sel(origen,0)
        while True:
            minimo = math.inf
            agenda = deque()
            agenda.append((origen,0))
            x = set()
            while len(agenda)>0:
                historia.append(((len(agenda),len(x))))
                n,costo = agenda[-1]
                if(self.is_goal(n)):
                    self.path = agenda
                    return(historia)
                if n not in x:
                    x.add(n)
                    sucesores = self.get_children(n)
                    sucesoresAux = []
                    for i in sucesores:
                        heu = self.heuristic_sel(i,costo)
                        nc = []
                        for j,k,l in sucesoresAux:
                            if(j == heu):
                                nc.append(k)
                        if(len(nc)==0):
                            nc = 0
                        else:
                            nc = max(nc)+1
                        heappush(sucesoresAux,(heu,nc,i))
                    sucesores = sucesoresAux

                    for s1,s2,s in sucesores:
                        if s1 <= c:
                            if s not in x:
                                agenda.append((s,costo+1))
                        else:
                            if(s1 < minimo):
                                minimo = s1
                else:
                    agenda.pop()
                    x.remove(n)
            c = minimo
            if c == math.inf:
                self.path = agenda
                return(historia)