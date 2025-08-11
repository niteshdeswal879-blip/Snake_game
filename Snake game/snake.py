from turtle import Turtle
MOVE_DISTANCE=20
STARTING_POSITIONS=[(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__ (self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle()
        tim.color("white")
        tim.shape("square")
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_no - 1].xcor()
            new_y = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def snake_reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)

        self.segments.clear()
        self.create_snake()


    def up(self):
        if self.segments[0].heading()==270:
            self.segments[0].setheading(270)
        else:
            self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading()==90:
            self.segments[0].setheading(90)
        else:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading()==180:
            self.segments[0].setheading(180)
        else:
            self.segments[0].setheading(0)
    def left (self):
        if self.segments[0].heading()==0:
            self.segments[0].setheading(0)
        else:
            self.segments[0].setheading(180)