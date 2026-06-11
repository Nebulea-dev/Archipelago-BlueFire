from typing import Dict, List, Any
import json
import os

# Load regions from the unified JSON file
def _load_locations_json() -> Dict[str, Any]:
    json_path = os.path.join(os.path.dirname(__file__), "locations.json")
    with open(json_path, 'r') as f:
        return json.load(f)

_locations_data: Dict[str, Any] = _load_locations_json()

# Dynamically generate all_regions from locations.json
# Structure: regions[region_name] = [subregion_name, ...]
all_regions: Dict[str, List[str]] = {}

for region in _locations_data.get("regions", []):
    region_name = region["name"]
    subregion_names = [subregion["name"] for subregion in region.get("subregions", [])]
    all_regions[region_name] = subregion_names