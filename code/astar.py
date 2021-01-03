from heapq import heappush,heappop
import numpy as np
import time

from puzzle import Puzzle

class Astar(object):
    def __init__(self,_heuristic,_start,_goal):
        self.heuristic = _heuristic
        self.start = _start
        self.goal = _goal
        self.parent = dict()
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
        if (self.heuristic == 'hamming'):
            return (nodo).hamming(self.goal) + costoAcumulado
        elif (self.heuristic == 'manhattan'):
            return (nodo).manhattan(self.goal) + costoAcumulado

    def trajectory(self):
        if(len(self.parent) == 0):
            return []
        path = [self.goal]
        nodo = self.goal
        while self.parent[nodo] != self.start:
            nodo = self.parent[nodo]
            path.append(nodo)
        path = path[::-1]
        self.path = path
        return path

    def print_trajectory(self):
        if(len(self.parent) == 0):
            print('No existe ruta')
            return None
        for i in self.path:
            print(i.pretty_print())

    def search(self):
        origen = self.start
        historia = [(0,0)]
        agenda = []
        expandidos = set()
        costoAcumulado = 0
        contador = 0
        if (self.is_goal(origen)):
            return(historia)
        self.parent[origen] = origen
        heu = self.heuristic_sel(origen,costoAcumulado)
        heappush(agenda,(heu,contador,costoAcumulado,origen))
        while (len(agenda) > 0):
            historia.append((len(agenda),len(expandidos)))
            heu,c,ca,nodo = heappop(agenda)
            expandidos.add(nodo)
            if (self.is_goal(nodo)):
                #print(historia)
                return(historia)
            for sucesor in self.get_children(nodo):
                if(sucesor not in expandidos):
                    heu = self.heuristic_sel(sucesor,ca)
                    nc = []
                    for i,j,k,l in agenda:
                        if(i == heu):
                            nc.append(j)
                    if(len(nc) == 0):
                        nc = 0
                    else:
                        nc = max(nc) + 1
                    heappush(agenda,(heu,nc,ca+1,sucesor))
                    self.parent[sucesor] = nodo
        return None