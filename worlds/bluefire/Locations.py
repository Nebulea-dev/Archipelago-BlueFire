from typing import Dict, List, TYPE_CHECKING, Any, Tuple
import json
import os

# Load locations from the unified JSON file
def _load_locations_json() -> Dict[str, Any]:
    json_path = os.path.join(os.path.dirname(__file__), "locations.json")
    with open(json_path, 'r') as f:
        return json.load(f)

_locations_data: Dict[str, Any] = _load_locations_json()

# Generate location IDs incrementally and build location name to ID mapping
_location_id_counter: int = 0
_location_name_to_id: Dict[str, int] = {}

# Convert JSON to the original format for backward compatibility
regions_to_locations: Dict[str, Dict[str, List[str]]] = {}

location_types: List[str] = ["chests", "statues", "pickups", "void_gates", "shops"]

# Map out the locations that need a dance as a rule
dance_locations: Dict[str, str] = {}

# NEW STRUCTURE: Region-first hierarchy
# Iterate: regions -> subregions -> location_types -> locations
for region in _locations_data.get("regions", []):
    region_name = region["name"]

    if region_name not in regions_to_locations:
        regions_to_locations[region_name] = {}

    # Process each subregion
    for subregion in region.get("subregions", []):
        subregion_name = subregion["name"]

        locations = []

        # Process each location type within the subregion
        for location_type in location_types:
            if location_type == "shops":
                # For shops, each item in the shop creates a separate location
                for shop in subregion.get("shops", []):
                    shop_name = shop["name"]
                    num_items = shop.get("items", 1)
                    # Create a location for each shop item
                    for item_idx in range(num_items):
                        loc_name = f"{shop_name} - Item {item_idx + 1}"
                        locations.append(loc_name)
                        # Store the full location path and its ID
                        full_path = f"{region_name} - {subregion_name} - {loc_name}"
                        _location_name_to_id[full_path] = _location_id_counter
                        _location_id_counter += 1
            else:
                # Regular location types
                for loc in subregion.get(location_type, []):
                    loc_name = loc["name"]
                    locations.append(loc_name)
                    # Store the full location path and its ID
                    full_path = f"{region_name} - {subregion_name} - {loc_name}"
                    _location_name_to_id[full_path] = _location_id_counter
                    _location_id_counter += 1

                    # Check for dance property (only on chests)
                    if location_type == "chests" and "dance" in loc:
                        dance_locations[full_path] = loc["dance"]

        if subregion_name not in regions_to_locations[region_name]:
            regions_to_locations[region_name][subregion_name] = locations
        else:
            regions_to_locations[region_name][subregion_name] += locations


forced_locations_items: Dict[str, str] = {
    "Victory - Victory - Victory": "Victory",
}
forced_locations: List[str] = [location for location, _ in forced_locations_items.items()]


all_locations: List[str] = [
    f"{region} - {subregion} - {location}"
    for region, subregions in regions_to_locations.items()
    if isinstance(subregions, dict)
    for subregion, locations in subregions.items()
    for location in locations
]

def get_location_id(location_name: str) -> int:
    if location_name not in _location_name_to_id:
        raise ValueError(f"Location '{location_name}' not found in location mapping")
    return _location_name_to_id[location_name]