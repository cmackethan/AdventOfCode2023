import sys
import time

visited_nodes = []
queue = []

class Node:
    def __init__(self, type: str, x: int, y: int):
        self.type = type
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def getNorth(self, data: list[str]):
        if self.y - 1 >= 0 and (self.x, self.y - 1) not in visited_nodes:
            return Node(data[self.y - 1][self.x], self.x, self.y - 1)
    
    def getSouth(self, data: list[str]):
        if self.y + 1 < len(data) and (self.x, self.y + 1) not in visited_nodes:
            return Node(data[self.y + 1][self.x], self.x, self.y + 1)
    
    def getEast(self, data: list[str]):
        if self.x + 1 < len(data[self.y]) and (self.x + 1, self.y) not in visited_nodes:
            return Node(data[self.y][self.x + 1], self.x + 1, self.y)
    
    def getWest(self, data: list[str]):
        if self.x - 1 >= 0 and (self.x - 1, self.y) not in visited_nodes:
            return Node(data[self.y][self.x - 1], self.x - 1, self.y)

def solve(file: str) -> int:
    data = list[str](map(lambda s: s.strip(), open(file, 'r').readlines()))
    (y, x) = getStartingPos(data)
    # root = Node('-', x, y) # TODO: Determine type at runtime
    root = Node('F', x, y)
    buildTree(data, root)
    printTree(root, 0)
    return height(root) - 1

def printTree(n: Node, level: int):
    if n != None:
        printTree(n.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(n.type))
        printTree(n.right, level + 1)

def buildTree(data: list[str], n: Node) -> int:
    if n == None:
        return
    elif n.type == '|':
        n.left  = n.getNorth(data)
        n.right = n.getSouth(data)
    elif n.type == '-':
        n.left  = n.getEast(data)
        n.right = n.getWest(data)
    elif n.type == 'L':
        n.left  = n.getNorth(data)
        n.right = n.getEast(data)
    elif n.type == 'J':
        n.left  = n.getNorth(data)
        n.right = n.getWest(data)
    elif n.type == '7':
        n.left  = n.getSouth(data)
        n.right = n.getWest(data)
    elif n.type == 'F':
        n.left  = n.getSouth(data)
        n.right = n.getEast(data)

    visited_nodes.append((n.x, n.y))

    queue.append(n.left)
    queue.append(n.right)

    buildTree(data, queue.pop(0))
    buildTree(data, queue.pop(0))

    return n

def getStartingPos(data: list[str]) -> (int, int):
    for i, line in enumerate(data):
        if 'S' in line:
            return (i, line.index('S'))

def height(root: Node) -> int:
    if root == None:
        return 0
    
    leftHeight = height(root.left)
    rightHeight = height(root.right)

    return 1 + max(leftHeight, rightHeight)

start_time = time.time()
print(solve('/Users/cmackethan/Development/AdventOfCode/day10/testinput2.txt'))
print("--- %s seconds ---" % (time.time() - start_time))