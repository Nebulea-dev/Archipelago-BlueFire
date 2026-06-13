from typing import Dict, List


all_connections: Dict[str, Dict[str, List[str]]] = {
    "Fire Keep": {
        "Intro": ["Fire Keep - Hub", "Fire Keep - High Spot"],
        "High Spot": ["Fire Keep - Intro"],
        "Hub": ["Fire Keep - Intro", "Arcane Tunnels - Main Room"],
    },

    "Arcane Tunnels": {
        "Main Room": ["Fire Keep - Hub", "Arcane Tunnels - Pipes", "Arcane Tunnels - Center Top", "Crossroads - Main Area"],
        "Pipes": ["Arcane Tunnels - Main Room"],
        "Center Top": ["Arcane Tunnels - Main Room"],
    },

    "Crossroads": {
        "Main Area": ["Arcane Tunnels - Main Room", "Crossroads - Left Area", "Stoneheart City - Main Area"],
        "Left Area": ["Crossroads - Main Area"],
    },

    "Stoneheart City": {
        "Main Area": ["Crossroads - Main Area", "Stoneheart City - Top", "Stoneheart City - Boy's Room", "Stoneheart City - Bottom Corridor", "Forest Temple - High Level", "Abandoned Path - Entrance", "Water Ways - Stoneheart Entrance"],
        "Top": ["Stoneheart City - Main Area"],
		"Boy's Room": ["Stoneheart City - Main Area"],
		"Bottom Corridor": ["Stoneheart City - Main Area"],
    },

    "Water Ways": {
        "Stoneheart Entrance": ["Stoneheart City - Main Area", "Water Ways - Main Area"],
        "Main Area": ["Water Ways - Stoneheart Entrance", "Arcane Tunnels - Pipes", "Abandoned Path - Entrance", "Firefall River - Main Area"],
    },

    "Forest Temple": {
        "High Level": ["Stoneheart City - Main Area", "Forest Temple - Middle Level"],
        "Middle Level": ["Forest Temple - High Level", "Forest Temple - Low Level", "Forest Temple - Ambush 1"],
        "Low Level": ["Forest Temple - Middle Level", "Forest Temple - Center Room Trunk"],
        "Ambush 1": ["Forest Temple - Middle Level", "Forest Temple - Ambush 2", "Forest Temple - Nuos Claw"],
        "Ambush 2": ["Forest Temple - Ambush 1"],
        "Nuos Claw": ["Forest Temple - Ambush 1"],
        "Center Room Trunk": ["Forest Temple - Low Level"],
    },

    "Abandoned Path": {
		"Entrance": ["Stoneheart City - Main Area", "Abandoned Path - Main Room"],
        "Main Room": ["Abandoned Path - Entrance", "Abandoned Path - Entrance Ravin", "Abandoned Path - Graveyard Balcony" ,"Abandoned Path - Heights", "Abandoned Path - End of Main Room", "Uthas Temple - Entrance"],
		"Entrance Ravin": ["Abandoned Path - Main Room"],
		"Graveyard Balcony": ["Abandoned Path - Main Room", "Water Ways - Main Area", "Temple Gardens - Entrance"],
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
        "Entrance": ["Water Ways - Main Area", "Firefall River - Main Area", "Victory - Victory"],
    },

    "Firefall River": {
        "Main Area": ["Water Ways - Main Area", "Rust Village - Main Area"],
    },

    "Rust Village": {
        "Main Area": ["Firefall River - Main Area"],
    },

    "Victory": {
        "Victory": []
    },
}