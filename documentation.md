# Code Documentation
-> Hello! This markdown file will be where I document how my functions work, their inputs and their uses.

* generate_torus(R1, R2)
  * INPUTS
    * This takes an input of R1 and R2 based on the donut.c article and my own personal notes.
  * This function uses the idea of "Solid of revolution", generating a circle for every iteration of phi and rotates it around the y-axis
  * OUTPUT
    * The function outputs the points for a torus of R2 radius and an inner radius of R1
    * The output is a 2d array with each nested array representing the [x, y, z, θ, ϕ] coordinates of each point
    * θ & ϕ are added for calculating Luminance later on

* rotate_point(point, angleA, angleB):
  * INPUTS
    * point is a list of 3 coordinates [x, y, z]
    * angleA is the rotation along the x-axis (refer to notes.md)
    * angleB is the rotation along the z-axis (refer to notes.md)
  * This function returns the new location of the point after being rotated by angleA and angleB
  * The formula is derived by multiplying (x, y, z) with the x and z generic rotation matrices
  * OUTPUT
    * The output is a list of the same size and format of the input point
    * [x, y, z, Luminance]
    * The Luminance value for each point is updated after each rotation
* rotate_points(points, angleA, angleB):
  * This is the same as rotate_point, except it takes a list of points instead of a single point and outputs a list of points
* Post processing of luminance
  * After calculating the luminance, before rendering we normalize the value so instead of ranging from -1.5 to 1.5, it instead ranges from 0 - 255.