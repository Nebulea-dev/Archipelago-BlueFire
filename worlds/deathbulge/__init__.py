from BaseClasses import Tutorial, ItemClassification, Region
from worlds.AutoWorld import World, CollectionState, WebWorld
from .connections import all_connections
from .items import (
    all_items,
    base_id,
    emote_items,
    weapon_items,
    tunic_items,
    spirit_items,
    ores_items,
    real_fillers_items,
)
from .locations import all_locations, forced_locations
from .options import DeathbulgeOptions
from .regions import all_regions
from .rules import DeathbulgeRules

from .subclasses import DeathbulgeRegion, DeathbulgeItem


class BluefireWeb(WebWorld):
    theme = "Party"

    bug_report_page = "https://github.com/Nebulea-dev/Archipelago-BlueFire/issues"

    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Blue Fire for Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Nebulea"]
    )]


class BluefireWorld(World):
    """
    Blue Fire is a soulslike exploration platformer featuring a fast-paced combat system,
    challenging boss fights, and an intricate world to explore.
    """

    game = "Blue Fire"
    options_dataclass = BluefireOptions  # options the player can set
    options: BluefireOptions  # typing hints for option results
    topology_present = True  # show path to required location checks in spoiler

    # The following two dicts are required for the generation to know which items exist.
    # They can be generated with arbitrary code during world load, but keep in mind that
    # anything expensive (e.g. parsing non-python data files) will delay world loading.
    # They can include events, but don't have to since events will be placed manually.

    item_name_to_id = {item["name"]: i + base_id for i, item in enumerate(all_items)}

    location_name_to_id = {name: id for id, name in enumerate(all_locations, base_id) if name not in forced_locations}

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups = {
        "emotes": {item["name"] for item in emote_items},
        "weapons": {item["name"] for item in weapon_items},
        "tunics": {item["name"] for item in tunic_items},
        "spirits": {item["name"] for item in spirit_items},
        "ores": {item["name"] for item in ores_items},
        "abilities": {item["name"] for item in ability_items},
    }


    def create_item(self, name: str) -> BluefireItem:
        item_id = self.item_name_to_id[name]
        item_data = all_items[item_id - base_id]
        return BluefireItem(name, item_data["classification"], item_id, self.player)

    def create_items(self) -> None:
        nb_items_added = 0
        useful_items = all_items.copy()

        useful_items = [item for item in useful_items if item["classification"] != ItemClassification.filler]

        for item in useful_items:
            for _ in range(item["count"]):
                new_item = self.create_item(item["name"])
                self.multiworld.itempool.append(new_item)
                nb_items_added += 1

        filler_count = len(all_locations)
        filler_count -= len(forced_locations)
        filler_count -= nb_items_added

        # TODO : why not add them randomized
        # Right now the bottom fillers will never be added
        for i in range(filler_count):
            index = i % len(real_fillers_items)
            filler_item = real_fillers_items[index]
            new_item = self.create_item(filler_item["name"])
            self.multiworld.itempool.append(new_item)

    def create_regions(self) -> None:
        list_regions = [
            BluefireRegion(f"{parent} - {subregion}", self, parent)
            for parent, sub_regions in all_regions.items()
            for subregion in sub_regions
        ]

        for region in list_regions:
            region_name = region.name.removeprefix(f"{region.parent} - ")
            connection_data = all_connections[region.parent][region_name]
            for exit_region in connection_data:
                region.connect(self.get_region(exit_region))

        menu_region = BluefireRegion("Menu", self)
        menu_region.add_exits({"Dream - Intro01": "Start game"})

    def set_rules(self) -> None:
        BluefireRules(self).set_bluefire_rules()
