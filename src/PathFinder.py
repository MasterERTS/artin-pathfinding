from Classes.World import World

from collections import OrderedDict
import time
import os

#####################################################################################################################################################################
#####################################################################################################################################################################

#### Utility Functions ####

def isAvailableTargetStart(World, start, target):
    start_check = World.is_accessible(start, "Start")
    target_check = World.is_accessible(target, "Target")
    if (not(start_check) or not(target_check)):
        print("Start or Target are not accessible TILES.")
        return(False)
    else:
        return(True)

def heuristic(World, current, target):
    # Manhattan distance but could use euclidian ?
    row_current = int(current / World.L)
    col_current = current % World.H
    row_target = int(target / World.L)
    col_target = target % World.H
    return(abs(row_current - row_target) + abs(col_current - col_target))

def get_path(predecessor, start, target):
    path = [target]
    elem = target

    while predecessor[elem] is not start:
        elem = predecessor[elem]
        path.append(elem)
    if (len(path) > 1):
        path.append(start)
    return path

def path_info(path_found, path, algorithm):
    if path_found:
        print("\nGoal reached.")
        print("With " + algorithm + " length of the shortest path is " + str(len(path)) + "\n")
    else:
        print("No path found...")

#####################################################################################################################################################################
#####################################################################################################################################################################

#### Path Planning Algorithms ####

def spanning_tree_walk(World, start, target):
    predecessors = dict()
    reached = False
    visited = []
    queue = [start]
    path = []

    while(queue and not(reached)):
        current_tile = queue.pop()
        if current_tile == target:
            reached = True
        else:
            visited.append(current_tile)
            children = World.successors(current_tile)
            for child_tile in children:
                if ((child_tile not in visited) and (child_tile not in queue)):
                    predecessors[child_tile] = current_tile
                    queue.append(child_tile)

    if reached:
        path = get_path(predecessors, start, target)
        path.reverse()

    return(reached, path)


def dfs(World, start, target):
    # Check accessibility of the begining and end of path
    if(not(isAvailableTargetStart(World, start, target))):
        return([], False)

    reached = False
    stack = [start]
    visited = []

    while(stack and not(reached)):
        current_tile = stack.pop()

        if current_tile not in visited:
            visited.append(current_tile)
            if target in visited:
                reached = True
            children = World.successors(current_tile)

            for child_tile in children:
                if(child_tile not in visited):
                    stack.append(child_tile)

    return (reached, visited)


def bfs(World, start, target):
    # Check accessibility of the begining and end of path
    if(not(isAvailableTargetStart(World, start, target))):
        return([], False)

    reached = False
    queue = [start]
    visited = []

    while(queue and not(reached)):
        current_tile = queue.pop(0)

        if current_tile not in visited:
            visited.append(current_tile)
            if target in visited:
                reached = True
            children = World.successors(current_tile)

            for child_tile in children:
                if(child_tile not in visited):
                    queue.append(child_tile)

    return (reached, visited)

def therealdijkstra(World, start, target):
    # Check accessibility of the begining and end of path
    if(not(isAvailableTargetStart(World, start, target))):
        return([], False)
        
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
        path.reverse()

    return(reached, path)

def a_star(World, start, target):
    # Check accessibility of the begining and end of path
    if(not(isAvailableTargetStart(World, start, target))):
        return([], False)
        
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
        path.reverse()

    return(reached, path)

#####################################################################################################################################################################
#####################################################################################################################################################################

#### Main Script ####

if __name__ == '__main__':

    # Create our World (Matrix of Availability)
    height = 20
    length = 50
    wall_percentage = 0.25
    w = World(length, height, wall_percentage)

    # Display options
    stepbystep_display = False
    display_rate = 0.1

    # Inputs
    path_finding = input("Enter chosen path finding algorithm : \n ---------- \n0: Dijkstra (A* h = 0) ; \n1: Astar ; \n2: DFS ; \n3: BFS(to be fixed) ; \n4: Spanning Tree Walk ; \nOthers: Compare Solutions for all the algorithms\n")


    if path_finding == "0":
        path_found, path = therealdijkstra(w, length + 1, height*length - length - 4)
        path_info(path_found, path, "DIJKSTRA (H = 0)")
    
    elif path_finding == "1":
        path_found, path = a_star(w, length + 1, height*length - length - 4)
        path_info(path_found, path, "A*")

    elif path_finding == "2":
        path_found, path = dfs(w, length + 1, height*length - length - 4)
        path_info(path_found, path, "DFS")

    elif path_finding == "3":
        path_found, path = bfs(w, length + 1, height*length - length - 4)
        path_info(path_found, path, "BFS")
    
    elif path_finding == "4":
        path_found, path = spanning_tree_walk(w, length + 1, height*length - length - 4)
        path_info(path_found, path, "Spanning Tree Walk")
    
    else:
        found_dfs, dfs = dfs(w, length + 1, height*length - length - 4)
        found_dij, dij = therealdijkstra(w, length + 1, height*length - length - 4)
        found_astar, astar = a_star(w, length + 1, height*length - length - 4)
        found_bfs, bfs = bfs(w, length + 1, height*length - length - 4)
        found_stw, stw = spanning_tree_walk(w, length + 1, height*length - length - 4)

        paths = dict()
        paths["A*"] = len(astar)
        paths["Dijkstra (H=0)"] = len(dij)
        paths["DFS"] = len(dfs)
        paths["BFS"] = len(bfs)
        paths["STW"] = len(stw)
        print(paths)
    
    if (path_finding == "0" or path_finding == "1" or path_finding == "2" or path_finding == "3" or path_finding == "4"): 
        if(path_found):
            if(stepbystep_display):
                w.display_stepbystep(path, display_rate)
            else:
                w.display_path(path)



    

