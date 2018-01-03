import FreeCAD as App
from assembly2solver import solveConstraints
import random
import time
import cache_assembly2
import Import
import Mesh
import os

#Import.open("/home/trygve/Programming/pyntcloud/h5_models/robots/IRB140/irb140.FCStd")
MODELdirr = "/home/trygve/Programming/pyntcloud/h5_models/robots/IRB140/"

SCRIPTdirr = "/home/trygve/Programming/pyntcloud/h5_models/robots/Scripts/"
model = "irb140"
#App.open(SCRIPTdirr + model + ".FCStd")

ground = App.ActiveDocument.getObjectsByLabel("IRB140_6kg_81_BASE_CAD_rev02_STEP1_01")[0]
shaft = App.ActiveDocument.getObjectsByLabel("IRB140_6kg_81_LINK1_CAD_rev02_STEP1_01")[0] 
arm1 = App.ActiveDocument.getObjectsByLabel("IRB140_6kg_81_LINK2_CAD_rev03_STEP1_01")[0]
joint1 = App.ActiveDocument.getObjectsByLabel("link3_01")[0]
arm2 = App.ActiveDocument.getObjectsByLabel("IRB140_6kg_81_LINK4_CAD_rev02_STEP1_01")[0]
head = App.ActiveDocument.getObjectsByLabel("IRB140_6kg_81_LINK5_CAD_rev02_STEP1_01")[0]
tool = App.ActiveDocument.getObjectsByLabel("IRB140_6kg_81_LINK6_CAD_rev02_STEP1_01")[0]

class Animation(object):
    def __init__(self):
        arm1.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,1,0),0), App.Vector(0,0,0))
        shaft.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,1,0),0), App.Vector(0,0,0))
        joint1.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,1,0),0), App.Vector(0,0,0))
        arm2.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,1,0),0), App.Vector(0,0,0))
        head.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,1,0),0), App.Vector(0,0,0))
        tool.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,1,0),0), App.Vector(0,0,0))

    def rotate(self):
    	r1 = random.randint(-180, 180)
    	r2 = random.randint(-45, 45)
    	r3 = random.randint(-45, 45) + r2
    	r4 = random.randint(-45, 45) + r3
    	shaft.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(r1,0,0), App.Vector(0,0,0))
    	arm1.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(r1,r2,0), App.Vector(0,0,0))
    	joint1.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(r1,r3,0), App.Vector(0,0,0))
    	arm2.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(r1,r3,0), App.Vector(0,0,0))
    	head.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(r1,r4,0), App.Vector(0,0,0))
    	tool.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(r1,r4,0), App.Vector(0,0,0))
    	self.reconstraints()

    def rotateMany(self,iterations = 2):
        start = len(os.listdir(MODELdirr + "ply2/"))
        print(start)
    	for i in range (start,iterations+start):
    		self.rotate()
    		self.reconstraints()
    		self.fusion()
    		Mesh.export(App.ActiveDocument.Objects, MODELdirr + "ply2/" + model + "_{}.ply".format(i))
    		#self.exportToPly(i)
    		self.unfuison()
            

    def fusion(self):
		App.activeDocument().addObject("Part::MultiFuse","Fusion")
		App.activeDocument().Fusion.Shapes = [ground,shaft,arm1,arm2,joint1,head,tool,]
		App.ActiveDocument.recompute()      

    def unfuison(self):
        App.getDocument("irb140").removeObject("Fusion")
        
    def reconstraints(self):
    	solveConstraints(App.ActiveDocument)
        
a = Animation()
