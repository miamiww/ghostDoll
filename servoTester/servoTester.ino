#include <Servo.h>
Servo panelServo;

int pos = 140;
int ledPin = 2;
int servoPin = 10;
int statePin = HIGH;
int knockPin = 0;
byte val = 0;
int THRESHOLD = 80;

void setup(){
  Serial.begin(9600);
  pinMode(ledPin,OUTPUT);
  digitalWrite(ledPin, HIGH);
  panelServo.attach(servoPin);
  panelServo.write(pos);
}

void loop(){
  val=analogRead(knockPin);
  
 if( val >= THRESHOLD){
   pos = 10;
   panelServo.write(pos);
   delay(30);
   statePin = HIGH;
   Serial.print("!");
   digitalWrite(ledPin, statePin);
 }
 delay(100);
 if(Serial.available()){
   pos = 140;
   panelServo.write(pos);
   delay(30);
   statePin = LOW;
   int readByte = Serial.read();
   digitalWrite(ledPin, statePin);
   
 }

}

//void serialEvent(){
//  statePin = LOW;
//  digitalWrite(ledPin, statePin);
//}
