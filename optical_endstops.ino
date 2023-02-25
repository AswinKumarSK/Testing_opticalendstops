// define the input pin for the optical endstop
const int endstopPin = 2;

void setup() {
  // set the endstop pin as an input
  pinMode(endstopPin, INPUT);
  
  // initialize the serial communication
  Serial.begin(9600);
}

void loop() {
  // read the state of the endstop
  int endstopState = digitalRead(endstopPin);

  // print the endstop state to the serial monitor
  Serial.println(endstopState);

  // wait for a short period of time
  delay(100);
}
