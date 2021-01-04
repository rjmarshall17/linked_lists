# -*- coding: utf-8 -*-

import sys


# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return "value=%s prev=%s next=%s" % (self.value,
                                             self.prev.value if self.prev is not None else "None",
                                             self.next.value if self.next is not None else "None")


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        # print('insertBefore: post remove: %s' % nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        # print('insertBefore: after insert: %s' % nodeToInsert)
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        for node in self.getNodesWithValue(value):
            self.remove(node)

    def getNodesWithValue(self, value):
        node = self.head
        ret = []
        while node is not None:
            if node.value == value:
                ret.append(node)
            node = node.next
        return ret

    def remove(self, node):
        # print("remove: About to remove: %s" % node)
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    def containsNodeWithValue(self, value):
        nodes = self.getNodesWithValue(value)
        return len(nodes) > 0

    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
            # print("removeNodeBindings: node.prev=%s" % node.prev)
        if node.next is not None:
            node.next.prev = node.prev
            # print("removeNodeBindings: node.next=%s" % node.next)
        node.prev = None
        node.next = None


def getNodeValuesHeadToTail(linkedList):
    values = []
    node = linkedList.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values


def getNodeValuesTailToHead(linkedList):
    values = []
    node = linkedList.tail
    # print("The current tail is: %s" % (node.value))
    while node is not None:
        values.append(node.value)
        # print("tailToHead: node.value=%s node.prev.value=%s" % (node.value,node.prev.value if node.prev is not None else "None"))
        node = node.prev
    return values


def bindNodes(nodeOne, nodeTwo):
    nodeOne.next = nodeTwo
    nodeTwo.prev = nodeOne
    # print("bindNode got: nodeOne=%s nodeTwo=%s" % (nodeOne.value,nodeTwo.value))
    # print("nodeOne is: %s" % nodeOne)
    # print("nodeTwo is: %s" % nodeTwo)
    # print("="*20)


if __name__ == '__main__':
    linkedList = DoublyLinkedList()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    three2 = Node(3)
    three3 = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    bindNodes(one, two)
    bindNodes(two, three)
    bindNodes(three, four)
    bindNodes(four, five)
    # linkedList.setHead(one)
    # linkedList.insertAfter(one,two)
    # linkedList.insertAfter(two,three)
    # linkedList.insertAfter(three,four)
    # linkedList.insertAfter(four,five)
    # print("After inserts head to tail: %s" % getNodeValuesHeadToTail(linkedList))
    # print("After inserts tail to head: %s" % getNodeValuesTailToHead(linkedList))
    linkedList.head = one
    linkedList.tail = five

    assert getNodeValuesHeadToTail(linkedList) == [1, 2, 3, 4, 5], "1 failed"
    assert getNodeValuesTailToHead(linkedList) == [5, 4, 3, 2, 1], "2 failed"

    linkedList.setHead(four)

    print("Head to tail: %s" % getNodeValuesHeadToTail(linkedList))
    print("Tail to head: %s" % getNodeValuesTailToHead(linkedList))
    sys.stdout.flush()

    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 3, 5], "1 failed"
    assert getNodeValuesTailToHead(linkedList) == [5, 3, 2, 1, 4], "2 failed"

    linkedList.setTail(six)
    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 3, 5, 6]
    assert getNodeValuesTailToHead(linkedList) == [6, 5, 3, 2, 1, 4]

    linkedList.insertBefore(six, three)
    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 5, 3, 6]
    assert getNodeValuesTailToHead(linkedList) == [6, 3, 5, 2, 1, 4]

    linkedList.insertAfter(six, three2)
    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 5, 3, 6, 3]
    assert getNodeValuesTailToHead(linkedList) == [3, 6, 3, 5, 2, 1, 4]

    linkedList.insertAtPosition(1, three3)
    assert getNodeValuesHeadToTail(linkedList) == [3, 4, 1, 2, 5, 3, 6, 3]
    assert getNodeValuesTailToHead(linkedList) == [3, 6, 3, 5, 2, 1, 4, 3]

    linkedList.removeNodesWithValue(3)
    print(getNodeValuesHeadToTail(linkedList))
    print(getNodeValuesTailToHead(linkedList))
    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 2, 5, 6]
    assert getNodeValuesTailToHead(linkedList) == [6, 5, 2, 1, 4]

    linkedList.remove(two)
    assert getNodeValuesHeadToTail(linkedList) == [4, 1, 5, 6]
    assert getNodeValuesTailToHead(linkedList) == [6, 5, 1, 4]

    assert linkedList.containsNodeWithValue(5) == True

    # linkedList.setTail(six)
    # self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 3, 5, 6])
    # self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 5, 3, 2, 1, 4])

    # linkedList.insertBefore(six, three)
    # self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 5, 3, 6])
    # self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 3, 5, 2, 1, 4])

    # linkedList.insertAfter(six, three2)
    # self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 5, 3, 6, 3])
    # self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 6, 3, 5, 2, 1, 4])

    # linkedList.insertAtPosition(1, three3)
    # self.assertEqual(getNodeValuesHeadToTail(linkedList), [3, 4, 1, 2, 5, 3, 6, 3])
    # self.assertEqual(getNodeValuesTailToHead(linkedList), [3, 6, 3, 5, 2, 1, 4, 3])

    # linkedList.removeNodesWithValue(3)
    # self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 2, 5, 6])
    # self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 5, 2, 1, 4])

    # linkedList.remove(two)
    # self.assertEqual(getNodeValuesHeadToTail(linkedList), [4, 1, 5, 6])
    # self.assertEqual(getNodeValuesTailToHead(linkedList), [6, 5, 1, 4])

    # self.assertEqual(linkedList.containsNodeWithValue(5), True)
