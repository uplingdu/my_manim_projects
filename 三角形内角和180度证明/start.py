from manimlib import *
import numpy as np

# 代码写的比较乱希望大家原谅
class test (Scene):
    def construct(self):
        # 默认字体不支持中文,必须更换
        text = Text("三角形内角和180°证明",font='simsun')
        self.add((text))
        self.wait()
        # 第一个证明
        text1 = Text("毕达哥拉斯证明",font='simsun')
        text1.to_edge(UP)
        self.play(Transform(text, text1))
        t = Triangle().scale(2)
        self.play(ShowCreation(t))
        # 把虚线加到三角形顶端
        d = DashedLine()
        d.shift(UP*1.8).scale(2)
        self.play(ShowCreation(d))
        
        arc = ArcBetweenPoints(
            start=np.array([-1, 2, 0]),
            end=np.array([1, 2, 0]),
            angle=PI,
            #fill_color=BLUE_A,          # 填充颜色
            stroke_color=YELLOW,         # 轮廓颜色
            stroke_width=5,             # 轮廓粗细
            
            #gloss=1.0                   # 反光度
        )
        arc.scale(0.5)
        self.play(ShowCreation(arc))
        self.wait(2)
        self.clear()

        # 第二个证明
        text2 = Text("欧几里得证明",font='simsun')
        text2.to_edge(UP)
        self.play(ShowCreation(text2))
        t = Triangle().shift(LEFT*1.5).scale(2)
        self.play(ShowCreation(t))
        d1 = DashedLine()
        d2 = DashedLine()
        # next_to 把三角形和虚线视作一个整体 RIGHT*0.1是为了填充虚线与三角之间的空隙，TAU / 6 调整第二条虚线角度为45°
        d1.next_to(t,RIGHT).shift(DOWN*1.5).scale(2)
        d2.next_to(t,RIGHT,buff=0.8).shift(DOWN*1.5).scale(1.7).set_angle(TAU / 6)
        
        self.play(ShowCreation(d1))
        self.play(ShowCreation(d2))

        arc1 = ArcBetweenPoints(
            start=np.array([1.6, -1.6 , 0]),
            end=np.array([-1.2, -1.6, 0]),
            angle=PI,
            #fill_color=BLUE_A,          # 填充颜色
            stroke_color=YELLOW,         # 轮廓颜色
            stroke_width=5,             # 轮廓粗细
            
            #gloss=1.0                   # 反光度
        )
        arc1.scale(0.5)
        self.play(ShowCreation(arc1))
        self.wait(2)
        self.clear()

        # 第三个证明
        text3 = Text("提波特旋转证明",font='simsun')
        text3.to_edge(UP)
        self.play(ShowCreation(text3))
        #l = Line()
        l = VGroup(
            Line().scale(1),
            Text("Y")
        )
        l.arrange(RIGHT,buff=0.1)
        l.shift(LEFT*0.3)
        l.shift(DOWN*0.5)
        self.play(Rotating(l,angle=PI/3,run_time=2,about_edge = [-1,0,0],))
        self.play(Rotating(l,angle=PI/3,about_edge = [1,1,0],run_time=2))
        self.play(Rotating(l,angle=PI/3,about_edge = [0.8,-0.3,0],run_time=2))
        self.remove(l)
        t = Triangle().scale(1).set_color(YELLOW)
        self.play(Indicate(t))
        self.wait(2)
        self.clear()

        
        # 第四个证明
        text4 = Text("折叠证明",font='simsun')
        text4.to_edge(UP)
        self.play(ShowCreation(text4))
        
        
        t = Triangle()
        self.add(t)
        
        t1 = Triangle().shift(DOWN*1.5).shift(LEFT*0.9)
        t2 = Triangle()
        t2.next_to(t1,RIGHT,buff=0)
        """ self.play(ShowCreation(t))
        self.play(ShowCreation(t1))
        self.play(ShowCreation(t2)) """
        self.add(t,t1,t2)
        self.play(
            Rotate(
                t,
                PI,
                run_time=2,
                axis=RIGHT,
                about_edge =[0,-1,0] ,
            )
        )

        arc = ArcBetweenPoints(
            end=np.array([-1, -2.2, 0]),
            start=np.array([1, -2.2, 0]),
            angle=PI,
            #fill_color=BLUE_A,          # 填充颜色
            stroke_color=YELLOW,         # 轮廓颜色
            stroke_width=5,             # 轮廓粗细
            
            #gloss=1.0                   # 反光度
        )
        arc.scale(0.5)

        self.play(ShowCreation(arc))
        self.wait(2)
        self.clear()

        text4 = Text("谢谢观看",font='simsun')
        #text4.to_edge(UP)
        self.play(ShowCreation(text4))