from typing import Dict, List, Tuple, TYPE_CHECKING
from worlds.generic.Rules import add_rule

if TYPE_CHECKING:
    from . import BluefireWorld
    from .Subclasses import BluefireLocation
else:
    BluefireWorld = object

from BaseClasses import CollectionState, CollectionRule

chest_dance_rules: List[Tuple["BluefireLocation", str]] = []
event_requirement_rules: List[Tuple["BluefireLocation", List[str]]] = []

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
            "Arcane Tunnels - Main Room -> Fire Keep - Hub": lambda state: True,
            "Arcane Tunnels - Main Room -> Arcane Tunnels - Pipes": self.hasDoubleJump and self.hasWallClimb and self.hasSpinAttack,
            "Arcane Tunnels - Main Room -> Arcane Tunnels - Center Top": self.hasWallClimb and (self.hasDoubleJump or self.hasSpinAttack),
            "Arcane Tunnels - Main Room -> Crossroads - Main Area": lambda state: True,
            "Arcane Tunnels - Main Room -> Water Ways - Arcane Tunnels Main Entrance": lambda state: True,
            "Arcane Tunnels - Pipes -> Arcane Tunnels - Main Room": lambda state: True,
            "Arcane Tunnels - Pipes -> Water Ways - Arcane Tunnels Pipes Entrance": lambda state: True,
            "Arcane Tunnels - Center Top -> Arcane Tunnels - Main Room": lambda state: True,

            # Crossroads
            "Crossroads - Main Area -> Arcane Tunnels - Main Room": lambda state: True,
            "Crossroads - Main Area -> Crossroads - Left Area": self.hasWallClimb,
            "Crossroads - Main Area -> Stoneheart City - Main Area": lambda state: True,
            "Crossroads - Left Area -> Crossroads - Main Area": self.hasWallClimb,

            # Stoneheart City
            "Stoneheart City - Main Area -> Crossroads - Main Area": lambda state: True,
            "Stoneheart City - Main Area -> Stoneheart City - Top": self.hasWallClimb and (self.hasDoubleJump or self.hasSpinAttack),
            "Stoneheart City - Main Area -> Stoneheart City - Boy's Room": lambda state: True,
            "Stoneheart City - Main Area -> Stoneheart City - Bottom Corridor": self.hasWallClimb,
            "Stoneheart City - Main Area -> Forest Temple - High Level": lambda state: True, # TODO : add lever event
            "Stoneheart City - Main Area -> Abandoned Path - Entrance": lambda state: state.has("Key Graveyard", self.player, 1),
            "Stoneheart City - Main Area -> Temple Gardens - Middle Balcony": lambda state: True,
            "Stoneheart City - Top -> Stoneheart City - Main Area": lambda state: True,
            "Stoneheart City - Boy's Room -> Stoneheart City - Main Area": lambda state: True,
            "Stoneheart City - Bottom Corridor -> Stoneheart City - Main Area": self.hasWallClimb,

            # Water Ways
            "Water Ways - Arcane Tunnels Main Entrance -> Arcane Tunnels - Main Room": lambda state: True,
            "Water Ways - Arcane Tunnels Main Entrance -> Water Ways - Main Area": lambda state: state.has("Unlock Arcane Tunnels Main Gate", self.player),
            "Water Ways - Arcane Tunnels Pipes Entrance -> Arcane Tunnels - Pipes": lambda state: True,
            "Water Ways - Arcane Tunnels Pipes Entrance -> Water Ways - Main Area": lambda state: state.has("Unlock Arcane Tunnels Pipes Gate", self.player),
            "Water Ways - Abandoned Path Entrance -> Abandoned Path - Graveyard Balcony": lambda state: True,
            "Water Ways - Abandoned Path Entrance -> Water Ways - Main Area": lambda state: state.has("Unlock Abandoned Path Gate", self.player),
            "Water Ways - Firefall River Entrance -> Firefall River - Main Area": lambda state: True,
            "Water Ways - Firefall River Entrance -> Water Ways - Main Area": lambda state: state.has("Unlock Firefall River Gate", self.player),
            "Water Ways - Main Area -> Water Ways - Arcane Tunnels Main Entrance": lambda state: state.has("Unlock Arcane Tunnels Main Gate", self.player),
            "Water Ways - Main Area -> Water Ways - Arcane Tunnels Pipes Entrance": lambda state: state.has("Unlock Arcane Tunnels Pipes Gate", self.player),
            "Water Ways - Main Area -> Water Ways - Abandoned Path Entrance": lambda state: state.has("Unlock Abandoned Path Gate", self.player),
            "Water Ways - Main Area -> Water Ways - Firefall River Entrance": lambda state: state.has("Unlock Firefall River Gate", self.player),
            "Water Ways - Main Area -> Water Ways - Samuel's Room": lambda state: state.has("Unlock Arcane Tunnels Main Gate", self.player) and state.has("Unlock Arcane Tunnels Pipes Gate", self.player) and state.has("Unlock Abandoned Path Gate", self.player) and state.has("Unlock Firefall River Gate", self.player),
            "Water Ways - Samuel's Room -> Water Ways - Main Area": lambda state: True,

            # Forest Temple
            "Forest Temple - High Level -> Stoneheart City - Main Area": lambda state: True,
            "Forest Temple - High Level -> Forest Temple - Middle Level": lambda state: True, # TODO : add lever event
            "Forest Temple - Middle Level -> Forest Temple - High Level": lambda state: True,
            "Forest Temple - Middle Level -> Forest Temple - Low Level": self.hasWallClimb, # TODO : add lever event
            "Forest Temple - Middle Level -> Forest Temple - Ambush 1": lambda state: state.has("Old Key", self.player, 2),
            "Forest Temple - Low Level -> Forest Temple - Middle Level": lambda state: True,
            "Forest Temple - Low Level -> Forest Temple - Center Room Trunk": self.hasWallClimb,  # TODO : add lever event
            "Forest Temple - Ambush 1 -> Forest Temple - Middle Level": lambda state: True,
            "Forest Temple - Ambush 1 -> Forest Temple - Ambush 2": lambda state: state.has("Old Key", self.player, 3),
            "Forest Temple - Ambush 1 -> Forest Temple - Nuos Claw": lambda state: state.has("Rare Key", self.player, 1),
            "Forest Temple - Ambush 2 -> Forest Temple - Ambush 1": lambda state: True,
            "Forest Temple - Nuos Claw -> Forest Temple - Ambush 1": lambda state: True,
            "Forest Temple - Center Room Trunk -> Forest Temple - Low Level": lambda state: True,

            # Abandoned Path
            "Abandoned Path - Entrance -> Stoneheart City - Main Area": lambda state: True,
            "Abandoned Path - Entrance -> Abandoned Path - Main Room": self.hasWallClimb or self.hasDoubleJump or self.hasSpinAttack,
            "Abandoned Path - Main Room -> Abandoned Path - Entrance": self.hasWallClimb or self.hasDoubleJump or self.hasSpinAttack,
            "Abandoned Path - Main Room -> Abandoned Path - Heights": self.hasWallClimb,
            "Abandoned Path - Main Room -> Abandoned Path - Entrance Ravin": self.hasDoubleJump or self.hasSpinAttack,
            "Abandoned Path - Main Room -> Abandoned Path - Graveyard Balcony": self.hasWallClimb or self.hasDoubleJump or self.hasSpinAttack,
            "Abandoned Path - Heights -> Abandoned Path - Beira's Room": self.hasAllBeiraShards,
            "Abandoned Path - Main Room -> Uthas Temple - Entrance": lambda state: state.has("Key Uthas Temple", self.player, 1),
            "Abandoned Path - Entrance Ravin -> Abandoned Path - Main Room": self.hasDoubleJump or self.hasSpinAttack,
            "Abandoned Path - Graveyard Balcony -> Abandoned Path - Main Room": self.hasWallClimb or self.hasDoubleJump or self.hasSpinAttack,
            "Abandoned Path - Graveyard Balcony -> Water Ways - Abandoned Path Entrance": lambda state: True,
            "Abandoned Path - Graveyard Balcony -> Temple Gardens - Entrance": lambda state: True,
            "Abandoned Path - Heights -> Abandoned Path - Main Room": lambda state: True,
            "Abandoned Path - Main Room -> Abandoned Path - End of Main Room": lambda state: True, # TODO : Need spirits to go here
            "Abandoned Path - Beira's Room -> Abandoned Path - Heights": lambda state: True,
            "Abandoned Path - End of Main Room -> Abandoned Path - Main Room": self.hasWallClimb and self.hasDoubleJump and self.hasSpinAttack, # TODO : Need spirits to go here

            # Uthas Temple
            "Uthas Temple - Entrance -> Abandoned Path - Entrance": lambda state: True,
            "Uthas Temple - Entrance -> Uthas Temple - Main Room": lambda state: state.has("Old Key", self.player, 4),
            "Uthas Temple - Entrance -> Uthas Temple - Top of Entrance": lambda state: self.hasWallClimb and (self.hasDoubleJump or self.hasSpinAttack),
            "Uthas Temple - Top of Entrance -> Uthas Temple - Entrance": lambda state: True,
            "Uthas Temple - Main Room -> Uthas Temple - Entrance": lambda state: True,
            "Uthas Temple - Main Room -> Uthas Temple - Ambush Room": lambda state: state.has("Old Key", self.player, 5) and (self.hasWallClimb or self.hasDoubleJump or self.hasSpinAttack),
            "Uthas Temple - Main Room -> Uthas Temple - Holy Tower Chest": lambda state: state.has("Rare Key", self.player, 2), # Holy Key
            "Uthas Temple - Main Room -> Uthas Temple - Main Room 2nd side": lambda state: state.has("Old Key", self.player, 6) and ((self.hasWallClimb and (self.hasDoubleJump or self.hasSpinAttack)) or (self.hasDoubleJump and self.hasSpinAttack)),
            "Uthas Temple - Ambush Room -> Uthas Temple - Main Room": lambda state: True,
            "Uthas Temple - Holy Tower Chest -> Uthas Temple - Main Room": lambda state: True,
            "Uthas Temple - Main Room 2nd side -> Uthas Temple - Main Room": lambda state: True,
            "Uthas Temple - Main Room 2nd side -> Uthas Temple - Final Floor": lambda state: state.has("Old Key", self.player, 7) and ((self.hasWallClimb and (self.hasDoubleJump or self.hasSpinAttack)) or (self.hasDoubleJump and self.hasSpinAttack)),
            "Uthas Temple - Final Floor -> Uthas Temple - Main Room 2nd side": lambda state: True,

            # Temple Gardens
            "Temple Gardens - Entrance -> Firefall River - Main Area": lambda state: True,
            "Temple Gardens - Entrance -> Temple Gardens - Temple of Gods": lambda state: True,
            "Temple Gardens - Entrance -> Temple Gardens - Middle Balcony": self.hasDoubleJump or self.hasSpinAttack,
            "Temple Gardens - Middle Balcony -> Temple Gardens - Entrance": self.hasDoubleJump or self.hasSpinAttack,
            "Temple Gardens - Middle Balcony -> Stoneheart City - Main Area": lambda state: True,
            "Temple Gardens - Temple of Gods -> Temple Gardens - Entrance": lambda state: True,
            "Temple Gardens - Temple of Gods -> Victory - Victory": lambda state: state.has("Beat Fire Boss", self.player) and state.has("Beat Samuel", self.player) and state.has("Beat Beira", self.player),


            # Firefall River
            "Firefall River - Main Area -> Water Ways - Firefall River Entrance": lambda state: True,
            "Firefall River - Main Area -> Firefall River - Steam House": lambda state: state.has("Iron Justice", self.player), # TODO : set this condition for the events not the Steam House
            "Firefall River - Steam House -> Firefall River - Main Area": lambda state: True,
            "Firefall River - Steam House -> Rust Village - Main Area": self.allGeneratorsRepaired,
            "Firefall River - Steam House -> Firefall River - Fire Boss Room": lambda state: state.has("Key Fire Master", self.player),
            "Firefall River - Fire Boss Room -> Firefall River - Steam House": lambda state: True,

            # Rust Village
            "Rust Village - Main Area -> Firefall River - Main Area": lambda state: True,
        }

    def hasDoubleJump(self, state: CollectionState) -> bool:
        return state.has("Double Jump Ability", self.player)

    def hasWallClimb(self, state: CollectionState) -> bool:
        return state.has("Wall Run Ability", self.player)

    def hasSpinAttack(self, state: CollectionState) -> bool:
        return state.has("Spin Attack Ability", self.player)

    def allGeneratorsRepaired(self, state: CollectionState) -> bool:
        return state.has("Repair Generator 1", self.player) and state.has("Repair Generator 2", self.player) and state.has("Repair Generator 3", self.player)

    def hasAllBeiraShards(self, state: CollectionState) -> bool:
        return state.has("Capture Beira Shards 1", self.player) and state.has("Capture Beira Shards 2", self.player) and state.has("Capture Beira Shards 3", self.player) and state.has("Capture Beira Shards 4", self.player)

    # Set all rules in the multiworld
    def set_bluefire_rules(self) -> None:
        multiworld = self.world.multiworld

        for entrance_name, rule in self.connection_rules.items():
            entrance = multiworld.get_entrance(entrance_name, self.player)
            add_rule(entrance, rule)

        for location, dance in chest_dance_rules:
            add_rule(location, lambda state, d=dance: state.has(f"{d} Emote", self.player))

        # Apply event requirement rules
        for location, required_items in event_requirement_rules:
            # Create a rule that checks for all required items
            def event_rule(state, items=required_items, player=self.player):
                return all(state.has(item, player) for item in items)
            add_rule(location, event_rule)

        multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
