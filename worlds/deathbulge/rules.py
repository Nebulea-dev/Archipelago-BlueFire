from typing import Dict, Callable, TYPE_CHECKING
from .items import treasure_legendary_beats_items

if TYPE_CHECKING:
    from . import DeathbulgeWorld
else:
    DeathbulgeWorld = object

from BaseClasses import CollectionState, CollectionRule


class DeathbulgeRules:
    player: int
    world: DeathbulgeWorld
    connection_rules: dict[str, CollectionRule]
    location_rules: Dict[str, Callable[[CollectionState], bool]]
    region_rules: Dict[str, Callable[[CollectionState], bool]]

    def __init__(self, world: DeathbulgeWorld) -> None:
        self.player = world.player
        self.world = world

        self.connection_rules = {
            "TheBus - TheBusElevator -> TheBus - TheBus07": self.has_13_deck_keycard,
            "TheBus - TheBusElevator -> TheBus - TheBus11": self.has_13_deck_keycard,
            "TheBus - TheBusElevator -> TheBus - TheBus08": self.has_14_deck_keycard,
            "TheBus - TheBusElevator -> TheBus - TheBus10": self.has_16_deck_keycard,
            "Hoho - Hoho01Lower -> BattleOfTheBands - BOTBLobby": self.has_all_legendary_beats,
            # Connections with indirect conditions ? (At least not when hard boss lock)
            "Bopstead - Bopstead02 -> Basement - Basement01": self.has_beaten_kkwak_claire,
            "Bopstead - Bopstead02 -> TheBus - TheBus01": self.has_beaten_modern_babby,
            "TheBus - TheBus10 -> Hoho - Hoho01-Bus": self.has_beaten_platinum_scrumptious,
            "Lab - Lab10 -> Hoho - Hoho02": self.has_beaten_mutilla,
            "Hoho - Hoho02 -> Lab - Lab10": self.has_beaten_mutilla,
            "Hoho - Hoho02 -> Pokalyps - Pokalyps01": self.has_beaten_mutilla,
            "ClaireHair - ClaireHair04Lower -> ClaireLower - ClaireLower01": self.has_beaten_pokalyps,
            "Pokalyps - Pokalyps05 -> Dream - Dream03Base": lambda state: self.has_goth_mod(state)
            and self.has_defeated_5_first_legends(state),
            # I know the next condition can be simplified, but this is for documenting the different ways to go here
            "Dream - Dream03Base -> Dream - Dream04Base": lambda state: self.has_remix_mod(state)
            or (self.has_well_toned_mod(state) and self.has_distorted_mod(state) and self.has_remix_mod(state)),
            "Dream - Dream04Base -> Dream - Dream05Base": lambda state: (
                self.has_avant_garde_mod(state) and self.has_well_toned_mod(state) and self.has_tuner_mod(state)
            )
            or (self.has_show_off_mod(state) and self.has_well_toned_mod(state) and self.has_busker_mod(state)),
            # TODO: Lock Jim house behind the 60 doors (create jim house and contains "Tonewood08Treasure02", "Tonewood08Treasure03", "Tonewood08Treasure04", "[Treasure] PrizeTicketJim")
            # TODO: Lock Babby Temple behind Inner Boot AND Location ClaireLower (create babby temple in Bopstead01 and contains only "Bopstead01Treasure02",)
            # TODO: Lock Tonewood arm while the Masstropod (Tonewood05) has not been beaten
            # TODO: Lock some dream locations behind having some class beats
        }

        self.location_rules = {
            "Hoho02Treasure06": self.has_all_legendary_beats,
            "Dream03Treasure01": lambda state: self.has_avant_garde_mod(state)
            and self.has_goth_mod(state)
            and self.has_distorted_mod(state)
            and self.has_remix_mod(state)
            and self.has_well_toned_mod(state)
            and self.has_tuner_mod(state),
            "Dream03Treasure02": self.has_show_off_mod,
            "Dream04Treasure01": self.has_tuner_mod,
            "Dream04Treasure02": lambda state: self.has_avant_garde_mod(state) and self.has_well_toned_mod(state),
            "Dream04Treasure03": lambda state: self.has_avant_garde_mod(state) and self.has_well_toned_mod(state),
            "Dream05Treasure01": lambda state: self.has_remix_mod(state)
            and self.has_busker_mod(state)
            and self.has_distorted_mod(state),
            # TODO: Lock the location `Whale25Treasure` behind `[Mod] Zero Hertz`
            # TODO: Lock the Sampler tuto behind [Beat] RH, [Beat] Gina and [Mod] REMIX Briff ?
            # TODO: Lock the tickets rewards behind a minimal number of tickets ?
        }

        # dict of connection names and the regions checked in the requirements to traverse the exit
        self.indirect_conditions = {
            # "Bopstead - Bopstead02 -> Basement - Basement01": [
            #     self.world.get_region("ClaireHair - ClaireHair08"),
            # ],
            # "Bopstead - Bopstead02 -> TheBus - TheBus01": [
            #     self.world.get_region("Basement - Basement07"),
            # ],
            # "TheBus - TheBus10 -> Hoho - Hoho01-Bus": [
            #     self.world.get_region("TheBus - TheBus10"),
            # ],
            # "Lab - Lab10 -> Hoho - Hoho02": [
            #     self.world.get_region("Lab - Lab10"),
            # ],
            # "Hoho - Hoho02 -> Lab - Lab10": [
            #     self.world.get_region("Lab - Lab10"),
            # ],
            # "Hoho - Hoho02 -> Pokalyps - Pokalyps01": [
            #     self.world.get_region("Lab - Lab10"),
            # ],
            # "ClaireHair04Lower -> ClaireLower - ClaireLower01": [
            #     self.world.get_region("Pokalyps - Pokalyps11"),
            # ],
        }

    # Items rules
    def has_13_deck_keycard(self, state: CollectionState) -> bool:
        return state.has("[Key Merch] 13th Deck Keycard", self.player)

    def has_14_deck_keycard(self, state: CollectionState) -> bool:
        return state.has("[Key Merch] 14th Deck Keycard", self.player)

    def has_16_deck_keycard(self, state: CollectionState) -> bool:
        return state.has("[Key Merch] 16th Deck Keycard", self.player)

    # Do NOT confuse with defeating the 5 first legends
    def has_all_legendary_beats(self, state: CollectionState) -> bool:
        for legendary_beat in treasure_legendary_beats_items:
            if not state.has(legendary_beat["name"], self.player):
                return False
        # TODO: Add Boss item for last legend, and the last legend beat is not randomized: Change this
        return True

    def has_defeated_5_first_legends(self, state: CollectionState) -> bool:
        # TODO: Create boss items for all the legends :)
        return True

    def has_remix_mod(self, state: CollectionState) -> bool:
        # TODO: Technically if we have enough beats rinna opens up her shop for Faye and Ian
        # return state.has("[Mod] REMIX Briff", self.player)
        return True

    def has_goth_mod(self, state: CollectionState) -> bool:
        # TODO: Count the ones in shop as collectable if region can be reached, and return true if we have one of the archipelago MOD
        return True

    def has_busker_mod(self, state: CollectionState) -> bool:
        # TODO: Count the ones in shop as collectable if region can be reached, and return true if we have one of the archipelago MOD
        return True

    def has_distorted_mod(self, state: CollectionState) -> bool:
        # TODO: Count the ones in shop as collectable if region can be reached, and return true if we have one of the archipelago MOD
        return True

    def has_avant_garde_mod(self, state: CollectionState) -> bool:
        # TODO: Count the ones in shop as collectable if region can be reached, and return true if we have one of the archipelago MOD
        return True

    # The following are here if someday I randomize the starting classes
    def has_show_off_mod(self, state: CollectionState) -> bool:
        # TODO: Count the ones in shop as collectable if region can be reached, and return true if we have one of the archipelago MOD
        return True

    def has_well_toned_mod(self, state: CollectionState) -> bool:
        # TODO: Count the ones in shop as collectable if region can be reached, and return true if we have one of the archipelago MOD
        return True

    def has_tuner_mod(self, state: CollectionState) -> bool:
        # TODO: Count the ones in shop as collectable if region can be reached, and return true if we have one of the archipelago MOD
        return True

    # Bosses rules
    def has_beaten_kkwak_claire(self, state: CollectionState) -> bool:
        return state.has("Basement Key", self.player)

    def has_beaten_modern_babby(self, state: CollectionState) -> bool:
        return state.has("Babby's corpse", self.player)

    def has_beaten_platinum_scrumptious(self, state: CollectionState) -> bool:
        return state.has("Bus ticket", self.player)

    def has_beaten_mutilla(self, state: CollectionState) -> bool:
        return state.has("Pokalyps concert's invite", self.player)

    def has_beaten_pokalyps(self, state: CollectionState) -> bool:
        return state.has("Claire's comb", self.player)

    # Set all rules in the multiworld
    def set_deathbulge_rules(self) -> None:
        multiworld = self.world.multiworld

        for entrance_name, rule in self.connection_rules.items():
            entrance = multiworld.get_entrance(entrance_name, self.player)
            entrance.access_rule = rule

            for region in self.indirect_conditions.get(entrance_name, ()):
                multiworld.register_indirect_condition(region, entrance)

        for loc in multiworld.get_locations(self.player):
            if loc.name in self.location_rules:
                loc.access_rule = self.location_rules[loc.name]

        multiworld.completion_condition[self.player] = lambda state: state.has("Beat Boosted KKwak", self.player)
