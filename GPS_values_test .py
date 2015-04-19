import serial
from time import sleep

arduino = serial.Serial('/dev/ttyUSB0', 57600)
sleep(2)

while(1):
	data = arduino.readline();
	print data;

arduino.close();