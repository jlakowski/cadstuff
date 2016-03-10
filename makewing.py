#http://www.freecadweb.org/wiki/index.php?title=Start_up_and_Configuration

import sys
sys.path.append('/usr/lib/freecad/lib/')
import FreeCAD
from FreeCAD import Base
import Part
import naca

name = '2412'
doc = FreeCAD.newDocument(name)

n = 100
fout = naca.naca(name, n)

vecs = []
for i in range(2*n + 1):
    vec = Base.Vector(fout[0][i], fout[1][i],0)
    vecs.append(vec)
lines = []
for i in range(1,2*n+1):
    lin = Part.Line(vecs[i-1], vecs[i])
    lines.append(lin)

lines.append(Part.Line(vecs[2*n], vecs[0]))

wingshape = Part.Shape(lines)
wingwire = Part.Wire(wingshape.Edges)
wingface = Part.Face(wingwire)
wp = wingface.extrude(Base.Vector(0,0,1))

wingpart = doc.addObject('Part::Feature', 'Algowing')
wingpart.Shape = wp 
#doc.recompute()

doc.saveAs('/home/jim/drawings/' + name + '.fcstd')
