#http://www.freecadweb.org/wiki/index.php?title=Start_up_and_Configuration

import sys
sys.path.append('/usr/lib/freecad/lib/')
import FreeCAD
from FreeCAD import Base
import Part
import naca

for k in range(1,10000):
    if( k < 10):
        name = '000'+ str(k)
    elif(10 <= k < 100):
        name = '00'+ str(k)
    elif(100 <= k < 1000):
        name = '0' + str(k)
    else:
        name = str(k)
    
    if( k%10 != 0):

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
        #wingpart.ViewObject.hide()
        doc.recompute()

        doc.saveAs('/home/jim/drawings/wings' + name + '.fcstd')
        print 'created wing number ' + name
