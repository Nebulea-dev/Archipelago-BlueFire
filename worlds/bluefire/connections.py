from typing import Dict, List


all_connections: Dict[str, Dict[str, List[str]]] = {
    "Fire Keep": {
        "Intro": ["Fire Keep - Hub"],
        "Hub": ["Fire Keep - Intro", "Arcane Tunnels"],
    },

    "Arcane Tunnels": ["Fire Keep - Hub", "Crossroads"],

    "Crossroads": ["Crossroads", "Stoneheart City"],

    "Stoneheart City": ["Stoneheart City", "Forest Temple - Water"],

    "Forest Temple": {
        "Water": ["Stoneheart City" ,"Forest Temple - Ambush 1", "Forest Temple - Center Tree"],
        "Ambush 1": ["Forest Temple - Water", "Forest Temple - Ambush 2", "Forest Temple - Nuos Claw"],
        "Ambush 2": ["Forest Temple - Ambush 1"],
        "Nuos Claw": ["Forest Temple - Ambush 1"],
        "Center Tree": ["Forest Temple - Water", "Forest Temple - Center Tree Trunk"],
        "Center Tree Trunk": ["Forest Temple - Center Tree", "Victory"],
    },

    "Victory": []
}
