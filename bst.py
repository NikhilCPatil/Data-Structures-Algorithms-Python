class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root,new_val)

    def insert_helper(self,currentnode,new_val):
        if currentnode.value < new_val:
                if currentnode.right:
                    self.insert_helper(currentnode.right,new_val)
                else:
                    currentnode.right = Node(new_val)
        else:
                if currentnode.left:
                    self.insert_helper(currentnode.left,new_val)
                else:
                    currentnode.left = Node(new_val)            

    def search(self, find_val):
        return self.search_helper(self.root,find_val)

    def search_helper(self,currentnode,find_val):
        if currentnode:
            if currentnode.value == find_val:
                return True
            elif(currentnode.value > find_val):
                return self.search_helper(currentnode.left,find_val)
            else:
                return self.search_helper(currentnode.right,find_val)
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))