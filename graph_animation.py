from manim import *
import numpy as np

class RecurrentGraphNetwork(Scene):
    def construct(self):
        # Define a graph with multiple nodes and connections
        G = Graph(
            [0, 1, 2, 3, 4, 5, 6, 7],
            [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 0)],
            layout="circular",  # Circular layout for simplicity
            labels=True,
            vertex_config={node: {"fill_color": BLUE} for node in range(8)}
        )

        # Show the initial graph
        self.play(Create(G))
        self.wait(1)

        # Iterate over several time steps to simulate updates
        num_time_steps = 3
        for t in range(num_time_steps):
            # Randomly select some nodes to simulate receiving updates
            updated_nodes = np.random.choice(list(G.vertices), size=4, replace=False)
            edges_to_highlight = [edge for edge in G.edges if edge[0] in updated_nodes and edge[1] in updated_nodes]

            # Highlight nodes and edges being updated
            self.play(
                *[
                    G[v].animate.set_color(RED) for v in updated_nodes
                ],
                *[
                    G.edges[e].animate.set_color(YELLOW) for e in edges_to_highlight
                ]
            )
            self.wait(1)

            # Simulate update
            self.play(
                *[
                    G[v].animate.set_color(PURPLE) for v in updated_nodes
                ]
            )
            self.wait(1)

            # Revert colors before next iteration
            self.play(
                *[
                    G[v].animate.set_color(BLUE) for v in G.vertices
                ],
                *[
                    G.edges[e].animate.set_color(WHITE) for e in edges_to_highlight
                ]
            )
            self.wait(1)

        # Clean up by fading out the graph
        self.play(FadeOut(G))
        self.wait(0.5)

# To render the animation, save this script and run it using the following command in your terminal:
# manim -pql your_script_name.py RecurrentGraphNetwork
