import random

import matplotlib.pyplot as plt
import networkx as nx
import pygraphviz  # used in the layout

from block import Block
from parameters import *
x = [i for i in range(0, 30, 3)]
y1=[1,1,0.95,0.92,0.87,0.82,0.79,0.74,0.70,0.68]
plt.plot(x,y1,label='verified in main chain',color='b',marker='o',markersize=5) 
plt.xlabel("average latency(s)")
plt.title("influence of latency")
plt.legend()
plt.show()
plt.savefig(image_file)
plt.close()
