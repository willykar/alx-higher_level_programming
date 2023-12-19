#!/usr/bin/python3
"""A classes for a singly-linked list"""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A singly-linked list"""

    def __init__(self):
        """A new SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new Node to the SinglyLinkedList
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tempo = self.__head
            while (tempo.next_node is not None and
                    tempo.next_node.data < value):
                tempo = tempo.next_node
            new.next_node = tempo.next_node
            tempo.next_node = new

    def __str__(self):
        """Print() representation of a SinglyLinkedList"""

        values = []
        tempo = self.__head
        while tempo is not None:
            values.append(str(tempo.data))
            tempo = tempo.next_node
        return ('\n'.join(values))
