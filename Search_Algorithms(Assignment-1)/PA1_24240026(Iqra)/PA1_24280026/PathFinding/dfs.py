from utils import get_neighbours

def Dfs(Grid, START, END, size):

    #############################################################################
    # TODO: Implement DFS and Return the final path & all paths explored in order 
    ##############################################################################
    
    Dfs_stack = [START]
    parent_path ={START : None} #track of final path nodes
    explored_path=[]
    visited_nodes=[START] 

    while len(Dfs_stack)>0:
        current_element=Dfs_stack.pop() #lifo manner
        explored_path.append(current_element)

        if (current_element==END):
            path=[] 
            while current_element is not None:
                 path.append(current_element)
                 current_element = parent_path[current_element]
            path.reverse()  
            return path, explored_path
        
        for neighbour in get_neighbours(current_element,size):
            if neighbour not in visited_nodes and Grid[neighbour[0]][neighbour[1]]!=1:  #not visited or blocked
                visited_nodes.append(neighbour)
                parent_path[neighbour] = current_element
                Dfs_stack.append(neighbour)

    print("final path is : " +  path)
    print("explored path is : " +  path)

    return [], []

