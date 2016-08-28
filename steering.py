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
    wheel_in_radius = 18
    marker_width = 10
    degrees = ac.getCarState(0, acsys.CS.Steer)-90
    
    ac.glBegin(1)
    for i in range(0,360,10):
        ac.glBegin(3)
        ac.glColor4f(1.0, 1.0, 1.0, 0.3)
        ac.glVertex2f(wheel_center_x + math.cos(math.radians(i+10))*wheel_out_radius,wheel_center_y + math.sin(math.radians(i+10))*wheel_out_radius)
        ac.glVertex2f(wheel_center_x + math.cos(math.radians(i))*wheel_out_radius,wheel_center_y + math.sin(math.radians(i))*wheel_out_radius)
        ac.glVertex2f(wheel_center_x + math.cos(math.radians(i))*wheel_in_radius,wheel_center_y + math.sin(math.radians(i))*wheel_in_radius)
        ac.glVertex2f(wheel_center_x + math.cos(math.radians(i+10))*wheel_in_radius,wheel_center_y + math.sin(math.radians(i+10))*wheel_in_radius)
        ac.glEnd()
    
    ac.glBegin(3)
    ac.glColor4f(1.0, 1.0, 1.0, 1.0)
    ac.glVertex2f(wheel_center_x + math.cos(math.radians(degrees+marker_width))*wheel_out_radius,wheel_center_y + math.sin(math.radians(degrees+marker_width))*wheel_out_radius)
    ac.glVertex2f(wheel_center_x + math.cos(math.radians(degrees-marker_width))*wheel_out_radius,wheel_center_y + math.sin(math.radians(degrees-marker_width))*wheel_out_radius)
    ac.glVertex2f(wheel_center_x + math.cos(math.radians(degrees-marker_width))*wheel_in_radius,wheel_center_y + math.sin(math.radians(degrees-marker_width))*wheel_in_radius)
    ac.glVertex2f(wheel_center_x + math.cos(math.radians(degrees+marker_width))*wheel_in_radius,wheel_center_y + math.sin(math.radians(degrees+marker_width))*wheel_in_radius)
    ac.glEnd()
    