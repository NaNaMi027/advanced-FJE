'''
different_factory文件
定义了TreeFactory和RectangleFactory两个工厂类
分别用于创建TreeNode和RectangleNode对象。
'''
from abc import ABC, abstractmethod
from nodes.tree_node import TreeNode
from nodes.rectangle_node import RectangleNode

class AbstractFactory(ABC):
    @abstractmethod
    def create_node(self, name: str, value: str = None):
        pass

class TreeFactory(AbstractFactory):
    def create_node(self, name: str, value: str = None):
        return TreeNode(name, value)

class RectangleFactory(AbstractFactory):
    def create_node(self, name: str, value: str = None):
        return RectangleNode(name, value)