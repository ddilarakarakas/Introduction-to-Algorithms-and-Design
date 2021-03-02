number = 0

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data_ = data

    def insert(self, data, insert_control):
        global number
        if self.data_:
            if data < self.data_:
                if 2*data < self.data_:
                    number += 1
                if insert_control:
                    if self.left is None:
                        self.left = Node(data)
                        if self.right is not None:
                            self.right.insert(data, False)
                    else:
                        self.left.insert(data, insert_control)
                        if self.right is not None:
                            self.right.insert(data, False)
                else:
                    if self.left is not None:
                        self.left.insert(data, insert_control)
                    if self.right is not None:
                        self.right.insert(data, insert_control)
            elif data > self.data_:
                if self.right is None:
                    if insert_control:
                        self.right = Node(data)
                else:
                    self.right.insert(data, insert_control)
        else:
            if insert_control:
                self.data_ = data

def inversion(arr):
    root = Node(arr[0])
    for i in range(1,len(arr)):
        root.insert(arr[i],True)

arr = [12,6,14,3,72,1,9]
inversion(arr)
print(number)
