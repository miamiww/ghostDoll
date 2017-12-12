
#include <Servo.h>

Servo panelServo;

int pos = 0;

int ledPin = 11;
int servoPin = 10;
int statePin = LOW;
int knockSensor = 0 ;
byte val = 0;
int THRESHOLD = 100;

void setup(){
  Serial.begin(9600);
  panelServo.attach(servoPin);
}

void loop(){
  val = analogRead(knockSensor);
  
  if( val >= THRESHOLD){
    pos = 90;
    statePin = HIGH;
    digitalWrite(ledPin, statePin);
    Serial.print("!");
    panelServo.write(pos);
    delay(45);
  }
  
  delay(100);
  if(Serial.available()){
    int readByte = Serial.read();
    pos = 120;
    panelServo.write(pos);
    delay(45);
    statePin = LOW;
    digitalWrite(ledPin, statePin);
  } 
}
