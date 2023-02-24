class BSTNode:
    def __init__(self, data) :
        self.data= data
        self.left=None
        self.right= None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        if self.root == No:
            return True
        else:
            return False

    def insert(self, data) :
        pNew = BSTNode(data)
        start = self.root
        #prev = None
        if self.is_empty():
            self.root = pNew
        else:
            while True:
                if data < start.data:
                    if start.left == None:
                        start.left = pNew
                        break
                    else:
                        start = start.left
                else:
                    if start.right == None:
                        start.right = pNew
                        break
                    else:
                        start = start.right
            #while start != None:
            #    if data < start.data:
            #        start.left = pNew
            #    else:
            #        prev = start
            #        start.right = pNew
            #prev.right = pNew
        return

    # def delete(self, data) :
    #     # deletedatafromBST

    def preorder(self, root) :
        if (root != None):
            print("->",root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root) :
        self.inorder(root.left)
        print("->",root.data,end=" ")
        self.inorder(root.right)

    def postorder(self, root) :
        if(root != None):
            self.postorder(root.left)
            self.postorder(root.right)
            print("->",root.data,end=" ")

    def traverse(self) :
        if self.root == None:
            print("Empty")
        else:
            print("preorder",end='')
            self.preorder()
            print("inorder",end='')
            self.inorder()
            print("postorder",end='')
            self.postorder()

    # def findMin(self) :
    #     # return minimum value

    # def findMax(self) :
    #     # return maximum value

myBST= BST()
myBST.insert(14)
#myBST.insert(23)
#myBST.insert(7)
#myBST.insert(10)
#myBST.insert(33)
#myBST.traverse() 