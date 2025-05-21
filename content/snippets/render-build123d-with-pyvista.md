+++
date = '2025-05-19T19:29:10-04:00'
draft = false
title = 'Render build123d with pyvista'
tags = ['python', 'build123d', 'pyvista', 'render']
+++
Use PyVista to quickly visualize your build123d models

<!--more-->

### build123d

[build123d](https://github.com/gumyr/build123d) is a "python-based, parametric,
boundary representation (BREP) modeling framework for 2D and 3D CAD."  If you
like writing your CAD models as code (ala OpenSCAD) and you want to do it in
Python, it's a strong contender.

A minimal example, generating a simple cylinder:

```python
import build123d


cylinder = build123d.Cylinder(radius=10, height=20)
```

build123d includes functions for exporting to various formats, including stl.

### PyVista

[PyVista](https://github.com/pyvista/pyvista) gives you "3D plotting and mesh analysis through a streamlined
interface for the Visualization Toolkit (VTK)".  It's useful for a lot of
things, but for the sake of this snippet, know that it has built-in methods to
render meshes.

### Putting them together

Using build123d's vtk_tools, you can convert your build123d models to pyvista
meshes easily.

```python
import build123d
import build123d.vtk_tools
import pyvista as pv


cylinder = build123d.Cylinder(radius=10, height=20)

poly_data = build123d.vtk_tools.to_vtk_poly_data(cylinder)
pv_mesh = pv.wrap(poly_data)
pv_mesh.plot()
```

There are other tools to visualize build123d projects, but this is the simplest
way to get a quick look I've found.
