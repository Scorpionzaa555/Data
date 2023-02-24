class BSTNode:
    def __init__(self, data) :
        self.data= data
        self.left=None
        self.right= None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        if self.root == None:
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
            while start:
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
        #return

    # def delete(self, data) :
    #     # deletedatafromBST

    def preorder(self, root) :
        if (root != None):
            print("->",root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root) :
        if (root != None):
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
            print("Preorder",end='')
            self.preorder(self.root)
            print("\nInorder",end='')
            self.inorder(self.root)
            print("\nPostorder",end='')
            self.postorder(self.root)

    def findMin(self, num) :
        while num.left != None:
            num = num.left
        return num.data

    def findMax(self, num) :
        while num.right != None:
            num = num.right
        return num.data

myBST= BST()
myBST.insert(14)
myBST.insert(23)
myBST.insert(7)
myBST.insert(10)
myBST.insert(33)
myBST.traverse()
print("\nMin:", myBST.findMin(myBST.root))
print("Max:", myBST.findMax(myBST.root))
