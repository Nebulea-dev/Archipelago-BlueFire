from BaseClasses import Region, Location, ItemClassification
from .Types import BluefireLocation, BluefireItem
from .Locations import location_table, is_valid_location
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import BluefireWorld

def create_regions(world: "BluefireWorld"):
    # Create main menu region
    menu = create_region(world, "Menu")

    # Create Blue Fire game regions - major areas
    fire_keep_intro = create_region_and_connect(world, "Fire Keep - Intro", "Menu -> Fire Keep - Intro", menu)
    fire_keep_hub = create_region_and_connect(world, "Fire Keep - Hub", "Fire Keep - Intro -> Fire Keep - Hub", fire_keep_intro)
    arcane_tunnels = create_region_and_connect(world, "Arcane Tunnels", "Fire Keep - Hub -> Arcane Tunnels", fire_keep_hub)
    crossroads = create_region_and_connect(world, "Crossroads", "Arcane Tunnels -> Crossroads", arcane_tunnels)
    stoneheart_city = create_region_and_connect(world, "Stoneheart City", "Crossroads -> Stoneheart City", crossroads)
    forest_temple_water = create_region_and_connect(world, "Forest Temple - Water", "Stoneheart City -> Forest Temple - Water", stoneheart_city)
    forest_temple_ambush_1 = create_region_and_connect(world, "Forest Temple - Ambush 1", "Forest Temple - Water -> Forest Temple - Ambush 1", forest_temple_water)
    forest_temple_ambush_2 = create_region_and_connect(world, "Forest Temple - Ambush 2", "Forest Temple - Ambush 1 -> Forest Temple - Ambush 2", forest_temple_ambush_1)
    forest_temple_nuos_claw = create_region_and_connect(world, "Forest Temple - Nuos Claw", "Forest Temple - Ambush 1 -> Forest Temple - Nuos Claw", forest_temple_ambush_1)
    forest_temple_center_tree = create_region_and_connect(world, "Forest Temple - Center Tree", "Forest Temple - Water -> Forest Temple - Center Tree", forest_temple_water)


    # Place victory item
    victory = Location(world.player, "Defeat game", None, forest_temple_center_tree)
    victory.place_locked_item(BluefireItem("Victory", ItemClassification.progression, None, world.player))
    forest_temple_center_tree.locations.append(victory)

    #temple_gardens = create_region_and_connect(world, "Temple Gardens", "Stoneheart City -> Temple Gardens", stoneheart_city)
    #abandoned_path = create_region_and_connect(world, "Abandoned Path", "Stoneheart City -> Abandoned Path", stoneheart_city)
    #uthas_temple = create_region_and_connect(world, "Uthas Temple", "Abandoned Path -> Uthas Temple", abandoned_path)
    #temple_of_gods = create_region_and_connect(world, "Temple of Gods", "Temple Gardens -> Temple of Gods", temple_gardens)
    #firefall_river = create_region_and_connect(world, "Firefall River", "Arcane Tunnels -> Firefall River", arcane_tunnels)
    #steam_house = create_region_and_connect(world, "Steam House", "Firefall River -> Steam House", firefall_river)
    #iron_caves = create_region_and_connect(world, "Iron Caves", "Steam House -> Iron Caves", steam_house)
    #waterway = create_region_and_connect(world, "Waterway", "Arcane Tunnels -> Waterway", arcane_tunnels)
    #void_challenges = create_region_and_connect(world, "Void Challenges", "Arcane Tunnels -> Void Challenges", arcane_tunnels)

    # Create alternate connections for shortcuts/non-linear access
    #firefall_river.connect(iron_caves, "Firefall River -> Iron Caves (alternate)")
    #waterway.connect(firefall_river, "Waterway -> Firefall River")

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