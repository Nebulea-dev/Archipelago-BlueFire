from typing import Dict, List, TYPE_CHECKING
import json
import os

# Load locations from the unified JSON file
def _load_locations_json():
    json_path = os.path.join(os.path.dirname(__file__), "locations.json")
    with open(json_path, 'r') as f:
        return json.load(f)

_locations_data = _load_locations_json()

# Generate location IDs incrementally and build location name to ID mapping
_location_id_counter = 0
_location_name_to_id: Dict[str, int] = {}

# Convert JSON to the original format for backward compatibility
regions_to_locations: Dict[str, Dict[str, List[str]] | List[str]] = {}

location_types: List[str] = ["chests", "statues", "pickups", "void_gates"]

for location_type in location_types:
    for region in _locations_data[location_type]:
        region_name = region["region"]

        if region_name not in regions_to_locations:
            regions_to_locations[region_name] = {}

        # Region has subregions
        if "subregions" in region:
            for subregion in region["subregions"]:
                subregion_name = subregion["name"]

                locations = []
                for loc in subregion["locations"]:
                    loc_name = loc["name"]
                    locations.append(loc_name)
                    # Store the full location path and its ID
                    full_path = f"{region_name} - {subregion_name} - {loc_name}"
                    _location_name_to_id[full_path] = _location_id_counter
                    _location_id_counter += 1

                if subregion_name not in regions_to_locations[region_name]:
                    regions_to_locations[region_name][subregion_name] = locations
                else:
                    regions_to_locations[region_name][subregion_name] += locations


forced_locations_items: Dict[str, str] = {
    "Victory - Victory - Victory": "Victory",
}
forced_locations = [location for location, item in forced_locations_items.items()]


all_locations = [
    f"{region} - {subregion} - {location}"
    for region, subregions in regions_to_locations.items()
    if isinstance(subregions, dict)
    for subregion, locations in subregions.items()
    for location in locations
]


def get_location_id(location_name: str) -> int:
    """
    Get the location ID for a given location name.

    Args:
        location_name: Full location path (e.g., "Fire Keep - Hub - Loot chest 1")

    Returns:
        The location ID (0-based index)
    """
    return _location_name_to_id.get(location_name, -1)
