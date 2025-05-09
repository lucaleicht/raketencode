# main.py
"""
Orchestrierung der Raketenmission:
- importiere Module: mission_data, keypad_handler, audio_player, display_manager
- Steuerungsschleife über alle Stationen
- Ablauf: Task -> FlyTo -> CodePrompt -> Launch -> Reise -> Ankommen -> nächste Station
"""

from mission_data import stations
from keypad_handler import get_code
from audio_player import set_volume, play_track
from display_manager import show_message, show_launch_animation

# Setze Standard-Lautstärke
set_volume(25)

# Hauptschleife über alle Stationen
for idx, station in enumerate(stations):
    name = station['name']

    # 1. Begrüßung oder Start
    if station.get('track_welcome'):
        show_message(f"Begrüßung: {name}", 2)
        play_track(station['track_welcome'])

    # 2. Aufgabenansage
    if station.get('track_task'):
        show_message("Aufgabe", 3)
        play_track(station['track_task'])

    # 3. Zielankündigung
    if station.get('track_fly_to'):
        play_track(station['track_fly_to'])
        show_message("Zielankündigung", 2)

    # 4. Codeeingabe
    if station.get('track_code_prompt'):
        play_track(station['track_code_prompt'])
        code = get_code()
        # Warten auf korrekten Code
        while code != station['code']:
            show_message("Falscher Code, bitte erneut", 2)
            code = get_code()
        # Code korrekt
        play_track(20)  # allgemeine Bestätigung "Code korrekt"

    # 5. Abflug-Ansage
    if station.get('track_launch'):
        play_track(station['track_launch'])
        show_launch_animation()

    # 6. Zwischenpause/Wegephase
    if station.get('track_fly_to'):
        show_message("Folgt den Pfeilen zum nächsten Ziel", 3)

# 7. Abschluss
end_station = stations[-1]
if end_station.get('track_end'):
    play_track(end_station['track_end'])
    show_message("Mission abgeschlossen!", 4)
