from BaseClasses import MultiWorld, Item, Tutorial
from worlds.AutoWorld import World, CollectionState, WebWorld
from typing import Dict

from .Locations import get_location_names, get_total_locations
from .Items import create_item, create_itempool, item_table
from .Options import BluefireOptions
from .Regions import create_regions
from .Rules import set_rules
from .Types import StartingLocation, starting_location_to_name


class BluefireWeb(WebWorld):
    theme = "Party"

    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Blue Fire for Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["ArchipelagoTeam"]
    )]


class BluefireWorld(World):
    """
    Blue Fire is a soulslike exploration platformer featuring a fast-paced combat system,
    challenging boss fights, and an intricate world to explore.
    """

    game = "Blue Fire"
    item_name_to_id = {name: data.ap_code for name, data in item_table.items()}
    location_name_to_id = get_location_names()
    options_dataclass = BluefireOptions
    web = BluefireWeb()

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def generate_early(self):
        pass

    def create_regions(self):
        create_regions(self)

    def create_items(self):
        self.multiworld.itempool += create_itempool(self)

    def create_item(self, name: str) -> Item:
        return create_item(self, name)

    def set_rules(self):
        set_rules(self)

    def fill_slot_data(self) -> Dict[str, object]:
        slot_data: Dict[str, object] = {
            "options": {
                "ExtraLocations":          self.options.ExtraLocations.value,
                "TrapChance":              self.options.TrapChance.value,
                "SpeedChangeTrapWeight":   self.options.SpeedChangeTrapWeight.value
            },
            "Seed": self.multiworld.seed_name,
            "Slot": self.multiworld.player_name[self.player],
            "TotalLocations": get_total_locations(self)
        }
        return slot_data

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        change = super().collect(state, item)
        if change and "Old Key" in item.name:
            state.prog_items[item.player]["key"] += 1
        return change


    def remove(self, state: "CollectionState", item: "Item") -> bool:
        change = super().collect(state, item)
        if change and "Old Key" in item.name:
            state.prog_items[item.player]["key"] -= 1
        return change