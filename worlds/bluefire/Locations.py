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
BASE_LOCATION_ID = 0xB70EF14E

# Fire Keep area - Starting zone
fire_keep_intro_locations = {
    "Fire Keep - Intro - Ambush chest 1": LocData(BASE_LOCATION_ID + 1, "Fire Keep - Intro"),
    "Fire Keep - Intro - Ambush chest 2": LocData(BASE_LOCATION_ID + 2, "Fire Keep - Intro"),
}

fire_keep_hub_locations = {
    "Fire Keep - Hub - Spin attack": LocData(BASE_LOCATION_ID + 3, "Fire Keep - Hub"),
    "Fire Keep - Hub - Loot chest 1": LocData(BASE_LOCATION_ID + 4, "Fire Keep - Hub"),
    "Fire Keep - Hub - Loot chest 2": LocData(BASE_LOCATION_ID + 5, "Fire Keep - Hub"),
    "Fire Keep - Hub - Loot chest 3": LocData(BASE_LOCATION_ID + 6, "Fire Keep - Hub"),
    "Fire Keep - Hub - Diamond Wing Chest": LocData(BASE_LOCATION_ID + 7, "Fire Keep - Hub"),
}

# Arcane Tunnels
arcane_tunnels_locations = {
    "Arcane Tunnels - North loot chest 1": LocData(BASE_LOCATION_ID + 8, "Arcane Tunnels"),
    "Arcane Tunnels - North loot chest 2": LocData(BASE_LOCATION_ID + 9, "Arcane Tunnels"),
    "Arcane Tunnels - North loot chest 3": LocData(BASE_LOCATION_ID + 10, "Arcane Tunnels"),
    "Arcane Tunnels - East loot chest 1": LocData(BASE_LOCATION_ID + 11, "Arcane Tunnels"),
    "Arcane Tunnels - East loot chest 4": LocData(BASE_LOCATION_ID + 12, "Arcane Tunnels"),
    "Arcane Tunnels - East loot chest 5": LocData(BASE_LOCATION_ID + 13, "Arcane Tunnels"),
    "Arcane Tunnels - Bloodstorm chest": LocData(BASE_LOCATION_ID + 14, "Arcane Tunnels"),
    "Arcane Tunnels - Arcane chest": LocData(BASE_LOCATION_ID + 15, "Arcane Tunnels"),
    "Arcane Tunnels - South key chest 2": LocData(BASE_LOCATION_ID + 16, "Arcane Tunnels"),
    "Arcane Tunnels - East loot chest 2": LocData(BASE_LOCATION_ID + 17, "Arcane Tunnels"),
    "Arcane Tunnels - East loot chest 3": LocData(BASE_LOCATION_ID + 18, "Arcane Tunnels"),
    "Arcane Tunnels - South loot chest": LocData(BASE_LOCATION_ID + 19, "Arcane Tunnels"),
    "Arcane Tunnels - South key chest 1": LocData(BASE_LOCATION_ID + 20, "Arcane Tunnels"),
}

# Water Ways / Stone Heart
water_ways_locations = {
    "Water Ways - Pure Shadow chest": LocData(BASE_LOCATION_ID + 21, "Water Ways"),
}
stone_heart_locations = {
    "Stone Heart - Stoneheart chest 3": LocData(BASE_LOCATION_ID + 22, "Stone Heart"),
    "Stone Heart - Stoneheart chest 1": LocData(BASE_LOCATION_ID + 23, "Stone Heart"),
    "Stone Heart - Stoneheart chest 2": LocData(BASE_LOCATION_ID + 24, "Stone Heart"),
    "Stone Heart - Stoneheart chest 4": LocData(BASE_LOCATION_ID + 25, "Stone Heart"),
    "Stone Heart - Merchants Robe chest": LocData(BASE_LOCATION_ID + 26, "Stone Heart"),
    "Stone Heart - Graveyard key chest 1": LocData(BASE_LOCATION_ID + 27, "Stone Heart"),
    "Stone Heart - Graveyard key chest 2": LocData(BASE_LOCATION_ID + 28, "Stone Heart"),
}

# Cross Roads
cross_roads_locations = {
    "Cross Roads - Crossroads loot chest 2": LocData(BASE_LOCATION_ID + 29, "Cross Roads"),
    "Cross Roads - Well crossroads loot chest 3": LocData(BASE_LOCATION_ID + 30, "Cross Roads"),
    "Cross Roads - Crossroads chest loot 1": LocData(BASE_LOCATION_ID + 31, "Cross Roads"),
    "Cross Roads - Crossroads chest loot 3": LocData(BASE_LOCATION_ID + 32, "Cross Roads"),
}

# Forest Temple - Water
forest_temple_water_locations = {
    "Forest Temple - Water - Loot chest 1": LocData(BASE_LOCATION_ID + 33, "Forest Temple - Water"),
    "Forest Temple - Water - Loot chest 2": LocData(BASE_LOCATION_ID + 34, "Forest Temple - Water"),
    "Forest Temple - Water - Key chest": LocData(BASE_LOCATION_ID + 35, "Forest Temple - Water"),
}

# Forest Temple - Ambush 1
forest_temple_ambush1_locations = {
    "Forest Temple - Ambush 1 - Key chest": LocData(BASE_LOCATION_ID + 36, "Forest Temple - Ambush 1"),
}

# Forest Temple - Ambush 2
forest_temple_ambush2_locations = {
    "Forest Temple - Ambush 2 - Key chest": LocData(BASE_LOCATION_ID + 37, "Forest Temple - Ambush 2"),
}

# Forest Temple - Nuos Claw
forest_temple_nuos_claw_locations = {
    "Forest Temple - Nuos Claw - Nuos Claw chest": LocData(BASE_LOCATION_ID + 38, "Forest Temple - Nuos Claw"),
}

# Forest Temple - Center Tree
forest_temple_center_tree_locations = {
    "Forest Temple - Center Tree - Loot chest 1": LocData(BASE_LOCATION_ID + 39, "Forest Temple - Center Tree"),
    "Forest Temple - Center Tree - Loot chest 2": LocData(BASE_LOCATION_ID + 40, "Forest Temple - Center Tree"),
    "Forest Temple - Center Tree - Loot chest 3": LocData(BASE_LOCATION_ID + 41, "Forest Temple - Center Tree"),
    "Forest Temple - Center Tree - Void chest": LocData(BASE_LOCATION_ID + 42, "Forest Temple - Center Tree"),
    "Forest Temple - Center Tree - Silverblades chest": LocData(BASE_LOCATION_ID + 43, "Forest Temple - Center Tree"),
    "Forest Temple - Center Tree - Key chest": LocData(BASE_LOCATION_ID + 44, "Forest Temple - Center Tree"),
}

# Forest Temple - Center Tree Trunk
forest_temple_center_tree_trunk_locations = {
    "Forest Temple - Center Tree Trunk - Loot chest 1": LocData(BASE_LOCATION_ID + 45, "Forest Temple - Center Tree Trunk"),
}

# Standard locations (always included)
standard_locations = {
    **fire_keep_intro_locations,
    **fire_keep_hub_locations,
    **arcane_tunnels_locations,
    **water_ways_locations,
    **stone_heart_locations,
    **cross_roads_locations,
    **forest_temple_water_locations,
    **forest_temple_ambush1_locations,
    **forest_temple_ambush2_locations,
    **forest_temple_nuos_claw_locations,
    **forest_temple_center_tree_locations,
    **forest_temple_center_tree_trunk_locations,
}

# Extra/optional locations
extra_locations = {
    #**void_locations,
}

# Combined location table
location_table = {
    **standard_locations,
    **extra_locations,
}
