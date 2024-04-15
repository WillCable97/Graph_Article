from manim import *

class GraphConvolution(Scene):
    def construct(self):
        # Define a larger and more connected graph
        G = Graph(
            [0, 1, 2, 3, 4, 5, 6, 7],
            [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 5), (4, 5), (5, 6), (6, 7), (1, 7)],
            layout="spring",  # Using a spring layout for a more natural look
            labels=True,
            vertex_config={node: {"fill_color": BLUE} for node in range(8)}
        )

        # Show graph
        self.play(Create(G))
        self.wait(1)

        # Highlight neighbors of a node, say node 5
        neighbors = [3, 4, 6]  # example neighbors of node 5
        edges = [(3, 5), (4, 5), (5, 6)]

        self.play(
            *[
                G[v].animate.set_color(RED) for v in neighbors
            ],
            *[
                G.edges[e].animate.set_color(YELLOW) for e in edges
            ]
        )
        self.wait(1)

        # Perform convolution on node 5
        self.play(
            G[5].animate.set_color(PURPLE)
        )
        self.wait(1)

        # Revert colors of nodes and edges
        self.play(
            *[
                G[v].animate.set_color(BLUE) for v in range(8)
            ],
            *[
                G.edges[e].animate.set_color(WHITE) for e in edges
            ]
        )
        self.wait(1)

        # Clean up by fading out the graph
        self.play(FadeOut(G))
        self.wait(0.5)

# To render the animation, save this script and run it using the following command in your terminal:
# manim -pql your_script_name.py GraphConvolution
