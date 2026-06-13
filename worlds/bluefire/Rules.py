from typing import Dict, List, Tuple, TYPE_CHECKING
from worlds.generic.Rules import add_rule

if TYPE_CHECKING:
    from . import BluefireWorld
    from .Subclasses import BluefireLocation
else:
    BluefireWorld = object

from BaseClasses import CollectionState, CollectionRule

chest_dance_rules: List[Tuple["BluefireLocation", str]] = []

class BluefireRules:
    player: int
    world: BluefireWorld
    connection_rules: Dict[str, CollectionRule]

    def __init__(self, world: BluefireWorld) -> None:
        self.player = world.player
        self.world = world

        self.connection_rules = {
            # Fire Keep
            "Fire Keep - Intro -> Fire Keep - Hub": lambda state: state.has("Old Key", self.player, 1),
            "Fire Keep - Intro -> Fire Keep - High Spot": self.hasDoubleJump or self.hasWallClimb or self.hasSpinAttack,
            "Fire Keep - High Spot -> Fire Keep - Intro": lambda state: True,
            "Fire Keep - Hub -> Fire Keep - Intro": lambda state: True,
            "Fire Keep - Hub -> Arcane Tunnels - Main Room": lambda state: True,

            # Arcane Tunnels
            "Arcane Tunnels - Main Room -> Fire Keep - Hub": True,
            "Arcane Tunnels - Main Room -> Arcane Tunnels - Pipes": self.hasDoubleJump and self.hasWallClimb and self.hasSpinAttack,
            "Arcane Tunnels - Main Room -> Arcane Tunnels - Center Top": self.hasWallClimb and (self.hasDoubleJump or self.hasSpinAttack),
            "Arcane Tunnels - Main Room -> Crossroads - Main Area": lambda state: True,
            "Arcane Tunnels - Pipes -> Arcane Tunnels - Main Room": lambda state: True,
            "Arcane Tunnels - Center Top -> Arcane Tunnels - Main Room": lambda state: True,

            # Crossroads
            "Crossroads - Main Area -> Arcane Tunnels - Main Room": lambda state: True,
            "Crossroads - Main Area -> Crossroads - Left Area": self.hasWallClimb,
            "Crossroads - Main Area -> Stoneheart City - Main Area": lambda state: True,
            "Crossroads - Left Area -> Crossroads - Main Area": self.hasWallClimb,

            # Stoneheart City
            "Stoneheart City - Main Area -> Crossroads - Main Area": True,
            "Stoneheart City - Main Area -> Stoneheart City - Top": self.hasWallClimb and (self.hasDoubleJump or self.hasSpinAttack),
            "Stoneheart City - Main Area -> Stoneheart City - Boy's Room": lambda state: state.has("Old Key", self.player, 1),
            "Stoneheart City - Main Area -> Stoneheart City - Bottom Corridor": self.hasWallClimb,
            "Stoneheart City - Main Area -> Forest Temple - High Level": lambda state: True, # TODO : add lever event
            "Stoneheart City - Main Area -> Abandoned Path - Entrance": lambda state: state.has("Graveyard Key", self.player, 1) and self.hasWallClimb,
            "Stoneheart City - Main Area -> Water Ways - Stoneheart Entrance": lambda state: True,
            "Stoneheart City - Top -> Stoneheart City - Main Area": lambda state: True,
            "Stoneheart City - Boy's Room -> Stoneheart City - Main Area": lambda state: True,
            "Stoneheart City - Bottom Corridor -> Stoneheart City - Main Area": lambda state: self.hasWallClimb,

            # Water Ways
            "Water Ways - Stoneheart Entrance -> Stoneheart City - Main Area": lambda state: True,
            "Water Ways - Stoneheart Entrance -> Water Ways - Main Area": lambda state: True,
            "Water Ways - Main Area -> Water Ways - Stoneheart Entrance": lambda state: True,
            "Water Ways - Main Area -> Arcane Tunnels - Pipes": lambda state: True,
            "Water Ways - Main Area -> Abandoned Path - Entrance": lambda state: True,
            "Water Ways - Main Area -> Firefall River - Main Area": lambda state: True,

            # Forest Temple
            "Forest Temple - High Level -> Stoneheart City - Main Area": lambda state: True,
            "Forest Temple - High Level -> Forest Temple - Middle Level": lambda state: True, # TODO : add lever event
            "Forest Temple - Middle Level -> Forest Temple - High Level": lambda state: True,
            "Forest Temple - Middle Level -> Forest Temple - Low Level": lambda state: self.hasWallClimb, # TODO : add lever event
            "Forest Temple - Middle Level -> Forest Temple - Ambush 1": lambda state: state.has("Old Key", self.player, 2),
            "Forest Temple - Low Level -> Forest Temple - Middle Level": lambda state: True,
            "Forest Temple - Low Level -> Forest Temple - Center Room Trunk": lambda state: self.hasWallClimb,  # TODO : add lever event
            "Forest Temple - Ambush 1 -> Forest Temple - Middle Level": lambda state: True,
            "Forest Temple - Ambush 1 -> Forest Temple - Ambush 2": lambda state: state.has("Old Key", self.player, 3),
            "Forest Temple - Ambush 1 -> Forest Temple - Nuos Claw": lambda state: state.has("Rare Key", self.player, 1),
            "Forest Temple - Ambush 2 -> Forest Temple - Ambush 1": lambda state: True,
            "Forest Temple - Nuos Claw -> Forest Temple - Ambush 1": lambda state: True,
            "Forest Temple - Center Room Trunk -> Forest Temple - Low Level": lambda state: True,

            # Abandoned Path
            "Abandoned Path - Entrance -> Stoneheart City - Main Area": lambda state: True,
            "Abandoned Path - Entrance -> Abandoned Path - Main Room": lambda state: self.hasWallClimb or self.hasDoubleJump or self.hasSpinAttack,
            "Abandoned Path - Main Room -> Abandoned Path - Entrance": lambda state: self.hasWallClimb or self.hasDoubleJump or self.hasSpinAttack,
            "Abandoned Path - Main Room -> Abandoned Path - Heights": lambda state: self.hasWallClimb,
            "Abandoned Path - Main Room -> Abandoned Path - Entrance Ravin": lambda state: self.hasDoubleJump or self.hasSpinAttack,
            "Abandoned Path - Main Room -> Abandoned Path - Graveyard Balcony": lambda state: self.hasWallClimb or self.hasDoubleJump or self.hasSpinAttack,
            "Abandoned Path - Heights -> Abandoned Path - Beira's Room": lambda state: True,
            "Abandoned Path - Main Room -> Uthas Temple - Entrance": lambda state: state.has("Key Uthas Temple", self.player, 1),
            "Abandoned Path - Entrance Ravin -> Abandoned Path - Main Room": lambda state: self.hasDoubleJump or self.hasSpinAttack,
            "Abandoned Path - Graveyard Balcony -> Abandoned Path - Main Room": lambda state: self.hasWallClimb or self.hasDoubleJump or self.hasSpinAttack,
            "Abandoned Path - Graveyard Balcony -> Water Ways - Main Area": self.hasWallClimb or self.hasDoubleJump or self.hasSpinAttack,
            "Abandoned Path - Graveyard Balcony -> Temple Gardens - Entrance": lambda state: True,
            "Abandoned Path - Heights -> Abandoned Path - Main Room": lambda state: True,
            "Abandoned Path - Main Room -> Abandoned Path - End of Main Room": lambda state: True, # TODO : Need spirits to go here
            "Abandoned Path - Beira's Room -> Abandoned Path - Heights": lambda state: True,
            "Abandoned Path - End of Main Room -> Abandoned Path - Main Room": lambda state: self.hasWallClimb and self.hasDoubleJump and self.hasSpinAttack, # TODO : Need spirits to go here

            # Uthas Temple
            "Uthas Temple - Entrance -> Abandoned Path - Entrance": lambda state: True,
            "Uthas Temple - Entrance -> Uthas Temple - Main Room": lambda state: True,
            "Uthas Temple - Entrance -> Uthas Temple - Top of Entrance": lambda state: True,
            "Uthas Temple - Top of Entrance -> Uthas Temple - Entrance": lambda state: True,
            "Uthas Temple - Main Room -> Uthas Temple - Entrance": lambda state: True,
            "Uthas Temple - Main Room -> Uthas Temple - Ambush Room": lambda state: True,
            "Uthas Temple - Main Room -> Uthas Temple - Holy Tower Chest": lambda state: True,
            "Uthas Temple - Main Room -> Uthas Temple - Main Room 2nd side": lambda state: True,
            "Uthas Temple - Ambush Room -> Uthas Temple - Main Room": lambda state: True,
            "Uthas Temple - Holy Tower Chest -> Uthas Temple - Main Room": lambda state: True,
            "Uthas Temple - Main Room 2nd side -> Uthas Temple - Main Room": lambda state: True,
            "Uthas Temple - Main Room 2nd side -> Uthas Temple - Final Floor": lambda state: True,
            "Uthas Temple - Final Floor -> Uthas Temple - Main Room 2nd side": lambda state: True,

            # Temple Gardens
            "Temple Gardens - Entrance -> Water Ways - Main Area": lambda state: True,
            "Temple Gardens - Entrance -> Firefall River - Main Area": lambda state: True,
            "Temple Gardens - Entrance -> Victory - Victory": lambda state: True,

            # Firefall River
            "Firefall River - Main Area -> Water Ways - Main Area": lambda state: True,
            "Firefall River - Main Area -> Rust Village - Main Area": lambda state: True,

            # Rust Village
            "Rust Village - Main Area -> Firefall River - Main Area": lambda state: True,
        }

    def hasDoubleJump(self, state: CollectionState) -> bool:
        return state.has("Double Jump Ability", self.player)

    def hasWallClimb(self, state: CollectionState) -> bool:
        return state.has("Wall Run Ability", self.player)

    def hasSpinAttack(self, state: CollectionState) -> bool:
        return state.has("Spin Attack Ability", self.player)

    # Set all rules in the multiworld
    def set_bluefire_rules(self) -> None:
        multiworld = self.world.multiworld

        for entrance_name, rule in self.connection_rules.items():
            entrance = multiworld.get_entrance(entrance_name, self.player)
            add_rule(entrance, rule)

        for location, dance in chest_dance_rules:
            add_rule(location, lambda state, d=dance: state.has(f"{d} Emote", self.player))

        multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
