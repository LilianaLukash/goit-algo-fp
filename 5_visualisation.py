import matplotlib.pyplot as plt
import networkx as nx
import uuid

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def visualize_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 8))
    nx.draw(tree, pos=pos, labels=labels, with_labels=True, node_size=2000, node_color=colors, font_weight='bold', arrows=False)
    plt.show()

def dfs(node, colors, current_color=0):
    if not node:
        return current_color
    node.color = colors[current_color % len(colors)]
    current_color += 1
    current_color = dfs(node.left, colors, current_color)
    current_color = dfs(node.right, colors, current_color)
    return current_color

def bfs(root, colors):
    if not root:
        return
    queue = [(root, 0)]
    while queue:
        node, current_color = queue.pop(0)
        node.color = colors[current_color % len(colors)]
        current_color += 1
        if node.left:
            queue.append((node.left, current_color))
        if node.right:
            queue.append((node.right, current_color))

# Creating the tree
root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)

colors = ['#0D3B66', '#0077B6', '#0096C7', '#00B4D8', '#48CAE4', '#90E0EF']

# DFS visualization
dfs(root, colors)
visualize_tree(root)

# Reset colors before BFS
root.color, root.left.color, root.right.color, root.left.left.color, root.left.right.color, root.right.left.color = ["skyblue"]*6

# BFS visualization
bfs(root, colors)
visualize_tree(root)
