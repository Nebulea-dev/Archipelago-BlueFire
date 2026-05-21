from BaseClasses import Region
from .Types import BluefireLocation
from .Locations import location_table, is_valid_location
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import BluefireWorld

def create_regions(world: "BluefireWorld"):
    # Create main menu region
    menu = create_region(world, "Menu")

    # Create Blue Fire game regions - major areas
    fire_keep = create_region_and_connect(world, "Fire Keep", "Menu -> Fire Keep", menu)
    arcane_tunnels = create_region_and_connect(world, "Arcane Tunnels", "Menu -> Arcane Tunnels", menu)
    crossroads = create_region_and_connect(world, "Crossroads", "Fire Keep -> Crossroads", fire_keep)
    stoneheart_city = create_region_and_connect(world, "Stoneheart City", "Crossroads -> Stoneheart City", crossroads)
    forest_temple = create_region_and_connect(world, "Forest Temple", "Stoneheart City -> Forest Temple", stoneheart_city)
    temple_gardens = create_region_and_connect(world, "Temple Gardens", "Stoneheart City -> Temple Gardens", stoneheart_city)
    abandoned_path = create_region_and_connect(world, "Abandoned Path", "Stoneheart City -> Abandoned Path", stoneheart_city)
    uthas_temple = create_region_and_connect(world, "Uthas Temple", "Abandoned Path -> Uthas Temple", abandoned_path)
    temple_of_gods = create_region_and_connect(world, "Temple of Gods", "Temple Gardens -> Temple of Gods", temple_gardens)
    firefall_river = create_region_and_connect(world, "Firefall River", "Arcane Tunnels -> Firefall River", arcane_tunnels)
    steam_house = create_region_and_connect(world, "Steam House", "Firefall River -> Steam House", firefall_river)
    iron_caves = create_region_and_connect(world, "Iron Caves", "Steam House -> Iron Caves", steam_house)
    waterway = create_region_and_connect(world, "Waterway", "Arcane Tunnels -> Waterway", arcane_tunnels)
    void_challenges = create_region_and_connect(world, "Void Challenges", "Arcane Tunnels -> Void Challenges", arcane_tunnels)

    # Create alternate connections for shortcuts/non-linear access
    firefall_river.connect(iron_caves, "Firefall River -> Iron Caves (alternate)")
    waterway.connect(firefall_river, "Waterway -> Firefall River")

def create_region(world: "BluefireWorld", name: str) -> Region:
    reg = Region(name, world.player, world.multiworld)

    # Add all locations belonging to this region
    for (key, data) in location_table.items():
        if data.region == name:
            if not is_valid_location(world, key):
                continue
            location = BluefireLocation(world.player, key, data.ap_code, reg)
            reg.locations.append(location)

    world.multiworld.regions.append(reg)
    return reg

def create_region_and_connect(world: "BluefireWorld",
                               name: str, entrance_name: str, connected_region: Region) -> Region:
    reg: Region = create_region(world, name)
    connected_region.connect(reg, entrance_name)
    return reg