from typing import Dict, List

# TODO: MAKE THE CONNECTIONS
all_connections: Dict[str, Dict[str, List[str]]] = {
    # Dream
    # TODO: Check the reality of all dream locations
    "Dream": {
        "Intro01": ["Bopstead - Bopstead01"],
        "Dream02": [],  # TODO: Find where this is ?
        "Dream03Base": [
            "Dream - Dream04Base",
            "Dream - Dream06",
            "Pokalyps - Pokalyps05",
        ],
        "Dream04Base": ["Dream - Dream05Base"],
        "Dream05Base": ["Dream - Dream03Base"],
        "Dream06": ["Dream - DreamUbers"],
        "DreamUbers": ["Dream - Dream04Base"],
    },
    # Bopstead
    "Bopstead": {
        "Bopstead01": [
            "Bopstead - Bopstead02",
            "Bopstead - Bopstead03",
            "Tonewood - Tonewood01",
        ],
        "Bopstead02": [
            "Bopstead - Bopstead01",
            "Bopstead - Bopstead04",
            "Bopstead - Bopstead05",
            "Basement - Basement01",
            "TheBus - TheBus01",
        ],
        "Bopstead03": ["Bopstead - Bopstead01"],
        "Bopstead04": ["Bopstead - Bopstead02"],
        "Bopstead05": ["Bopstead - Bopstead02"],
    },
    # Tonewood
    "Tonewood": {
        "Tonewood01": ["Tonewood - Tonewood02"],
        "Tonewood02": [
            "Tonewood - Tonewood01",
            "Tonewood - Tonewood03",
            "Tonewood - Tonewood07",
        ],
        "Tonewood03": [
            "Tonewood - Tonewood02",
            "Tonewood - Tonewood04",
        ],
        "Tonewood04": [
            "Tonewood - Tonewood03",
            "Tonewood - Tonewood05",
            "Tonewood - Tonewood06",
        ],
        "Tonewood05": [
            "Tonewood - Tonewood04",
        ],
        "Tonewood06": [
            "Tonewood - Tonewood04",
            "ClaireHair - ClaireHair01",
        ],
        "Tonewood07": [
            "Tonewood - Tonewood02",
            "Tonewood - Tonewood07-01",
        ],
        "Tonewood07-01": [
            "Tonewood - Tonewood07",
            "Tonewood - Tonewood07-02",
        ],
        "Tonewood07-02": [
            "Tonewood - Tonewood07",
            "Tonewood - Tonewood07-01",
            "Tonewood - Tonewood07-03",
        ],
        "Tonewood07-03": [
            "Tonewood - Tonewood07",
            "Tonewood - Tonewood07-02",
            "Tonewood - Tonewood07-04",
        ],
        "Tonewood07-04": [
            "Tonewood - Tonewood07",
            "Tonewood - Tonewood07-03",
            "Tonewood - Tonewood07-05",
        ],
        "Tonewood07-05": [
            "Tonewood - Tonewood07",
            "Tonewood - Tonewood07-04",
            "Tonewood - Tonewood08",
        ],
        "Tonewood08": ["Tonewood - Tonewood07"],
    },
    # ClaireHair
    "ClaireHair": {
        "ClaireHair01": [
            "Tonewood - Tonewood06",
            "ClaireHair - ClaireHair02",
        ],
        "ClaireHair02": [
            "ClaireHair - ClaireHair01",
            "ClaireHair - ClaireHair03",
            "ClaireHair - ClaireHair04Lower",
        ],
        "ClaireHair03": [
            "ClaireHair - ClaireHair02",
            "ClaireHair - ClaireHair04Upper",
        ],
        "ClaireHair04Lower": [
            "ClaireHair - ClaireHair02",
            "ClaireHair - ClaireHair06",
            "ClaireHair - ClaireHair07",
            "ClaireLower - ClaireLower01",
        ],
        "ClaireHair04Upper": [
            "ClaireHair - ClaireHair03",
            "ClaireHair - ClaireHair05",
        ],
        "ClaireHair05": [
            "ClaireHair - ClaireHair04Upper",
        ],
        "ClaireHair06": [
            "ClaireHair - ClaireHair04Lower",
            "ClaireHair - ClaireHair07",
        ],
        "ClaireHair07": [
            "ClaireHair - ClaireHair04Lower",
            "ClaireHair - ClaireHair06",
            "ClaireHair - ClaireHair08",
        ],
        "ClaireHair08": ["ClaireHair - ClaireHair07"],
    },
    # Basement
    "Basement": {
        "Basement01": [
            "Bopstead - Bopstead02",
            "Basement - Basement02",
        ],
        "Basement02": [
            "Basement - Basement01",
            "Basement - Basement03",
            "Basement - Basement05",
            "Basement - Basement07",
        ],
        "Basement03": [
            "Basement - Basement02",
            "Basement - Basement04",
        ],
        "Basement04": [
            "Basement - Basement03",
            "Basement - Basement05",
        ],
        "Basement05": [
            "Basement - Basement02",
            "Basement - Basement04",
            "Basement - Basement06",
        ],
        "Basement06": [
            "Basement - Basement05",
            "Basement - Basement07",
        ],
        "Basement07": [
            "Basement - Basement06",
            "Basement - Basement02",
        ],
        "BasementEndingStudio": [],  # Only at the ending
    },
    # TheBus
    "TheBus": {
        "TheBus01": [
            "Bopstead - Bopstead02",
            "TheBus - TheBus02",
        ],
        "TheBus02": [
            "TheBus - TheBus01",
            "TheBus - TheBus03",
        ],
        "TheBus03": [
            "TheBus - TheBus02",
            "TheBus - TheBus04",
        ],
        "TheBus04": [
            "TheBus - TheBus03",
            "TheBus - TheBusElevator",
        ],
        "TheBus05": [
            "TheBus - TheBusElevator",
            "TheBus - TheBus06",
        ],
        "TheBus06": [
            "TheBus - TheBus05",
            "TheBus - TheBusElevator",
        ],
        "TheBus07": ["TheBus - TheBusElevator"],  # TODO: Verify, I think this is only glamourella / Floor 13 ?
        "TheBus08": [
            "TheBus - TheBusElevator",
            "TheBus - TheBus09",
        ],  # TODO: Verify, I think this is only Floor 14 ?
        "TheBus09": [
            "TheBus - TheBus08",
            "TheBus - TheBus10",
        ],
        "TheBus10": [
            "TheBus - TheBus09",
            "TheBus - TheBusElevator",
            "Hoho - Hoho01-Bus",
        ],
        "TheBus11": ["TheBus - TheBusElevator"],
        "TheBusElevator": [
            "TheBus - TheBus04",
            "TheBus - TheBus05",
            "TheBus - TheBus06",  # Floor 10
            "TheBus - TheBus07",  # Floor 13
            "TheBus - TheBus08",  # Floor 14
            "TheBus - TheBus10",  # Floor 16 - 17
            "TheBus - TheBus11",  # Floor 30
        ],
    },
    # Hoho
    "Hoho": {
        "Hoho01Lower": [
            "Bopstead - Bopstead02",
            "Hoho - Hoho02",
            "BattleOfTheBands - BOTBLobby",
            "Lab - Lab01",  # Briff Kidnapping
        ],
        "Hoho01Observatory": ["Hoho - Hoho02"],
        "Hoho01-Bus": ["Hoho - Hoho01Lower"],
        "Hoho02": [
            "Hoho - Hoho01Lower",
            "Hoho - Hoho01Observatory",
            "Lab - Lab10",
            "Pokalyps - Pokalyps01",
        ],
    },
    # Lab
    "Lab": {
        "Lab01": [
            "Lab - Lab02",
            "Lab - Lab04",
        ],
        "Lab02": [
            "Lab - Lab01",
            "Lab - Lab03",
        ],
        "Lab03": [
            "Lab - Lab02",
            "Lab - Lab11",
        ],
        "Lab04": [
            "Lab - Lab01",
            "Lab - Lab03",
            "Lab - Lab05",
        ],
        "Lab05": [
            "Lab - Lab04",
            "Lab - Lab06",
        ],
        "Lab06": [
            "Lab - Lab05",
            "Lab - Lab07",
        ],
        "Lab07": [
            "Lab - Lab06",
            "Lab - Lab08",
            "Lab - Lab12",
        ],
        "Lab08": [
            "Lab - Lab07",
            "Lab - Lab09",
        ],
        "Lab09": [
            "Lab - Lab08",
            "Lab - Lab10",
        ],
        "Lab10": [
            "Lab - Lab09",
            "Hoho - Hoho02",
        ],
        "Lab11": ["Lab - Lab03"],
        "Lab12": ["Lab - Lab07"],
    },
    # Pokalyps
    "Pokalyps": {
        "Pokalyps01": [
            "Hoho - Hoho02",
            "Pokalyps - Pokalyps02Lower",
            "Pokalyps - Pokalyps05",
        ],
        "Pokalyps02Lower": [
            "Pokalyps - Pokalyps01",
            "Pokalyps - Pokalyps03",
        ],
        "Pokalyps02Upper": ["Pokalyps - Pokalyps08"],
        "Pokalyps03": [
            "Pokalyps - Pokalyps02Lower",
            "Pokalyps - Pokalyps04Middle",
        ],
        "Pokalyps04Middle": [
            "Pokalyps - Pokalyps03",
            "Pokalyps - Pokalyps05",
        ],
        "Pokalyps04Lower": [
            "Pokalyps - Pokalyps05",
            "Pokalyps - Pokalyps06",
            "Pokalyps - Pokalyps07",
        ],
        "Pokalyps04Upper": [
            "Pokalyps - Pokalyps07",
            "Pokalyps - Pokalyps08",
        ],
        "Pokalyps04EvenUpper": [
            "Pokalyps - Pokalyps08",
            "Pokalyps - Pokalyps09",
        ],
        "Pokalyps05": [
            "Pokalyps - Pokalyps04Middle",
            "Pokalyps - Pokalyps04Lower",
            "Dream - Dream03Base",
            "Pokalyps - Pokalyps01",
        ],
        "Pokalyps06": ["Pokalyps - Pokalyps04Lower"],
        "Pokalyps07": [
            "Pokalyps - Pokalyps04Lower",
            "Pokalyps - Pokalyps04Upper",
        ],
        "Pokalyps08": [
            "Pokalyps - Pokalyps04Upper",
            "Pokalyps - Pokalyps04EvenUpper",
            "Pokalyps - Pokalyps02Upper",
        ],
        "Pokalyps09": [
            "Pokalyps - Pokalyps04EvenUpper",
            "Pokalyps - Pokalyps10",
        ],
        "Pokalyps10": [
            "Pokalyps - Pokalyps09",
            "Pokalyps - Pokalyps11",
        ],
        "Pokalyps11": [
            "Pokalyps - Pokalyps10",
        ],
    },
    # ClaireLower
    "ClaireLower": {
        "ClaireLower01": [
            "ClaireHair - ClaireHair04Lower",
            "ClaireLower - ClaireLower02",
        ],
        "ClaireLower02": [
            "ClaireLower - ClaireLower01",
            "ClaireLower - ClaireLower03",
        ],
        "ClaireLower03": [
            "ClaireLower - ClaireLower02",
            "ClaireLower - ClaireLower04",
        ],
        "ClaireLower04": [
            "ClaireLower - ClaireLower03",
            "ClaireLower - TobbyCabin",
            "ClaireLower - ClaireLower01",
        ],
        "TobbyCabin": ["ClaireLower - ClaireLower04"],
    },
    # BattleOfTheBands
    "BattleOfTheBands": {
        "BOTBLobby": ["Hoho - Hoho01Lower"],
    },
}
