from manim import *

class GraphToAdjacencyMatrix(Scene):
    def construct(self):
        # Define the graph data
        nodes = ['A', 'B', 'C', 'D']
        edges = [
            ('A', 'B'), ('B', 'C'), ('D', 'A'), ('B', 'D')
        ]

        # Create the graph with proper layout
        graph = Graph(nodes, edges, layout="circular", labels=True).scale(0.8)
        graph.to_edge(LEFT, buff=1)

        self.play(Create(graph))
        self.wait(1)

        # Generate adjacency matrix
        adjacency_matrix = [[0,1,0,1], [1,0,1,1], [0,1,0,0],[1,1,0,0]]
        #adjacency_matrix = [
        #    [0 if j not in [i[1] for i in edges if i[0] == node] else 1 for j in nodes]
        #    for node in nodes
        #]

        # Create matrix mobject
        matrix = Matrix(adjacency_matrix, v_buff=1.5).scale(0.8)
        matrix.next_to(graph, RIGHT, buff=1)

        # Matrix label centered above the matrix
        matrix_label = Text("", color=WHITE).next_to(matrix, UP, buff=0.75)
        #Adjacency Matrix
        # Row labels (to the left of the matrix)
        for i, node in enumerate(nodes):
            label = Text(node, color=WHITE).next_to(matrix.get_rows()[i], LEFT, buff=0.5)
            self.add(label)

        # Column labels (above the matrix)
        for i, node in enumerate(nodes):
            label = Text(node, color=WHITE).next_to(matrix.get_columns()[i], UP, buff=0.5)
            self.add(label)

        # Show matrix and labels
        self.play(Write(matrix), Write(matrix_label))
        self.wait(2)

        # Show fading of both graph and matrix after display
        self.play(FadeOut(graph), FadeOut(matrix), FadeOut(matrix_label))

# To run this script:
# manim -pql script_name.py GraphToAdjacencyMatrix
