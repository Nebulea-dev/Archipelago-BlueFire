from typing import Dict, List, Any
import yaml
import os

# Load regions from the unified YAML file
def _load_locations_yaml() -> Dict[str, Any]:
    yaml_path = os.path.join(os.path.dirname(__file__), "Locations.yaml")
    with open(yaml_path, 'r') as f:
        return yaml.safe_load(f)

_locations_data: Dict[str, Any] = _load_locations_yaml()

# Dynamically generate all_regions from locations.json
# Structure: regions[region_name] = [subregion_name, ...]
all_regions: Dict[str, List[str]] = {}

for region in _locations_data.get("regions", []):
    region_name = region["name"]
    subregion_names = [subregion["name"] for subregion in region.get("subregions", [])]
    all_regions[region_name] = subregion_names