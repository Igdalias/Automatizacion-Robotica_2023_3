#include <SoftwareSerial.h>

SoftwareSerial bt(10, 11); // RX TX

// BT   ARDUINO
// 5V  -  5V
// GND    GND
// TX     RX(10)
// RX     TX(11)

void setup() {
  
  Serial.begin(38400); // Velocidad de configuracion
  bt.begin(38400);

}

void loop() {
  
  if(Serial.available()){
    bt.write(Serial.read());
  }

  if(bt.available()){
    Serial.write(bt.read());
  }

}
