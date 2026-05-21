from typing import Dict, TYPE_CHECKING
import logging

from .Types import LocData

if TYPE_CHECKING:
    from . import BluefireWorld

def did_include_extra_locations(world: "BluefireWorld") -> bool:
    return bool(world.options.ExtraLocations)

def get_total_locations(world: "BluefireWorld") -> int:
    total = 0
    for name in location_table:
        if not did_include_extra_locations(world) and name in extra_locations:
            continue

        if is_valid_location(world, name):
            total += 1

    return total

def get_location_names() -> Dict[str, int]:
    names = {name: data.ap_code for name, data in location_table.items()}
    return names

def is_valid_location(world: "BluefireWorld", name) -> bool:
    if not did_include_extra_locations(world) and name in extra_locations:
        return False

    return True

# Base location ID for Blue Fire
BASE_LOCATION_ID = 20050100

# Fire Keep area - Starting zone
fire_keep_locations = {
    "Fire Keep - Lab": LocData(BASE_LOCATION_ID + 1, "Fire Keep"),
    "Fire Keep - Bitoven": LocData(BASE_LOCATION_ID + 2, "Fire Keep"),
    "Fire Keep - Keep Ducks": LocData(BASE_LOCATION_ID + 3, "Fire Keep"),
    "Fire Keep - Keep Vessel": LocData(BASE_LOCATION_ID + 4, "Fire Keep"),
    "Fire Keep - Shield": LocData(BASE_LOCATION_ID + 5, "Fire Keep"),
    "Fire Keep - First Void": LocData(BASE_LOCATION_ID + 6, "Fire Keep"),
    "Fire Keep - Crates": LocData(BASE_LOCATION_ID + 7, "Fire Keep"),
    "Fire Keep - Memorial": LocData(BASE_LOCATION_ID + 8, "Fire Keep"),
}

# Arcane Tunnels area
arcane_tunnels_locations = {
    "Arcane Tunnels - North": LocData(BASE_LOCATION_ID + 10, "Arcane Tunnels"),
    "Arcane Tunnels - South": LocData(BASE_LOCATION_ID + 11, "Arcane Tunnels"),
    "Arcane Tunnels - Spirit Hunter": LocData(BASE_LOCATION_ID + 12, "Arcane Tunnels"),
    "Arcane Tunnels - Ducks": LocData(BASE_LOCATION_ID + 13, "Arcane Tunnels"),
}

# Crossroads and Well area
crossroads_locations = {
    "Crossroads": LocData(BASE_LOCATION_ID + 20, "Crossroads"),
    "Well": LocData(BASE_LOCATION_ID + 21, "Crossroads"),
}

# Stoneheart City area
stoneheart_locations = {
    "Stoneheart City": LocData(BASE_LOCATION_ID + 30, "Stoneheart City"),
}

# Forest Temple area
forest_temple_locations = {
    "Forest Temple - Water Levels": LocData(BASE_LOCATION_ID + 40, "Forest Temple"),
    "Forest Temple - Nuos Claw": LocData(BASE_LOCATION_ID + 41, "Forest Temple"),
    "Forest Temple - Tree": LocData(BASE_LOCATION_ID + 42, "Forest Temple"),
    "Forest Temple - Forest Ducks": LocData(BASE_LOCATION_ID + 43, "Forest Temple"),
    "Forest Temple - Gruh Boss": LocData(BASE_LOCATION_ID + 44, "Forest Temple"),
}

# Temple Gardens area
temple_gardens_locations = {
    "Temple Gardens": LocData(BASE_LOCATION_ID + 50, "Temple Gardens"),
}

# Abandoned Path / Tower area
abandoned_path_locations = {
    "Abandoned Path": LocData(BASE_LOCATION_ID + 60, "Abandoned Path"),
    "Beira Shrine": LocData(BASE_LOCATION_ID + 61, "Abandoned Path"),
}

# Uthas Temple area
uthas_temple_locations = {
    "Uthas Temple - Start": LocData(BASE_LOCATION_ID + 70, "Uthas Temple"),
    "Uthas Temple - Bracelet": LocData(BASE_LOCATION_ID + 71, "Uthas Temple"),
    "Uthas Temple - Ducks": LocData(BASE_LOCATION_ID + 72, "Uthas Temple"),
    "Uthas Temple - Puzzle": LocData(BASE_LOCATION_ID + 73, "Uthas Temple"),
    "Uthas Temple - Combat": LocData(BASE_LOCATION_ID + 74, "Uthas Temple"),
    "Uthas Temple - Platforming": LocData(BASE_LOCATION_ID + 75, "Uthas Temple"),
    "Uthas Temple - End": LocData(BASE_LOCATION_ID + 76, "Uthas Temple"),
}

# Temple of Gods area
temple_of_gods_locations = {
    "Sanctuary Stone Location": LocData(BASE_LOCATION_ID + 80, "Temple of Gods"),
    "Queen Chamber": LocData(BASE_LOCATION_ID + 81, "Temple of Gods"),
}

# Firefall River area
firefall_river_locations = {
    "Firefall River - Spirit Hunter": LocData(BASE_LOCATION_ID + 90, "Firefall River"),
    "Firefall River - Bunny": LocData(BASE_LOCATION_ID + 91, "Firefall River"),
    "Firefall River - Lake Molva": LocData(BASE_LOCATION_ID + 92, "Firefall River"),
    "Firefall River - Ducks": LocData(BASE_LOCATION_ID + 93, "Firefall River"),
}

# Steam House area
steam_house_locations = {
    "Steam House - Core": LocData(BASE_LOCATION_ID + 100, "Steam House"),
    "Steam House - Ducks": LocData(BASE_LOCATION_ID + 101, "Steam House"),
    "Steam House - Platforming": LocData(BASE_LOCATION_ID + 102, "Steam House"),
}

# Sirion and Rust Village areas
iron_caves_locations = {
    "Sirion": LocData(BASE_LOCATION_ID + 110, "Iron Caves"),
    "Rust Village": LocData(BASE_LOCATION_ID + 111, "Iron Caves"),
}

# Waterway area
waterway_locations = {
    "Waterway": LocData(BASE_LOCATION_ID + 120, "Waterway"),
    "Waterway - Ducks": LocData(BASE_LOCATION_ID + 121, "Waterway"),
    "Waterway - Samael Boss": LocData(BASE_LOCATION_ID + 122, "Waterway"),
}

# Void Challenges area (optional locations)
void_locations = {
    "Void - Path of Victory": LocData(BASE_LOCATION_ID + 130, "Void Challenges"),
    "Void - Arigos Challenge": LocData(BASE_LOCATION_ID + 131, "Void Challenges"),
    "Void - Brisas Fate": LocData(BASE_LOCATION_ID + 132, "Void Challenges"),
    "Void - Julians Song": LocData(BASE_LOCATION_ID + 133, "Void Challenges"),
    "Void - Alchemist": LocData(BASE_LOCATION_ID + 134, "Void Challenges"),
    "Void - The Void": LocData(BASE_LOCATION_ID + 135, "Void Challenges"),
}

# Standard locations (always included)
standard_locations = {
    **fire_keep_locations,
    **arcane_tunnels_locations,
    **crossroads_locations,
    **stoneheart_locations,
    **forest_temple_locations,
    **temple_gardens_locations,
    **abandoned_path_locations,
    **uthas_temple_locations,
    **temple_of_gods_locations,
    **firefall_river_locations,
    **steam_house_locations,
    **iron_caves_locations,
    **waterway_locations,
}

# Extra/optional locations
extra_locations = {
    **void_locations,
}

# Event/victory location
event_locations = {
    # This is handled via the victory item in Items.py
}

# Combined location table
location_table = {
    **standard_locations,
    **extra_locations,
    **event_locations,
}
