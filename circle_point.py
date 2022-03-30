import shapes_module as sm
circle=sm.Circle(sm.Point(2,3),5)
line1=sm.Line(4,(1,11))
line2=sm.Line(3,2)

print(line1)
print(line2)
print(circle)
print(line1.calc_intersect(line2))