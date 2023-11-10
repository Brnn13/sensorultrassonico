#include <NewPing.h>

#define TRIGGER_PIN 3  // selecionar pin trigger do arduino.
#define ECHO_PIN 6  // selecionar pin echo do arduino.
#define MAX_CM_DISTANCE 10 // distância máxima em cm. capacidade do sensor 400-500cm.

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_CM_DISTANCE);

String status;
float porcentagem;
bool statuscheio;

void setup() {
  Serial.begin(115200); // Taxa do monitor 115200.
}

void loop() {
  delay(1000);                     // tempo em ms (1 s = 1000 ms)
  float distancia = sonar.ping_cm();
  float porcentagem = (1.0 - (distancia/10)) * 100.0;
  if (porcentagem >= 70.00)  {
    statuscheio = false;
  } else {
    statuscheio = true;
  }

  if (statuscheio) {
    status = "vazio"; // Se status é verdadeiro, então statuscheio é "vazio"
  } else {
    status = "cheio"; // Se status é falso, então statuscheio é "cheio"
  }
 
  Serial.print("distancia: ");
  Serial.println(distancia);
  Serial.print("status: ");
  Serial.println(status);
  Serial.print("porcentagem: ");
  Serial.println(porcentagem);
  Serial.print("statuscheio: ");
  Serial.println(statuscheio);
}