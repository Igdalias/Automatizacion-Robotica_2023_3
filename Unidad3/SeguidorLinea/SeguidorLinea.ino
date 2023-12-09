int matrizDireccion[4][4] = {
  { 0, 0, 0, 0 },
//{ 1, 0, 1, 0 },
  { 0, 1, 0, 1 },
  { 1, 0, 0, 1 },
  { 0, 1, 1, 0 }
};

int matrizVelocidad[4][2] = {
  { 0, 0 },
  //{ 150, 150 },
  { 255, 255 },
  { 255, 255 },
  { 255, 255 }
};


int inputs[] = { 3, 4, 5, 6 };  // in1, in2, in3, in4 --pines digitales
int enables[] = { 8, 9 };       // pines para PWM ... Enables A - Enable B
int i;


int S1 = 12;
int S2 = 13;
void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);

  for (int i = 0; i < 4; i++) {
    pinMode(inputs[i], OUTPUT);
  };

  for (int i = 0; i < 2; i++) {
    pinMode(enables[i], OUTPUT);
  }

  pinMode(S1, INPUT);
  pinMode(S2, INPUT);
}



void loop() {

int v1 = digitalRead(S1);
int v2 = digitalRead(S2);

Serial.print(v1);
Serial.println(v2);

if (v1 == 0 && v2 == 0){
  direccion(1);
}
if(v1 == 1 && v2 == 0){
  direccion(2);
  delay(500);
}
if(v1 == 0 && v2 == 1){
  direccion(3);
  delay(500);
}
if(v1 == 1 && v2 == 1){
  direccion(0);
  
}

//delay(300);

}

void direccion(int estado) {
  for (i = 0; i < 4; i++) {
    digitalWrite(inputs[i], matrizDireccion[estado][i]);
    //Serial.println(inputs[i] + " ");
    //Serial.print(matrizDireccion[estado][i]);
  }
  for (i = 0; i < 2; i++) {
    analogWrite(enables[i], matrizVelocidad[estado][i]);
    //Serial.println(enables[i] + " ");
    //Serial.print(matrizVelocidad[estado][i]);
  }
}