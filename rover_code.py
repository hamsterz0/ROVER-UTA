import pygame
import math
from time import sleep
import serial    
pygame.init()

# Initialize the joysticks
pygame.joystick.init()
#arduino = serial.Serial('/dev/ttyUSB0', 57600)
sleep(2)
 
X = 0
Y = 0
# -------- Main Program Loop -----------

def arm():            
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

        vals = camera("a090090") + values()
        if(vals == camera("a090090") + "2"):
            break
 #       arduino.write(vals)
        print(vals)        #Un-comment to see values being inputted
        
        clock.tick(2)      #Change the rate here  



def values():
    joystick = pygame.joystick.Joystick(0)
    nums = ""

    

    #Axis   threshhold = +-.3
    axes = joystick.get_numaxes()       
    temp=""
    for i in range( axes-1 ):
       axis = round(joystick.get_axis( i )*100,2)
       if (axis < 30 and axis > -30): #If axis is in dead zone
           temp+=("0")
       if (axis >= 30):               #Check rover controller if up is negative.
           temp+=("1")
       if (axis <= -30):
           temp+=("-1")
    nums+=temp

    #Buttons
    buttons = joystick.get_numbuttons()
    temp1 = ""
    kill_switch = 0;
    for i in range( buttons ):
        if(joystick.get_button(7) and joystick.get_button(0)):
            return str(2)
            break
        button = joystick.get_button( i )
        temp1+=(str(button))

    nums+=temp1

    #Hats
    hat_s = ["0","0","0","0"]        # left,right,down,up
    hat = joystick.get_hat( 0 )
    if (hat[0] == -1):
        hat_s[0] = "1"
    if (hat[0] == 1):
        hat_s[1] = "1"
    if (hat[1] == -1):
        hat_s[2] = "1"
    if (hat[1] == 1):
        hat_s[3] = "1"
    hats = hat_s[0]+hat_s[1]+hat_s[2]+hat_s[3]
    nums+=hats

    nums+="/"
    return nums

def camera(movement):
    cam = 0
    if(joystick.get_axis(3) > -0.1 and joystick.get_axis(3) < 0.1):
        movement+= "2"
    if(joystick.get_axis(3) < -0.9):
        movement+= "1"
    if(joystick.get_axis(3) > 0.9):
        movement+= "3"

    return movement

while True:
    # EVENT PROCESSING STEP
    pygame.event.get() # User did something
    # Possible joystick actions: JOYAXISMOTION-1
    pygame.event.pump()
    # Get count of joysticks
    joystick = pygame.joystick.Joystick(0)  #taking the joystick
    joystick.init()                 #initializing the joystick
    button_0 = joystick.get_button (0)
    button_7 = joystick.get_button (7)
    button_6 = joystick.get_button (6)        #asking for the buttin
    clock = pygame.time.Clock()
    nums = ""
    
    if button_6:
        break

    if (button_7):
        arm()

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
    movement = "d" + str(J[1]) + str(J[0])

    movement = camera(movement)

    movement+="00000000000000000000/"
    print movement


    sleep(.3)  


    
#    arduino.write(movement)
    
#arduino.close()  
pygame.quit()
