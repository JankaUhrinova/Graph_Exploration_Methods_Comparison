import networkx as nx
import matplotlib.pyplot as plt

# graph creation - taking width and height as parameters
G = nx.grid_2d_graph(13,13)
#print(list(G.nodes))

# the list of nodes that should be deleted 
# passed as list of tuples where each tuple represents a node by x, y coordinates. Eg. [(0,0),(1,1)]
obstacles = eval(input())
#print(obstacles)

for obstacle in obstacles:
    G.remove_node(obstacle)    


# graph visualisation
positions = {}
for i in range(13):
    for j in range(13):
        if (i,j) in G.nodes:
            positions[(i,j)] = (5*i,5*(13-j))

nx.draw(G, positions)
plt.show()