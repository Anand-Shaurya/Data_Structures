# make a binary tree with the following inpute
#arr = [1,2,3,4,5,6,7,8,9,10]

class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class Tree():
    def __init__(self) :
        self.root = None
    
    def insert_node(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            temp = self.root
            last_node = traverse(temp)
            print(last_node.value)
            if not last_node.left:
                last_node.left = Node(value)
            elif not last_node.right:
                last_node.right = Node(value)
    
    def insert_node(self, root, value):
        if root:
            visited.append(root.value)
            self.insert_node(root.left, value)
            self.insert_node(root.right, value) 
        return visited

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

# tree1.print()
# print(tree1.print_tree(tree1.root, []))



        
