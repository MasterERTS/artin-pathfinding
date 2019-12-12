from Classes.World import World

from collections import OrderedDict
import time
import os

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

def get_path(predecessor, start, target):
    path = [target]
    elem = target

    while predecessor[elem] is not start:
        elem = predecessor[elem]
        path.append(elem)
    if (len(path) > 1):
        path.append(start)
    return path


def heuristic(World, current, target):
    row_current = int(current / World.L)
    col_current = current % World.H
    row_target = int(target / World.L)
    col_target = target % World.H
    return(abs(row_current - row_target) + abs(col_current - col_target))

def dijkstra(World, start, target, display):
    # Check accessibility of the begining and end of path
    start_check = World.is_accessible(start, "Start")
    target_check = World.is_accessible(target, "Target")
    if (not(start_check) or not(target_check)):
        print("Start or Target are not accessible TILES.")
        return(False, [])

    available_tiles = World.list_available_tiles()
    queue = []
    path = []

    predecessor = dict()
    cost = dict()

    for elem in available_tiles:
        cost[elem] = 9999

    cost[start] = 0
    reached = False
    queue.append(start)

    while queue and not(reached):
        # Extract smallest cost from queue    
        sorted_cost = OrderedDict(sorted(cost.items(), key = lambda x: x[1]))
        for tile in sorted_cost.keys():
            if tile in queue:
                current_tile = tile
                queue.remove(tile)
        
        # Did we reach the end ?
        if current_tile == target:
            reached = True
            break
        
        children = World.successors(current_tile)
        for elem in children:
            if cost[elem] > cost[current_tile] + 1:
                cost[elem] = cost[current_tile] + 1 
                predecessor[elem] = current_tile
                queue.append(elem)

    if reached:
        path = get_path(predecessor, start, target)

    return(reached, path)

def therealdijkstra(World, start, target, display):
    # Check accessibility of the begining and end of path
    start_check = World.is_accessible(start, "Start")
    target_check = World.is_accessible(target, "Target")
    if (not(start_check) or not(target_check)):
        print("Start or Target are not accessible TILES.")
        return(False, [])
        
    available_tiles = World.list_available_tiles()

    reached = False
    open_list = [start]
    closed_list = []
    path = []

    predecessor = dict()
    f_score = dict()
    g_score = dict()
    h_score = dict()

    for elem in available_tiles:
        f_score[elem] = 0
        g_score[elem] = 0
        h_score[elem] = 0

    while (not(reached) and open_list):
        sorted_f = OrderedDict(sorted(f_score.items(), key = lambda x: x[1]))
        for tile in sorted_f.keys():
            if tile in open_list:
                current_tile = tile
                open_list.remove(tile)
                closed_list.append(current_tile)
                break

        if target in closed_list:
            reached = True
            break

        children = World.successors(current_tile)
        for child_tile in children:
            if child_tile not in closed_list:
                if child_tile in open_list:
                    new_g = g_score[current_tile] + 1
                    if g_score[child_tile] > new_g:
                        g_score[child_tile] = new_g
                        predecessor[child_tile] = current_tile
                else:
                    g_score[child_tile] = g_score[current_tile] + 1
                    h_score[child_tile] = 0
                    predecessor[child_tile] = current_tile
                    f_score[child_tile] = g_score[child_tile] + h_score[child_tile]
                    open_list.append(child_tile)
                    
    if reached:
        path = get_path(predecessor, start, target)

    return(reached, path)

def a_star(World, start, target, display):
    # Check accessibility of the begining and end of path
    start_check = World.is_accessible(start, "Start")
    target_check = World.is_accessible(target, "Target")
    if (not(start_check) or not(target_check)):
        print("Start or Target are not accessible TILES.")
        return(False, [])
        
    available_tiles = World.list_available_tiles()

    reached = False
    open_list = [start]
    closed_list = []
    path = []

    predecessor = dict()
    f_score = dict()
    g_score = dict()
    h_score = dict()

    for elem in available_tiles:
        f_score[elem] = 0
        g_score[elem] = 0
        h_score[elem] = 0

    while (not(reached) and open_list):
        sorted_f = OrderedDict(sorted(f_score.items(), key = lambda x: x[1]))
        for tile in sorted_f.keys():
            if tile in open_list:
                current_tile = tile
                open_list.remove(tile)
                closed_list.append(current_tile)
                break

        if target in closed_list:
            reached = True
            break

        children = World.successors(current_tile)
        for child_tile in children:
            if child_tile not in closed_list:
                if child_tile in open_list:
                    new_g = g_score[current_tile] + 1
                    if g_score[child_tile] > new_g:
                        g_score[child_tile] = new_g
                        predecessor[child_tile] = current_tile
                else:
                    g_score[child_tile] = g_score[current_tile] + 1
                    h_score[child_tile] = heuristic(World, current_tile, target)
                    predecessor[child_tile] = current_tile
                    f_score[child_tile] = g_score[child_tile] + h_score[child_tile]
                    open_list.append(child_tile)
                    
    if reached:
        path = get_path(predecessor, start, target)

    return(reached, path)

def path_info(path_found, path, algorithm):
    if path_found:
        print("\nGoal reached.")
    else:
        print("No path found...")
    print("With " + algorithm + " length of the shortest path is " + str(len(path)) + "\n")

if __name__ == '__main__':
    # create a world
    os.system('clear')

    height = 20
    length = 50
    wall_percentage = 0.25
    path_finding = input("Enter chosen path finding algorithm : [0: Dijkstra (A* h = 0); 1: Astar ; 2: DFS ; 3: BFS(to be fixed) ; Others: Compare Solutions]\n")

    w = World(length, height, wall_percentage)
    display = False

    if path_finding == "0":
        path_found, path = therealdijkstra(w, length + 1, height*length - length - 4, display)
        path_info(path_found, path, "DIJKSTRA (H = 0)")
    
    elif path_finding == "1":
        path_found, path = a_star(w, length + 1, height*length - length - 4, display)
        path_info(path_found, path, "A*")

    elif path_finding == "2":
        path_found, path = dfs(w, length + 1, height*length - length - 4, display)
        path_info(path_found, path, "DFS")

    elif path_finding == "3":
        path_found, path = bfs(w, length + 1, height*length - length - 4, display)
        path_info(path_found, path, "BFS")
    
    else:
        found_dfs, dfs = dfs(w, length + 1, height*length - length - 4, display)
        found_dij, dij = therealdijkstra(w, length + 1, height*length - length - 4, display)
        found_astar, astar = a_star(w, length + 1, height*length - length - 4, display)
        found_bfs, bfs = bfs(w, length + 1, height*length - length - 4, display)

        paths = dict()
        paths["A*"] = len(astar)
        paths["Dijkstra (H=0)"] = len(dij)
        paths["DFS"] = len(dfs)
        paths["BFS"] = len(bfs)
        print(paths)
    
    if (path_finding == "0" or path_finding == "1" or path_finding == "2" or path_finding == "3"): 
        w.display_path(path)



    

