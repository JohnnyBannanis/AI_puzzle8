from heapq import heappush,heappop
from collections import deque
import numpy as np
import math
import matplotlib.pyplot as plt
import time


class Puzzle(object):
    def __init__(self,node):
        self.state = node
    def __hash__(self):
        return hash(np.array_str(self.state.ravel()))
    def __eq__(self,other):
        return np.array_equal(other.state,self.state)

    def manhattan(self,goal):
        dim = self.state.shape[0]
        diff_mat = np.zeros((dim,dim))
        for i in range(dim):
            for j in range(dim):
                if goal.state[i,j]!=0:
                    u,v = map(np.int,np.where(self.state == goal.state[i,j]))
                    diff_mat[i,j] = abs(i-u) + abs(j-v)
        return int(diff_mat.sum())

    def hamming(self,goal):
        dim = self.state.shape[0]
        diff_mat = np.zeros((dim,dim))
        diff_mat = self.state!=goal.state
        dist=np.sum(diff_mat.astype(int).ravel())
        if (dist > 0):
            dist = dist-1
        return dist

    def pretty_print(self):
        a = np.array_str(self.state.ravel())
        pretty = [[int(a[1]),int(a[3]),int(a[5])], [int(a[7]),int(a[9]),int(a[11])], [int(a[13]),int(a[15]),int(a[17])]  ]
        print(pretty[0])
        print(pretty[1])
        print(pretty[2])
        print("\n")
 
    def solvable(self):
        return len([(a,b) for i,a in enumerate(self.state.ravel()) for b in self.state.ravel()[i:] if a>b & b!=0])%2==0

