









class treeNOde:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def height(root):
    if root==None:
        return 0
    return 1+max(height(root.left),height(root.right))




def traverse(node, level, pos):
    if not node:
        return
    left_padding, spacing = 2 ** (rows - level - 1) - 1, 2 ** (rows - level) - 1
    index = left_padding + pos * (spacing + 1)
    print(level, index, node.val)
    res[level][index] = str(node.val)
    traverse(node.left, level + 1, pos << 1)
    traverse(node.right, level + 1, (pos << 1) + 1)
    traverse(root, 0, 0)
    return res



root=treeNOde(1)
root.left=treeNOde(2)
root.right=treeNOde(3)
root.left.right=treeNOde(4)

rows=height(root)
cols = 2 ** rows - 1
res = [['' for _ in range(cols)] for _ in range(rows)]



print()