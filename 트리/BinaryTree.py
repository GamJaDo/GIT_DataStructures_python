from collections import deque

class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def preorder(n): #전위 순회
    if n is not None:
        print(n.data, end = ' ')
        preorder(n.left)
        preorder(n.right)
def inorder(n): #중위 순회
    if n is not None:
        inorder(n.left)
        print(n.data, end = ' ')
        inorder(n.right)
def postorder(n): #후위 순회
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end = ' ')
def levelorder(root): #레벨 순회
    q = deque()
    q.append(root)
    while q:
        n = q.popleft()
        if n is not None:
            print(n.data, end = ' ')
            q.append(n.left)
            q.append(n.right)

def count_node(n):
    if n is None:
        return 0
    else:
        return 1+count_node(n.left)+count_node(n.right)

def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n):
    if n is None:
        return 0

    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if hLeft > hRight:
        return hLeft + 1
    else:
        return hRight + 1

"""
d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)

print("\n   In-Order : ", end = '')
inorder(root)
print("\n  Pre-Order : ", end = '')
preorder(root)
print("\n Post-Order : ", end = '')
postorder(root)
print("\nLevel-Order : ", end = '')
levelorder(root)

print()
print("노드의 개수 = %d개" %(count_node(root)))
print("단말의 개수 = %d개" %(count_leaf(root)))
print("트리의 높이 = %d" %(calc_height(root)))
"""
