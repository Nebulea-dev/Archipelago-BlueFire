from typing import Dict, List

from typing import Dict, List


all_connections: Dict[str, Dict[str, List[str]]] = {
    "Fire Keep": {
        "Intro": ["Fire Keep - Hub", "Fire Keep - High Spot"],
        "High Spot": ["Fire Keep - Hub"],
        "Hub": ["Fire Keep - Intro", "Arcane Tunnels - Main Room"],
    },

    "Arcane Tunnels": {
        "Main Room": ["Fire Keep - Hub", "Arcane Tunnels - Pipes", "Arcane Tunnels - Center Top", "Water Ways - Arcane Tunnels Entrance"],
        "Pipes": ["Arcane Tunnels - Main Room"],
        "Center Top": ["Arcane Tunnels - Main Room","Arcane Tunnels - Center Top Dance"],
        "Center Top Dance": ["Arcane Tunnels - Center Top"],
    },

    "Crossroads": {
        "Main Area": ["Arcane Tunnels - Main Room", "Crossroads - Left Area", "Stoneheart City - Main Area"],
        "Left Area": ["Crossroads - Main Area"],
    },

    "Stoneheart City": {
        "Main Area": ["Crossroads - Main Area", "Stoneheart City - Top", "Stoneheart City - Void Gate", "Forest Temple - Water", "Abandoned Path - Entrance"],
        "Top": ["Stoneheart City - Main Area"],
        "Void Gate": ["Stoneheart City - Main Area"],
    },

    "Water Ways": {
        "Arcane Tunnels Entrance": ["Stoneheart City - Main Area", "Water Ways - Main Area"],
        "Main Area": ["Water Ways - Arcane Tunnels Entrance", "Arcane Tunnels - Pipes", "Abandoned Path - Entrance", "Firefall River - Main Area"],
    },

    "Forest Temple": {
        "Water": ["Stoneheart City - Main Area" ,"Forest Temple - Ambush 1", "Forest Temple - Center Tree"],
        "Ambush 1": ["Forest Temple - Water", "Forest Temple - Ambush 2", "Forest Temple - Nuos Claw"],
        "Ambush 2": ["Forest Temple - Ambush 1"],
        "Nuos Claw": ["Forest Temple - Ambush 1"],
        "Center Tree": ["Forest Temple - Water", "Forest Temple - Center Tree Trunk"],
        "Center Tree Trunk": ["Forest Temple - Center Tree"],
    },

    "Abandoned Path": {
        "Entrance": ["Stoneheart City - Main Area", "Water Ways - Main Area", "Abandoned Path - Heights", "Abandoned Path - Beira's Room", "Uthas Temple - Entrance", "Temple Gardens - Entrance"],
        "Heights": ["Abandoned Path - Entrance"],
        "Beira's Room": ["Abandoned Path - Entrance"],
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
        "Main Area": ["Water Ways - Main Area", "Firefall River - Party Dance", "Rust Village - Main Area"],
        "Party Dance": ["Firefall River - Main Area"],
    },

    "Rust Village": {
        "Main Area": ["Firefall River - Main Area", "Rust Village - Aggressive Dance", "Rust Village - No Dance"],
        "Aggressive Dance": ["Rust Village - Main Area"],
        "No Dance": ["Rust Village - Main Area"],
    },

    "Victory": {
		"Victory": []
    },
}