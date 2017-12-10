
int ledPin = 11;
int statePin = LOW;
int knockSensor = 0 ;
byte val = 0;
int THRESHOLD = 100;

void setup(){
  Serial.begin(9600);
}

void loop(){
  val = analogRead(knockSensor);
  if( val >= THRESHOLD){
    Serial.print("!");
  }
  delay(100);
  if(Serial.available()){
    statePin = !statePin;
    digitalWrite(ledPin, statePin);
  }
}
