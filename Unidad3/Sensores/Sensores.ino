int S1 = 12;
int S2 = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(S1, INPUT);
  pinMode(S2, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  int v1 = digitalRead(S1);
  int v2 = digitalRead(S2);
  Serial.print(v1);
  Serial.println(v2);

  delay(600);

}
