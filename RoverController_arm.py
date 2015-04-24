"""
Output is:
4 Axis values of -1, 0, or 1
X Button values of 0 or 1
Order of button output is:
Right 4 buttons, .... ,4 directional buttons

The mode button switches the directional buttons and left analog stick output.
It does not actually register as a button.
Make sure the remote is switched to D on the back.
"""

import pygame           
import serial
from time import sleep

arduino = serial.Serial('/dev/ttyACM0',57600)
sleep(2)

def main():            
    pygame.init()
    clock = pygame.time.Clock()
    pygame.joystick.init()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True

        vals = values()
        arduino.write(vals)
        print(vals)        #Un-comment to see values being inputted
        
        clock.tick(2)      #Change the rate here
    pygame.quit()    

def values():
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    nums = ""
    
    #Axis   threshhold = +-.3
    axes = joystick.get_numaxes()       
    temp=""
    for i in range( axes ):
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
    for i in range( buttons ):
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

main()
