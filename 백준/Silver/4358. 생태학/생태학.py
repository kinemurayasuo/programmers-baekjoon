import sys

# 입력 받기
trees = {}
total_trees = 0
for line in sys.stdin:
    tree = line.strip()
    if tree == "":
        break
    trees[tree] = trees.get(tree, 0) + 1
    total_trees += 1

# 결과 출력
sorted_trees = sorted(trees.items())
for tree, count in sorted_trees:
    percentage = (count / total_trees) * 100
    print(f"{tree} {percentage:.4f}")