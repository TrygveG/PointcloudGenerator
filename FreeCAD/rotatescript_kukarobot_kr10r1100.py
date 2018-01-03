import FreeCAD as App
from assembly2solver import solveConstraints
import random
import time
import cache_assembly2
import Import
import Mesh

App.open("C:\Users\Mattias\Desktop\CAD\Kuka_robot\kuka_robot.FCStd")

ground = App.ActiveDocument.getObjectsByLabel("base")[0]
shaft = App.ActiveDocument.getObjectsByLabel("shaft")[0] 
arm1 = App.ActiveDocument.getObjectsByLabel("arm1")[0]
joint1 = App.ActiveDocument.getObjectsByLabel("joint")[0]
arm2 = App.ActiveDocument.getObjectsByLabel("arm2")[0]
head = App.ActiveDocument.getObjectsByLabel("head")[0]
tool = App.ActiveDocument.getObjectsByLabel("tool")[0]

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

    def rotateMany(self):
    	for i in range (0,3):
    		self.rotate()
    		self.reconstraints()
    		self.fusion()
    		Mesh.export(App.ActiveDocument.Objects, "C:\Users\Mattias\Desktop\CAD\Kuka_robot\Meshes\kuka_robot_%s" % i)
    		#self.exportToPly()
    		self.unfuison()
            

    def fusion(self):
		App.activeDocument().addObject("Part::MultiFuse","Fusion")
		App.activeDocument().Fusion.Shapes = [ground,shaft,arm1,arm2,joint1,head,tool,]
		Gui.ActiveDocument.Fusion.ShapeColor=Gui.ActiveDocument.IRB140_6kg_81_BASE_CAD_rev02_STEP1_01.ShapeColor
		Gui.ActiveDocument.Fusion.DisplayMode=Gui.ActiveDocument.IRB140_6kg_81_BASE_CAD_rev02_STEP1_01.DisplayMode
		App.ActiveDocument.recompute()      

    def unfuison(self):
        App.getDocument("irb140TEST").removeObject("Fusion")
        
    def reconstraints(self):
    	solveConstraints(App.ActiveDocument)
        
    #def exportToPly(number):
    #	Mesh.export(App.ActiveDocument.Objects, "C:\Users\Mattias\Desktop\CAD\IRB2400_12kg-155_IRC5_rev04_STEP_j\Meshes\TEST.ply")


a = Animation()