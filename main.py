# main.py
"""
Orchestrierung der Raketenmission im Terminal-Modus mit curses:
- importiere Module: mission_data, keypad_handler, audio_player, display_manager
- steuere die Text- und ASCII-Anzeige über curses.wrapper
- Ablauf: Begrüßung -> Aufgabe -> Ziel -> Code -> Abflug -> Wegphase -> nächste Station -> Abschluss
"""
import curses
from mission_data import stations
from keypad_handler import get_code
from audio_player import set_volume, play_track
from display_manager import show_message, show_launch_animation


def mission_loop(stdscr):
    # curses initialisieren
    curses.curs_set(0)
    stdscr.nodelay(False)

    # Setze Standard-Lautstärke
    set_volume(25)

    # Hauptschleife über alle Stationen
    for station in stations:
        name = station['name']

        # 1. Begrüßung oder Start
        if station.get('track_welcome'):
            show_message(stdscr, f"Begrüßung: {name}", 2)
            play_track(station['track_welcome'])

        # 2. Aufgabenansage
        if station.get('track_task'):
            show_message(stdscr, "Aufgabe:", 2)
            play_track(station['track_task'])

        # 3. Zielankündigung
        if station.get('track_fly_to'):
            play_track(station['track_fly_to'])
            show_message(stdscr, "Zielankündigung…", 2)

        # 4. Codeeingabe
        if station.get('track_code_prompt'):
            play_track(station['track_code_prompt'])
            code = get_code()
            # Warten auf korrekten Code
            while code != station['code']:
                show_message(stdscr, "Falscher Code, bitte erneut.", 2)
                code = get_code()
            # Code korrekt
            play_track(20)  # allgemeine Bestätigung "Code korrekt"

        # 5. Abflug-Ansage + Animation
        if station.get('track_launch'):
            play_track(station['track_launch'])
            show_launch_animation(stdscr)

        # 6. Wegephase (Hinweis)
        if station.get('track_fly_to'):
            show_message(stdscr, "Folgt den Pfeilen zum nächsten Ziel…", 3)

    # 7. Abschluss
    end_station = stations[-1]
    if end_station.get('track_end'):
        play_track(end_station['track_end'])
        show_message(stdscr, "Mission abgeschlossen!", 4)


if __name__ == '__main__':
    curses.wrapper(mission_loop)
