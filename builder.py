'''
builder文件
定义了Builder类
用于构建树形结构
'''
from factories.different_factory import AbstractFactory

class Builder:
    def __init__(self, factory: AbstractFactory):
        self.factory = factory

    def recbuild(self, parent_node, data, level=0, Lastchar=False):
        data_len = len(data)
        for i, (key, value) in enumerate(data.items()):
            if level == 0 :
                if i == data_len - 1:
                    Lastchar = True
                else:
                    Lastchar = False
            if isinstance(value, dict):
                node = self.factory.create_node(key)
                parent_node.adding_child(node)
                self.recbuild(node, value, level+1, Lastchar)
            else:
                node = self.factory.create_node(key, str(value))
                parent_node.adding_child(node)
            if i == 0:
                node.isFirst = True
            else:
                node.isFirst = False
            if i == data_len - 1:
                node.isLast = True
            else:
                node.isLast = False
            node.level = level
            node.Lastchar = Lastchar

    def first_row(self, root_node):
        root_node.children[0].FirstRow = True

    def last_row(self, root_node):
        if len(root_node.children) > 1:
            self.last_row(root_node.children[-1])
        elif len(root_node.children) == 1:
            self.last_row(root_node.children[0])
        else:
            root_node.LastRow = True
    
    def build(self, data: dict):
        root = self.factory.create_node("root")
        self.recbuild(root, data)
        self.first_row(root)
        self.last_row(root)
        return root
    
    def display(self, root_node):
        root_node.display()

    def display_without_root(self, root_node):
        root_node.display_without_root()

    

