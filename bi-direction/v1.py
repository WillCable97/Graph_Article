from manim import *

class GraphScene(Scene):
    def construct(self):
        # Define the graph vertices and edges
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
        
        # Create an undirected graph
        graph = Graph(vertices, edges, layout="circular", labels=True)
        self.play(Create(graph))  # Animate the creation of the graph
        self.wait(1)  # Pause for a moment
        
        # Define directed edges including bi-directional ones with offset
        directed_edges = edges + [(2, 1), (3, 2), (4, 3), (1, 4)]  # Additional reverse edges for bi-directionality
        
        # Clear the undirected graph
        self.play(FadeOut(graph))

        # Create the new graph with offset edges to show bi-directionality
        graph = Graph(
            vertices, directed_edges, layout="circular", labels=True,
            edge_type=Arrow, 
            edge_config={
                (u, v): {
                    "stroke_width": 2, 
                    "tip_length": 0.2,
                    "buff": 0 if (u, v) in edges else 0.15  # Offset reversed edges
                } for u, v in directed_edges
            }
        )

        # Animate each arrow creation separately to highlight the bi-directional aspect
        for edge in directed_edges:
            self.play(Create(graph.edges[edge]), run_time=0.5)
            self.wait(0.1)  # Brief pause between arrow animations

        self.wait(2)  # Pause at the end

# To run this scene, use the following command in your terminal:
# manim -pql graph_animation.py GraphScene
