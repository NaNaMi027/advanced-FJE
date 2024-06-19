'''
iterator文件
创建Iterator类
用于遍历节点树
'''

class Iterator:
    def __init__(self, stem):
        self.stem = stem
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.stem.children):
            raise StopIteration
        else:
            self.index += 1
            return self.stem.children[self.index-1]
    
    def __len__(self):
        return len(self.stem.children)
    
    def __getitem__(self, index):
        return self.stem.children[index]