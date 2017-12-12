

int ledPin = 2;
int statePin = HIGH;
int knockPin = 0;
byte val = 0;
int THRESHOLD = 100;

void setup(){
  Serial.begin(9600);
  pinMode(ledPin,OUTPUT);
  digitalWrite(ledPin, HIGH);
}

void loop(){
  val=analogRead(knockPin);
  
 if( val >= THRESHOLD){
   statePin = HIGH;
   Serial.print("!");
   digitalWrite(ledPin, statePin);
 }
 delay(100);
 if(Serial.available()){
   statePin = LOW;
   int readByte = Serial.read();
   digitalWrite(ledPin, statePin);
 }

}

//void serialEvent(){
//  statePin = LOW;
//  digitalWrite(ledPin, statePin);
//}
