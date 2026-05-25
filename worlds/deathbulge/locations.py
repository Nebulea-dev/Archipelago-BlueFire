from typing import Dict, List, TYPE_CHECKING

regions_to_locations: Dict[str, Dict[str, List[str]]] = {
    "Menu": {
        "Menu": [],
    },
    # Dream
    "Dream": {
        "Intro01": [],
        "Dream02": [],
        "Dream03Base": [
            "Dream03Treasure01",
            "Dream03Treasure02",
            "Dream03Treasure03",
        ],
        "Dream04Base": [
            "Dream04Treasure02",
            "Dream04Treasure01",
            "Dream04Treasure03",
        ],
        "Dream05Base": [
            "Dream05Treasure01",
        ],
        "Dream06": [],
        "DreamUbers": [],
    },
    # Bopstead
    "Bopstead": {
        "Bopstead01": [
            "[Treasure] MODPODClass",
            "[Treasure] PartyHouseReward",
            "[Treasure] NelReward",
            "Bopstead01Treasure01",
            "Bopstead01Treasure02",
            "Bopstead01Treasure03",
            "[Treasure] PrizeTicketPlat",
            "[Treasure] FoggyRewardPatch",  # TODO: Check if real region
            "[Treasure] FoggyRewardMoney",  # TODO: Check if real region
            "[Treasure] Foggy300",  # TODO: Check if real region
        ],
        "Bopstead02": [
            "[Treasure] DaemoPatch",
            "Bopstead02Treasure01",
            "Bopstead02Treasure02",
            "Bopstead02Treasure03",
            "Bopstead02Treasure04",
            "[Treasure] GeorgeousReward",
        ],
        "Bopstead03": [
            "Bopstead03Treasure01",
            "[Treasure] PrizeTicketBrioche",
        ],
        "Bopstead04": [
            "Bopstead04Treasure01",
            "[Treasure] PrizeTicketBarry",
        ],
        "Bopstead05": [],
    },
    # Tonewood
    "Tonewood": {
        "Tonewood01": [
            "Tonewood01Treasure01",
        ],
        "Tonewood02": [
            "Tonewood02Treasure01",
        ],
        "Tonewood03": [
            "Tonewood03Treasure01",
            "Tonewood03Treasure02",
            "[Treasure] GillianFork",
        ],
        "Tonewood04": [
            "Tonewood04Treasure01",
            "Tonewood04Treasure02",
        ],
        "Tonewood05": [],
        "Tonewood06": [
            "Tonewood06Treasure01",
            "Tonewood06Treasure02",
        ],
        "Tonewood07": [],
        "Tonewood07-01": [],
        "Tonewood07-02": [],
        "Tonewood07-03": [],
        "Tonewood07-04": [],
        "Tonewood07-05": [],
        "Tonewood08": [
            "Tonewood08Treasure01",
            "Tonewood08Treasure02",
            "Tonewood08Treasure03",
            "Tonewood08Treasure04",
            "[Treasure] PrizeTicketJim",  # TODO: Check if real region
            "[Treasure] TonewoodGig02-Shrubbanshee",
        ],
    },
    # ClaireHair
    "ClaireHair": {
        "ClaireHair01": [],
        "ClaireHair02": [
            "Claire02Treasure01",
        ],
        "ClaireHair03": [],
        "ClaireHair04Lower": [
            "Claire04Treasure01",
            "Claire04Treasure02",
            "Claire04Treasure03",
            "Claire04Treasure04",
            "Claire04Treasure05",
        ],
        "ClaireHair04Upper": [],
        "ClaireHair05": [
            "Claire05Treasure01",
            "[Treasure] PrizeTicketMadam",
            "[Treasure] ClaireGig03-Madam",
        ],
        "ClaireHair06": [
            "Claire06Treasure01",
        ],
        "ClaireHair07": [
            "Claire07Treasure01",
            "Claire07Treasure02",
        ],
        "ClaireHair08": ["Beat KKwak"],
    },
    # Basement
    "Basement": {
        "Basement01": [
            "[Treasure] BasementGig01-Cuttlebro",  # TODO: Find real region
        ],
        "Basement02": [
            "Basement02Treasure01",
            "Basement02Treasure02",
        ],
        "Basement03": [
            "Basement03Treasure01",
            "Basement03Treasure02",
            "Basement03Treasure03",
        ],
        "Basement04": [
            "[Treasure] BasementGig02-Whale",
            "Basement04Treasure01",
            "Whale25Treasure",
        ],
        "Basement05": [
            "[Treasure] BasementGig04-Shutup",
            "Basement05Treasure01",
            "[Treasure] PrizeTicketBase",
        ],
        "Basement06": [
            "Basement06Treasure01",
            "Basement06Treasure02",
            "Basement06Treasure03",
            "[Treasure] BasementGig05-Cuttle",
        ],
        "Basement07": ["Beat Modern Babby"],
        "BasementEndingStudio": [],
    },
    # TheBus
    "TheBus": {
        "TheBus01": [],
        "TheBus02": [
            "TheBus02Treasure01",
        ],
        "TheBus03": [],
        "TheBus04": [],
        "TheBus05": [
            "TheBus05Treasure01",
            "TheBus05Treasure02",
            "TheBus05Treasure03",
            "[Treasure] PrizeTicketBus",
        ],
        "TheBus06": [
            "[Treasure] 13DeckKeycard",  # TODO: Check if real region
            "[Treasure] 14DeckKeycard",
            "[Treasure] TheBusGig01-Glamourella",
        ],
        "TheBus07": [],
        "TheBus08": [
            "TheBus08Treasure02",
            "TheBus08Treasure01",
            "TheBus08Treasure03",
        ],
        "TheBus09": [
            "TheBus09Treasure01",
            "[Treasure] TheBusGig02-Weaver",
        ],
        "TheBus10": [
            "TheBus10Treasure01",
            "TheBus10Treasure02",
            "TheBus10Treasure03",
            "Beat Platinum Scrumptious",
        ],
        "TheBus11": [
            "TheBus11Treasure01",
        ],
        "TheBusElevator": [],
    },
    # Hoho
    "Hoho": {
        "Hoho01Lower": [
            "Hoho01Treasure01",  # TODO: Verify if effectively lower
            "Hoho01Treasure02",  # TODO: Verify if effectively lower
        ],
        "Hoho01Observatory": [],
        "Hoho01-Bus": [],
        "Hoho02": [
            "Hoho02Treasure01",
            "Hoho02Treasure02",
            "Hoho02Treasure03",
            "Hoho02Treasure04",
            "Hoho02Treasure05",
            "Hoho02Treasure06",
            "[Treasure] PrizeTicketHoho",  # TODO: Check if real region
        ],
    },
    # Lab
    "Lab": {
        "Lab01": [
            "Lab01Treasure01",
        ],
        "Lab02": [],
        "Lab03": [
            "Lab03Treasure01",
        ],
        "Lab04": [
            "Lab04Treasure01",
            "Lab04Treasure02",
        ],
        "Lab05": [],
        "Lab06": [],
        "Lab07": [
            "Lab07Treasure01",
            "Lab07Treasure02",
        ],
        "Lab08": [
            "Lab08Treasure01",
        ],
        "Lab09": [
            "Lab09Treasure01",
        ],
        "Lab10": [
            "Lab10Treasure01",
            "Lab10Treasure02",
            "Beat Mutilla",
        ],
        "Lab11": [
            "[Treasure] LabGig02-WIP",
            "[Treasure] PrizeTicketLab",
        ],
        "Lab12": [
            "Lab12Treasure01",
        ],
    },
    # Pokalyps
    "Pokalyps": {
        "Pokalyps01": [
            "Pokalyps01Treasure01",
            "Pokalyps01Treasure02",
        ],
        "Pokalyps02Lower": [
            "Pokalyps02Treasure01",
        ],
        "Pokalyps02Upper": [
            "Pokalyps02Treasure02",
        ],
        "Pokalyps03": [],
        "Pokalyps04Middle": [],
        "Pokalyps04Lower": [],
        "Pokalyps04Upper": [],
        "Pokalyps04EvenUpper": [
            "Pokalyps04Treasure01",
        ],
        "Pokalyps05": [
            "Pokalyps05Treasure01",
            "Pokalyps05Treasure02",
        ],
        "Pokalyps06": [
            "Pokalyps06Treasure01",
        ],
        "Pokalyps07": [
            "Pokalyps07Treasure01",
        ],
        "Pokalyps08": [],
        "Pokalyps09": [
            "Pokalyps09Treasure01",
        ],
        "Pokalyps10": [
            "Pokalyps10Treasure01",
        ],
        "Pokalyps11": [
            "[Treasure] PrizeTicketPok",  # TODO: Find real region
            "Beat Pokalyps",
        ],
    },
    # ClaireLower
    "ClaireLower": {
        "ClaireLower01": [
            "ClaireLower01Treasure01",
        ],
        "ClaireLower02": [
            "ClaireLower02Treasure01",
        ],
        "ClaireLower03": [
            "ClaireLower03Treasure01",
            "ClaireLower03Treasure02",
            "ClaireLower03Treasure03",
        ],
        "ClaireLower04": [
            "ClaireLower04Treasure01",
            "ClaireLower04Treasure02",
        ],
        "TobbyCabin": [],
    },
    # BattleOfTheBands
    "BattleOfTheBands": {
        "BOTBLobby": ["Beat Boosted KKwak"],
    },
}


all_locations = [
    location
    for region, subregions in regions_to_locations.items()
    for subregion, locations in subregions.items()
    for location in locations
]

# Currently the list is static, but I will allow the items to be in the pool
forced_locations_items: Dict[str, str] = {
    "Beat KKwak": "Basement Key",
    "Beat Modern Babby": "Babby's corpse",
    "Beat Platinum Scrumptious": "Bus ticket",
    "Beat Mutilla": "Pokalyps concert's invite",
    "Beat Pokalyps": "Claire's comb",
    "Beat Boosted KKwak": "Beat Boosted KKwak",
}

forced_locations = [location for location, item in forced_locations_items.items()]
