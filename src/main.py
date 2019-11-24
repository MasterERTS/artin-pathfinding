from Classes.PathFinder import PathFinder
from Classes.World import World

# create a world
w = World(20, 10, 0.2)
PFinder = PathFinder(21, 164)


# print the tile numbers of the successors of the starting tile (1, 1)
#print(w.successors(w.L + 1))
path_found, path = PFinder.dfs() 
path_found_bfs, path_bfs = PFinder.bfs()

if path_found:
    print("Goal reached.")
else:
    print("No path found...")

print("DFS path length = " + len(path))
print("BFS path length = " + len(path_bfs))