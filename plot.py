#!/usr/bin/env python
import vtk

#colors = vtk.vtkNamedColors()

    # Create the geometry of a point (the coordinate)
points = vtk.vtkPoints()

topologia=[[178, 95,0], [161, 112,0], [150, 145,0], [150, 172,0], [161, 195,0], [186, 218,0], [210, 232,0], [233, 239,0], [255, 250,0], [279, 267,0], [289, 291,0], [291, 316,0], [283, 332,0], [272, 346,0], [258, 361,0], [238, 381,0], [216,
396,0], [198, 412,0], [178, 435,0], [168, 448,0], [189, 476,0], [222, 488,0], [247, 498,0], [279, 509,0], [306, 513,0], [329, 514,0], [354, 519,0], [377, 510,0], [399, 502,0], [410, 477,0], [415, 457,0], [421, 428,0], [428, 406,0],
[448, 391,0], [471, 377,0], [487, 356,0], [497, 314,0], [476, 286,0], [461, 302,0], [439, 326,0], [431, 330,0], [424, 312,0], [427, 292,0], [435, 267,0], [448, 242,0], [444, 209,0], [439, 193,0], [429, 173,0], [410, 151,0], [387,
140,0], [360, 145,0], [340, 127,0], [344, 107,0], [357, 86,0], [351, 73,0], [325, 69,0], [311, 80,0], [300, 107,0], [282, 99,0], [274, 77,0], [261, 61,0], [246, 57,0], [230, 77,0], [231, 102,0], [220, 131,0]]


    # Create the topology of the point (a vertex)
vertices = vtk.vtkCellArray()

for i in range(len(topologia)):
    pid =points.InsertNextPoint(topologia[i])
    vertices.InsertNextCell(1)
    vertices.InsertCellPoint(pid)
    # We need an an array of point id's for InsertNextCell.

point = vtk.vtkPolyData()

    # Set the points and vertices we created as the geometry and topology of the polydata
point.SetPoints(points)
point.SetVerts(vertices)

    # Visualize
mapper = vtk.vtkPolyDataMapper()
mapper.SetInput(point)

actor = vtk.vtkActor()
actor.SetMapper(mapper)
#actor.GetProperty().SetColor(colors.GetColor3d("Tomato"))
actor.GetProperty().SetPointSize(3)

renderer = vtk.vtkRenderer()
renderWindow = vtk.vtkRenderWindow()
renderWindow.SetWindowName("Point")
renderWindow.AddRenderer(renderer)
renderWindowInteractor = vtk.vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)

renderer.AddActor(actor)
#renderer.SetBackground(colors.GetColor3d("DarkOliveGreen"))

renderWindow.Render()
renderWindowInteractor.Start()
