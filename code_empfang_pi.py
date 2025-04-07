
import serial

# Pfad zum seriellen Gerät (ggf. mit 'ls /dev/ttyACM*' prüfen)
SERIAL_PORT = "/dev/ttyACM0"
BAUD_RATE = 9600

print(f"Öffne {SERIAL_PORT} mit {BAUD_RATE} Baud...")

try:
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
        print("Bereit. Warte auf Eingaben...")
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line:
                print(f"Empfangen: {line}")
except serial.SerialException as e:
    print(f"Fehler beim Öffnen der seriellen Verbindung: {e}")
except KeyboardInterrupt:
    print("Beendet.")
