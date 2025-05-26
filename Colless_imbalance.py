### Example
# frin Bio import Phylo
# from io import StringIO
# demo_tree_a = Phylo.read(StringIO("((c,d)a,b)root;"), "newick")
# import matplotlib.pyplot as plt
# Phylo.draw_ascii(demo_tree_a)



# Calculate the number of descendants for a specific node.
def count_desc(node):
    if node.is_terminal():
        return 0
    count = 0
    for subclade in clade.clades:
        count += 1 + count_descendants(subclade)
    return count

# Colless imbalance is a metric that relates to the shape of phylogenetic trees.
def colless_imbalance(tree):
    """
    input: a Newick.Tree object including a rooted binary tree
    Assumptions: Every node in tree has a unique name and has either 0 children or 2 children
    Return a floating-point number
    """

    nodes = [clade for clade in tree.find_clades(order = "level")]
    n = len(nodes)
    if n < 3:       # If tree contains fewer than 3 nodes, we can't calculate.
        return None
    
    imbalance_ttl = 0
    for node in nodes:
        if node.is_terminal() == False:
            desc_nodes = node.clades
            imbalance = abs(count_desc(desc_nodes[0]) - count_desc(desc_nodes[1]))
            imbalance_ttl += imbalance

    collece = imbalance_ttl / ((n - 1) * (n - 2) / 2)
    return collece
