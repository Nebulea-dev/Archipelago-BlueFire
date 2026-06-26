from typing import Dict, List, Any
import pkgutil
import yaml
import os

# Load locations from the unified YAML file
def _load_locations_yaml() -> Dict[str, Any]:
    yaml_data = pkgutil.get_data(__name__, "Locations.yaml")
    return yaml.safe_load(yaml_data)

_locations_data: Dict[str, Any] = _load_locations_yaml()

# Dynamically generate all_regions from locations.json
# Structure: regions[region_name] = [subregion_name, ...]
all_regions: Dict[str, List[str]] = {}

for region in _locations_data.get("regions", []):
    region_name = region["name"]
    subregion_names = [subregion["name"] for subregion in region.get("subregions", [])]
    all_regions[region_name] = subregion_names