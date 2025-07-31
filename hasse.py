# hasse.py
#
# This module provides functions to visualize a partially ordered set (poset)
# as a Hasse diagram using NetworkX and Matplotlib.
# It includes validation of the poset, transitive reduction, node level assignment,
# and customizable visualization parameters.

import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Tuple

# Define a type alias for pairs representing ordered relations in the poset
Pair = Tuple[int, int]


def remove_reflexive_pairs(pairs: List[Pair]) -> List[Pair]:
    """
    Remove reflexive pairs (x, x) from the input list.

    Reflexive pairs do not appear in the Hasse diagram edges,
    since posets are reflexive by definition but reflexive edges are implicit.

    Parameters:
        pairs (List[Pair]): List of ordered pairs representing the poset.

    Returns:
        List[Pair]: List of pairs excluding reflexive pairs.
    """
    return [pair for pair in pairs if pair[0] != pair[1]]


def transitive_reduction(poset: List[Pair]) -> nx.DiGraph:
    """
    Compute the transitive reduction of the given poset.

    The transitive reduction is the minimal set of edges that
    preserve the reachability of the original poset graph,
    used to create the Hasse diagram without redundant edges.

    Parameters:
        poset (List[Pair]): List of ordered pairs representing the poset.

    Returns:
        nx.DiGraph: Directed graph representing the transitive reduction.
    """
    g = nx.DiGraph()
    g.add_edges_from(poset)  # Create graph from poset edges

    tr = nx.DiGraph()
    tr.add_nodes_from(g.nodes)  # Ensure all nodes are present

    # For each edge, check if there is an intermediate node creating
    # an indirect path; if not, keep the edge.
    for u, v in g.edges:
        if not any(
                nx.has_path(g, u, w) and nx.has_path(g, w, v)
                for w in g.nodes if w not in (u, v)
        ):
            tr.add_edge(u, v)

    return tr


def assign_levels(graph: nx.DiGraph) -> dict:
    """
    Assign hierarchical levels to nodes based on the longest path from sources.

    This facilitates vertical positioning in the Hasse diagram,
    with minimal elements at level 0 and greater elements at higher levels.

    Parameters:
        graph (nx.DiGraph): Directed acyclic graph representing the poset.

    Returns:
        dict: Mapping from node to its assigned level (int).
    """
    levels = {}
    # Topological order guarantees that predecessors have levels assigned first
    for node in nx.topological_sort(graph):
        preds = list(graph.predecessors(node))
        if not preds:
            # Minimal elements start at level 0
            levels[node] = 0
        else:
            # Node level is max predecessor level + 1
            levels[node] = max(levels[pred] + 1 for pred in preds)
    return levels


def is_valid_poset(poset: List[Pair]) -> bool:
    """
    Validate if the input list of pairs represents a valid poset.

    Checks include:
    - Directed acyclic graph (no cycles)
    - Antisymmetry (no pairs (a,b) and (b,a) unless a == b)

    Parameters:
        poset (List[Pair]): List of ordered pairs representing the poset.

    Returns:
        bool: True if valid poset, False otherwise.
    """
    g = nx.DiGraph()
    g.add_edges_from(poset)

    # Check acyclicity (posets must be DAGs)
    if not nx.is_directed_acyclic_graph(g):
        return False

    # Check antisymmetry: no two-way edges unless equal nodes
    edges = set(g.edges)
    for u, v in edges:
        if u != v and (v, u) in edges:
            return False

    return True


def display_hasse_diagram(
        poset: List[Pair],
        title: str = "Hasse Diagram",
        node_color: str = "white"
) -> None:
    """
    Display the Hasse diagram of a poset given as a list of pairs.

    This function:
    - Validates the input poset.
    - Removes reflexive pairs.
    - Computes the transitive reduction.
    - Assigns vertical levels to nodes.
    - Calculates positions for horizontal layout within levels.
    - Adjusts figure size based on the poset structure.
    - Sizes nodes proportionally to the poset size.
    - Sets the window title and displays the graph with Matplotlib.

    Parameters:
        poset (List[Pair]): List of ordered pairs representing the poset.
        title (str): Title for the plot and window.
        node_color (str): Color of the nodes in the plot (default: "white").

    Returns:
        None: The function displays the plot or prints an error.
    """
    # Remove reflexive edges (implicit in posets)
    poset = remove_reflexive_pairs(poset)

    try:
        # Validate poset structure before plotting
        if not is_valid_poset(poset):
            raise ValueError("Input does not represent a valid poset")

        # Compute transitive reduction for minimal edges
        reduced_graph = transitive_reduction(poset)

        # Assign vertical levels based on longest path
        levels = assign_levels(reduced_graph)

        # Group nodes by their level for layout
        level_nodes = {}
        for node, level in levels.items():
            level_nodes.setdefault(level, []).append(node)

        # Calculate positions: horizontal spread per level, vertical by level
        pos = {}
        max_nodes_in_level = max(len(nodes) for nodes in level_nodes.values())
        for level, nodes in level_nodes.items():
            n = len(nodes)
            x_start = - (n - 1) / 2  # Center nodes horizontally
            for i, node in enumerate(sorted(nodes)):
                pos[node] = (x_start + i, -level)  # Negative level to invert y-axis later

        # Dynamically set figure size based on poset size
        width = max(8, max_nodes_in_level * 1.5)
        height = max(6, len(level_nodes) * 1.5)

        # Set node size: bigger for small posets, smaller for large
        n_nodes = reduced_graph.number_of_nodes()
        if n_nodes <= 10:
            node_size = 1000
        else:
            node_size = max(100, int(10000 / n_nodes))

        # Create figure and axis with constrained layout for neat spacing
        fig, ax = plt.subplots(figsize=(width, height), constrained_layout=True)

        # Set the window title to match plot title
        fig.canvas.manager.set_window_title(title)

        # Set extra margins
        xs = [p[0] for p in pos.values()]
        ys = [p[1] for p in pos.values()]

        x_min, x_max = min(xs), max(xs)
        y_min, y_max = min(ys), max(ys)

        x_margin = (x_max - x_min) * 0.3 if (x_max - x_min) != 0 else 1
        y_margin = (y_max - y_min) * 0.3 if (y_max - y_min) != 0 else 1

        ax.set_xlim(x_min - x_margin, x_max + x_margin)
        ax.set_ylim(y_min - y_margin, y_max + y_margin)

        # Draw the graph with customized node appearance
        nx.draw(
            reduced_graph,
            pos,
            ax=ax,
            with_labels=True,
            node_size=node_size,
            node_color=node_color,
            edgecolors='black',  # Node border color
            linewidths=1,  # Border width for nodes
            font_size=10,
            font_weight="bold",
            arrows=False,  # Hasse diagrams omit arrowheads
        )

        # Set the plot title with a bit of vertical padding
        ax.set_title(title, fontsize=14, pad=20)

        # Invert y-axis so minimal elements appear at the bottom
        ax.invert_yaxis()

        # Keep aspect ratio equal to avoid distortion
        ax.set_aspect('equal')

        # Display the plot
        plt.show()

    except ValueError as e:
        # Print error message if the input is not a valid poset
        print(f"Error: {e}")
