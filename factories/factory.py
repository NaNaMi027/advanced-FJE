'''
factory文件
定义了Factory类
根据style_type返回不同的工厂类
'''
from factories.different_factory import TreeFactory,RectangleFactory

class Factory:
    @staticmethod
    def get_factory(style_type: str):
        if style_type == "tree":
            return TreeFactory()
        elif style_type == "rectangle":
            return RectangleFactory()
        else:
            raise ValueError(f"Unknown style type: {style_type}")
        



