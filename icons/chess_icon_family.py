'''
ChessIconFamily文件
定义了ChessIconFamily类
继承自IconFamily类
用于定义象棋图标族
'''
from icons.icon_family import IconFamily

class ChessIconFamily(IconFamily):
    def __init__(self):
        super().__init__("♚", "♖")
