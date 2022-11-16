class Node : 
    def __init__(self , data )  :
        self.left = None  
        self.right = None  
        self.data = data 
    
    def insert(self, data) : 
        if data < self.data : 
            if self.left : 
                self.left.insert(data)
            else : 
                self.left = Node(data)
                return
        
        else : 
            if self.right : 
                self.right.insert(data)
            else : 
                self.right = Node(data)
                return
    
    def PrintTree(self) : 
        if self.left : 
            self.left.PrintTree()
        print(self.data)
        if self.right : 
            self.right.PrintTree()

l = Node(2) 
l.insert(5)         
l.insert(1)         
l.insert(7)         
l.insert(9)         
l.insert(10)
l.PrintTree()         