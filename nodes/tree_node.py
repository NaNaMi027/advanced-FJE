'''
tree_node文件
继承自node.py
用于构建树形结构
'''
from nodes.node import Node

class TreeNode(Node):
    def accept(self, visitor, icon_family=None):
        visitor.visit(self, icon_family)

    def display(self, icon_family=None):
        for child in self.children:
            child.display_without_root(icon_family=icon_family)

    def display_without_root(self, icon_family=None):
        if icon_family is not None:
            if len(self.children) == 0:
                icon = icon_family.leaficon
            else:
                icon = icon_family.midicon
        else:
            icon = " "
        if self.value is not None and self.value != "None":
            self.value = f": {self.value}"
        else:
            self.value = ""
        prefix = ""
        if self.level > 0:
            if self.Lastchar:
                prefix += "   " * (self.level - 1) + "   "
            else:
                prefix += "│  " + (self.level - 1) * "   "
        if self.isLast == True:
            print(prefix + "└─" + icon + self.name + self.value)
        else:   
            print(prefix + "├─" + icon + self.name + self.value)
        for child in self.children:
            child.display_without_root(icon_family=icon_family)
