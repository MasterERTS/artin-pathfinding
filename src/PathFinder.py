from Classes.World import World

from collections import OrderedDict
import time

# Depth-first search
# starting from tile number start, find a path to tile number target
# return (reached, path) where reached is true if such a path exists, false otherwise
# and path contains the path if it exists  

def dfs(World, start, target, display):

    # Check accessibility of the begining and end of path
    start_check = World.is_accessible(start, "Start")
    target_check = World.is_accessible(target, "Target")
    if (not(start_check) or not(target_check)):
        print("Start or Target are not accessible TILES.")
        return(False, [])

    # Depth First Search Algorithm
    reached = False
    stack = []
    visited = []
    visited.append(start)
    current_tile = start

    # First iteration for stack not to be empty at first
    iterations = 0
    children = World.successors(current_tile)
    for elem in children:
        if elem not in visited:
            stack.append(elem)

    while (stack and not(reached)):
        if (iterations != 0):
            children = World.successors(current_tile)
            for elem in children:
                if elem not in visited:
                    stack.append(elem)

        current_tile = stack.pop()
        visited.append(current_tile)

        if display:
            World.display_path(visited)

        iterations += 1
        if target in visited:
            reached = True
            break

    return (reached, visited)

def bfs(World, start, target, display):
    # Check accessibility of the begining and end of path
    start_check = World.is_accessible(start, "Start")
    target_check = World.is_accessible(target, "Target")
    if (not(start_check) or not(target_check)):
        print("Start or Target are not accessible TILES.")
        return(False, [])

    # Depth First Search Algorithm
    reached = False
    queue = []
    visited = []
    visited.append(start)
    current_tile = start

    # First iteration for queue not to be empty at first
    iterations = 0
    children = World.successors(current_tile)
    for elem in children:
        if elem not in visited:
            queue.append(elem)

    while (queue and not(reached)):
        if (iterations != 0):
            children = World.successors(current_tile)
            for elem in children:
                if elem not in visited:
                    queue.append(elem)

        current_tile = queue.pop(0)
        visited.append(current_tile)

        if display:
            World.display_path(visited)

        iterations += 1
        if target in visited:
            reached = True
            break

    return (reached, visited)

def dijkstra(World, start, target, display):
    available_tiles = World.list_available_tiles()
    predecessors = []
    queue = []
    cost = dict()
    for elem in available_tiles:
        cost[elem] = 99999
    cost[start] = 0
    reached = False
    queue.append(start)

    while queue and not(reached):
        # Extract smallest cost from queue    
        sorted_cost = OrderedDict(sorted(cost.items(), key = lambda x: x[1]))
        for tile in queue:
            if tile in sorted_cost.keys():
                current_tile = tile
                queue.remove(tile)
        
        # Did we reach the end ?
        if current_tile == target:
            reached = True
            break
        else:
            children = World.successors(current_tile)
            for elem in children:
                if cost[current_tile] < cost[elem]:
                    cost[elem] = cost[current_tile]
                    predecessors.append(current_tile)
                    queue.append(elem)

    if display:   
        World.display_path(predecessors)

    return(reached, predecessors)

"""def heuristic(current, target):
    World.w[current]
    row = current % H
    col = current % L
    return abs(self.row - Node.target.row) + abs(self.column - Node.target.column)
"""
def a_star():
    return 0

def path_info(path_found, path, algorithm):
    if path_found:
        print("Goal reached.")
    else:
        print("No path found...")
    print("With " + algorithm + " length of the shortest path is " + str(len(path)))

if __name__ == '__main__':
    matrix = World(20, 10, 0.2)
    matrix.display()
    test_tile = 20
    print(matrix.w[test_tile])
    print(str(test_tile % matrix.L))
    print(str(test_tile % matrix.H))
    # create a world
    """  w = World(20, 10, 0.2)
    display = False

    path_found, dijkstra = dijkstra(w, 21, 164, display)
    path_info(path_found, dijkstra, "DIJKSTRA")

    path_found, dfs = dfs(w, 21, 164, display)
    path_info(path_found, dfs, "DFS")

    path_found, bfs = bfs(w, 21, 164, display)
    path_info(path_found, bfs, "BFS")"""



    

