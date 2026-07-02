from dataclasses import dataclass
from Options import Toggle, Range, Choice, PerGameCommonOptions

"""
class StartWithFastTravel(Toggle):

    display_name = "Start with fast Travel"  # this is the option name as it's displayed to the user on the webhost and in the spoiler log


class TeamStart(Choice):

    display_name = "Team start"
    option_faye = 0
    option_ian = 1
    option_briff = 2
    alias_faye_and_ian = 1
    alias_all = 2
    default = 0


class StartingMoney(Range):

    display_name = "Stating money"
    range_start = 0
    range_end = 10000
    default = 0
"""


class ProgressivePouches(Toggle):
    """Enable progressive pouch upgrades. When enabled, pouches are a progressive item in the item pool.
    When disabled, pouches are added as separate items like before."""

    display_name = "Progressive Pouches"
    default = 1


@dataclass
class BluefireOptions(PerGameCommonOptions):
    progressive_pouches: ProgressivePouches
