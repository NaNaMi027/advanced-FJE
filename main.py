import json
from builder import Builder
from factories.factory import Factory
from icons.star_icon_family import StarIconFamily
from icons.chess_icon_family import ChessIconFamily
from visitors.display_visitor import TreeDisplayVisitor
from visitors.display_visitor import RectangleDisplayVisitor
from visitors.iterator import Iterator

# 从文件中读取JSON数据
def load_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    # 读取JSON数据
    json_file_path = 'data.json'
    data = load_data_from_file(json_file_path)
    # 创建tree工厂
    factory = Factory.get_factory("tree")
    # 创建节点树并展示
    builder = Builder(factory)
    root = builder.build(data)
    # 图标族1
    icon_family = StarIconFamily() 
    # 创建访问者
    visitor = TreeDisplayVisitor()
    iterator = Iterator(root)
    for node in iterator:
        node.accept(visitor, icon_family)
    print()

    # 创建rectangle工厂
    factory = Factory.get_factory("rectangle")
    builder = Builder(factory)
    root = builder.build(data)
    # 创建访问者
    visitor = RectangleDisplayVisitor()
    iterator = Iterator(root)
    for node in iterator:
        node.accept(visitor, icon_family)
    print()

    # 创建tree工厂
    factory = Factory.get_factory("tree")
    # 创建节点树并展示
    builder = Builder(factory)
    root = builder.build(data)
    # 图标族2
    icon_family = ChessIconFamily() 
    # 创建访问者
    visitor = TreeDisplayVisitor()
    iterator = Iterator(root)
    for node in iterator:
        node.accept(visitor, icon_family)
    print()

    # 创建rectangle工厂
    factory = Factory.get_factory("rectangle")
    builder = Builder(factory)
    root = builder.build(data)
    # 创建访问者
    visitor = RectangleDisplayVisitor()
    iterator = Iterator(root)
    for node in iterator:
        node.accept(visitor, icon_family)
    print()

if __name__ == "__main__":
    main()
