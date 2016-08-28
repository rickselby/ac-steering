import sys
import ac
import acsys
import math

appWindow=0

def acMain(ac_version):
    global appWindow
    appWindow = ac.newApp("Steering Input")
    ac.setSize(appWindow, 60, 100)
    ac.setTitle(appWindow, "")
    ac.drawBorder(appWindow, 0)
    ac.setIconPosition(appWindow, 0, -10000)
    ac.setBackgroundOpacity(appWindow, 0)
    ac.addRenderCallback(appWindow, drawWheel)
    return "Steering Input"

def drawWheel(deltaT):
    global appWindow
    ac.setBackgroundOpacity(appWindow, 0)
    
    wheel_center_x = 30
    wheel_center_y = 70
    wheel_out_radius = 25
    degrees = ac.getCarState(0, acsys.CS.Steer)-90
   
    circleWheel(wheel_center_x, wheel_center_y, wheel_out_radius, degrees)

def circleWheel(center_x, center_y, out_radius, degrees):
    in_radius = out_radius * 0.75
    marker_width = 10
    ac.glColor4f(1.0, 1.0, 1.0, 0.3)
    for i in range(0, 360, 10):
        drawWheelPart(center_x, center_y, out_radius, in_radius, i, i+10)

    ac.glColor4f(1.0, 1.0, 1.0, 1.0)
    for i in range(-marker_width, marker_width, 10):
        drawWheelPart(center_x, center_y, out_radius, in_radius, degrees+i, degrees+i+10)
        
def simpleWheel(center_x, center_y, out_radius, degrees):
    in_radius = out_radius * 0.75
    ac.glColor4f(1.0, 1.0, 1.0, 0.3)
    for i in range(0, 360, 10):
        drawWheelPart(center_x, center_y, out_radius, in_radius, i, i+10)
        
    ac.glBegin(3)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees+80))*in_radius,  center_y + math.sin(math.radians(degrees+80))*in_radius)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees-80))*in_radius,  center_y + math.sin(math.radians(degrees-80))*in_radius)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees-90))*in_radius,  center_y + math.sin(math.radians(degrees-90))*in_radius)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees+90))*in_radius,  center_y + math.sin(math.radians(degrees+90))*in_radius)
    ac.glEnd()
    ac.glBegin(3)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees+90))*in_radius,  center_y + math.sin(math.radians(degrees+90))*in_radius)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees-90))*in_radius,  center_y + math.sin(math.radians(degrees-90))*in_radius)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees-100))*in_radius,  center_y + math.sin(math.radians(degrees-100))*in_radius)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees+100))*in_radius,  center_y + math.sin(math.radians(degrees+100))*in_radius)
    ac.glEnd()

    inner1 = math.sin(math.radians(10))*in_radius 
    inner = math.sqrt(inner1 * inner1 * 2)
    ac.glBegin(3)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees+135))*inner,  center_y + math.sin(math.radians(degrees+135))*inner)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees+180))*inner1,  center_y + math.sin(math.radians(degrees+180))*inner1)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees-180))*in_radius,  center_y + math.sin(math.radians(degrees-180))*in_radius)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees+170))*in_radius,  center_y + math.sin(math.radians(degrees+170))*in_radius)
    ac.glEnd()
    ac.glBegin(3)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees+180))*inner1,  center_y + math.sin(math.radians(degrees+180))*inner1)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees-135))*inner,  center_y + math.sin(math.radians(degrees-135))*inner)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees-170))*in_radius,  center_y + math.sin(math.radians(degrees-170))*in_radius)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees+180))*in_radius,  center_y + math.sin(math.radians(degrees+180))*in_radius)
    ac.glEnd()

def drawWheelPart(center_x, center_y, out_radius, in_radius, degrees_start, degrees_end):
    ac.glBegin(3)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees_end))*out_radius,   center_y + math.sin(math.radians(degrees_end))*out_radius)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees_start))*out_radius, center_y + math.sin(math.radians(degrees_start))*out_radius)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees_start))*in_radius,  center_y + math.sin(math.radians(degrees_start))*in_radius)
    ac.glVertex2f(center_x + math.cos(math.radians(degrees_end))*in_radius,    center_y + math.sin(math.radians(degrees_end))*in_radius)
    ac.glEnd()
