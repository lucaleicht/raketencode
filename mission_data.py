## mission_data.py
# Definition der Missionsstationen und zugehörigen Audiodateien

# Jede Station enthält:
#  - name: Bezeichnung
#  - code: Startcode für Abflug
#  - track_fly_to: Track-Nr für Zielankündigung
#  - track_welcome: Track-Nr für Begrüßung bei Ankunft
#  - track_task: Track-Nr für die Aufgabenansage
#  - track_code_prompt: Track-Nr für Aufforderung zur Codeeingabe
#  - track_launch: Track-Nr für die abenteuerliche Abflugansage

stations = [
    {
        "name": "Erde (Start)",
        "code": "",  # kein Code beim Start
        "track_fly_to": None,
        "track_welcome": 1,
        "track_task": 2,
        "track_code_prompt": None,
        "track_launch": None,
    },
    {
        "name": "Mond",
        "code": "xxxx",  # bitte ersetzen
        "track_fly_to": 3,
        "track_welcome": 4,
        "track_task": 5,
        "track_code_prompt": 31,
        "track_launch": None,  # z.B. Abflugansage-Track
    },
    {
        "name": "Merkur",
        "code": "xxxx",
        "track_fly_to": 6,
        "track_welcome": 7,
        "track_task": 8,
        "track_code_prompt": 32,
        "track_launch": None,
    },
    {
        "name": "Venus",
        "code": "xxxx",
        "track_fly_to": 9,
        "track_welcome": 10,
        "track_task": 11,
        "track_code_prompt": 33,
        "track_launch": None,
    },
    {
        "name": "Mars",
        "code": "xxxx",
        "track_fly_to": 12,
        "track_welcome": 13,
        "track_task": 14,
        "track_code_prompt": 34,
        "track_launch": None,
    },
    {
        "name": "Jupiter",
        "code": "xxxx",
        "track_fly_to": 15,
        "track_welcome": 16,
        "track_task": 17,
        "track_code_prompt": 35,
        "track_launch": None,
    },
    {
        "name": "Saturn",
        "code": "xxxx",
        "track_fly_to": 18,
        "track_welcome": 19,
        "track_task": 20,
        "track_code_prompt": 36,
        "track_launch": None,
    },
    {
        "name": "Uranus",
        "code": "xxxx",
        "track_fly_to": 21,
        "track_welcome": 22,
        "track_task": 23,
        "track_code_prompt": 37,
        "track_launch": None,
    },
    {
        "name": "Neptun",
        "code": "xxxx",
        "track_fly_to": 24,
        "track_welcome": 25,
        "track_task": 26,
        "track_code_prompt": 38,
        "track_launch": None,
    },
    {
        "name": "Pluto",
        "code": "xxxx",
        "track_fly_to": 27,
        "track_welcome": 28,
        "track_task": 29,
        "track_code_prompt": 39,
        "track_launch": None,
    },
    {
        "name": "Erde (Rückkehr)",
        "code": None,
        "track_fly_to": None,
        "track_welcome": None,
        "track_task": None,
        "track_code_prompt": None,
        "track_launch": None,
        "track_end": 30,
    }
]
