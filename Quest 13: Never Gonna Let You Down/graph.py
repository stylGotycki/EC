class PriorityQueue:
    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        return len(self.queue) == 0
    
    def insert(self, data):
        self.queue.append(data)
        
    def delete(self):
        try:
            min_val = 0
            for i in range(len(self.queue)):
                if self.queue[i] < self.queue[min_val]:
                    min_val = i
            item = self.queue[min_val]
            del self.queue[min_val]
            return item
        except IndexError:
            print()
            exit()


class Vertex:
    def __init__(self, index: tuple[int, int], value: str, edges: list[tuple[int, int]]):
        self.index = index
        self.value = value
        self.edges = edges

    def __str__(self):
        return f"Index: {self.index}, value:{self.value}, edges(connects_to):{self.edges}"

    def __repr__(self):
        return f"Index: {self.index}, value:{self.value}, edges(connects_to):{self.edges}"


class MazeGraph:    
    def __init__(self, maze_info: dict):
        self.vertices = {}
        self.start, self.end = (), ()
                
        for key in maze_info.keys():
            index = (key[0], key[1])
            value = key[2]
            edges = maze_info[key]
            
            self.vertices[index] = (Vertex(index, value, edges))
            
            if value == 'S':
                self.start = index
                self.vertices[index].value = 0

            if value == 'E':
                self.end = index
                self.vertices[index].value = 0
                
    
    def __min_distance():
        pass
    
    def find_shortest_path(self):
        distances = {}
        visited = {}
        for index in self.vertices:
            distances[index] = 1e7
            visited[index] = False
            
        distances[self.start] = 0

        pq = PriorityQueue()
        pq.insert(distances[self.start])
        
        while not pq.isEmpty():
            current = pq.delete()
            current['visited'] = True
            