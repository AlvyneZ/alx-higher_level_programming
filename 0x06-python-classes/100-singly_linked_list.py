#!/usr/bin/python3
"""
Module of class for defining a singly-linked list
"""


class Node:
    """
    Class that defines a node of a singly-linked list

    Attributes:
        self.__data (integer): value stored in a node instance
        self.__next_node (Node): next node of the linked list

    Properties:
        data: getter and setter for self.__data
        next_node: getter and setter for self.__next_node
    """
    def __init__(self, data, next_node=None):
        """
        Initializer for setting node attributes

        Args:
            data (integer): value stored in the node
            next_node (Node): next node of the linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the private instance attribute data of a node instance

        Returns:
            The side length of the current square instance
        """
        return self.__data

    @data.setter
    def data(self, data):
        """
        Sets the private instance attribute data checking its type

        Args:
            data (integer): value stored in the node
        """
        if type(data) != int:
            raise(TypeError("data must be an integer"))
        self.__data = data

    @property
    def next_node(self):
        """
        Retrieves the private instance attribute next_node of a node instance

        Returns:
            The next node of the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        """
        Sets the private instance attribute next_node checking its type

        Args:
            next_node (Node): next node of the linked list
        """
        if (next_node is not None) and (type(next_node) != Node):
            raise(TypeError("next_node must be a Node object"))
        self.__next_node = next_node


class SinglyLinkedList:
    """
    Class that defines a singly-linked list head and methods

    Attributes:
        self.__head (Node): starting node of the linked list
    """
    def __init__(self):
        """
        Initializer for setting head to None
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the
            list (increasing order)

        Args:
            value (integer): value to be stored by new node
        """
        if self.__head is None:
            self.__head = Node(value)
            return
        prev = None
        cur = self.__head
        while (cur is not None) and (cur.data < value):
            prev = cur
            cur = cur.next_node
        new_node = Node(value, cur)
        if prev is None:
            self.__head = new_node
        else:
            prev.next_node = new_node

    def __str__(self):
        """
        Converts the singly linked to a printable string of node values
        """
        if self.__head is None:
            return ""
        array = []
        cur = self.__head
        while cur is not None:
            array.append("{:d}".format(cur.data))
            cur = cur.next_node
        return "\n".join(array)


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
