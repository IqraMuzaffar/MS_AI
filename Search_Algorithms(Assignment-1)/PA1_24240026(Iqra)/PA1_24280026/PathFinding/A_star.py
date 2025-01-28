# A* algorithm with exploration tracking
# from utils import path_construction
from utils import get_neighbours
import heapq

def heuristic(cell1, cell2):
    #############################################################################
    # TODO: Calculate and return the Manhattan distance 
    ##############################################################################

    print(cell1)
    x1_coordinate, y1_coordinate = cell1
    x2_coordinate, y2_coordinate = cell2
    diff_x= abs(x1_coordinate - x2_coordinate)
    diff_y=abs(y1_coordinate-y2_coordinate)
    return diff_x + diff_y 

def A_star(Grid, START, END, size):

    A_star_list = [START]  #list of tupes (x1,y1)
    parent_path = {}
    g_score = {START: 0}
    heuristics= heuristic(START, END)
    f_score = {START: 0+ heuristics }
    explored_path = []
    visited_nodes=[START]

    while A_star_list:
        current_node = min(A_star_list, key=lambda node: f_score.get(node, float('inf'))) #priority queue
        A_star_list.remove(current_node)
        explored_path.append(current_node)  # Track the explored nodes
        visited_nodes.append(current_node)


        if current_node==END:               #path constrct
            path=[]
            while current_node is not None:
                 path.append(current_node)
                 current_node = parent_path.get(current_node, None)
            path.reverse()  
            return path, explored_path


        for neighbor in get_neighbours(current_node, size):
            if neighbor not in visited_nodes and Grid[neighbor[0]][neighbor[1]]!=1:  #not visited or blocked
                current_g_score=g_score[current_node] + Grid[neighbor[0]][neighbor[1]] 

                if neighbor not in g_score or current_g_score < g_score[neighbor]:
                    parent_path[neighbor] = current_node
                    g_score[neighbor] = current_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, END)

                    if neighbor not in A_star_list:
                        A_star_list.append(neighbor)


    return [], explored_path  # No path found
    # return [], []

