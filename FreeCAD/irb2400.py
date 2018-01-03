import FreeCAD as App
from assembly2solver import solveConstraints
import random
import time
import cache_assembly2
import Import
import Mesh
import os

MODELdirr = "/home/trygve/Programming/pyntcloud/h5_models/robots/IRB2400/" #dir to model

model = "irb2400"

ground = App.ActiveDocument.getObjectsByLabel("IRB2400_12kg_155_BASE_CAD_rev03_STEP1_01")[0]
shaft = App.ActiveDocument.getObjectsByLabel("IRB2400_12kg_155_LINK1_CAD_rev03_STEP1_01")[0] 
arm1 = App.ActiveDocument.getObjectsByLabel("IRB2400_12kg_155_LINK2_CAD_rev03_STEP1_01")[0]
joint1 = App.ActiveDocument.getObjectsByLabel("IRB2400_12kg_155_LINK3_CAD_rev03_STEP1_01")[0]
arm2 = App.ActiveDocument.getObjectsByLabel("link4_01")[0]
head = App.ActiveDocument.getObjectsByLabel("IRB2400_12kg_155_LINK5_CAD_rev04_STEP1_01")[0]
tool = App.ActiveDocument.getObjectsByLabel("IRB2400_12kg_155_LINK6_CAD_rev04_STEP1_01")[0]

class Animation(object):
    def __init__(self):
        arm1.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,1,0),0), App.Vector(0,0,0))
        shaft.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,1,0),0), App.Vector(0,0,0))
        joint1.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,1,0),0), App.Vector(0,0,0))
        arm2.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,1,0),0), App.Vector(0,0,0))
        head.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,1,0),0), App.Vector(0,0,0))
        tool.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,1,0),0), App.Vector(0,0,0))

    def rotate(self):
    	r1 = random.randint(-180, 180) #Degrees of rotation, base
    	r2 = random.randint(-45, 45)   #Degrees of rotation, arm1
    	r3 = random.randint(-45, 45) + r2 #Degrees of rotation arm2
    	r4 = random.randint(-45, 45) + r3 #Degree of rotation tool
    	shaft.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(r1,0,0), App.Vector(0,0,0))
    	arm1.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(r1,r2,0), App.Vector(0,0,0))
    	joint1.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(r1,r3,0), App.Vector(0,0,0))
    	arm2.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(r1,r3,0), App.Vector(0,0,0))
    	head.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(r1,r4,0), App.Vector(0,0,0))
    	tool.Placement=App.Placement(App.Vector(0,0,0), App.Rotation(r1,r4,0), App.Vector(0,0,0))
    	self.reconstraints()

    def rotateMany(self,iterations = 2): #Rotate and generate a number of models
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
		App.ActiveDocument.recompute()

    def unfuison(self):
        App.getDocument(model).removeObject("Fusion")
        
    def reconstraints(self):
    	solveConstraints(App.ActiveDocument)

a = Animation()
