
######################################################################
# File:  SimulationVectors.py
#
# Decription: Creates lattice using linear combination of 2 basis
#             vectors, and returns 2D and 3D atomic locations
#            
# Author: Stanley Urbanek
#
# Created: 4/20/15
#
# Last updated: 5/28/15
######################################################################

#################
## IMPORT LIST ##
#################

import math
from math import sin
from math import cos
from math import pi
import turtle
from numpy import *

#################################################################
## FUNCTION: Draws a square boundary
##
##   [args]: ttl      - turtle object;
##           (xi, yi) - initial x,y coords of ttl;
##           (dx, dy) - boundary side lengths
##
#################################################################

def drawBound(ttl, xi, yi, dx, dy):
    ttl.penup()
    ttl.goto(xi, yi)
    ttl.pendown()
    ttl.goto(xi + dx, yi)
    ttl.goto(xi + dx, yi + dy)
    ttl.goto(xi, yi + dy)
    ttl.goto(xi, yi)
    ttl.penup()

###########################################################################
## FUNCTION: Creates triangular lattice
##           Draws all possible combinations of atomic locations within bound
##           box, by linearly combining two, 2-D vectors           
##
##   [args]: ttl        - turtle object;
##           (xi, yi)   - initial x,y coords of ttl;
##           (Xb, Yb  ) - x,y bounds of simulation box;
##           (v1x, v1y) - x,y components of vector 1;
##           (v2x, v2y) - x,y components of vector 2;
##           doesRotate - boolean, for "There is a rotation";
##           theta, phi - rotation angles about Y, Z axes, respectively
##           scale      - scaling factor for problem; facilitates visualizations only
###########################################################################

def triangularLattice( ttl, xi, yi, Xb, Yb, v1x, v1y, v2x, v2y, doesRotate, theta, phi, scale):

    # Initialization
    sgn = 1
    nx = 0
    ny = 0
    P0x = xi #Should this be set to 0?
    P0y = yi
    pnewx = xi
    pnewy = yi

    # Within boundary conditions
    while ny * v2y < Yb:
        while nx * v1x < Xb:

            ########## 2 Dim #####################

            # Get new point, (pnewx, pnewy)
            pnewx = P0x + nx * v1x
            pnewy = P0y + nx * v1y

            # DRAW 2 dim point
            ttl.goto(pnewx, pnewy)
            ttl.pendown()
            ttl.dot(1)
            ttl.penup()

            # FUTURE FIX
            print( str(pnewx) + ' ' + str(pnewy))

            ############ 3 Dim #####################
 
            # Calculate 3 dim point
            xf, yf, zf = conv2to3dim(pnewx, pnewy, Xb, Yb, doesRotate, theta, phi, scale)
            
            # DRAW 3 dim point
            # CHANGE: if you want ONLY the nth (1st, 3rd) number drawn
            # Start:

            # If not rotated, only draw 1st point
            if (not doesRotate):
                if nx == 0:
                    ttl.goto(-100 + yf, zf)
                    ttl.dot(1)
                    ttl.penup()

            # Otherwise, draw all points
            else:
                ttl.goto(-100 + yf, zf)
                ttl.dot(1)
                ttl.penup()

            # End indent
            nx += 1

        # Alter variables
        print('\n')
        nx = 0
        P0x = P0x + sgn * v2x
        P0y = P0y + v2y
        sgn = sgn * -1
        ny = ny + 1

    return

####################################################################
## FUNCTION: Creates honeycomb lattice;
##           Draws all combinations of atomic locations within bound
##           box, by linearly combining two, 2-D vectors           
##
##   [args]: ttl        - turtle object;
##           (xi, yi)   - initial x,y coords of ttl;
##           (Xb, Yb  ) - x,y bounds of simulation box;
##           (v1x, v1y) - x,y components of vector 1;
##           (v2x, v2y) - x,y components of vector 2;
##           doesRotate - boolean, for "There is a rotation";
##           theta, phi - rotation angles about Y, Z axis, respectively
##           scale      - scaling factor for problem; facilitates visualizations only
##           trace      - boolean, for "Trace atomic pairs"; facilitates visualizations only
##           infile     - file for saving all atomic locations in
###################################################################

def honeycombLattice(ttl, xi, yi, Xb, Yb, v1x, v1y, v2x, v2y, doesRotate, theta, phi, scale, trace, infile):

    # Initialization
    sgn = 1
    nx = 0
    ny = 0
    P0x = xi #Should this be set to 0?
    P0y = yi
    pnewx = xi
    pnewy = yi

    atomCounter = 0

    # Within boundary conditions
    while ny * v2y <= Yb: #F<=
        while nx * v1x < Xb:

            ########## 2 Dim #####################

            # TRIANGLE TO HONEYCOMB
            
            # TRI code \\:
            # Get new point, (pnewx, pnewy)
            pnewx = P0x + nx * v1x
            pnewy = P0y + nx * v1y
            #pnewy = P0y + ny * v1y

            # Send these TRI code coords, to HONEY fcn
            pnewy1, pnewy2 = getHoneycombYCoordinates ( ttl, pnewy, scale )

            # Print both new coordinates

            # Coord set 1
            # POINT OF CONTENTION: Boundary Conditions

            
            if (Yb - (ny * v2y) >= v2y/2): # >=v2y
                ttl.goto(pnewx, pnewy1)
                ttl.pendown()
                ttl.dot(1)
                ttl.penup()

                # FUTURE FIX (1/2)
                print( str(pnewx) + ' ' + str(pnewy1))
            
            # Coord set 2
            # POINT OF CONTENTION: Boundary Conditions
            # Conditional created, to not include lowermost, extra-boundarial points

            if ny != 0:
                ttl.goto(pnewx, pnewy2)
                ttl.pendown()
                ttl.dot(1)
                ttl.penup()
                
                # FUTURE FIX (2/2)
                print( str(pnewx) + ' ' + str(pnewy2))


            ############ 3 Dim #####################

            
            # Calculate 3 dim point
            # Should only calculate them, if not at boundary points

            # For the pnewy1, upper lattice point in the duo
            # if within normal boundary, confirms to do upper point
            if (Yb - (ny * v2y) >= v2y/2): # >=v2y
                xf1, yf1, zf1, atomCounter = conv2to3dim(pnewx, pnewy1, Xb, Yb, doesRotate, theta, phi, scale, infile, atomCounter)
                

            # For the pnewy2, lower lattice point in the duo
            # if within normal boundary, confirms to do lower point
            if ny != 0:
                xf2, yf2, zf2, atomCounter = conv2to3dim(pnewx, pnewy2, Xb, Yb, doesRotate, theta, phi, scale, infile, atomCounter)


            #xf1, yf1, zf1 = conv2to3dim(pnewx, pnewy1, Xb, Yb, doesRotate, theta, phi, scale, infile)
            #xf2, yf2, zf2 = conv2to3dim(pnewx, pnewy2, Xb, Yb, doesRotate, theta, phi, scale, infile)
            
            # DRAW 3 dim point
            # CHANGE: if you want ONLY the nth (1st, 3rd) number drawn
            # Start:

            # If at upper boundary region, keep it simple, and only draw that pt
            if (Yb - (ny * v2y) >= v2y/2) and (ny == 0): # >=v2y
                ttl.goto(-100 + yf1, zf1)
                ttl.dot(1)
                ttl.penup()

            # Now, if at lower boundary region
            elif (Yb - (ny * v2y) < v2y/2) and (ny != 0):
                ttl.goto(-100 + yf2, zf2)
                ttl.dot(1)
                ttl.penup()
            
            # If not rotated, only draw 1st point
            elif (not doesRotate):
                if nx == 0:
                    ttl.goto(-100 + yf1, zf1)
                    ttl.dot(1)
                    if trace:
                        ttl.pendown()
                    else:
                        ttl.penup()
                    ttl.goto(-100 + yf2, zf2)
                    ttl.dot(1)
                    ttl.penup()

            # Otherwise, draw all points
            else:
                ttl.goto(-100 + yf1, zf1)
                ttl.dot(1)
                if trace:
                    ttl.pendown()
                else:
                    ttl.penup()
                ttl.goto(-100 + yf2, zf2)
                ttl.dot(1)
                ttl.penup()

            # End indent
            nx += 1

        # Alter variables
        print('\n')
        nx = 0
        P0x = P0x + sgn * v2x
        P0y = P0y + v2y
        sgn = sgn * -1
        ny = ny + 1

    return


############################################################################
## FUNCTION: Converts 2-Dim coordinate set into 3-Dim using
##           (x,y) => (x,y,z)
##                 =  (x, r*sin(th), r*(1-cos(th)))
##                     where r = L_y/ 2*pi, th = y_i / r
##
## OPTIONAL: Rotate 3-dim coords by theta, phi
##           Controlled by boolean 'doesRotate'
##
##     NOTE: For visualizations, when rolled into 3D, the 2D object is seen
##           from -x looking towards +x; i.e. it is the LHS y-side that is
##           seen, from edge on, in 3D
##
##   [args]: (x_i, y_i) - initial x,y coordinates
##           (Xb, Yb)   - boundary lengths
##           doesRotate - boolean, for "There is a rotation"
##           theta      - rotation angle about Y-axis
##           phi        - rotation angle about Z-axis
##           scale      - scaling factor, for visualizations
##           infile     - file for saving atomic locations in
##           atomCounter- integer, counts number of atoms assigned a location
############################################################################


def conv2to3dim(x_i, y_i, Xb, Yb, doesRotate, theta, phi, scale, infile, atomCounter):
    
    # Initialization
    r = ( Yb ) / ( 2 * math.pi ) # Radius; should work for cases when y_i != 1
    #print(">>>>>RADIUS: " + str(r))

    # Update
    atomCounter = atomCounter + 1

    # Converting a single point
    x_f = x_i
    y_f = r * math.sin( y_i / r)
    z_f = r * (1 - math.cos ( y_i / r) )

    # If we do NOT have rotation, doesRotate = False
    if (not doesRotate):
        # Print coords, and return them

        print(str(x_f) + ' ' + str(y_f) + ' ' + str(z_f))
        infile.write(str(atomCounter) +' ' +  str(1)+ ' ' +str(0.0) + ' ' + str(x_f) + ' ' + str(y_f) + ' ' + str(z_f))
        infile.write('\n')
        return x_f, y_f, z_f, atomCounter

    # Otherwise, we DO have rotation
    # Send final coordinates to rotate3dim
    else:
        x_f, y_f, z_f = rotate3dim ( x_f, y_f, z_f, theta, phi )

        # FUTURE FIX
        print(str(x_f) + ' ' + str(y_f) + ' ' + str(z_f))
        infile.write(str(atomCounter) +' ' +  str(1) + ' ' +str(0.0) + ' ' + str(x_f) + '   ' + str(y_f) + '   ' + str(z_f))
        infile.write('\n')
        return float(x_f), float(y_f), float(z_f), atomCounter
    

########################################################################
## FUNCTION: Rotates 3-dim coordinate set (x,y,z)  by theta, phi
##
##   [args]: (x_f, y_f, z_f) - finalized, 3-dim coordinates; unrotated
##           theta           - rotation angle about Y axis
##           phi             - rotation angle about Z axis
##
########################################################################
 
def rotate3dim ( x_f, y_f, z_f, theta, phi ):

    # Begin Marder edits
    #theta=.2
    #phi=.4

    #rotate=matrix([[sin(theta)*cos(phi),sin(theta)*sin(phi),0],[-sin(theta)*sin(phi),sin(theta)*cos(phi),0],[0,    0,  cos(theta)]])
    # Rotation matrix about z axis
    #rotate = matrix([[cos(theta) , sin(theta) , 0],[-sin(theta), cos(theta), 0],[0 , 0, 1]])

    #Rotation matrix for R_y * R_z
    rotate = matrix( [ [cos(theta)*cos(phi), cos(theta) * sin(phi), - sin(theta)],[-sin(phi),cos(phi),0],[sin(theta)*cos(phi),sin(theta) * sin(phi), cos (theta) ] ] )
    rotated=rotate*matrix([[x_f],[y_f],[z_f]])

    # Returns rotated 3-dim x,y,z coordinates
    return float(rotated[0]), float(rotated[1]),float(rotated[2])


#########################################################################
## FUNCTION: Gets the 2 replacement, y coordinates, for the honeycomb lattice;
##           Uses points from the triangle lattice, to determine honeycomb
##           point locations (y components only)
##
##   [args]: ttl   - turtle object
##           yi    - initial y position, for triangle lattice
##           scale - scaling factor, for visualization facilitation
##
##########################################################################

def getHoneycombYCoordinates ( ttl, yi , scale) :
    
    # Initialization ~ triangular lattice replacement vectors for honeycomb
    # Note: No Vx components exist
    Vy1 = 1.0 / (2.0*math.sqrt(3)) * scale
    Vy2 = -1.0 / (2.0*math.sqrt(3)) * scale
    
    # Calculate the 2 new locations
    yf1 = yi + Vy1
    yf2 = yi - Vy1

    # Return the 2 new y-positions
    return yf1, yf2

##################################################################
## MAIN FUNCTION
##
##
##################################################################

def main():

    # Turtle initialization
    turtle.setup(1000,1000,0,0)
    turtle.screensize(100,100)
    turtle.speed(0)
    ttl = turtle.Turtle()

    # Scale initialization
    d_carbonBondLength = 1.42 #Angstroms
    scale = math.sqrt(3) * d_carbonBondLength  # Ref. notebook 5/26   
                                               #25 good for visuals


    # Basis vector designation
    v1x = 1*scale #S
    v1y = 0 * scale #S
    v2x = 0.5 * scale #S
    v2y = math.sqrt(3)/2 * scale #S

    # Boundary setting ~ (basis vector) * (scale) * (number of atoms spaced)
    Xb = 1 * scale * 70  # S                 # Yields len = 172.16585 A
    Yb = math.sqrt(3)/2 * scale * 25 # S     # Yields dia = 16.950001 A ~ 1.7 nm
                                             # dia = Yb / pi

    doesRotate = True
    trace = True
    theta = pi/4
    phi = pi/4

    # Because I want to write all atomic locations to a text file
    infile = open("honeycombAtomicPlacement.txt","w")
    
    
    drawBound(ttl, 0, 0, 1*Xb,1*Yb)

    infile.close()
    ttl.penup()
    ttl.goto(-150,-150)
    turtle.done()

main()
