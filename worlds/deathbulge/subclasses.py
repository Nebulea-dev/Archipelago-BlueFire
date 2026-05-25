from typing import Dict, List, TypedDict, TYPE_CHECKING
from BaseClasses import Region, Location, Item, ItemClassification
from .locations import regions_to_locations, forced_locations, forced_locations_items
from .items import boss_lock_items

if TYPE_CHECKING:
    from . import DeathbulgeWorld


class DeathbulgeRegion(Region):
    parent: str | None

    def __init__(self, name: str, world: "DeathbulgeWorld", parent: str | None = None) -> None:
        super().__init__(name, world.player, world.multiworld)
        self.parent = parent
        locations = []
        if parent in regions_to_locations:
            subregions_to_locations = regions_to_locations[parent]
            region_name = name.removeprefix(f"{parent} - ")
            if region_name in subregions_to_locations:
                locations = [location for location in subregions_to_locations[region_name]]
        loc_dict = {location: world.location_name_to_id.get(location, None) for location in locations}
        self.add_locations(loc_dict, DeathbulgeLocation)

        self.multiworld.regions.append(self)


class DeathbulgeItem(Item):
    name: str = "Deathbulge"


class ItemDict(TypedDict):
    name: str
    count: int
    classification: ItemClassification


class DeathbulgeLocation(Location):
    game: str = "Deathbulge"

    def __init__(self, player: int, name: str, loc_id: int | None, parent: DeathbulgeRegion) -> None:
        super().__init__(player, name, loc_id, parent)
        if name in forced_locations:
            self.place_locked_item(
                DeathbulgeItem(forced_locations_items[name], ItemClassification.progression, None, parent.player)
            )
