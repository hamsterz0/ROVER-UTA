import pygame
from time import sleep
import serial    
pygame.init()

# Initialize the joysticks
pygame.joystick.init()
arduino = serial.Serial('/dev/ttyACM0', 9600)
sleep(2)
 
# -------- Main Program Loop -----------
while True:
    # EVENT PROCESSING STEP
    pygame.event.get() # User did something
    # Possible joystick actions: JOYAXISMOTION-1
    pygame.event.pump()
    # Get count of joysticks
    joystick = pygame.joystick.Joystick(0)  #taking the joystick
    joystick.init()                 #initializing the joystick
    #axis0 = joystick.get_axis(0)
    #axis1 = joystick.get_axis(1)       #asking for the axis
    button = joystick.get_button (1)        #asking for the buttin
    if button == 1:
        break
    elif(joystick.get_axis(0)):
        axis = joystick.get_axis(0)
        a = int(axis*-90) + 90 
        if(len(str(a)) < 3):
            b=str(0)+str(a)+'090'+'/'
            print b         
        else:
            b=str(a)+'090'+'/'
            print b 
    elif(joystick.get_axis(1)):
        axis = joystick.get_axis(1)
        a = int(axis*-90) + 90 
        if(len(str(a)) < 3):
            b=str(0)+str(a)+'090'+'/'
            print b         
        else:
            b=str(a)+'090'+'/'
            print b 
            
    sleep(.3)  
    
    arduino.write(b)
    
arduino.close()  
pygame.quit()
