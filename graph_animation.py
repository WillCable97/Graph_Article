from manim import *

class GraphWithLabels(Scene):
    def construct(self):
        # Create a graph
        graph = Graph(
            [1, 2, 3],  # Nodes
            [(1, 2), (2, 3)],  # Edges
            layout='circular',  # Circular layout
            labels=True,  # Show labels on nodes
        )
        
        # Create labels for a node and an edge
        node_label = Tex("Node 1").next_to(graph[1], DOWN)
        edge_label = Tex("Edge (1, 2)").move_to(graph.edges[(1, 2)].get_center()).shift(UP*0.5)

        # Draw the graph
        self.play(Create(graph))
        self.wait(1)

        # Animate in the labels
        self.play(Write(node_label), run_time=1)
        self.play(Write(edge_label), run_time=1)

        # Hold the frame to view result
        self.wait(2)

# To execute the script, save it in a .py file and run it with Manim.
# Example command to render the animation:
# manim -pql your_script_name.py GraphWithLabels
