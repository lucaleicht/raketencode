import serial
import time

# Serieller Port über UART
ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)

# Hilfsfunktion zum Senden von DFPlayer-Befehlen
def send_command(cmd, param1=0, param2=0):
    command = [0x7E, 0xFF, 0x06, cmd, 0x00, param1, param2]
    checksum = 0 - sum(command[1:])
    checksum = checksum & 0xFFFF
    command.append((checksum >> 8) & 0xFF)
    command.append(checksum & 0xFF)
    command.append(0xEF)
    ser.write(bytearray(command))
    time.sleep(0.2)

# Beispiel: Lautstärke setzen (0–30)
def set_volume(level):
    level = max(0, min(level, 30))  # Begrenzung
    send_command(0x06, 0x00, level)

# Beispiel: Track 1 abspielen
def play_track(nr):
    send_command(0x03, 0x00, nr)

# Beispiel-Aufruf
if __name__ == "__main__":
    print("Setze Lautstärke auf 25...")
    set_volume(25)

    print("Spiele Track 2...")
    play_track(2)
