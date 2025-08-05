
class Tree:
    def __init__(self, num):
        self.val = num
        self.left = None
        self.right = None
        self.parent = None

    def append(self, num):
        node = self
        while node is not None:
            if num > node.val:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = Tree(num)
                    return
            elif num < node.val:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = Tree(num)
                    return

    def traverse(self, code, level):
        node = self
        code += str(level)
        if node.left is not None:
            code += 'L'
            code += node.left.traverse("", level + 1)
        if node.right is not None:
            code += 'R'
            code += node.right.traverse("", level + 1)
        return code



# collect input
nk = input().split(' ')
n = int(nk[0])
k = int(nk[1])

# create trees
trees = []
weights = set()
for i in range(0,n):
    cur_tree = None
    numbers = input().split(' ')
    for num in numbers:
        if cur_tree is None:
            cur_tree = Tree(int(num))
        else:
            cur_tree.append(int(num))
    trees.append(cur_tree)

# determine result
codes = set()
for t in trees:
    codes.add(t.traverse("", 0))
print(len(codes))
