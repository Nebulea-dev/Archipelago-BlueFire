from typing import Dict, List, TYPE_CHECKING

regions_to_locations: Dict[str, Dict[str, List[str]] | List[str]] = {
    "Menu": [],

    "Fire Keep": {
        "Intro": [
            "Ambush chest 1",
            "Ambush chest 2"
        ],
        "Hub": [
            "Spin attack",
            "Loot chest 1",
            "Loot chest 2",
            "Loot chest 3",
            "Diamond Wing Chest",
        ],
    },

    "Arcane Tunnels": [
        "North loot chest 1",
        "North loot chest 2",
        "North loot chest 3",
        "East loot chest 1",
        "East loot chest 4",
        "East loot chest 5",
        "Bloodstorm chest",
        "Arcane chest",
        "South key chest 2",
        "East loot chest 2",
        "East loot chest 3",
        "South loot chest",
        "South key chest 1",
    ],

    "Crossroads": [
        "Well Loot Chest 3",
        "Loot Chest 1",
        "Loot chest 2",
        "Loot Chest 3",
    ],

    "Stoneheart City": [
        "Pure Shadow chest",
        "Stoneheart chest 3",
        "Stoneheart chest 1",
        "Stoneheart chest 2",
        "Stoneheart chest 4",
        "Merchants Robe chest",
        "Graveyard key chest 1",
        "Graveyard key chest 2",
    ],

    "Forest Temple": {
        "Water": [
            "Loot chest 1",
            "Loot chest 2",
            "Key chest",
        ],
        "Ambush 1": [
            "Key chest",
        ],
        "Ambush 2": [
            "Key chest",
        ],
        "Nuos Claw": [
            "Nuos Claw chest",
        ],
        "Center Tree": [
            "Loot chest 1",
            "Loot chest 2",
            "Loot chest 3",
            "Void chest",
            "Silverblades chest",
            "Key chest",
        ],
        "Center Tree Trunk": [
            "Loot chest 1",
        ],
    },

    "Victory": [
		"Victory"
	],
}


regions_with_subregions = [
    f"{region} - {subregion} - {location}"
    for region, subregions in regions_to_locations.items()
	if isinstance(subregions, dict)
    for subregion, locations in subregions.items()
    for location in locations
]

regions_without_subregions = [
    f"{region} - {location}"
    for region, locations in regions_to_locations.items()
	if isinstance(locations, list)
    for location in locations
]


all_locations : List[str] = (
    regions_with_subregions
	+ regions_without_subregions
)


forced_locations_items: Dict[str, str] = {
    "Victory - Victory": "Victory",
}

forced_locations = [location for location, item in forced_locations_items.items()]
