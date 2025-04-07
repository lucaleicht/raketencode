#test DFPlayer

import serial
import time

# Öffne serielle Verbindung über ttyS0 (Mini-UART)
ser = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

# Befehl: MP3-Track Nr. 1 abspielen
def play_track_1():
    # DFPlayer Kommandoformat: 10 Bytes
    # Beispiel: Play track 1 = 0x7E 0xFF 0x06 0x03 0x00 0x00 0x01 checksum_H checksum_L 0xEF
    command = [0x7E, 0xFF, 0x06, 0x03, 0x00, 0x00, 0x01]
    checksum = 0 - sum(command[1:])  # Nur Bytes 1 bis 6
    checksum = checksum & 0xFFFF     # 16-bit checksum
    command.append((checksum >> 8) & 0xFF)  # High byte
    command.append(checksum & 0xFF)        # Low byte
    command.append(0xEF)
    ser.write(bytearray(command))

print("Starte Wiedergabe von Track 1...")
play_track_1()
