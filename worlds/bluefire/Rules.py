from typing import Dict, List, Tuple, NamedTuple, TYPE_CHECKING
from worlds.generic.Rules import add_rule
from dataclasses import dataclass

if TYPE_CHECKING:
    from . import BluefireWorld
    from .Subclasses import BluefireLocation
else:
    BluefireWorld = object

from BaseClasses import CollectionState, CollectionRule


class MovementInventory(NamedTuple):
    """Represents movement capabilities as a 5D vector.
    Order: wall_climb, jump, spin_attack, dash, movement
    """
    wall_climb: int = 0
    jump: int = 0
    spin_attack: int = 0
    dash: int = 0
    movement: int = 0

    def satisfies(self, requirement: "MovementInventory") -> bool:
        """Check if this inventory meets or exceeds a requirement (component-wise)."""
        return (self.wall_climb >= requirement.wall_climb and
                self.jump >= requirement.jump and
                self.spin_attack >= requirement.spin_attack and
                self.dash >= requirement.dash and
                self.movement >= requirement.movement)


@dataclass(frozen=True)
class MovementRule:
    """A minimal set of movement requirements to access a region.
    Multiple MovementInventory entries can be used for alternative paths (OR logic).
    """
    requirements: List[MovementInventory]

    def is_satisfied(self, current: MovementInventory) -> bool:
        """True if current inventory satisfies ANY of the requirements."""
        return any(current.satisfies(req) for req in self.requirements)

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
            "Fire Keep - Intro -> Fire Keep - Hub": lambda state: state.has("Old Key - Fire Keep", self.player, 1),
            "Fire Keep - Intro -> Fire Keep - High Spot": self._check_movement(MovementRule([
                MovementInventory(jump=3),
                MovementInventory(wall_climb=1),
                MovementInventory(spin_attack=1),
            ])),
            "Fire Keep - High Spot -> Fire Keep - Intro": lambda state: True,
            "Fire Keep - Hub -> Fire Keep - Intro": lambda state: True,
            "Fire Keep - Hub -> Fire Keep - Top of Lula's Void Gate Room": self._check_movement(MovementRule([
                MovementInventory(jump=1, spin_attack=1),
            ])),
            "Fire Keep - Top of Lula's Void Gate Room -> Fire Keep - Hub": lambda state: True,
            "Fire Keep - Hub -> Arcane Tunnels - Main Room": lambda state: True,

            # Arcane Tunnels
            "Arcane Tunnels - Main Room -> Fire Keep - Hub": lambda state: True,
            "Arcane Tunnels - Main Room -> Arcane Tunnels - Pipes": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1, jump=1, spin_attack=1),
            ])),
            "Arcane Tunnels - Main Room -> Arcane Tunnels - Center Top": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1, jump=1),
                MovementInventory(wall_climb=1, spin_attack=1),
            ])),
            "Arcane Tunnels - Main Room -> Crossroads - Main Area": lambda state: True,
            "Arcane Tunnels - Main Room -> Water Ways - Arcane Tunnels Main Entrance": lambda state: True,
            "Arcane Tunnels - Main Room -> Arcane Tunnels - Guard Room": lambda state: True,
            "Arcane Tunnels - Main Room -> Arcane Tunnels - Guard Armory": lambda state: True,
            "Arcane Tunnels - Main Room -> Arcane Tunnels - Spirit Hunter Room": lambda state: True,
            "Arcane Tunnels - Guard Room -> Arcane Tunnels - Main Room": lambda state: True,
            "Arcane Tunnels - Guard Armory -> Arcane Tunnels - Main Room": lambda state: True,
            "Arcane Tunnels - Spirit Hunter Room -> Arcane Tunnels - Main Room": lambda state: True,
            "Arcane Tunnels - Pipes -> Arcane Tunnels - Main Room": lambda state: True,
            "Arcane Tunnels - Pipes -> Water Ways - Arcane Tunnels Pipes Entrance": lambda state: True,
            "Arcane Tunnels - Center Top -> Arcane Tunnels - Main Room": lambda state: True,

            # Crossroads
            "Crossroads - Main Area -> Arcane Tunnels - Main Room": lambda state: True,
            "Crossroads - Main Area -> Crossroads - Left Area": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1),
            ])),
            "Crossroads - Main Area -> Stoneheart City - Main Area": lambda state: True,
            "Crossroads - Left Area -> Crossroads - Main Area": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1),
            ])),

            # Stoneheart City
            "Stoneheart City - Main Area -> Crossroads - Main Area": lambda state: True,
            "Stoneheart City - Main Area -> Stoneheart City - Top": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1, jump=1),
                MovementInventory(wall_climb=1, spin_attack=1),
            ])),
            "Stoneheart City - Main Area -> Stoneheart City - Boy's Room": lambda state: True,
            "Stoneheart City - Main Area -> Stoneheart City - Bottom Corridor": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1),
            ])),
            "Stoneheart City - Main Area -> Stoneheart City - Breemur's Tavern": lambda state: state.has("Beat Gruh", self.player),
            "Stoneheart City - Main Area -> Forest Temple - High Level": lambda state: True, # TODO : add lever event
            "Stoneheart City - Main Area -> Abandoned Path - Entrance": lambda state: state.has("Graveyard Key", self.player, 1),
            "Stoneheart City - Main Area -> Temple Gardens - Middle Balcony": lambda state: True,
            "Stoneheart City - Top -> Stoneheart City - Main Area": lambda state: True,
            "Stoneheart City - Boy's Room -> Stoneheart City - Main Area": lambda state: True,
            "Stoneheart City - Bottom Corridor -> Stoneheart City - Main Area": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1),
            ])),
            "Stoneheart City - Breemur's Tavern -> Stoneheart City - Main Area": lambda state: True,

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
            "Forest Temple - Middle Level -> Forest Temple - Low Level": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1),
            ])), # TODO : add lever event
            "Forest Temple - Middle Level -> Forest Temple - Ambush 1": lambda state: state.has("Old Key - Forest Temple Ambush", self.player, 1),
            "Forest Temple - Low Level -> Forest Temple - Middle Level": lambda state: True,
            "Forest Temple - Low Level -> Forest Temple - Center Room": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1),
                MovementInventory(jump=3),
            ])),
            "Forest Temple - Low Level -> Forest Temple - Long Corridor": self._check_movement(MovementRule([
                MovementInventory(jump=1, wall_climb=1, spin_attack=1),
            ])), # TODO : Need spirits to go here
            "Forest Temple - Center Room -> Forest Temple - Center Room Trunk": lambda state: state.has("Old Key - Forest Temple Center Room", self.player, 1),  # TODO : add lever event
            "Forest Temple - Center Room -> Forest Temple - Parkour Room": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1),
            ])),
            "Forest Temple - Center Room -> Forest Temple - Boss Room": lambda state: state.has("Holy Key - Forest Temple Boss", self.player, 1),
            "Forest Temple - Ambush 1 -> Forest Temple - Middle Level": lambda state: True,
            "Forest Temple - Ambush 1 -> Forest Temple - Ambush 2": lambda state: state.has("Old Key - Forest Temple Ambush 2", self.player, 1),
            "Forest Temple - Ambush 1 -> Forest Temple - Nuos Claw Room": lambda state: state.has("Holy Key - Forest Temple Nuos Claw", self.player, 1),
            "Forest Temple - Ambush 2 -> Forest Temple - Ambush 1": lambda state: True,
            "Forest Temple - Nuos Claw Room -> Forest Temple - Ambush 1": lambda state: True,
            "Forest Temple - Center Room Trunk -> Forest Temple - Center Room": lambda state: True,
            "Forest Temple - Parkour Room -> Forest Temple - Center Room": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1),
            ])),
            "Forest Temple - Boss Room -> Forest Temple - Center Room": lambda state: True,
            "Forest Temple - Long Corridor -> Forest Temple - Low Level": lambda state: True,

            # Abandoned Path
            "Abandoned Path - Entrance -> Stoneheart City - Main Area": lambda state: True,
            "Abandoned Path - Entrance -> Abandoned Path - Main Room": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1),
                MovementInventory(jump=3),
                MovementInventory(spin_attack=1),
            ])),
            "Abandoned Path - Main Room -> Abandoned Path - Entrance": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1),
                MovementInventory(jump=3),
                MovementInventory(spin_attack=1),
            ])),
            "Abandoned Path - Main Room -> Abandoned Path - Heights": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1),
            ])),
            "Abandoned Path - Main Room -> Abandoned Path - Entrance Ravin": self._check_movement(MovementRule([
                MovementInventory(jump=3),
                MovementInventory(spin_attack=1),
            ])),
            "Abandoned Path - Main Room -> Abandoned Path - Graveyard Balcony": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1),
                MovementInventory(jump=3),
                MovementInventory(spin_attack=1),
            ])),
            "Abandoned Path - Main Room -> Abandoned Path - Right side of Tower": lambda state: True,
            "Abandoned Path - Heights -> Abandoned Path - Beira's Room": self.hasAllBeiraShards,
            "Abandoned Path - Main Room -> Uthas Temple - Entrance": lambda state: state.has("Uthas Temple Key", self.player, 1),
            "Abandoned Path - Entrance Ravin -> Abandoned Path - Main Room": self._check_movement(MovementRule([
                MovementInventory(jump=3),
                MovementInventory(spin_attack=1),
            ])),
            "Abandoned Path - Graveyard Balcony -> Abandoned Path - Main Room": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1),
                MovementInventory(jump=3),
                MovementInventory(spin_attack=1),
            ])),
            "Abandoned Path - Graveyard Balcony -> Water Ways - Abandoned Path Entrance": lambda state: True,
            "Abandoned Path - Graveyard Balcony -> Temple Gardens - Entrance": lambda state: True,
            "Abandoned Path - Heights -> Abandoned Path - Main Room": lambda state: True,
            "Abandoned Path - Main Room -> Abandoned Path - End of Main Room": lambda state: True, # TODO : Need spirits to go here
            "Abandoned Path - Beira's Room -> Abandoned Path - Heights": lambda state: True,
            "Abandoned Path - End of Main Room -> Abandoned Path - Main Room": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1, jump=1, spin_attack=1),
            ])), # TODO : Need spirits to go here
            "Abandoned Path - Right side of Tower -> Abandoned Path - Main Room": lambda state: True,

            # Uthas Temple
            "Uthas Temple - Entrance -> Abandoned Path - Entrance": lambda state: True,
            "Uthas Temple - Entrance -> Uthas Temple - Main Room": lambda state: state.has("Old Key - Uthas Temple Main Room", self.player, 1),
            "Uthas Temple - Entrance -> Uthas Temple - Top of Entrance": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1, jump=1),
                MovementInventory(wall_climb=1, spin_attack=1),
            ])),
            "Uthas Temple - Top of Entrance -> Uthas Temple - Entrance": lambda state: True,
            "Uthas Temple - Main Room -> Uthas Temple - Entrance": lambda state: True,
            "Uthas Temple - Main Room -> Uthas Temple - Ambush Room": lambda state: state.has("Old Key - Uthas Temple Ambush", self.player, 1) and self._check_movement(MovementRule([
                MovementInventory(wall_climb=1),
                MovementInventory(jump=3),
                MovementInventory(spin_attack=1),
            ]))(state),
            "Uthas Temple - Main Room -> Uthas Temple - Holy Tower Chest": lambda state: state.has("Holy Key - Uthas Temple Holy Tower", self.player, 1),
            "Uthas Temple - Main Room -> Uthas Temple - Main Room 2nd side": lambda state: state.has("Old Key - Uthas Temple 2nd Side", self.player, 1) and self._check_movement(MovementRule([
                MovementInventory(wall_climb=1, jump=1),
                MovementInventory(wall_climb=1, spin_attack=1),
                MovementInventory(jump=1, spin_attack=1),
            ]))(state),
            "Uthas Temple - Ambush Room -> Uthas Temple - Main Room": lambda state: True,
            "Uthas Temple - Holy Tower Chest -> Uthas Temple - Main Room": lambda state: True,
            "Uthas Temple - Main Room 2nd side -> Uthas Temple - Main Room": lambda state: True,
            "Uthas Temple - Main Room 2nd side -> Uthas Temple - Final Floor": lambda state: state.has("Old Key - Uthas Temple Final Floor", self.player, 1) and self._check_movement(MovementRule([
                MovementInventory(wall_climb=1, jump=1),
                MovementInventory(wall_climb=1, spin_attack=1),
                MovementInventory(jump=1, spin_attack=1),
            ]))(state),
            "Uthas Temple - Final Floor -> Uthas Temple - Main Room 2nd side": lambda state: True,

            # Temple Gardens
            "Temple Gardens - Entrance -> Firefall River - Main Area": lambda state: True,
            "Temple Gardens - Entrance -> Temple Gardens - Temple of Gods": lambda state: True,
            "Temple Gardens - Entrance -> Temple Gardens - Middle Balcony": self._check_movement(MovementRule([
                MovementInventory(jump=3),
                MovementInventory(spin_attack=1),
            ])),
            "Temple Gardens - Entrance -> Abandoned Path - Graveyard Balcony": lambda state: True,
            "Temple Gardens - Entrance -> Temple Gardens - Temple of Gods Bell Towers": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1, jump=1, spin_attack=1),
            ])),
            "Temple Gardens - Entrance -> Temple Gardens - Top of Temple of Gods Door": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1, jump=1, spin_attack=1),
            ])),
            "Temple Gardens - Middle Balcony -> Temple Gardens - Entrance": self._check_movement(MovementRule([
                MovementInventory(jump=3),
                MovementInventory(spin_attack=1),
            ])),
            "Temple Gardens - Middle Balcony -> Stoneheart City - Main Area": lambda state: True,
            "Temple Gardens - Temple of Gods -> Temple Gardens - Entrance": lambda state: True,
            "Temple Gardens - Temple of Gods -> Victory - Victory": lambda state: state.has("Beat Fire Boss", self.player) and state.has("Beat Samuel", self.player) and state.has("Beat Beira", self.player),
            "Temple Gardens - Temple of Gods Bell Towers -> Temple Gardens - Entrance": lambda state: True,
            "Temple Gardens - Top of Temple of Gods Door -> Temple Gardens - Entrance": lambda state: True,

            # Firefall River
            "Firefall River - Main Area -> Water Ways - Firefall River Entrance": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1),
                MovementInventory(jump=3),
                MovementInventory(spin_attack=1),
            ])), # TODO : Need spirits to go here
            "Firefall River - Main Area -> Firefall River - Steam House": self._check_movement(MovementRule([
                MovementInventory(wall_climb=1),
                MovementInventory(jump=3),
                MovementInventory(spin_attack=1),
            ])), # TODO : Need spirits to go here
            "Firefall River - Main Area -> Firefall River - Entrance Left Side": lambda state: True,
            "Firefall River - Steam House -> Firefall River - Main Area": lambda state: True,
            "Firefall River - Steam House -> Rust Village - Main Area": self.allGeneratorsRepaired,
            "Firefall River - Steam House -> Firefall River - Fire Boss Room": lambda state: state.has("Key of Ember", self.player),
            "Firefall River - Fire Boss Room -> Firefall River - Steam House": lambda state: True,
            "Firefall River - Entrance Left Side -> Firefall River - Main Area": lambda state: True,

            # Rust Village
            "Rust Village - Main Area -> Firefall River - Steam House": lambda state: True,
            "Rust Village - Main Area -> Firefall River - Main Area": lambda state: True,
        }

        self.event_rules = {
            "Firefall River - Steam House - Repair Generator 1": lambda state: state.has("Iron Justice", self.player) or state.has("Progressive Weapon", self.player, 8),
            "Firefall River - Steam House - Repair Generator 2": lambda state: state.has("Iron Justice", self.player) or state.has("Progressive Weapon", self.player, 8),
            "Firefall River - Steam House - Repair Generator 3": lambda state: state.has("Iron Justice", self.player) or state.has("Progressive Weapon", self.player, 8),
        }

    def _build_movement_inventory(self, state: CollectionState) -> MovementInventory:
        """Build current movement inventory from progressive items."""
        return MovementInventory(
            wall_climb=state.count("Progressive Wall Climb", self.player),
            jump=state.count("Progressive Jump", self.player),
            spin_attack=state.count("Progressive Spin Attack", self.player),
            dash=state.count("Progressive Dash", self.player),
            movement=state.count("Progressive Running", self.player),
        )

    def _check_movement(self, rule: MovementRule) -> callable:
        """Convert a MovementRule into a rule function."""
        def check(state: CollectionState) -> bool:
            inventory = self._build_movement_inventory(state)
            return rule.is_satisfied(inventory)
        return check

    def allGeneratorsRepaired(self, state: CollectionState) -> bool:
        return state.has("Repair Generator 1", self.player) and state.has("Repair Generator 2", self.player) and state.has("Repair Generator 3", self.player)

    def hasAllBeiraShards(self, state: CollectionState) -> bool:
        return state.has("Capture Beira Shards 1", self.player) and state.has("Capture Beira Shards 2", self.player) and state.has("Capture Beira Shards 3", self.player) and state.has("Capture Beira Shards 4", self.player)

    # Set all rules in the multiworld
    def set_bluefire_rules(self) -> None:
        multiworld = self.world.multiworld

        for event_name, rule in self.event_rules.items():
            location = multiworld.get_location(event_name, self.player)
            add_rule(location, rule)

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