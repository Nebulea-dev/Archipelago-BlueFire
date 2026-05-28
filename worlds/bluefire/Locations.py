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

for region in _locations_data["regions"]:
    region_name = region["name"]

    if region["subregions"]:
        # Region has subregions
        regions_to_locations[region_name] = {}
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
            regions_to_locations[region_name][subregion_name] = locations
    else:
        # Region has no subregions
        locations = []
        for loc in region["locations"]:
            loc_name = loc["name"]
            locations.append(loc_name)
            # Store the full location path and its ID
            full_path = f"{region_name} - {loc_name}"
            _location_name_to_id[full_path] = _location_id_counter
            _location_id_counter += 1
        regions_to_locations[region_name] = locations


regions_with_subregions = [
    f"{region} - {subregion} - {location}"
    for region, subregions in regions_to_locations.items()
    if isinstance(subregions, dict)
    for subregion, locations in subregions.items()
    for location in locations
]

regions_without_subregions = [
    f"{region} - {location}"
    for region, locations in regions_to_locations.items()
    if isinstance(locations, list)
    for location in locations
]


all_locations : List[str] = (
    regions_with_subregions
    + regions_without_subregions
)


forced_locations_items: Dict[str, str] = {
    "Victory - Victory": "Victory",
}

forced_locations = [location for location, item in forced_locations_items.items()]


def get_location_id(location_name: str) -> int:
    """
    Get the location ID for a given location name.

    Args:
        location_name: Full location path (e.g., "Fire Keep - Hub - Loot chest 1")

    Returns:
        The location ID (0-based index)
    """
    return _location_name_to_id.get(location_name, -1)
