import FreeCAD
from FreeCAD import Base

doc = FreeCAD.newDocument('Cylinders')
cs = []
for i in range(10):
    b = Part.makeCylinder(10,20)
    vec = Base.Vector(20*i,0,0)
    b.translate(vec)
    Part.show(b)
    cs.append(b)

