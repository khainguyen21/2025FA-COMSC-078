# --- Tree Data Abstraction ---

def tree(label, branches=[]):
    """Constructor for a tree. Returns a list representation."""
    for b in branches:
        # Verify that all branches are also valid trees.
        assert is_tree(b), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Selector for the label of the root node."""
    return tree[0]

def branches(tree):
    """Selector for the list of branches."""
    return tree[1:]

def is_tree(tree):
    """Verifies if a given list has the structure of a tree."""
    if type(tree) != list or len(tree) < 1:
        return False
    for b in branches(tree):
        if not is_tree(b):
            return False
    return True

def is_leaf(tree):
    """Returns True if a tree has no branches (is a leaf)."""
    return not branches(tree)

def count_leaves(t):
    """Counts the number of leaves in a tree."""
    if is_leaf(t):
        return 1
    else:
        # Sum the leaf counts of all branches.
        return sum([count_leaves(b) for b in branches(t)])


def print_tree(tree, indent=0):
    """
    Print a representation of this tree in which each node is indented
    by two spaces times its depth from the root.
    """
    print('  ' * indent + str(label(tree)))
    for branch in branches(tree):
        print_tree(branch, indent + 1)

# --- Driver Program ---

# 1. Construct the tree using a nested expression.
# The structure is built from the inside out:
# - tree(1) and tree(3) are the leaves of the '2' node.
# - tree(2, [tree(1), tree(3)]) creates the left sub-tree.
# - tree(5) is the right sub-tree (which is also a leaf).
# - The final tree has root '4' with the two sub-trees as its branches.
my_tree = tree(4, [
    tree(2, [tree(1), tree(3)]),
    tree(6, [tree(5)])
])

# 2. Print out the tree and its properties.
print("--- Tree Analysis ---")

# The nested list that represents the tree
print(f"Nested Tree: {my_tree}")

# The label of the root node
print(f"Root Label: {label(my_tree)}")

# The list of branches from the root
print(f"Branches: {branches(my_tree)}")

# The total number of leaves
print(f"Number of Leaves: {count_leaves(my_tree)}")
print("---------------------")