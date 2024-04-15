from manim import *

class GraphAnimation(Scene):
    def construct(self):
        # Circular layout for the nodes
        layout = {
            1: UP * 2,
            2: LEFT * 2,
            3: DOWN * 2,
            4: RIGHT * 2,
            5: UR * 2,   # Upper right corner
            6: UL * 2    # Upper left corner
        }

        # Initial set of nodes and edges
        nodes = {i: Dot(layout[i], color=BLUE) for i in range(1, 5)}
        edges = {
            (1, 2): Line(layout[1], layout[2], color=BLUE),
            (2, 3): Line(layout[2], layout[3], color=BLUE),
            (3, 4): Line(layout[3], layout[4], color=BLUE),
            (4, 1): Line(layout[4], layout[1], color=BLUE)
        }

        # Create nodes and edges
        for node in nodes.values():
            self.play(FadeIn(node), run_time=0.5)
        for edge in edges.values():
            self.play(Create(edge), run_time=0.5)
        self.wait(1)

        # Time label for t=1
        time_label = Text("t=1", font_size=36).to_edge(DOWN)
        self.play(Write(time_label))
        self.wait(1)

        # Adding node 5 and edge (1, 5) at t=2
        new_node = Dot(layout[5], color=RED)
        new_edge = Line(layout[4], layout[5], color=RED)
        self.play(FadeIn(new_node), Create(new_edge))
        nodes[5] = new_node
        edges[(1, 5)] = new_edge

        # Update time label to t=2
        new_time_label = Text("t=2", font_size=36).to_edge(DOWN)
        self.play(ReplacementTransform(time_label, new_time_label))
        time_label = new_time_label
        self.wait(1)

        # Adding node 6 and edges (5, 6) and (6, 3) at t=3
        new_node_6 = Dot(layout[6], color=GREEN)
        new_edge_5_6 = Line(layout[5], layout[6], color=GREEN)
        new_edge_6_3 = Line(layout[6], layout[3], color=GREEN)
        self.play(FadeIn(new_node_6), Create(new_edge_5_6), Create(new_edge_6_3))
        nodes[6] = new_node_6
        edges[(5, 6)] = new_edge_5_6
        edges[(6, 3)] = new_edge_6_3

        # Update time label to t=3
        new_time_label = Text("t=3", font_size=36).to_edge(DOWN)
        self.play(ReplacementTransform(time_label, new_time_label))
        self.wait(2)

# To run this script, save it as graph_anim.py and use the following command:
# manim -pql graph_anim.py GraphAnimation
