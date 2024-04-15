from manim import *

class CustomGraphScene(Scene):
    def construct(self):
        # Define a more dispersed and non-linear layout for the graph
        layout = {
            "A": LEFT * 2 + UP * 2,
            "B": LEFT * 2 + DOWN * 2,
            "C": ORIGIN,  # Center point
            "D": RIGHT * 2 + UP * 2,
            "E": RIGHT * 2 + DOWN * 2
        }

        # Define the graph with 5 nodes
        graph = Graph(
            ["A", "B", "C", "D", "E"],  # List of vertices
            [("A", "B"), ("B", "C"), ("C", "D"), ("D", "E"), ("A", "C"), ("C", "E")],  # List of edges
            layout=layout,
            vertex_config={"A": {"fill_color": BLUE}, "B": {"fill_color": YELLOW}, "C": {"fill_color": GREEN}, "D": {"fill_color": RED}, "E": {"fill_color": PURPLE}},
            edge_config={("A", "B"): {"stroke_color": GREEN}, ("B", "C"): {"stroke_color": ORANGE}, ("C", "D"): {"stroke_color": RED}, ("D", "E"): {"stroke_color": PURPLE}, ("A", "C"): {"stroke_color": BLUE}, ("C", "E"): {"stroke_color": YELLOW}},
            labels=True
        )

        # Add the graph to the scene
        self.play(Create(graph))
        self.wait(1)

        # Add a label for one node
        node_label = Text("This is node C", font_size=24).next_to(graph["C"], UP, buff=0.5)
        node_arrow = Arrow(node_label.get_bottom(), graph["C"].get_top(), buff=0.1, color=WHITE)
        self.play(Write(node_label), GrowArrow(node_arrow))
        self.wait(1)

        # Add a label for one edge
        edge_label = Text("This is edge C-D", font_size=24).next_to(graph.edges[("C", "D")], RIGHT, buff=0.1)
        edge_arrow = Arrow(edge_label.get_left(), graph.edges[("C", "D")].get_center(), buff=0.1, color=WHITE)
        self.play(Write(edge_label), GrowArrow(edge_arrow))
        self.wait(2)

        # Clear everything
        self.play(FadeOut(node_label), FadeOut(edge_label), FadeOut(node_arrow), FadeOut(edge_arrow), FadeOut(graph))

# To run this script, ensure you have Manim installed and configured.
# Save this script in a file, say `custom_graph_animation.py`, and execute it using the command:
# manim -pql custom_graph_animation.py CustomGraphScene
