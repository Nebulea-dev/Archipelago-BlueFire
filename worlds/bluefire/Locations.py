from typing import Dict, List, TYPE_CHECKING, Any
import pkgutil
import yaml
import os

# Load locations from the unified YAML file
def _load_locations_yaml() -> Dict[str, Any]:
    yaml_data = pkgutil.get_data(__name__, "Locations.yaml")
    return yaml.safe_load(yaml_data)

_locations_data: Dict[str, Any] = _load_locations_yaml()

# Generate location IDs incrementally and build location name to ID mapping
_location_id_counter: int = 0
_location_name_to_id: Dict[str, int] = {}
upgrade_current_count: int = 0

# Convert JSON to the original format for backward compatibility
regions_to_locations: Dict[str, Dict[str, List[str]]] = {}

location_types: List[str] = ["chests", "statues", "pickups", "void_gates", "shops", "mana_upgrades"]

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
            elif location_type == "mana_upgrades":
                # For mana upgrades, each upgrade creates a separate location
                for upgrade in subregion.get("mana_upgrades", []):
                    upgrade_count = upgrade["number"]
                    for _ in range(upgrade_count):
                        loc_name = f"Mana Upgrade {upgrade_current_count + 1}"
                        upgrade_current_count += 1
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

# Parse events data structure for world generation (events have id=None, not regular IDs)
def get_events_data() -> Dict[str, Dict[str, List[Dict[str, Any]]]]:
    """
    Returns a dict mapping region names to dicts mapping subregion names to lists of event objects.
    Each event object contains 'name' and 'requiredItems' fields.
    Events are NOT included in the regular location mapping and will be created with id=None.
    """
    events_data = {}
    for region in _locations_data.get("regions", []):
        region_name = region["name"]
        events_data[region_name] = {}
        for subregion in region.get("subregions", []):
            subregion_name = subregion["name"]
            raw_events = subregion.get("events", [])
            if raw_events:
                # Normalize events to always be objects with 'name' and 'requiredItems'
                normalized_events = []
                for event in raw_events:
                    if isinstance(event, str):
                        # Handle legacy string format for backward compatibility
                        normalized_events.append({
                            "name": event,
                            "requiredItems": []
                        })
                    else:
                        # Handle new object format
                        normalized_events.append({
                            "name": event.get("name", ""),
                            "requiredItems": event.get("requiredItems", [])
                        })
                events_data[region_name][subregion_name] = normalized_events
    return events_data
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