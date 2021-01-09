import string
"""
to make a sentence or paragraph as a graph with direction and weight
every word represents a vertex, and the relationships between words indicates edges.
"""

# class Vertex representing a word
class Vertex:

    def __init__(self, word):
        self.word = word
        self.edges = []

    def add_edge(self, vertex, sequence):
        """
        create the connection between two words
        """
        
        #get available edge that these two words have been connected.
        edge = self._get_available_edge(vertex)
        

        if edge is None: # if not exisst, create a new one and append into edges
            edge = Edge(vertex, sequence)
            self.edges.append(edge)
            return

        #otherwise need to increase weight, and set the sequence
        edge.increase_weight()
        edge.add_sequence(sequence)

    def _get_available_edge(self, vertex):
        """
        get a available edge that has existed in edges, otherwise return None
        """
        if len(self.edges) == 0:
            return None  

        filtered = list(filter(lambda e: e.vertex == vertex, self.edges))
        if len(filtered) == 0:
            return None
        return filtered[0] # if exist, return the first one

    def __str__(self):
        return self.word

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.word == other.word

# edge class represents the relationship or connection between two words    
class Edge:

    def __init__(self, vertex, sequence):
        self.vertex = vertex
        self.weight = 1
        self.sequence = {sequence}

    def increase_weight(self):
        self.weight += 1
        
    def add_sequence(self, sequence):
        self.sequence.add(sequence)

    def __str__(self):
        return str(self.vertex) + str(self.sequence)



class Graph:

    def __init__(self):
        self.root = None
    
    # build graph through out file
    def build_from_file(self, filename):
        with open(filename) as f:
            text = f.read()
            self.build_from_text(text)


    def build_from_text(self, text):

        # remove all things such as white space, punctuations
        text = ' '.join(text.lower().split())
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()

        vertices = {}
        previous = None
        sequence = 0

        for word in words:
            word = word.strip()
            if self.root is None: # set the first word as root
                self.root = Vertex(word)
                previous = self.root
            else:
                current = vertices.get(word, Vertex(word)) # check if this word already existes, otherwise create a new one
                previous.add_edge(current, sequence) # create connection between previous word and current word
                previous = current
                sequence += 1
            vertices[word] = previous

    # to make the graph iterable
    def __iter__(self):
        current = self.root
        i = 0

        while current:
            yield current.word
            edges = [e for e in current.edges if i in e.sequence]
            current = None if len(edges) == 0 else edges[0].vertex
            i += 1


graph = Graph()
graph.build_from_text('I am a student. I am playing basketball and I will get a job')

print(list(iter(graph)))