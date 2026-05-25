from typing import List, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, Range

def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in bluefire_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))
    return option_group_list

class ExtraLocations(Toggle):
    """
    Include void challenge locations in the seed.
    These are optional end-game content.
    """
    display_name = "Include Void Challenges"
    default = 1

class TrapChance(Range):
    """
    Percentage chance for any filler item to become a trap.
    Set to 0 for no traps.
    """
    display_name = "Trap Chance (%)"
    range_start = 0
    range_end = 100
    default = 0

class SpeedChangeTrapWeight(Range):
    """
    Weight of speed change traps in the trap pool.
    """
    display_name = "Speed Change Trap Weight"
    range_start = 0
    range_end = 100
    default = 25

@dataclass
class BluefireOptions(PerGameCommonOptions):
    ExtraLocations:             ExtraLocations
    TrapChance:                 TrapChance
    SpeedChangeTrapWeight:      SpeedChangeTrapWeight

bluefire_option_groups: Dict[str, List[Any]] = {
    "General Options": [ExtraLocations],
    "Trap Options": [TrapChance, SpeedChangeTrapWeight]
}