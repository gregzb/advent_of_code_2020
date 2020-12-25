from collections import *
import math
import bisect

data = None

with open('in.txt') as f:
    data = int(f.read().strip())

d = {}

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def remove_3(node):
    # 0 1 2 3 4
    # node.prev is 0
    # node is 1
    # node.next is 2
    # node.next.next is 3
    # node.next.next.next is 4

    node.prev.next = node.next.next.next
    node.next.next.next.prev = node.prev
    node.prev = None
    node.next.next.next = None
    return node

def insert_3(base, node):
    end = base.next
    base.next = node
    node.prev = base
    
    end.prev = node.next.next
    node.next.next.next = end

def contains(nodes, target):
    curr = nodes
    while curr:
        if curr.val == target.val:
            return True
        curr = curr.next
    return False

def sim(curr_node):
    three = remove_3(curr_node.next)
    destination = d[curr_node.val-1]

    while contains(three, destination):
        destination = d[destination.val-1]

    insert_3(destination, three)
    return curr_node.next

def solve(num):
    global d
    cups = [int(cup) for cup in str(num)]
    for i in range(max(cups)+1, 1000000+1):
        cups.append(i)

    max_val = max(cups)

    curr_node = Node(cups[0])
    d[cups[0]] = curr_node
    tmp = curr_node
    for i, val in enumerate(cups):
        if i == 0:
            continue
        tmp.next = Node(val)
        d[val] = tmp.next
        tmp.next.prev = tmp
        tmp = tmp.next
        if i == len(cups) - 1:
            tmp.next = curr_node
            curr_node.prev = tmp
        
        if val == max_val:
            d[0] = tmp

    for _ in range(10000000):
        curr_node = sim(curr_node)

    while curr_node.val != 1:
        curr_node = curr_node.next

    return curr_node.next.val * curr_node.next.next.val
    
solved = solve(data)
print(solved)