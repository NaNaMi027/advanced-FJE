'''
visitor文件
用于构建访问者类
'''
from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit(self, node, icon_family=None):
        pass

