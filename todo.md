# manim笔记

## 默认图形

```python
from manimlib import *

class test(Scene):
    def construct(self):
        circle = Circle()
        # 设置圆的填充色，透明度为不透明
        circle.set_fill(BLUE,opacity=1)
        # 设置圆外围颜色，默认是红色
        # circle.set_stroke(WHITE)
        square = Square()
        triangle = Triangle()
        self.add(circle,square,triangle)
```

这段代码向我们展示了如何创建对象，并且把对象添加到场景中去，值得注意的是self.add方法是有顺序的，如果圆最后添加那么三角形就会被覆盖掉

## 自定义图形

```python
from manimlib import *

class test(Scene):
    def construct(self):
        # 创建网格为了更好定位，原点坐标是np.array[x,y,0]
        grid  = NumberPlane()
        
        self.add(grid )
```

## 动画效果物体变化

shift

move_to

scale

rotate

flip

stretch

to_corner

to_edge

align_to

next_to

set_width

set_height
