# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:44:46 2019

@author: Andrew
"""

class S_Node:
    def __init__(self, val):
        self.val = val
        self.next = None ## the pointer is initially not pointing to anything

    def traverse(self):
        current_node = self
        while(current_node != None):
            print(current_node.val)
            current_node = current_node.next
    
    def remove_duplicates(self):
        already_seen = [self.val]
        current_node = self
        next_node = current_node.next
        while(next_node != None):
            if(next_node.val not in already_seen):
                already_seen.append(next_node.val)
                current_node = next_node
                next_node = current_node.next
            else:
                current_node.next = next_node.next
                next_node = current_node.next
           
            
class D_Node:
    def __init__(self, val):
        self.val = val
        self.next = None ## the next pointer is initially not pointing to anything
        self.previous = None ## the previous pointer is initially not pointing to anything

    def traverse(self):
        current_node = self
        while(current_node != None):
            print(current_node.val)
            current_node = current_node.next
    
    def remove_duplicates(self):
        already_seen = [self.val]
        current_node = self
        next_node = current_node.next
        while(next_node != None):
            if(next_node.val not in already_seen):
                already_seen.append(next_node.val)
                current_node = next_node
                next_node = current_node.next
            else:
                current_node.next = next_node.next
                next_node = current_node.next
                if(next_node != None):
                    next_node.previous = current_node
    
    def delete_node(self):
        current_node = self
        if(current_node.next != None):
            next_node = current_node.next
            next_node.previous = current_node.previous
        if(current_node.previous != None):
            previous_node = current_node.previous
            previous_node.next = current_node.next
            

################
## Problem #1 ##
################
## create a singly linked list with values 12 -> 99 -> 37
node1 = S_Node(12)
node2 = S_Node(99)
node3 = S_Node(37)

node1.next = node2
node2.next = node3

################
## Problem #2 ##
################
## traverse and print the singly linked list from Problem #1
node1.traverse()

################
## Problem #3 ##
################
## create new linked list 12 -> 99 -> 37 -> 12 -> 37 -> 11 -> 5 -> 99
## and remove duplicates
node1 = S_Node(12)
node2 = S_Node(99)
node3 = S_Node(37)
node4 = S_Node(12)
node5 = S_Node(37)
node6 = S_Node(11)
node7 = S_Node(5)
node8 = S_Node(99)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

node1.traverse()
node1.remove_duplicates()
node1.traverse()


################
## Problem #4 ##
################
## create new doubly linked list 12 <-> 99 <-> 37 <-> 12 <-> 37 <-> 11 <-> 5 <-> 99
## delete a node from the doubly linked list
node1 = D_Node(12)
node2 = D_Node(99)
node3 = D_Node(37)
node4 = D_Node(12)
node5 = D_Node(37)
node6 = D_Node(11)
node7 = D_Node(5)
node8 = D_Node(99)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

node2.previous = node1
node3.previous = node2
node4.previous = node3
node5.previous = node4
node6.previous = node5
node7.previous = node6
node8.previous = node7

node1.traverse()
node2.delete_node()
node1.traverse()
node8.delete_node()
node1.traverse()

