from typing import Dict, TYPE_CHECKING
from worlds.generic.Rules import add_rule

if TYPE_CHECKING:
    from . import BluefireWorld
else:
    BluefireWorld = object

from BaseClasses import CollectionState, CollectionRule


class BluefireRules:
    player: int
    world: BluefireWorld
    connection_rules: Dict[str, CollectionRule]

    def __init__(self, world: BluefireWorld) -> None:
        self.player = world.player
        self.world = world

        self.connection_rules = {
            "Fire Keep - Intro -> Fire Keep - Hub": lambda state: state.has("Old Key", self.player, 1),
            "Forest Temple - Water -> Forest Temple - Ambush 1": lambda state: state.has("Old Key", self.player, 2),
            "Forest Temple - Ambush 1 -> Forest Temple - Ambush 2": lambda state: state.has("Old Key", self.player, 3),
            "Forest Temple - Ambush 1 -> Forest Temple - Nuos Claw": lambda state: state.has("Old Key", self.player, 4),
            "Forest Temple - Water -> Forest Temple - Center Tree": lambda state: state.has("Old Key", self.player, 5),
            "Stoneheart City - Main Area -> Abandoned Path - Entrance": lambda state: state.has("Graveyard Key", self.player, 1) and state.has("Wall Run Ability", self.player, 1),
        }

    # Set all rules in the multiworld
    def set_bluefire_rules(self) -> None:
        multiworld = self.world.multiworld

        for entrance_name, rule in self.connection_rules.items():
            entrance = multiworld.get_entrance(entrance_name, self.player)
            add_rule(entrance, rule)

        multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
