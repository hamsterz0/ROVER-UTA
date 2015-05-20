#include <Servo.h> 


Servo DriveRight;
Servo DriveLeft;

int RposInt = 90;
int LposInt = 90;
char input[] = "000000/"; 
String rawposStr = "000000";
String RposStr = "000";
String LposStr = "000";

void setup()

{
  DriveRight.attach(8);
  DriveLeft.attach(9);
  Serial.begin(57600);

}

void loop()

{
  // Read serial input:1111
  while (Serial.available() > 0) 
  {
    Serial.readBytesUntil('/',input,7);
    rawposStr = String(input);
    
  
    //string splice
    RposStr = rawposStr.substring(0,3);
    LposStr = rawposStr.substring(3,6);
     //integer conversion   
    RposInt = RposStr.toInt();
    LposInt = LposStr.toInt();
    
    //Serial.print(LposInt);
    //Serial.println(RposInt);
    Serial.println(LposStr);
    Serial.print(RposStr);
  }
  
  DriveRight.write(RposInt);
  DriveLeft.write(LposInt);
  delay(150);
  }
