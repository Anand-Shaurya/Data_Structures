# make a binary tree with the following inpute
#arr = [1,2,3,4,5,6,7,8,9,10]

from collections import deque


class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class Tree():
    def __init__(self) :
        self.root = None
    
    
    def insert_node(self, value):
        temp = self.root 
        node = Node(value)
        if not temp:
            self.root = node
            return
        else:
            que = deque([temp])
            while que:
                curr = que.popleft()
                if not curr.left:
                    curr.left = node
                    return
                elif not curr.right:
                    curr.right = node
                    return
                else:
                    que.append(curr.left if curr.left else curr.right)
    

    def print_tree(self, root, visited):
        if root:
            visited.append(root.value)
            self.print_tree(root.left, visited)
            self.print_tree(root.right, visited) 
        return visited
    

    def print(self):
        arr = []
        def dfs(r):
            if not r: return
            arr.append(r.value)
            dfs(r.left)
            dfs(r.right)
        dfs(self.root)
        print(arr)

         
tree1 = Tree()
arr = [1,2,3,4,5,6,7,8,9,10,11]
for i in arr:
    tree1.insert_node(i)

tree1.print()
print(tree1.print_tree(tree1.root, []))



        
