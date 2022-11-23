import collections
from graphical import drawtree , deserialize

NodesBeenMade = 0  

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
            global NodesBeenMade 
            NodesBeenMade +=1 
            trav += (str(start.data) + "," )
            trav = self.preorder_tree(start.left , trav) 
            trav = self.preorder_tree(start.right , trav)
        return trav 
        
    def inorder_tree(self , start , trav) : 
        ## LEFT > ROOT > RIGHT
        if start : 
            global NodesBeenMade 
            NodesBeenMade +=1 
            trav = self.inorder_tree(start.left , trav) 
            trav += (str(start.data) + ",")
            trav = self.inorder_tree(start.right , trav)
        return trav 
    
    def postorder_tree(self , start , trav)  :
        ## LEFT > RIGHT > ROOT 
        if start : 
            global NodesBeenMade 
            NodesBeenMade +=1 
            trav = self.postorder_tree(start.left , trav) 
            trav = self.postorder_tree(start.right , trav)
            trav += (str(start.data) + ",")
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
    
    def floors_number(self) : 
        result = tree.PrintTree("levelorder")
        return len(result)
    
    def delete_tree(self) : 
        tree.root = None 
        
    def MAX_MIN(self) : 
        result = tree.PrintTree("preorder")
        result = result.split(",")
        result.pop()
        result = [int(x) for x in result ]
        return max(result),min(result)
    
    def find(self , atribute) : 
        result = tree.PrintTree("levelorder")
        x = 0 
        for i in result :
            x +=1  
            for j in i : 
                if j == atribute : 
                    return x
        return "Not Found ! "
    
    def MakeList(self , type ) -> list :
        MyList = []
        result = tree.PrintTree(type)
        for i in result :
            if i != "," : 
                MyList.append(int(i))
        return MyList
    
    def compare(self , type ) : 
        result = tree.MakeList(type)
        print(result)
        lst = list(map(int , input('Enter your tree with desired order : ').split()))
        return True if result == lst else False
    
    def draw(self) :
        result = tree.PrintTree('levelorder') 
        result_fixed = []
        for i in result : 
            for j in i :
                result_fixed.append(j)
        drawtree(deserialize(str(result_fixed)))    
    
    def countLeaves(self) : 
        result = tree.PrintTree("levelorder")
        return len(result[2])         
            
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


# making a test binary tree 
tree = BinaryTree(2)   
tree.root.left = Node(3)
tree.root.right = Node(4)
tree.root.left.left = Node(5)
tree.root.left.right = Node(6)

# trying out the methods 
print(tree.PrintTree('preorder'))
print(tree.PrintTree('inorder'))
print(tree.PrintTree('postorder'))
print(tree.PrintTree('levelorder'))
print(tree.floors_number())
print(tree.MAX_MIN())
print(tree.find(7))
print(tree.draw())
print(tree.countLeaves())


