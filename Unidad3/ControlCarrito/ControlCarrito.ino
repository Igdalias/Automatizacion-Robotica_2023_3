  #include <SoftwareSerial.h>

  SoftwareSerial bt(10, 11); // RX TX

  int matrizDireccion[5][4] = {
    {0, 0, 0, 0},
    {1, 0, 1, 0},
    {0, 1, 0, 1},
    {1, 0, 0, 1},
    {0, 1, 1, 0}
  };

  int matrizVelocidad[5][2] = {
    {0, 0},
    {255, 255},
    {255, 255},
    {255, 175},
    {175, 255}
  };

  int inputs[] = {3, 4, 5, 6}; // in1, in2, in3, in4 --pines digitales
  int enables[] = {8, 9}; // pines para PWM ... Enables A - Enable B
  int i;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  bt.begin(9600);
  Serial.setTimeout(100);

  for(int i = 0; i < 4; i++){
    pinMode(inputs[i], OUTPUT);
  };

  for(int i = 0; i < 2; i++){
    pinMode(enables[i], OUTPUT);
  }



}


String comando; // variable para almacenar los comandos;

void loop() {

if(bt.available() > 0){
  //if(Serial.available() > 0){
    
    String cadena = bt.readString();
    int estado = cadena.toInt();
    //int estado = Serial.readString().toInt();
    direccion(estado);
    bt.println(estado);
  }
  
}

}

void direccion(int estado){
  for(i = 0; i < 4; i++){
    digitalWrite(inputs[i], matrizDireccion[estado][i]);
    //Serial.println(inputs[i] + " "); 
    //Serial.print(matrizDireccion[estado][i]);
    bt.println(inputs[i] + " "); 
    bt.print(matrizDireccion[estado][i]);
  }
  for(i = 0; i < 2; i++){
    analogWrite(enables[i], matrizVelocidad[estado][i]);
    //Serial.println(enables[i] + " "); 
    //Serial.print(matrizVelocidad[estado][i]);
    bt.println(enables[i] + " "); 
    bt.print(matrizVelocidad[estado][i]);
  }
}