# Code Documentation
-> Hello! This markdown file will be where I document how my functions work, their inputs and their uses.

* generate_torus(R1, R2)
  * INPUTS
    * This takes an input of R1 and R2 based on the donut.c article and my own personal notes.
  * This function uses the idea of "Solid of revolution", generating a circle for every iteration of phi and rotates it around the y-axis
  * OUTPUT
    * The function outputs the points for a torus of R2 radius and an inner radius of R1
    * The output is a 2d array with each nested array representing the [x, y, z] coordinates of each point