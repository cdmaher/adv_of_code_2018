import sys, re
from sets import Set

file = open(sys.argv[1], 'r')

lines = file.readlines()

entries = lines[0].split()


class TreeNode:
    def __init__(self, numChildren, numMetadata):
        self.numChildren = numChildren
        self.numMetadata = numMetadata
        self.metadatas = []
        self.children = []
        self.calced = None

    def __str__(self):
        return str(self.numChildren) + ' ' + str(self.numMetadata) + ' ' + str(
            len(self.children))

    def decChildren(self):
        self.numChildren -= 1

    def appendChild(self, node):
        self.children.append(node)

    def setCalced(self, calced):
        self.calced = calced

    def appendMeta(self, meta):
        self.metadatas.append(meta)

    __repr__ = __str__


treeStack = []
metadata = 0

i = 0
curNode = None

print 'entries ' + str(len(entries))

while i < len(entries):
    if len(treeStack) > 0:
        curNode = treeStack[len(treeStack) - 1]

    print 'treeStack ' + str(treeStack)
    if curNode != None and curNode.numChildren == 0:
        treeStack.pop()
        if len(treeStack) > 0:
            treeStack[len(treeStack) - 1].decChildren()
        for meta in range(i, i + curNode.numMetadata):
            metadata += int(entries[meta])
            curNode.appendMeta(int(entries[meta]))
        i += curNode.numMetadata
    else:
        node = TreeNode(int(entries[i]), int(entries[i + 1]))
        treeStack.append(node)
        if len(treeStack) > 1:
            treeStack[len(treeStack) - 2].appendChild(node)
        i += 2

print 'hi ' + str(metadata)
print 'curr ' + str(curNode)

print 'children ' + str(curNode.children)
print 'metas ' + str(curNode.metadatas)


def calcMetadata(node):
    nodeMetadata = 0
    print 'node :' + str(node)
    if len(node.children) == 0:
        calced = reduce((lambda x, y: x + y), node.metadatas)
        node.setCalced(calced)
        return calced
    else:
        for childIndex in node.metadatas:
            if childIndex < len(node.children) + 1:
                if node.children[childIndex - 1].calced == None:
                    nodeMetadata += calcMetadata(node.children[childIndex - 1])
                else:
                    print 'does this work'
                    nodeMetadata += node.children[childIndex - 1].calced
        node.setCalced(nodeMetadata)
        return nodeMetadata


print 'done ' + str(calcMetadata(curNode))
