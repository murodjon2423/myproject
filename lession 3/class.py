from collections import namedtuple
Point2d=namedtuple(typename='Point2d',field_names='x,y',defaults=[8])
Vectors=namedtuple(typename='Vectors',field_names=('x','y','x1','y2'))
p=Point2d(0,0)
p1=Point2d(9)
v=Vectors(3,4,5,6)
'''class Point2d:
    def __init__(self,x,y):
        self.x=x
        self.y=y
p1=Point2d(2,3)
print(p1)
print(p1.__dict__)'''