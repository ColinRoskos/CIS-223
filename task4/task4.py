# CIS-223
# Author: Colin Roskos
# Date: 4/1/2020
# Task 4
#
# Implement binary search tree
#
#

class Node:
    """
    binary tree node.
    has a left and right child and a stored value.
    """

    def __init__(self, key=None):
        self.left_child = None
        self.right_child = None
        self.value = key

    def getValue(self):
        return self.value

    def setValue(self, new_value):
        self.value = new_value

    def getLeft(self):
        return self.left_child

    def setLeft(self, node):
        self.left_child = node

    def getRight(self):
        return self.right_child

    def setRight(self, node):
        self.right_child = node


class BST:
    """
    BST : Binary Search Tree
    """

    def __init__(self):
        self.root = None

    def insertNode(self, node):
        if not isinstance(node, Node):
            node = Node(node)
        if self.root is None:
            self.root = node
            node.setLeft(None)
            node.setRight(None)
            return
        cur = self.root
        while cur is not None:
            if node.getValue() < cur.getValue():
                if cur.getLeft() is None:
                    cur.setLeft(node)
                    cur = None
                else:
                    cur = cur.getLeft()
            else:
                if cur.getRight() is None:
                    cur.setRight(node)
                    cur = None
                else:
                    cur = cur.getRight()
            node.setLeft(None)
            node.setRight(None)

    def deleteNode(self, key, _from=None):
        if key is None:
            return False
        par = None
        if _from is None:
            cur = self.root
        else:
            cur = _from

        while cur is not None:
            if cur.getValue() == key:
                if cur.getLeft() is None and cur.getRight() is None:
                    if par is None:
                        self.root = None
                    elif par.getLeft() == cur:
                        par.setLeft(None)
                    elif par.getRight() == cur:
                        par.setRight(None)
                elif cur.getLeft() is not None and cur.getRight() is None:
                    if par is None:
                        self.root = cur.getLeft()
                    elif par.getLeft() == cur:
                        par.setLeft(cur.getLeft())
                    else:
                        par.setRight(cur.getLeft())
                elif cur.getLeft() is None and cur.getRight() is not None:
                    if par is None:
                        self.root = cur.getRight()
                    elif par.getLeft() == cur:
                        par.setLeft(cur.getRight())
                    else:
                        par.setRight(cur.getRight())
                else:
                    suc = cur.getRight()
                    while suc.getLeft() is not None:
                        suc = suc.getLeft()
                    suc_value = suc.getValue()
                    self.deleteNode(suc_value, cur)
                    cur.setValue(suc_value)
                return
            elif cur.getValue() < key:
                par = cur
                cur = cur.getRight()
            else:
                par = cur
                cur = cur.getLeft()
        return


    def searchNode(self, key):
        if key is None or self._search(self.root, key) is None:
            return "Not Found"
        return "Found"

    def _search(self, node, key):
        if node is None:
            return None
        node_value = node.getValue()
        if node_value == key:
            return node
        if key < node_value:
            return self._search(node.left_child, key)
        if node_value < key:
            return self._search(node.right_child, key)

    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.getLeft())
        print(node.getValue(), end=" ")
        self.inOrder(node.getRight())

    def printTree(self):
        self.inOrder(self.root)


def main():

    tree = BST()
    tree.insertNode(2)
    tree.insertNode(1)
    tree.insertNode(1)
    tree.insertNode(4)
    tree.insertNode(3)
    tree.insertNode(5)
    print(tree.searchNode(5))
    print(tree.searchNode(10))
    tree.deleteNode(2)
    tree.printTree()


if __name__ == '__main__':
    main()
