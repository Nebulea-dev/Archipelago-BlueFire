from enum import IntEnum
from typing import NamedTuple, Optional
from BaseClasses import Location, Item, ItemClassification

# These 2 make it so that the generic Location and Item types are more specific for your game
class BluefireLocation(Location):
    game = "Blue Fire"

class BluefireItem(Item):
    game = "Blue Fire"

# Starting location enum for player choice
class StartingLocation(IntEnum):
    Lab = 1
    Crossroads = 2
    FirekeepWest = 3

starting_location_to_name = {
    StartingLocation.Lab:        "Fire Keep - Lab",
    StartingLocation.Crossroads: "Crossroads",
    StartingLocation.FirekeepWest: "Fire Keep - Crates"
}

# Here is where all the stuff from the Items.py comes from
# You can add or take away anything you want but ap_code and classification are pretty important
# Adding Optional[] makes it so you dont have to include it when you create an ItemData
# Adding = x at the end adds a default to it so if you dont include it, it'll default to whatever you put after it
class ItemData(NamedTuple):
    ap_code: Optional[int]
    classification: ItemClassification
    count: Optional[int] = 1

# Again where all the Location.py things come from
# You can add whatever you want here as well but ap_code and region are pretty important
class LocData(NamedTuple):
    ap_code: Optional[int]
    region: Optional[str]