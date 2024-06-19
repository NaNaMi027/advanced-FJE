'''
star_icon_family文件
定义了StarIconFamily类
继承自IconFamily类
用于定义星星图标族
'''
from icons.icon_family import IconFamily

class StarIconFamily(IconFamily):
    def __init__(self):
        super().__init__("☆", "✡")