import pygame
import math
from time import sleep
import serial    
pygame.init()

# Initialize the joysticks
pygame.joystick.init()
arduino = serial.Serial('/dev/ttyACM0', 9600)
sleep(2)
 
X = 0
Y = 0
# -------- Main Program Loop -----------
while True:
    # EVENT PROCESSING STEP
    pygame.event.get() # User did something
    # Possible joystick actions: JOYAXISMOTION-1
    pygame.event.pump()
    # Get count of joysticks
    joystick = pygame.joystick.Joystick(0)  #taking the joystick
    joystick.init()                 #initializing the joystick
    button = joystick.get_button (1)        #asking for the buttin
    if button == 1:
        break
    Y = joystick.get_axis(0)
       
    X = joystick.get_axis(1)
         
    V = (32768-abs(X)) * (Y/32768) + Y
    W = (32768-abs(Y)) * (X/32768) + X
    R = (V+W)/2 
    L = (V-W)/2
    R = int(R*-90) + 90 
    L = int(L*90) + 90
    J = [R, L]
    for i in range(0,2):
        if(J[i] > 180): J[i] = 180
        elif(J[i] < 0): J[i] = 0
    #print str(J)
    for i in range(0,2):
        if(len(str(J[i])) < 3 and len(str(J[i])) >= 2):
            J[i] = "0" + str(J[i])
        elif(len(str(J[i])) < 2):
            J[i] = "00" + str(J[i])
    movement = str(J[1]) + str(J[0]) + "/"
    print movement

    sleep(.3)  
    
    arduino.write(movement)
    
arduino.close()  
pygame.quit()
