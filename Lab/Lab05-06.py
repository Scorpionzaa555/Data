class BSTNode:
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

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

    # def delete(self, data) :
    #     if self.is_empty():
    #         print("Cannot delete Empty tree")
    #         return
    #     else:
    #         start = self.root
    #         while True:
    #             if start.data == data:
    #                 break
    #             elif data < start.data:
    #                 prev = start
    #                 start = start.left
    #             else:
    #                 prev = start
    #                 start = start.right
                
    #         if start.left == None and start.right == None: #ไม่มีลูก
    #             if prev.right.data == data:
    #                 prev.right = None
    #             else:
    #                 prev.left = None
                    
    #         elif start.left != None and start.right != None: #มีลูก 2 ตัว
    #             if data == self.root:
    #                 pass
    #             else:
    #                 start = start.left
    #                 while True:
    #                     if start.right != None:
    #                         start = start.right
    #                     else:
    #                         start = None
    #         else: #มีลูกข้างใดข้างหนึ่ง
    #             start = self.root
    #             # if prev.right.data == data:
    #             #     prev.right = None
                    
    #             # else:
    #             #     prev.left = None
    #             if start.data == data:
    #                 self.root = self.root.next
    #                 return
    #             while start.next != None:
    #                 if start.next.data == data:
    #                     start.next = start.next.next
    #                     return
    #                 start = start.next
    #     return data
    
    def delete(self, data) :
        print(data, end=" ")
        if self.is_empty():
            print("Cannot delete Empty tree")
            return
        else:
            start = self.root
            prev = None
            while True:
                if start.data == data:
                    bfDelNode = prev
                    DelNode = start
                    break
                elif data < start.data:
                    prev = start
                    start = start.left
                else:
                    prev = start
                    start = start.right
                
            if start.left == None and start.right == None: #ไม่มีลูก
                print("No Child?")
                if prev == None:#ถ้าลบ root
                    self.root = None
                    return data
                elif prev.right == DelNode:
                    prev.right = None
                elif prev.left == DelNode:
                    prev.left = None

            elif start.left != None and start.right != None: #มีลูก 2 ตัว
                print("2 Child?")
                prev = start
                start = start.left #ขยับไปดูต้นไม้ซ้าย
                if start.right != None: #ไปล้วงเอาตัวขวาสุดของต้นไม้มา (ถ้ามี) เอาค่ามันมาแทนที่แล้วลบตัวขวาสุดนั้น
                    while True:
                        if start.right != None:#หาไป
                            prev = start
                            start = start.right
                        else:#ขวาสุดละ
                            DelNode.data = start.data
                            prev.right = start.left if start.left != None else None #เช็คว่ามีลูกมั้ย(ลูกถ้ามีก็มีแค่กิ่งซ้ายแน่ๆ)
                            del start
                            break
                else: #ถ้าไม่มี
                    start.right = prev.right
                    if prev == self.root: #ถ้าตัวที่จะลบเป็น root
                        self.root = start
                    else:
                        if bfDelNode.left == DelNode:
                            bfDelNode.left = start
                        elif bfDelNode.right == DelNode:
                            bfDelNode.right = start

            else: #นอกจากนี้(มีลูก 1 ตัว) (หรือมากกว่า แต่ไม่มากกว่าหรอก)
                print("1 Child?")
                if start.left != None: #ถ้าลูกอยู่ซ้าย --------->(ก็อปจากอัน 2 ลูกมาเลย)<-------------
                    prev = start
                    start = start.left #ขยับไปดูต้นไม้ซ้าย
                    if start.right != None: #ไปล้วงเอาตัวขวาสุดของต้นไม้มา (ถ้ามี) เอาค่ามันมาแทนที่แล้วลบตัวขวาสุดนั้น
                        while True:
                            if start.right != None:#หาไป
                                prev = start
                                start = start.right
                            else:#ขวาสุดละ
                                DelNode.data = start.data
                                prev.right = start.left if start.left != None else None #เช็คว่ามีลูกมั้ย(ลูกถ้ามีก็มีแค่กิ่งซ้ายแน่ๆ) ละก็ต่อนู่นนี่
                                del start
                                break
                    else: #ถ้าไม่มี
                        start.right = prev.right #เอาลูกด้านขวาของตัวที่จะลบ มาต่อเป็นลูกของลูกด้านซ้ายของมันเอง
                        if prev == self.root: #กรณีถ้าตัวที่จะลบเป็น root
                            self.root = start
                        else:
                            if bfDelNode.left == DelNode:
                                bfDelNode.left = start
                            elif bfDelNode.right == DelNode:
                                bfDelNode.right = start
                else:#โค้ดเหมือนด้านบน แต่สลับด้าน
                    prev = start
                    start = start.right 
                    if start.left != None:
                        while True:
                            if start.left != None:
                                prev = start
                                start = start.left
                            else:
                                DelNode.data = start.data
                                prev.left = start.right if start.right != None else None
                                del start
                                break
                    else:
                        start.left = prev.left
                        if prev == self.root:
                            self.root = start
                        else:
                            if bfDelNode.left == DelNode:
                                bfDelNode.left = start
                            elif bfDelNode.right == DelNode:
                                bfDelNode.right = start
        return data

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
            print("\nPreorder",end=" ")
            self.preorder(self.root)
            print("\nInorder",end=" ")
            self.inorder(self.root)
            print("\nPostorder",end=" ")
            self.postorder(self.root)

    def findMin(self) :
        start = self.root
        while True:
            if start.left != None:
                start = start.left
            else:
                return start.data

    def findMax(self) :
        start = self.root
        while True:
            if start.right != None:
                start = start.right
            else:
                return start.data

myBST= BST()
myBST.insert(15)
myBST.insert(10)
myBST.insert(8)
myBST.insert(12)
myBST.insert(20)
myBST.insert(18)
myBST.insert(16)
myBST.insert(19)
myBST.insert(25)
myBST.insert(30)
myBST.traverse()
myBST.delete(18)
myBST.traverse()
print("\nMin :", myBST.findMin())
print("Max :", myBST.findMax())
