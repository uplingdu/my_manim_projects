from manimlib import *

class Hello(Scene):
    def construct(self):
        text = Text("manim安装",font='黑体',font_size=120)
        self.add(text)
        self.wait()