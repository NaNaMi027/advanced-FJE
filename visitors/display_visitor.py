'''
display_visitor文件
用于构建展示访问者类
继承自Visitor类
'''

from visitors.visitor import Visitor

class TreeDisplayVisitor(Visitor):
    def visit(self, node, icon_family=None):
        node.display_without_root(icon_family)

class RectangleDisplayVisitor(Visitor):
    def visit(self, node, icon_family=None):
        node.display_without_root(icon_family)