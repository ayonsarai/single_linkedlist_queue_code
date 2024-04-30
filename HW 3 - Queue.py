#Sarai Ayon
#4/23/2024
# HW 3: Stacks and Queues
# Queues - Implement a queue. You can use a doubly linked list.  Use your HW 1 implementation of a Linked List.

from typing import List 

#This class defines a node for a singly linked list.
# Each node has two attributes: data, which holds the value of the node, and next, 
#which is a reference to the next node in the list.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

#This class represents a singly linked list.
#It has an append method to add a new node with given data to the end of the list.
#If the list is empty (self.head is None), it sets the new node as the head.
#If the list is not empty, it traverses the list until it finds the last node, 
#then appends the new node to the next attribute of the last node.
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)


#Define a Queue class that utilizes the LinkedList class.
class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

#Implement the Enqueue method to add elements to the queue.
    def enqueue(self, data):
        self.linked_list.append(data)

#Implement the Dequeue method to remove elements from the queue.
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        else:
            data = self.linked_list.head.data
            self.linked_list.head = self.linked_list.head.next
            return data
        
#Implement the is_empty method to check if the queue is empty.
    def is_empty(self):
        return self.linked_list.head is None

#Implement the is_full method to check if the queue is full.
    def is_full(self):
        # Linked list implementation doesn't have a predefined limit
        # Return False since there's no practical limit
        return False

#   Implement the peek method to return the front element of the queue.
    def peek(self):
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return None
        else:
            return self.linked_list.head.data




#This part demonstrates the usage of the Queue class.
# It creates a Queue object named queue.
queue = Queue()

#Elements 1, 2, and 3 are enqueued into the queue.
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# One element is dequeued from the queue.
print("Dequeued element:", queue.dequeue())

# Check if the queue is empty
print("Is queue empty?", queue.is_empty())

# Peeks the front element of the queue.
print("Front element of the queue:", queue.peek())





 