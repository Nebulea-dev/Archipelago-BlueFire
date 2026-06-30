from typing import Dict, List


all_connections: Dict[str, Dict[str, List[str]]] = {
    "Fire Keep": {
        "Intro": ["Fire Keep - Hub", "Fire Keep - High Spot"],
        "High Spot": ["Fire Keep - Intro"],
        "Hub": ["Fire Keep - Intro", "Arcane Tunnels - Main Room"],
    },

    "Arcane Tunnels": {
        "Main Room": ["Fire Keep - Hub", "Arcane Tunnels - Pipes", "Arcane Tunnels - Center Top", "Crossroads - Main Area", "Water Ways - Arcane Tunnels Main Entrance"],
        "Pipes": ["Arcane Tunnels - Main Room", "Water Ways - Arcane Tunnels Pipes Entrance"],
        "Center Top": ["Arcane Tunnels - Main Room"],
    },

    "Crossroads": {
        "Main Area": ["Arcane Tunnels - Main Room", "Crossroads - Left Area", "Stoneheart City - Main Area"],
        "Left Area": ["Crossroads - Main Area"],
    },

    "Stoneheart City": {
        "Main Area": ["Crossroads - Main Area", "Stoneheart City - Top", "Stoneheart City - Boy's Room", "Stoneheart City - Bottom Corridor", "Stoneheart City - Breemur's Tavern", "Forest Temple - High Level", "Abandoned Path - Entrance", "Temple Gardens - Middle Balcony"],
        "Top": ["Stoneheart City - Main Area"],
		"Boy's Room": ["Stoneheart City - Main Area"],
		"Bottom Corridor": ["Stoneheart City - Main Area"],
		"Breemur's Tavern": ["Stoneheart City - Main Area"],
    },

    "Water Ways": {
        "Arcane Tunnels Main Entrance": ["Arcane Tunnels - Main Room", "Water Ways - Main Area"],
		"Arcane Tunnels Pipes Entrance": ["Arcane Tunnels - Pipes", "Water Ways - Main Area"],
		"Abandoned Path Entrance": ["Abandoned Path - Graveyard Balcony", "Water Ways - Main Area"],
		"Firefall River Entrance": ["Firefall River - Main Area", "Water Ways - Main Area"],
        "Main Area": ["Water Ways - Arcane Tunnels Main Entrance", "Water Ways - Arcane Tunnels Pipes Entrance", "Water Ways - Abandoned Path Entrance", "Water Ways - Firefall River Entrance", "Water Ways - Samuel's Room"],
		"Samuel's Room": ["Water Ways - Main Area"],
    },

    "Forest Temple": {
        "High Level": ["Stoneheart City - Main Area", "Forest Temple - Middle Level"],
        "Middle Level": ["Forest Temple - High Level", "Forest Temple - Low Level", "Forest Temple - Ambush 1"],
        "Low Level": ["Forest Temple - Middle Level", "Forest Temple - Center Room"],
        "Ambush 1": ["Forest Temple - Middle Level", "Forest Temple - Ambush 2", "Forest Temple - Nuos Claw Room"],
        "Ambush 2": ["Forest Temple - Ambush 1"],
        "Nuos Claw Room": ["Forest Temple - Ambush 1"],
        "Center Room": ["Forest Temple - Low Level", "Forest Temple - Center Room Trunk", "Forest Temple - Parkour Room", "Forest Temple - Boss Room"],
        "Center Room Trunk": ["Forest Temple - Center Room"],
		"Parkour Room": ["Forest Temple - Center Room"],
		"Boss Room": ["Forest Temple - Center Room"],
    },

    "Abandoned Path": {
		"Entrance": ["Stoneheart City - Main Area", "Abandoned Path - Main Room"],
        "Main Room": ["Abandoned Path - Entrance", "Abandoned Path - Entrance Ravin", "Abandoned Path - Graveyard Balcony" ,"Abandoned Path - Heights", "Abandoned Path - End of Main Room", "Uthas Temple - Entrance"],
		"Entrance Ravin": ["Abandoned Path - Main Room"],
		"Graveyard Balcony": ["Abandoned Path - Main Room", "Water Ways - Abandoned Path Entrance", "Temple Gardens - Entrance"],
        "Heights": ["Abandoned Path - Main Room", "Abandoned Path - Beira's Room"],
        "Beira's Room": ["Abandoned Path - Heights"],
        "End of Main Room": ["Abandoned Path - Main Room"],
    },

    "Uthas Temple": {
        "Entrance": ["Abandoned Path - Entrance", "Uthas Temple - Main Room", "Uthas Temple - Top of Entrance"],
        "Top of Entrance": ["Uthas Temple - Entrance"],
        "Main Room": ["Uthas Temple - Entrance", "Uthas Temple - Ambush Room", "Uthas Temple - Holy Tower Chest", "Uthas Temple - Main Room 2nd side"],
        "Ambush Room": ["Uthas Temple - Main Room"],
        "Holy Tower Chest": ["Uthas Temple - Main Room"],
        "Main Room 2nd side": ["Uthas Temple - Main Room", "Uthas Temple - Final Floor"],
        "Final Floor": ["Uthas Temple - Main Room 2nd side"],
    },

    "Temple Gardens": {
        "Entrance": ["Temple Gardens - Middle Balcony", "Temple Gardens - Temple of Gods", "Firefall River - Main Area"],
		"Middle Balcony": ["Temple Gardens - Entrance", "Stoneheart City - Main Area"],
		"Temple of Gods": ["Temple Gardens - Entrance", "Victory - Victory"]
    },

    "Firefall River": {
        "Main Area": ["Firefall River - Steam House", "Water Ways - Firefall River Entrance"],
		"Steam House": ["Firefall River - Main Area", "Firefall River - Fire Boss Room", "Rust Village - Main Area"],
		"Fire Boss Room": ["Firefall River - Steam House"]
    },

    "Rust Village": {
        "Main Area": ["Firefall River - Main Area"],
    },

    "Victory": {
        "Victory": []
    },
}