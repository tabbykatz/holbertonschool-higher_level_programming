#!/usr/bin/python3


class Node:
    """Define a node
    Args:
        data: what to put in the node
        next_node: which node is next
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get data for this node
        Returns:
            self.__data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """validate and set data for node
        Args:
            value: the int t put in the node as data
        Raises:
            TypeError: if value != int
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """get the next node for this node
        Returns:
            the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set the next node for this node
        Args:
            value: the next node
        Raises:
            TypeError: if it's not a node object
        """
        if value is not None and type(value) != Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """define a sll"""
    def __init__(self):
        self.head = None

    def __str__(self):
        """teach python to print my way
        Returns: the printed thing"""
        printsll = ""
        location = self.head
        while location:
            printsll += str(location.data) + "\n"
            location = location.next_node
        return printsll[:-1]

    def sorted_insert(self, value):
        """insert in a sorted fashion
        Args:
            value: what the value will be on the node
        """
        new = Node(value)
        if not self.head:
            self.head = new
            return
        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            new.next_node = location.next_node
        location.next_node = new
