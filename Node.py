import collections


class Node : 
    def __init__(self , data )  :
        self.left = None  
        self.right = None  
        self.data = data 
    
class BinaryTree : 
    def __init__(self , root) : 
        self.root = Node(root)
    
    def PrintTree(self , trav_type) :
        if trav_type == "preorder"  : 
            return self.preorder_tree(tree.root , "")
        elif trav_type == "inorder" :
            return self.inorder_tree(tree.root , "")
        elif trav_type == "postorder" : 
            return self.postorder_tree(tree.root , "")
        elif trav_type == "levelorder" : 
            return self.levelorder_tree(tree.root)
        else : 
            return False 
    
    def preorder_tree(self , start , trav) : 
        ## ROOT > LEFT > RIGHT
        if start : 
            trav += (str(start.data) + "__" )
            trav = self.preorder_tree(start.left , trav) 
            trav = self.preorder_tree(start.right , trav)
        return trav 
        
    def inorder_tree(self , start , trav) : 
        ## LEFT > ROOT > RIGHT
        if start : 
            trav = self.inorder_tree(start.left , trav) 
            trav += (str(start.data) + "__")
            trav = self.inorder_tree(start.right , trav)
        return trav 
    
    def postorder_tree(self , start , trav)  :
        ## LEFT > RIGHT > ROOT 
        if start : 
            trav = self.postorder_tree(start.left , trav) 
            trav = self.postorder_tree(start.right , trav)
            trav += (str(start.data) + "__")
        return trav 
    def levelorder_tree(self , start) :
        ans = []
        if start is None : 
            return ans 
        
        queue = collections.deque()
        queue.append(start)
        
        while queue :
            currSize = len(queue)
            currList = []
            
            while currSize > 0 :
                currNode = queue.popleft()
                currList.append(currNode.data)
                currSize -= 1
                
                if currNode.left is not None : 
                    queue.append(currNode.left)
                    
                if currNode.right is not None : 
                    queue.append(currNode.right) 
            ans.append(currList) 
        return ans
        
            
        """_summary_
       2
      /  \
     3    4
    / \
   5   6
   [2]
   [3.4]
   [5,6]
        """
    

tree = BinaryTree(2)   
tree.root.left = Node(3)
tree.root.right = Node(4)
tree.root.left.left = Node(5)
tree.root.left.right = Node(6)

print(tree.PrintTree("levelorder"))