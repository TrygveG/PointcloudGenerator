import FreeCAD as App
from assembly2solver import solveConstraints
import random
import time
import cache_assembly2
import Import
import Mesh
import os

MODELdirr = "/home/trygve/Programming/pyntcloud/h5_models/robots/r30L16/"

model = "r30l16"

ground = App.ActiveDocument.getObjectsByLabel("base_step1_01")[0]
shaft = App.ActiveDocument.getObjectsByLabel("shaft_step1_01")[0] 
arm1 = App.ActiveDocument.getObjectsByLabel("arm1_step1_01")[0]
joint1 = App.ActiveDocument.getObjectsByLabel("joint_step1_01")[0]
arm2 = App.ActiveDocument.getObjectsByLabel("arm2_step1_01")[0]
head = App.ActiveDocument.getObjectsByLabel("head_step1_01")[0]
tool = App.ActiveDocument.getObjectsByLabel("tool_step1_01")[0]

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
    		self.fusion()
    		Mesh.export(App.ActiveDocument.Objects, MODELdirr + "ply2/" + model + "_{}.ply".format(i))
    		self.unfuison()
            
    def fusion(self):
		App.activeDocument().addObject("Part::MultiFuse","Fusion")
		App.activeDocument().Fusion.Shapes = [ground,shaft,arm1,arm2,joint1,head,tool,]
		#App.ActiveDocument.recompute()      

    def unfuison(self):
        App.getDocument(model).removeObject("Fusion")
        
    def reconstraints(self):
    	solveConstraints(App.ActiveDocument)

a = Animation()
