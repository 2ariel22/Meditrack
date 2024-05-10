import serial
import keyboard

arduino = serial.Serial('COM4')

while True:
    if arduino.in_waiting > 0:
        rawString = arduino.readline().decode()
        print(rawString)
    
    if keyboard.is_pressed('q'):
        print("Presionaste 'q'. Saliendo del bucle...")
        break

print("saliste")
arduino.close()
