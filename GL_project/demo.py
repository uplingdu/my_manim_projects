from manimlib import *


class Mytest(Scene):
    def construct(self):

        """
        grid = NumberPlane()
        self.add(grid)
        """

        r0 = Rectangle(height=1.2, width=0.1).set_fill(BLUE, opacity=1).set_stroke(BLUE)
        r1 = Rectangle(height=1.4, width=0.1).set_fill(BLUE, opacity=1).set_stroke(BLUE)
        r2 = Rectangle(height=1.6, width=0.1).set_fill(BLUE, opacity=1).set_stroke(BLUE)
        r3 = Rectangle(height=1.0, width=0.1).set_fill(BLUE, opacity=1).set_stroke(BLUE)
        r4 = Rectangle(height=1.8, width=0.1).set_fill(BLUE, opacity=1).set_stroke(BLUE)
        r5 = Rectangle(height=2.0, width=0.1).set_fill(BLUE, opacity=1).set_stroke(BLUE)
        r6 = Rectangle(height=2.2, width=0.1).set_fill(BLUE, opacity=1).set_stroke(BLUE)
        r7 = Rectangle(height=2.4, width=0.1).set_fill(BLUE, opacity=1).set_stroke(BLUE)
        r8 = Rectangle(height=2.6, width=0.1).set_fill(BLUE, opacity=1).set_stroke(BLUE)
        r9 = Rectangle(height=2.8, width=0.1).set_fill(BLUE, opacity=1).set_stroke(BLUE)

        mobs = VGroup(r0, r1, r2, r3, r4, r5, r6, r7, r8, r9)

        """
        mobjects = VGroup(
        Rectangle(height=2,width=0.1).set_fill(BLUE,opacity=1).set_stroke(BLUE),
        Rectangle(height=2.2,width=0.1).set_fill(BLUE,opacity=1).set_stroke(BLUE),
        Rectangle(height=2.4,width=0.1).set_fill(BLUE,opacity=1).set_stroke(BLUE),
        Rectangle(height=1.8,width=0.1).set_fill(BLUE,opacity=1).set_stroke(BLUE),
        Rectangle(height=2.6,width=0.1).set_fill(BLUE,opacity=1).set_stroke(BLUE),
        Rectangle(height=2.8,width=0.1).set_fill(BLUE,opacity=1).set_stroke(BLUE),
        )
        """


        mobs.arrange(RIGHT, buff=0.1, aligned_edge=DOWN)
        self.play(*[FadeIn(mob) for mob in mobs])
        # move_to() 方法在这里会偏移 
        self.play(r3.shift, LEFT * 3)
        self.play(r2.shift, RIGHT * 0.2)
        self.play(r1.shift, RIGHT * 0.2)
        self.play(r0.shift, RIGHT * 0.2)
        self.play(r3.shift, RIGHT * 2.4)
