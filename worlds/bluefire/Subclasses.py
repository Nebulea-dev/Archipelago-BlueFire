from typing import Dict, List, TypedDict, TYPE_CHECKING
from BaseClasses import Region, Location, Item, ItemClassification
from .Locations import regions_to_locations, forced_locations, forced_locations_items, dance_locations
from .Rules import chest_dance_rules

if TYPE_CHECKING:
    from . import BluefireWorld


class BluefireRegion(Region):
    parent: str | None

    def __init__(self, name: str, world: "BluefireWorld", parent: str | None = None) -> None:
        super().__init__(name, world.player, world.multiworld)
        self.parent = parent
        locations = []
        if parent in regions_to_locations:
            subregions_to_locations = regions_to_locations[parent]
            region_name = name.removeprefix(f"{parent} - ")
            if region_name in subregions_to_locations:
                locations = [f"{parent} - {region_name} - {location}" for location in subregions_to_locations[region_name]]

        else:
            locations = [f"{name} - {location}" for location in regions_to_locations[name]]

        loc_dict = {location: world.location_name_to_id.get(location, None) for location in locations}

        self.add_locations(loc_dict, BluefireLocation)

        self.multiworld.regions.append(self)


class BluefireItem(Item):
    name: str = "Blue Fire"


class ItemDict(TypedDict):
    name: str
    count: int
    classification: ItemClassification


class BluefireLocation(Location):
    game: str = "Blue Fire"

    def __init__(self, player: int, name: str, loc_id: int | None, parent: BluefireRegion) -> None:
        super().__init__(player, name, loc_id, parent)
        if name in forced_locations:
            self.place_locked_item(
                BluefireItem(forced_locations_items[name], ItemClassification.progression, None, parent.player)
            )

        if name in dance_locations:
            chest_dance_rules.append((self, dance_locations[name]))
