import numpy as np

with open('01-advent-of-code-challenge/08/sample.in', 'r') as f:
    lines = f.readlines()
    lines = [entry.strip() for entry in lines]

trees = np.zeros((len(lines), len(lines[0])), dtype=int)
for i, line in enumerate(lines):
    trees[i, :] = np.array(list(line))

scenic_scores = np.zeros((len(lines), len(lines[0])), dtype=int)

def compute_scenic_score(route):
    big_trees_array = list(route >= 0)
    if True in big_trees_array:
        return big_trees_array.index(True) + 1
    else:
        return len(big_trees_array)

for i in range(1, trees.shape[0]-1):
    for j in range(1, trees.shape[1]-1):
        tree_column = trees[:, j] - trees[i, j]
        tree_row = trees[i, :] - trees[i, j]
        routes = [tree_row[j-1::-1], tree_row[j+1:], tree_column[i-1::-1], tree_column[i+1:]]
        scenic_scores[i,j] = np.prod(list(map(compute_scenic_score, routes)))
    
print(np.max(scenic_scores))