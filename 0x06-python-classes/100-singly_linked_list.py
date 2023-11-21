#!/usr/bin/python3

"""Define a singly linked list module.

This module includes a Node class representing a node in a singly linked list
and a SinglyLinkedList class representing the linked list itself.
"""


class Node:
    """Define a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new node.

        Args:
            data: The data of the node.
            next_node: The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value: The value to set as the data.

        Raises:
            TypeError: If the data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next node in the linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the linked list.

        Args:
            value: The next node to set.

        Raises:
            TypeError: If the next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Define a singly linked list."""

    def __init__(self):
        """Initialize a new singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new node into the correct sorted position in the list.

        Args:
            value: The value to insert into the list.
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and value >= current.next_node.data:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Define the string representation of the linked list."""
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return '\n'.join(values)
