'''
node文件
定义了Node类
用于构建树形结构的节点
'''
class Node:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []
        self.level = 0
        self.isLast = False
        self.Lastchar = False
        self.FirstRow = False
        self.LastRow = False

    def adding_child(self, child):
        self.children.append(child)
        child.level = self.level + 1

    def display(self, icon_family=None):
        pass

    def display_without_root(self, icon_family=None):
        pass

    def set_isLast(self, isLast):
        self.isLast = isLast

    def set_Lastchar(self, Lastchar):
        self.Lastchar = Lastchar

    def set_FirstRow(self, FirstRow):
        self.FirstRow = FirstRow

    def set_LastRow(self, LastRow):
        self.LastRow = LastRow
    
