# PointcloudGenerator
The following program was written by Trygve Gröndahl, Mattias Rahm and Mattias Landgren during a course at Chalmers University of Technology during the fall 2017.

## Introduction
The task was to classify objects from a point cloud of a factory environment. In order to do this, CAD models of robots were assembled, and using freeCAD and the rotate script, a range of different orientations of the robots were extracted. From the generated ply files, Pyntcloud can create h5 files containing point clouds. The point clouds were used to train a pointnet network to classify the robots.

This project adds the translation between the different programs and filetypes. Reading the documentation of the programs is needed in order to get a working program

## Installation
To implement this project yourself you will need some software, 
[FreeCAD](https://www.freecadweb.org/)
[PyntCloud](https://pyntcloud.readthedocs.io/en/latest/index.html)
[PointNet](https://github.com/charlesq34/pointnet)

## Usage
Here are some short descriptions on how to use the different programs.

### FreeCAD
The rotation was done because a robot in a factory can be in any position, and relevant training data was required. Copy paste the rotation scripts into the python console. To generate new models, assemble the models and use the name of the parts to rotate.

### PyntCloud
Using their environment the Visualize script generates plots of the models and output and can cluster points from a cloud and generate separate ply files from them. These can be classified using a trained PointNet. The Generator script can be used to generate h5 files from ply files.

### PointNet
When h5 files containing models and labels are generated, a PointNet can be trained. In order to use it, the number of models needs to be replaced in 'train.py', 'evalute.py' and in the neural net in 'pointnet_cls.py'. Which h5 file that is used is changed in 'train_files.txt' and 'test_files.txt'.

## Future work
The results were promissing for own models, but in order to classify a real-life point cloud, a better clustering algorithm is needed to extract a single robot. New robot CAD models and real-life training data is important for further improvement and verification that it works for robots with cables and other details that is not in the CAD models.
