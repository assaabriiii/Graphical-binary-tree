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
# made a binary tree -> 1 
# node class -> 1 
# insert method -> 1
# NodesBeenMade for number of nodes -> 1
# number of floors -> 1
# how to define number of leaves -> 0
# made the 4 method and its working  -> 1 
# delete the tree -> 1
# MAX and MIN in our tree -> 1 
# full tree -> 0 
# compare of two tree -> 1 



tree = BinaryTree(2)   
tree.root.left = Node(3)
tree.root.right = Node(4)
tree.root.left.left = Node(5)
tree.root.left.right = Node(6)




# print(tree.PrintTree("preorder"))
# result = tree.MAX_MIN()
# print("MAX and MIN is equal to : " , result)
# x = tree.find(5)
# print("Found the desired element at the : [" , x , "] floor ")
print(tree.draw())

# lst = list(map(int , input('Enter your tree with ' , type , " order : ").split()))
# print(lst)

