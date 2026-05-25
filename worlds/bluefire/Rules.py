from worlds.generic.Rules import add_rule, forbid_item
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import BluefireWorld

def set_rules(world: "BluefireWorld"):
    player = world.player
    options = world.options

    # ====== ENTRANCE RULES ======
    # These control progression through regions
    # Note: Entrance rules should only check for ITEMS, not locations (to avoid circular logic)

    # Fire Keep is accessible from start - no rule needed

    add_rule(world.multiworld.get_entrance("Fire Keep - Intro -> Fire Keep - Hub", player),
             lambda state: state.has("key", player, 1))

    add_rule(world.multiworld.get_entrance("Forest Temple - Water -> Forest Temple - Ambush 1", player),
             lambda state: state.has("key", player, 2))

    add_rule(world.multiworld.get_entrance("Forest Temple - Ambush 1 -> Forest Temple - Ambush 2", player),
             lambda state: state.has("key", player, 3))

    add_rule(world.multiworld.get_entrance("Forest Temple - Ambush 1 -> Forest Temple - Nuos Claw", player),
             lambda state: state.has("key", player, 4))

    add_rule(world.multiworld.get_entrance("Forest Temple - Water -> Forest Temple - Center Tree", player),
             lambda state: state.has("key", player, 5))



    """
    # Crossroads requires some Fire Keep items
    add_rule(world.multiworld.get_entrance("Fire Keep -> Crossroads", player),
             lambda state: state.count("Old Key", player) > 0)

    # Forest Temple requires movement abilities
    add_rule(world.multiworld.get_entrance("Stoneheart City -> Forest Temple", player),
             lambda state: state.has("Wall Run", player) or state.count("Old Key", player) > 0)

    # Temple Gardens requires multiple keys
    add_rule(world.multiworld.get_entrance("Stoneheart City -> Temple Gardens", player),
             lambda state: state.has("Old Key", player) and state.has("Key Holy Master", player))

    # Abandoned Path requires movement
    add_rule(world.multiworld.get_entrance("Stoneheart City -> Abandoned Path", player),
             lambda state: state.has("Wall Run", player) or state.has("Double Jump", player))

    # Uthas Temple requires temple key
    add_rule(world.multiworld.get_entrance("Abandoned Path -> Uthas Temple", player),
             lambda state: state.has("Key Uthas Temple", player))

    # Temple of Gods requires god key
    add_rule(world.multiworld.get_entrance("Temple Gardens -> Temple of Gods", player),
             lambda state: state.has("Key God Master", player))

    # Firefall River requires Sanctuary Stone
    add_rule(world.multiworld.get_entrance("Arcane Tunnels -> Firefall River", player),
             lambda state: state.has("Sanctuary Stone", player))

    # Steam House progression
    add_rule(world.multiworld.get_entrance("Firefall River -> Steam House", player),
             lambda state: state.has("Double Jump", player) or state.has("Wall Run", player))

    # Iron Caves requires steam key
    add_rule(world.multiworld.get_entrance("Steam House -> Iron Caves", player),
             lambda state: state.has("Key Steam", player))

    # Void Challenges require movement abilities
    add_rule(world.multiworld.get_entrance("Arcane Tunnels -> Void Challenges", player),
             lambda state: state.has("Double Jump", player) and state.has("Wall Run", player) and state.has("Sprint", player))

    # ====== Location-specific rules ======

    # Forest Temple locations require appropriate keys/abilities
    add_rule(world.multiworld.get_location("Forest Temple - Nuos Claw", player),
             lambda state: state.has("Old Key", player))

    # Complex locations need multiple items
    add_rule(world.multiworld.get_location("Forest Temple - Tree", player),
             lambda state: state.has("Wall Run", player) and state.has("Double Jump", player))

    # Gruh boss requires key
    add_rule(world.multiworld.get_location("Forest Temple - Gruh Boss", player),
             lambda state: state.has("Key Holy Master", player))

    # Uthas Temple requires keys
    add_rule(world.multiworld.get_location("Uthas Temple - Combat", player),
             lambda state: state.has("Wall Run", player) and state.has("Old Key", player))

    add_rule(world.multiworld.get_location("Uthas Temple - Platforming", player),
             lambda state: state.has("Double Jump", player) and state.has("Wall Run", player) and state.has("Old Key", player))

    # Uthas end requires progression
    add_rule(world.multiworld.get_location("Uthas Temple - End", player),
             lambda state: state.has("Key Holy Master", player))

    # Temple of Gods requires sanctuary stone and keys
    add_rule(world.multiworld.get_location("Sanctuary Stone Location", player),
             lambda state: state.has("Key God Master", player))

    # Queen Chamber (Victory) requires all keys and sanctuary stone
    add_rule(world.multiworld.get_location("Queen Chamber", player),
             lambda state: state.has("Sanctuary Stone", player) and
                          state.count("Old Key", player) > 0 and
                          state.has("Key Holy Master", player) and
                          state.has("Key God Master", player) and
                          state.has("Wall Run", player))

    # Firefall locations require abilities
    add_rule(world.multiworld.get_location("Firefall River - Bunny", player),
             lambda state: state.has("Double Jump", player) or state.has("Wall Run", player))

    add_rule(world.multiworld.get_location("Firefall River - Lake Molva", player),
             lambda state: state.has("Double Jump", player))

    # Steam House locations need keys
    add_rule(world.multiworld.get_location("Steam House - Platforming", player),
             lambda state: state.has("Key Steam", player) and state.has("Double Jump", player) and state.has("Wall Run", player))

    # Sirion requires fire master key and sanctuary stone
    add_rule(world.multiworld.get_location("Sirion", player),
             lambda state: state.has("Key Fire Master", player) and state.has("Wall Run", player) and state.has("Sanctuary Stone", player))

    # Rust Village requires Iron Justice weapon
    add_rule(world.multiworld.get_location("Rust Village", player),
             lambda state: state.has("Iron Justice", player) or (state.has("Key Steam", player) and state.has("Double Jump", player)))

    # Waterway locations
    add_rule(world.multiworld.get_location("Waterway - Ducks", player),
             lambda state: state.has("Sanctuary Stone", player) and state.has("Double Jump", player))

    add_rule(world.multiworld.get_location("Waterway - Samael Boss", player),
             lambda state: state.has("Sanctuary Stone", player) and state.has("Wall Run", player) and state.count("Old Key", player) > 0)

    # Beira Shrine requires significant progression
    add_rule(world.multiworld.get_location("Beira Shrine", player),
             lambda state: state.has("Sanctuary Stone", player) and state.has("Wall Run", player) and state.has("Beira Vessel", player))

    # Void challenges require specific movements and items
    add_rule(world.multiworld.get_location("Void - Path of Victory", player),
             lambda state: True)

    add_rule(world.multiworld.get_location("Void - Arigos Challenge", player),
             lambda state: state.has("Double Jump", player))

    add_rule(world.multiworld.get_location("Void - Brisas Fate", player),
             lambda state: state.has("Wall Run", player) and state.has("Double Jump", player))

    add_rule(world.multiworld.get_location("Void - Julians Song", player),
             lambda state: True)

    add_rule(world.multiworld.get_location("Void - Alchemist", player),
             lambda state: state.has("Wall Run", player))

    add_rule(world.multiworld.get_location("Void - The Void", player),
             lambda state: state.has("Double Jump", player) and state.has("Wall Run", player) and state.has("Sprint", player))

    # ====== Prevent softlocks ======

    # Never place Victory at locked locations
    forbid_item(world.multiworld.get_location("Fire Keep - Lab", player), "Victory", player)
    forbid_item(world.multiworld.get_location("Fire Keep - Bitoven", player), "Victory", player)

    # Never place progression keys at locations requiring those same keys
    for loc in world.multiworld.get_locations(player):
        if "Void" in loc.name:
            forbid_item(loc, "Double Jump", player)
            forbid_item(loc, "Wall Run", player)
            forbid_item(loc, "Sprint", player)
    """

    # ====== Victory Condition ======
    world.multiworld.completion_condition[player] = lambda state: state.has("Victory", player)