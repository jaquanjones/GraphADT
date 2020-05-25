import data


def print_cities():
    for index, location in data.index_val.items():
        print("{}: {}".format(index, location))


def get_input():
    g = Graph()

    try:
        start = int(input("Enter starting city using number from 0 - 11: "))

        print("\nYou entered city name: {}".format(data.index_val[start]))

        print("\nStarting at {}, 12 cities are searched in this Depth-First Search order:"
              .format(data.index_val[start]))
        g.depth_first_traversal(start)

        print("\nStarting at {}, 12 cities are searched in this Breadth-First Search order:"
              .format(data.index_val[start]))
        g.breadth_first_traversal(start)
        restart()
    except KeyError:
        print("Index not in range.")


def restart():
    start_over = int(input("\nTry another city?\n1: Yes\n2: No\n"))

    try:
        if start_over == 1:
            get_input()
        elif start_over == 2:
            exit()
        else:
            return
    except ValueError:
        print("Invalid input.")


class Graph:

    def __init__(self):
        self.max_cities = 12
        self.visited = set()  # store visited dfs
        self.visit = []  # store visited bfs
        self.queue = []  # queue for bfs

    def depth_first_traversal(self, v):
        city_index = data.index_val[v]
        self.dfs(city_index, self.visited)
        print(end="\n")

    def dfs(self, city_index, visited):
        if city_index not in visited:
            print(city_index, end=", ")
            self.visited.add(city_index)

            for adj in data.adjacent_cities[city_index]:
                self.dfs(adj, visited)

    def breadth_first_traversal(self, v):
        city_index = data.index_val[v]
        self.bfs(city_index, self.visit)
        print(end="\n")

    def bfs(self, city_index, visit):
        self.visit.append(city_index)
        self.queue.append(city_index)

        while self.queue:
            q = self.queue.pop(0)
            print(q, end=", ")

            for adj in data.adjacent_cities[q]:
                if adj not in visit:
                    self.visit.append(adj)
                    self.queue.append(adj)
