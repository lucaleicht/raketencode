
from pad4pi import rpi_gpio
import RPi.GPIO as GPIO
import time

# GPIO-Pins für die 4x4-Matrix
KEYPAD = [
    ["1","2","3","A"],
    ["4","5","6","B"],
    ["7","8","9","C"],
    ["*","0","#","D"]
]

ROW_PINS = [5, 6, 13, 19]     # Verbunden mit den Zeilen des Keypads
COL_PINS = [12, 16, 20, 21]   # Verbunden mit den Spalten des Keypads

def printKey(key):
    print(f"Taste gedrückt: {key}")

factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

keypad.registerKeyPressHandler(printKey)

print("Keypad-Test läuft. Drücke Tasten (Strg+C zum Beenden)...")
try:
    while True:
        time.sleep(0.2)
except KeyboardInterrupt:
    print("Beendet.")
    GPIO.cleanup()
