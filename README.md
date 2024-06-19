# 设计文档

| 姓名  | 学号       | 任务      |
| --- | -------- | ------- |
| 李宇轩 | 21307032 | FJE进阶设计 |
## 设计模式：
* 类图如下：
  

* 文件与模式：
  * data.json中为输入数据，可自行修改
  * icons文件夹下为icon模块：
    * icon_family.py文件中为图标族类
	    * chess_icon_family.py文件中定义了ChessIconFamily类，继承自IconFamily类
	    * star_icon_family.py文件中定义了StarIconFamily类，继承自IconFamily类
  * builder.py文件定义了Builder类，用于构建树形结构，调用Factory，为**建造者设计模式**
  * factories文件夹下为factory模块：
    * different_factory.py文件，定义了三个类，分别为抽象工厂类AbstractFactory以及继承自AbstractFactory的两个类：
	    * TreeFactory类，用于创建树类风格对象
	    * RectangleFactory类，用于创建矩形风格对象
	  * factory.py文件，定义Factory类，用于调用不同风格的工厂类，为**工厂设计模式**
  * nodes文件夹下为nodes模块：
    * node.py文件，定义了Node类，用于构建树形结构的节点
	    * tree_node.py文件，定义了TreeNode类，继承自Node类，用于构建树类风格的节点
	    * rectangle_node.py文件，定义了RectangleNode类，继承自Node类，用于构建矩形风格的节点
    * node相关文件使用了**组合设计模式**
  * visitors文件夹下为访问者模块：
    * visitor.py文件定义了Visitor类，用于构建访问者
      * display_visitor.py文件定义了TreeDisplayVisitor类和RectangleDisplayVisitor类，继承自Visitor类，用于展示访问者
    * iterator.py文件，定义了Iterator类，用于迭代，遍历节点树
  * main文件


## 运行结果：
执行 python main.py执行即可，结果如下：
![alt text](image/四次运行FJE.png)


上述内容为四次运行fje的结果：

其中前两种为星星图标族情况下树形风格和矩形风格的结果，可见五芒星和六芒星分别在中间节点和叶子节点前

后两种为国际象棋图标族情况下树形风格和矩形风格的结果，可见填充和镂空象棋分别在中间节点和叶子节点前


## 参考资料：
* unicode 制表符与图标： https://unicode.yunser.com/