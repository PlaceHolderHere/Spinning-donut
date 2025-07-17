# Terms
* Framebuffer - a bitmap that contains all the data for the pixels to be rendered on screen
* Z-Buffer - data buffer for storing depth information for 3d objects
- helps to prevent draw points that are behind another point
* Z' - distance from eye to screen
- renamed to K1
* (x', y') - corresponding 2d position of 3d point
* R1 - radius of inner circle
* R2 - radius of donut/torus
* θ - Theta represents the current angle used to drawing the 2d circle
* ϕ - Phi represents the angle of rotation along the Y-Axis
* A - A represents the angle of rotation along the X-axis
* B - B represents the angle of rotation along the Z-axis

# Notes
-basically use different ascii characters ('.,-~:;=!*#$@') to represent different levels of brightness
-relative proportions are maintained 
* x' = K1*x/z
* y' = K1*y/z
# Determining value of K1
-for a 100x100 screen, to see an object 10 units wide & 5 units back, K1 should be chosen so that the point x=10, z=5 is on screen with x' < 50; 10*K1 / 5 < 50 or K1 < 25
* z^-1 = 0 is infinite depth

# Drawing the Circle
* (x,y,z)=(R2​,0,0)+(R1​cosθ,R1​sinθ,0)
- This is the formula for drawing a circle with a radius of R1 units and x is shifted R2 units away
- θ goes from 0 to 2π to make a full circle

# Rotation Matrices
- Each rotation matrix takes in a point as an input and rotates it around a certain axis
- For instance, if we rotate our point around the x-axis, our value for x remains constant while we rotate the y and z coordinates based on Phi
