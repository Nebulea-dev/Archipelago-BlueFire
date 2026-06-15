from enum import IntEnum

from BaseClasses import Tutorial, ItemClassification
from worlds.AutoWorld import World, WebWorld
from .Connections import all_connections
from .Items import (
    all_items,
    base_id,
    emote_items,
    weapon_items,
    tunic_items,
    spirit_items,
    ability_items,
    regular_items,
    key_items
)
from .Locations import all_locations, forced_locations, forced_locations_items, get_events_data
from .Options import BluefireOptions
from .Regions import all_regions
from .Rules import BluefireRules

from .Subclasses import BluefireRegion, BluefireItem


class ItemCategory(IntEnum):
    """Enum for organizing items into categories with consistent ID offsets."""
    EMOTE = 0
    WEAPON = 100
    TUNIC = 200
    SPIRIT = 300
    ABILITY = 400
    REGULAR = 500
    KEY = 600


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

    emote_item_name_to_id: dict[str, int] = {item["name"]: i for i, item in enumerate(emote_items, base_id + ItemCategory.EMOTE) if item is not None}
    weapon_item_name_to_id: dict[str, int] = {item["name"]: i for i, item in enumerate(weapon_items, base_id + ItemCategory.WEAPON) if item is not None}
    tunic_item_name_to_id: dict[str, int] = {item["name"]: i for i, item in enumerate(tunic_items, base_id + ItemCategory.TUNIC) if item is not None}
    spirit_item_name_to_id: dict[str, int] = {item["name"]: i for i, item in enumerate(spirit_items, base_id + ItemCategory.SPIRIT) if item is not None}
    ability_item_name_to_id: dict[str, int] = {item["name"]: i for i, item in enumerate(ability_items, base_id + ItemCategory.ABILITY) if item is not None}
    regular_item_name_to_id: dict[str, int] = {item["name"]: i for i, item in enumerate(regular_items, base_id + ItemCategory.REGULAR) if item is not None}
    key_item_name_to_id: dict[str, int] = {item["name"]: i for i, item in enumerate(key_items, base_id + ItemCategory.KEY) if item is not None}

    item_name_to_id: dict[str, int] = {
        **emote_item_name_to_id,
        **weapon_item_name_to_id,
        **tunic_item_name_to_id,
        **spirit_item_name_to_id,
        **ability_item_name_to_id,
        **regular_item_name_to_id,
        **key_item_name_to_id,
    }

    location_name_to_id: dict[str, int] = {name: id for id, name in enumerate(all_locations, base_id) if name not in forced_locations}


    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    item_name_groups: dict[str, set[str]] = {
        "emotes": {item["name"] for item in emote_items if item is not None},
        "weapons": {item["name"] for item in weapon_items if item is not None},
        "tunics": {item["name"] for item in tunic_items if item is not None},
        "spirits": {item["name"] for item in spirit_items if item is not None},
        "abilities": {item["name"] for item in ability_items if item is not None},
    }


    def create_item(self, name: str) -> BluefireItem:
        item_id = self.item_name_to_id[name] - base_id
        item_category = ItemCategory(item_id - (item_id % 100))
        item_data = {}

        match item_category:
            case ItemCategory.EMOTE:
                item_data = emote_items[item_id - item_category]
            case ItemCategory.WEAPON:
                item_data = weapon_items[item_id - item_category]
            case ItemCategory.TUNIC:
                item_data = tunic_items[item_id - item_category]
            case ItemCategory.SPIRIT:
                item_data = spirit_items[item_id - item_category]
            case ItemCategory.ABILITY:
                item_data = ability_items[item_id - item_category]
            case ItemCategory.REGULAR:
                item_data = regular_items[item_id - item_category]
            case ItemCategory.KEY:
                item_data = key_items[item_id - item_category]

        if not item_data:
            raise ValueError(f"Item data not found for '{name}' in category {item_category.name}")

        return BluefireItem(name, item_data["classification"], item_id, self.player)

    def create_items(self) -> None:
        nb_items_added = 0
        useful_items = all_items.copy()
        unique_fillers_items = all_items.copy()
        repeatable_fillers_items = all_items.copy()

        useful_items = [item for item in useful_items if item is not None and item["classification"] != ItemClassification.filler]
        unique_fillers_items = [item for item in unique_fillers_items if item is not None and item["classification"] == ItemClassification.filler and "repeatable" not in item]
        repeatable_fillers_items = [item for item in repeatable_fillers_items if item is not None and item["classification"] == ItemClassification.filler and "repeatable" in item]

        for item in useful_items:
            for _ in range(item["count"]):
                new_item = self.create_item(item["name"])
                self.multiworld.itempool.append(new_item)
                nb_items_added += 1

        for item in unique_fillers_items:
            for _ in range(item["count"]):
                new_item = self.create_item(item["name"])
                self.multiworld.itempool.append(new_item)
                nb_items_added += 1

        repeatable_filler_count = len(all_locations)
        repeatable_filler_count -= len(forced_locations)
        repeatable_filler_count -= nb_items_added

        for i in range(repeatable_filler_count):
            index = i % len(repeatable_fillers_items)
            filler_item = repeatable_fillers_items[index]
            new_item = self.create_item(filler_item["name"])
            self.multiworld.itempool.append(new_item)

    def create_regions(self) -> None:
        list_regions = [
            BluefireRegion(f"{parent} - {subregion}", self, parent)
            for parent, sub_regions in all_regions.items()
            for subregion in sub_regions
        ]

        for region in list_regions:
            if region.parent is not None:
                region_name = region.name.removeprefix(f"{region.parent} - ")
                connection_data = all_connections[region.parent][region_name]
                for exit_region in connection_data:
                    region.connect(self.get_region(exit_region))

            else:
                connection_data = all_connections[region.name]
                for exit_region in connection_data:
                    region.connect(self.get_region(exit_region))

        menu_region = BluefireRegion("Menu", self)
        menu_region.add_exits({"Fire Keep - Intro": "Start game"})

        # Create event locations and items
        self.create_events()

    def create_events(self) -> None:
        """Create event locations and items with id=None for all events in Locations.json."""
        from BaseClasses import Location, ItemClassification
        from .Subclasses import BluefireLocation, BluefireItem

        events_data = get_events_data()

        for region_name, subregions in events_data.items():
            for subregion_name, event_names in subregions.items():
                # Get the region object
                full_region_name = f"{region_name} - {subregion_name}"
                region = self.get_region(full_region_name)

                # Create event locations and items
                for event_name in event_names:
                    # Create event location with id=None
                    event_location = BluefireLocation(
                        self.player,
                        f"{region_name} - {subregion_name} - {event_name}",
                        None,  # id=None for event locations
                        region
                    )

                    # Create event item with id=None
                    event_item = BluefireItem(
                        event_name,
                        ItemClassification.progression,
                        None,  # id=None for event items
                        self.player
                    )

                    # Place the event item on the event location
                    event_location.place_locked_item(event_item)

                    # Add the event location to the region
                    region.locations.append(event_location)

    def set_rules(self) -> None:
        BluefireRules(self).set_bluefire_rules()
