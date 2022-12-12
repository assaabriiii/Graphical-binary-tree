class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)
    
root = None

def Banching(data):
    for d in data:
        insert(root, d)

def insert(node, value):
    global root
    if root == None:
        root = TreeNode(value)
        return
    
    if node.val > value:
        if node.left != None:
            insert(node.left, value)
        else:
            node.left = TreeNode(value)
    elif node.val < value:
        if node.right != None:
            insert(node.right, value)
        else:
            node.right = TreeNode(value)
    else:
        print("dublicated")

def drawtree():
    global root
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y-20)
            t.write(str(node.val), align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x-dx, y-60, dx/2)
            jumpto(x, y-20)
            draw(node.right, x+dx, y-60, dx/2)
    import turtle
    t = turtle.Turtle()
    t.speed(0); turtle.delay(0)
    h = height(root)
    jumpto(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()
    
if __name__ == '__main__':
    Banching([2,3,1,4,5])
    drawtree()
    
    
    
# BINARY TREE EXPLANTION
    
