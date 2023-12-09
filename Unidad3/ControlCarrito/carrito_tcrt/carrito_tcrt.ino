int matrizDireccion[4][4] = {
  { 1, 0, 1, 0 },
  { 1, 0, 0, 1 },
  { 0, 1, 1, 0 },
  { 0, 0, 0, 0 }
};

int matrizVelocidad[4][2] = {
  { 120, 120 },
  //{ 120, 120 },
  //{ 120, 120 },
  { 90, 180 },
  { 180, 90 },
  { 0, 0 }
};

String matrizEstados[4] = {
  { "00" },
  { "01" },
  //{"0100"},
  //{"0010"},
  { "10" },
  { "11" }
};

int inputs[4] = { 2, 4, 7, 8 };
int enables[2] = { 3, 6 };  // pines PWM...
int tcrt[2] = { 12, 13 };
String cadena = "";
int ex = 0;
long tiempo = 0;

void SetDireccion(int estado) {
  for (int i = 0; i < 4; i++) {
    digitalWrite(inputs[i], matrizDireccion[estado][i]);
  }
  for (int i = 0; i < 2; i++) {
    analogWrite(enables[i], matrizVelocidad[estado][i]);
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  for (int i = 0; i < 4; i++) {
    pinMode(inputs[i], OUTPUT);
  }
  for (int i = 0; i < 2; i++) {
    pinMode(enables[i], OUTPUT);
  }
  for (int i = 0; i < 2; i++) {
    pinMode(tcrt[i], INPUT);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  /*if (ex == 0) {
    SetDireccion(2);
    if (cadena == "0001") {
      long tiempoIN = millis();
      SetDireccion(2);
      if (cadena == "1000") {
        SetDireccion(4);
        long tiempoOUT = millis();
        tiempo = (tiempoOUT - tiempoIN) / 2;
      }
      SetDireccion(2);
      delay(tiempo);
      SetDireccion(5);
      ex = 1;
    }


  }*/

  for (int i = 0; i < 2; i++) {
    int v = digitalRead(tcrt[i]);
    cadena = cadena + String(v);
  }
  Serial.println(cadena);

  for (int i = 0; i < 5; i++) {
    if (cadena == matrizEstados[i]) {
      if (i == 1 || i == 2) {
        SetDireccion(4);
        SetDireccion(i);
        delay(500);
      } else {
        SetDireccion(i);
      }
    }
  }

  cadena = "";
}
