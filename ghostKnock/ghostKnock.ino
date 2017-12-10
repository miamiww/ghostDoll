
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
    Serial.print("!");
  }
  delay(100);
  if(Serial.available()){
    for(pos = 0; pos < 180; pos += 1){
      panelServo.write(pos);
      delay(15);
    }
    statePin = HIGH;
    digitalWrite(ledPin, statePin);
  } else{
    for(pos = 180; pos >= 1; pos-=1){
      panelServo.write(pos);
      delay(15);
    }
  }
}
