# -*- coding: utf-8 -*-

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        
    def __repr__(self):
        return "value: %s next=%s" % (self.value,"None" if self.next is None else self.next.value)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def append(self,node):
        if not isinstance(node,Node):
            raise ValueError("append: Node required but not found")
            
        node.next = None            
        if self.head is None:
            self.head = node
        else:
            lastNode = self.__find_at_position__()
            lastNode.next = node
        self.size += 1
    
    def insert(self,node,position=0):
        if not isinstance(node,Node):
            raise ValueError("insert: Node required but not found")
        
        if self.head is None:
            self.head = node
            self.head.next = None
        elif position == 1:
            node.next = self.head
            self.head = node
            print("Just adjusted the head: %s" % self.head)
        elif position == self.size:
            self.append(node)
        else:
            current = self.__find_at_position__(position if position <= 0 else position - 1)
            print("insert: The current node is: %s" % current.value)
            node.next = current.next
            current.next = node
        self.size += 1
        
    def __find_at_position__(self,position=-1):
        if position < 0:
            position = self.size
        if position == 1:
            return self.head
        node = self.head
        count = 1
        while node.next is not None:
            if count >= position:
                break
            node = node.next
            count += 1            
        return node
    
    def getList(self):
        ret = []
        node = self.head
        while node is not None:
            ret.append(node.value)
            node = node.next
        return ret
    
    def __len__(self):
        return self.size

if __name__ == '__main__':
    one = Node("1")
    two = Node("2")
    three = Node("3")
    four = Node("4")
    five = Node("5")
    six = Node("6")
    seven = Node("7")
    
    linkedList = SinglyLinkedList()
    linkedList.append(one)
    linkedList.append(two)
    linkedList.append(three)
    linkedList.append(four)
    linkedList.append(five)
    print("The number of elements in the list is: %d and they are: %s" % (len(linkedList),linkedList.getList()))
    linkedList.insert(six,3)
    print("The number of elements in the list is: %d and they are: %s" % (len(linkedList),linkedList.getList()))
    linkedList.insert(seven,1)
    print("The number of elements in the list is: %d and they are: %s" % (len(linkedList),linkedList.getList()))
    