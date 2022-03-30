import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return str(self.x)+", "+str(self.y)

class Circle:
    def __init__(self, center, radius):
        self.center=center
        self.radius=radius
        self.update_area()
    def expand_rad(self, inc):
        self.radius+=inc
        self.update_area()
    def update_area(self):
        self.area=0.5*math.pi*(self.radius**2)
    def contains_point(self,point):
        x_diff=abs(self.center.x-point.x)
        y_diff=abs(self.center.y-point.y)
        distance=math.sqrt((x_diff**2)+(y_diff**2))
        print("distance: " + str(distance))
        return distance<=self.radius
class Line:
    def __init__(self,slope,*args):
        self.slope=slope
        if len(args)==1:
            self.y_int=args[0]
        else:
            self.point=Point(args[0],args[1])
            self.y_int=self.calc_y_int()
        print(self.y_int)
    def calc_y(self,x):
        return (x*self.slope)+self.y_int
    def calc_y_int(self):
        return self.point.y-(self.point.x*self.slope)
    def calc_intersect(self,line):
        s2=line.slope
        y2=line.y_int
        assert s2!=self.slope, "Lines are parallel"
        s_diff=s2-self.slope
        y_diff=self.y_int-y2
        x_intersect=y_diff/s_diff
        y_intersect=self.calc_y(x_intersect)
        return(x_intersect,y_intersect)
circle=Circle(Point(0,0),5)
# print(circle.contains_point(Point(-3,-3.9)))
line1=Line(4,1,11)
line2=Line(3,2)
# print(line1.calc_intersect(line2))
#y=3x+7
#y=4x+2
#3x+7=4x+2
#5=x
#y=22