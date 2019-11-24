from .World import World

class PathFinder(World):
    # initialise the world
    # L is the number of columns
    # H is the number of lines
    # P is the probability of having a wall in a given tile
    def __init__(self, start, target):
        self.start = start
        self.target = target

    # Depth-first search
    # starting from tile number self.start, find a path to tile number self.target
    # return (r, path) where r is true if such a path exists, false otherwise
    # and path contains the path if it exists  
    def dfs(self):
        r = False
        path = []
        stack = []
        visited = []

        stack.append(self.start)
        path.append(self.start)
        visited.append(self.start)

        current_tile = self.start

        while stack:
            children = super().successors(current_tile)
            for elem in children:
                if elem not in path:
                    if elem not in visited:
                        stack.append(elem)
            
            current_tile = stack.pop()
            visited.append(current_tile)

            if visited[len(visited) - 1] in visited:
                path.append(current_tile)

            else:
                last_tile = path[len(path) - 1]
                current_children = super().successors(current_tile)

                if last_tile in current_children:
                    path.append(current_tile)

            super().display_path(path)
            print(path)
            print(stack)
        
            if self.target in path:
                r = True
                break
            
        return (r, path)


    def bfs(self):
        r = False
        path = []
        stack = []
        visited = []

        stack.append(self.start)
        path.append(self.start)
        visited.append(self.start)

        current_tile = self.start

        while stack:
            children = super().successors(current_tile)
            for elem in children:
                if elem not in path:
                    stack.append(elem)
            
            current_tile = stack.pop(0)
            visited.append(current_tile)

            if visited[len(visited) - 1] in visited:
                path.append(current_tile)

            else:
                last_tile = path[len(path) - 1]
                current_children = super().successors(current_tile)

                if last_tile in current_children:
                    path.append(current_tile)

            super().display_path(path)
            print(path)
            print(stack)
        
            if self.target in path:
                r = True
                break
            
        return (r, path)

    def dijkstra(self):

        return 0

    def a_star(self):

        return 0