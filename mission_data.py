## mission_data.py
# Definition der Missionsstationen und zugehörigen Audiodateien

# Jede Station enthält:
#  - name: Bezeichnung
#  - code: Startcode für Abflug (für Erde = Code zum Mond)
#  - track_fly_to: Track-Nr für Zielankündigung
#  - track_welcome: Track-Nr für Begrüßung bei Ankunft
#  - track_task: Track-Nr für Aufgabenansage
#  - track_code_prompt: Track-Nr für Aufforderung zur Codeeingabe
#  - track_launch: Track-Nr für die abenteuerliche Abflugansage
#  - optional track_end: für Abschlussansage

stations = [
    {
        "name": "Erde (Start)",
        "code": "38",               # Code für den Flug zum Mond eintragen
        "track_fly_to": 3,             # Zielankündigung: Mond
        "track_welcome": 1,            # Begrüßung Zuhause
        "track_task": 2,               # Aufgabenansage Erde
        "track_code_prompt": 31,       # Aufforderung Code Mond
        "track_launch": 40,            # Abflugansage-Track (z.B. "Bitte anschnallen...")
    },
    {
        "name": "Mond",
        "code": "2578",               # Code für den Flug zu Merkur
        "track_fly_to": 6,
        "track_welcome": 4,
        "track_task": 5,
        "track_code_prompt": 32,
        "track_launch": 41,
    },
    {
        "name": "Merkur",
        "code": "1863",
        "track_fly_to": 9,
        "track_welcome": 7,
        "track_task": 8,
        "track_code_prompt": 33,
        "track_launch": 42,
    },
    {
        "name": "Venus",
        "code": "5421",
        "track_fly_to": 12,
        "track_welcome": 10,
        "track_task": 11,
        "track_code_prompt": 34,
        "track_launch": 43,
    },
    {
        "name": "Mars",
        "code": "1104",
        "track_fly_to": 15,
        "track_welcome": 13,
        "track_task": 14,
        "track_code_prompt": 35,
        "track_launch": 44,
    },
    {
        "name": "Jupiter",
        "code": "6395",
        "track_fly_to": 18,
        "track_welcome": 16,
        "track_task": 17,
        "track_code_prompt": 36,
        "track_launch": 45,
    },
    {
        "name": "Saturn",
        "code": "4621",
        "track_fly_to": 21,
        "track_welcome": 19,
        "track_task": 20,
        "track_code_prompt": 37,
        "track_launch": 46,
    },
    {
        "name": "Uranus",
        "code": "8174",
        "track_fly_to": 24,
        "track_welcome": 22,
        "track_task": 23,
        "track_code_prompt": 38,
        "track_launch": 47,
    },
    {
        "name": "Neptun",
        "code": "3924",
        "track_fly_to": 27,
        "track_welcome": 25,
        "track_task": 26,
        "track_code_prompt": 39,
        "track_launch": 48,
    },
    {
        "name": "Pluto",
        "code": "xxxx",
        "track_fly_to": None,
        "track_welcome": 28,
        "track_task": 29,
        "track_code_prompt": None,
        "track_launch": 49,
    },
    {
        "name": "Erde (Rückkehr)",
        "code": None,
        "track_fly_to": None,
        "track_welcome": None,
        "track_task": None,
        "track_code_prompt": None,
        "track_launch": None,
        "track_end": 30,              # Abschlussansage
    }
]
