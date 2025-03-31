# raketencode
Kleines Raketenspielzeug

# GPIO PLAN

|Funktion	|Bauteil	|GPIO-Pin (BCM)	|Bemerkung|
|-|-|-|-|
|Display	|Elegoo 3.5" |GPIO	|Belegt mehrere Pins (Treiberabhängig)	|
|Keypad	|HX543 (4×4)	|GPIO 5, 6, 13, 19, 12, 16, 20, 21	|Kann angepasst werden|
|APA106-LEDs	|Countdown-LEDs	|GPIO 18	|Nur ein Datenpin nötig|
|DFPlayer Mini	|Audio	|GPIO 14 (TX), 15 (RX)	|Seriell über UART0|
|Reset-Knopf	|Reset-Eingabe	|GPIO 23	|Pull-down Widerstand nötig|
|Wiederholen-Knopf	|Ansage wiederholen	|GPIO 24	|Pull-down Widerstand nötig|
|Antennen-LEDs	|Statuslicht rot	|GPIO 25	|Optional blinken lassen|

# APA106 LEDs

VCC -> 5V (Pin2)

GND -> GND (Pin6)

DIN -> GPIO18 (Pin2)

# DFPlayer Mini

   RX → GPIO 14 (über Spannungsteiler!)

   TX → GPIO 15

   VCC → 5V

   GND → GND

   Lautsprecher → direkt an SPK_1 / SPK_2

   MicroSD mit deinen MP3-Dateien einlegen

# Taster 
 Knopf 1 Reset -> GPIO23, GND, Pull-Down
 Knopf 2 (Wiederholen -> GPIO24, GND, Pull-Down

# Pinpad Pinbelegung: 
|Pin	|Funktion	|Raspberry Pi (BCM)|
|--|-------|---|
|R1|Zeile 1|GPIO 5
|R2	|Zeile 2	|GPIO 6|
|R3	|Zeile 3	|GPIO 13|
|R4	|Zeile 4	|GPIO 19|
|C1	|Spalte 1	|GPIO 12|
|C2	|Spalte 2	|GPIO 16|
|C3	|Spalte 3	|GPIO 20|
|C4	|Spalte 4|	GPIO 21|



# Installation:

sudo apt update

sudo apt install python3-pip python3-pygame pyserial git

pip3 install RPi.GPIO pad4pi rpi_ws281x

ggf: pip3 install pad4pi --break-system-packages




