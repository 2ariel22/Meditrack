#include <SPI.h>
#include <MFRC522.h>
#include <BluetoothSerial.h>

// Definiciones de pines para el primer lector RFID
#define RST_PIN1 27  
#define SS_PIN1  5   

// Definiciones de pines para el segundo lector RFID
#define RST_PIN2 16  
#define SS_PIN2  17  

// Definiciones de pines para el tercer lector RFID
#define RST_PIN3 2   
#define SS_PIN3  4   

// Creación de instancias del objeto MFRC522 para los tres lectores
MFRC522 mfrc522_1(SS_PIN1, RST_PIN1);  
MFRC522 mfrc522_2(SS_PIN2, RST_PIN2);  
MFRC522 mfrc522_3(SS_PIN3, RST_PIN3);

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);    // Iniciar la comunicación serie
  SerialBT.begin("ESP32"); // Iniciar el Bluetooth
  // Iniciar SPI con configuración de pines para SCK, MISO, MOSI
  delay(200);
  SPI.begin(18, 19, 23);   
  mfrc522_1.PCD_Init();     // Iniciar el primer MFRC522
  mfrc522_2.PCD_Init();     // Iniciar el segundo MFRC522
  mfrc522_3.PCD_Init();     // Iniciar el tercer MFRC522
  SerialBT.println("hola");
}

void loop() {
  // Revisar todos los lectores para ver si hay nuevas tarjetas presentes
  checkRFID(mfrc522_1, "1");
  checkRFID(mfrc522_2, "2");
  checkRFID(mfrc522_3, "3");
}
void checkRFID(MFRC522& mfrc522, String readerId) {
  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    String message = readerId + " ";
    for (byte i = 0; i < mfrc522.uid.size; i++) {
      message += (mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
      message += String(mfrc522.uid.uidByte[i], HEX);
    }
    Serial.println(message);

    // Convertir la cadena a bytes
    uint8_t buffer[message.length()];
    for (int i = 0; i < message.length(); i++) {
      buffer[i] = message.charAt(i);
    }

    // Envío por Bluetooth
    SerialBT.write(buffer, message.length());
    
    mfrc522.PICC_HaltA(); // Detener la lectura de tarjetas
  }
}
