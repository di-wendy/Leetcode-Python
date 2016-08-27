# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 20:20:27 2016

@author: diwang
"""

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)
        

def print_list(node):
    while node:
        print node,
        node = node.next
    print


'''
n = len(list_input)
for i in range(0,n):
    if i%2 == 0:
        list_output.append(list_input[i])

for i in range(0,n):
    if i%2 != 0:
        list_output.append(list_input[i])
        '''

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

head = node1


if head:
            last_ji, record = head, head.next   
            while record and record.next:
                first_ou = last_ji.next
                last_ji.next = record.next
                last_ji = last_ji.next
                record.next = last_ji.next
                last_ji.next = first_ou
                record = record.next 
                
                
                

        
'''                first_ou = last_ji.next
                last_ji.next = record.next
                last_ji = last_ji.next
                record.next = last_ji.next
                last_ji.next = first_ou
                record = record.next    '''
        
        
        
