'''
rectangle_node文件
用于构建矩形结构
继承自node.py中的Node类
'''
from nodes.node import Node
# 指定矩形长度
length = 50

class RectangleNode(Node):
    '''
    矩形节点类，用于构建矩形结构
    '''
    def accept(self, visitor, icon_family=None):
        visitor.visit(self, icon_family)


    def display(self, icon_family=None):
        # 防止展示root节点
        for child in self.children:
            child.display_without_root(icon_family=icon_family)

    def display_without_root(self, icon_family=None):
        # 如果有图标族就使用图标族的图标
        if icon_family is not None:
            if len(self.children) == 0:
                icon = icon_family.leaficon
            else:
                icon = icon_family.midicon
        else:
            icon = " "
        # icon += " "

        # 如果有value就对value进行处理
        if self.value is not None and self.value != "None":
            self.value = f": {self.value}"
        else:
            self.value = ""

        if self.FirstRow:
            cur_str = "┌─" + icon + self.name + self.value + " "
            print(cur_str + (length - len(cur_str) - 1) * "─"  + "┐")
        elif self.LastRow:
            cur_str = "└──" * self.level +  "└─" + icon + self.name + self.value + " "
            print(cur_str + (length - len(cur_str) - 1) * "─"  + "┘")
        else:
            cur_str = "|  " * self.level + "├─" + icon + self.name + self.value + " "
            print(cur_str + (length - len(cur_str) - 1) * "─"  + "┤")

        # 递归打印子节点
        for child in self.children:
            child.display_without_root(icon_family=icon_family)