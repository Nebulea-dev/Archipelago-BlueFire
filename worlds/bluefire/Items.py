from BaseClasses import Item, ItemClassification
from .Types import ItemData, StartingLocation, BluefireItem, starting_location_to_name
from .Locations import get_total_locations
from typing import List, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from . import BluefireWorld

def create_itempool(world: "BluefireWorld") -> List[Item]:
    itempool: List[Item] = []

    #starting_location = starting_location_to_name[StartingLocation(world.options.StartingLocation)]
    starting_location = "Menu"

    # Add all items except the starting one
    for item_name, item_data in item_table.items():
        if item_data.count is None or item_data.count <= 0:
            continue
        # Skip starting location item
        if item_name == starting_location:
            continue
        for _ in range(item_data.count):
            itempool.append(create_item(world, item_name))

    # Fill remaining slots with junk
    itempool += create_junk_items(world, get_total_locations(world) - len(itempool) - 1)

    return itempool

def create_item(world: "BluefireWorld", name: str) -> Item:
    data = item_table[name]
    return BluefireItem(name, data.classification, data.ap_code, world.player)

def create_junk_items(world: "BluefireWorld", count: int) -> List[Item]:
    trap_chance = world.options.TrapChance.value
    junk_pool: List[Item] = []
    junk_list: Dict[str, int] = {}
    trap_list: Dict[str, int] = {}

    for name in item_table.keys():
        ic = item_table[name].classification
        if ic == ItemClassification.filler:
            junk_list[name] = junk_weights.get(name, 1)
        elif trap_chance > 0 and ic == ItemClassification.trap:
            trap_list[name] = trap_weights.get(name, 1)

    for i in range(count):
        if trap_chance > 0 and world.random.randint(1, 100) <= trap_chance and trap_list:
            junk_pool.append(world.create_item(
                world.random.choices(list(trap_list.keys()), weights=list(trap_list.values()), k=1)[0]))
        elif junk_list:
            junk_pool.append(world.create_item(
                world.random.choices(list(junk_list.keys()), weights=list(junk_list.values()), k=1)[0]))

    return junk_pool

# Base ID for Blue Fire items
BASE_ITEM_ID = 0xB70EF14E

# Progression items - keys and essential abilities
progression_items = {
    # Keys
    "Old Key": ItemData(BASE_ITEM_ID + 1, ItemClassification.progression),
    "Key Holy Master": ItemData(BASE_ITEM_ID + 5, ItemClassification.progression),
    #"Key Fire Master": ItemData(BASE_ITEM_ID + 3, ItemClassification.progression),
    #"Key Steam": ItemData(BASE_ITEM_ID + 4, ItemClassification.progression),
    #"Key Graveyard Key": ItemData(BASE_ITEM_ID + 5, ItemClassification.progression),
    #"Key Uthas Temple": ItemData(BASE_ITEM_ID + 6, ItemClassification.progression),
    #"Key God Master": ItemData(BASE_ITEM_ID + 7, ItemClassification.progression),

    # Core abilities
    #"Double Jump": ItemData(BASE_ITEM_ID + 11, ItemClassification.progression),
    "Nuos Claw": ItemData(BASE_ITEM_ID + 10, ItemClassification.progression),
    #"Sprint": ItemData(BASE_ITEM_ID + 13, ItemClassification.progression),
    #
    #"Spin Attack": ItemData(BASE_ITEM_ID + 15, ItemClassification.progression),

    # Essential items
    #"Sanctuary Stone": ItemData(BASE_ITEM_ID + 20, ItemClassification.progression),
    #"Beira Vessel": ItemData(BASE_ITEM_ID + 50, ItemClassification.progression),
    #"Fire Charm": ItemData(BASE_ITEM_ID + 50, ItemClassification.progression), # Is it really essential ?

    # Emotes
    #"Aggressive": ItemData(BASE_ITEM_ID + 20, ItemClassification.progression),
    #"Applause": ItemData(BASE_ITEM_ID + 21, ItemClassification.progression),
    "Celebration": ItemData(BASE_ITEM_ID + 22, ItemClassification.progression),
    #"Empty": ItemData(BASE_ITEM_ID + 23, ItemClassification.progression),
    #"Hat": ItemData(BASE_ITEM_ID + 24, ItemClassification.progression),
    #"Hello2": ItemData(BASE_ITEM_ID + 25, ItemClassification.progression),
    #"KungFu": ItemData(BASE_ITEM_ID + 26, ItemClassification.progression),
    #"Levitation": ItemData(BASE_ITEM_ID + 27, ItemClassification.progression),
    #"No": ItemData(BASE_ITEM_ID + 28, ItemClassification.progression),
    #"Party": ItemData(BASE_ITEM_ID + 29, ItemClassification.progression),
    #"Photo": ItemData(BASE_ITEM_ID + 30, ItemClassification.progression),
    #"Techno": ItemData(BASE_ITEM_ID + 31, ItemClassification.progression),
    #"Triceps": ItemData(BASE_ITEM_ID + 32, ItemClassification.progression),
    #"Wave": ItemData(BASE_ITEM_ID + 33, ItemClassification.progression),
    "Windmill": ItemData(BASE_ITEM_ID + 34, ItemClassification.progression),
}

# Useful items - helpful but not strictly necessary
useful_items = {
    # Pouches
    "Large Pouch": ItemData(BASE_ITEM_ID + 30, ItemClassification.useful),
    "Extra Large Pouch": ItemData(BASE_ITEM_ID + 31, ItemClassification.useful),

    # Quest items
    #"Necklace": ItemData(BASE_ITEM_ID + 40, ItemClassification.useful),
    #"Book": ItemData(BASE_ITEM_ID + 41, ItemClassification.useful),
    #"Odd Rock": ItemData(BASE_ITEM_ID + 42, ItemClassification.useful),
    #"Bremur Picture": ItemData(BASE_ITEM_ID + 43, ItemClassification.useful),
    #"House Key": ItemData(BASE_ITEM_ID + 44, ItemClassification.useful),
    #"House Contract": ItemData(BASE_ITEM_ID + 45, ItemClassification.useful),
    #"Mandoline": ItemData(BASE_ITEM_ID + 46, ItemClassification.useful),
    #"Rare Glasses": ItemData(BASE_ITEM_ID + 47, ItemClassification.useful),
    #"Rare Snow": ItemData(BASE_ITEM_ID + 48, ItemClassification.useful),
    #"Composer Letter": ItemData(BASE_ITEM_ID + 49, ItemClassification.useful),
    #"Beira Shards": ItemData(BASE_ITEM_ID + 51, ItemClassification.useful),
    #"Fire Essence Slot": ItemData(BASE_ITEM_ID + 52, ItemClassification.useful),

    # Equipment
    "Shield": ItemData(BASE_ITEM_ID + 60, ItemClassification.useful),
    #"Fire Ball": ItemData(BASE_ITEM_ID + 60, ItemClassification.useful),
    #"Down Smash": ItemData(BASE_ITEM_ID + 61, ItemClassification.useful),
}

emote_items = {

		{ "Wave Emote", 0 },
		{ "Applause Emote", 1 },
		{ "Levitation Emote", 2 },
		{ "Windmill Emote", 2 },

		{ "Hat Kid Emote", 2 },
		{ "Triceps Emote", 2 },

		{ "Aggressive Emote", 2 },
		{ "No Emote", 2 },

		{ "Photo Emote", 2 },

		{ "Celebration Emote", 2 },
		{ "Levitation Emote", 2 },
}

# Equipment (weapons, tunics, spirits)
equipment_items = {
    # Weapons
    "Bloodstorm Blades": ItemData(BASE_ITEM_ID + 101, ItemClassification.useful),
    "Diamond Wings": ItemData(BASE_ITEM_ID + 102, ItemClassification.useful),
    "Shadow Casters": ItemData(BASE_ITEM_ID + 103, ItemClassification.useful),
    "Ember Twins": ItemData(BASE_ITEM_ID + 104, ItemClassification.useful),
    "Iron Justice": ItemData(BASE_ITEM_ID + 105, ItemClassification.useful),
    "Ice Destroyers": ItemData(BASE_ITEM_ID + 106, ItemClassification.useful),
    "Peace Keepers": ItemData(BASE_ITEM_ID + 107, ItemClassification.useful),
    "Steel Shanks": ItemData(BASE_ITEM_ID + 108, ItemClassification.useful),
    "Bremur Family Swords": ItemData(BASE_ITEM_ID + 109, ItemClassification.useful),
    "Silver Blades": ItemData(BASE_ITEM_ID + 110, ItemClassification.useful),
    "Kina Defenders": ItemData(BASE_ITEM_ID + 111, ItemClassification.useful),

    # Tunics
    "Shadow Cloak": ItemData(BASE_ITEM_ID + 120, ItemClassification.useful),
    "Fire Garment": ItemData(BASE_ITEM_ID + 121, ItemClassification.useful),
    "Onop Coat": ItemData(BASE_ITEM_ID + 122, ItemClassification.useful),
    "Performer Costume": ItemData(BASE_ITEM_ID + 123, ItemClassification.useful),
    "Merchants Robe": ItemData(BASE_ITEM_ID + 124, ItemClassification.useful),
    "Bunny Suit": ItemData(BASE_ITEM_ID + 125, ItemClassification.useful),
    "Forest Tunic": ItemData(BASE_ITEM_ID + 126, ItemClassification.useful),
    "Pure Shadow": ItemData(BASE_ITEM_ID + 127, ItemClassification.useful),
    "Silver Cloak": ItemData(BASE_ITEM_ID + 128, ItemClassification.useful),
    "Golden Robe": ItemData(BASE_ITEM_ID + 129, ItemClassification.useful),
    "Steam Worker Tunic": ItemData(BASE_ITEM_ID + 130, ItemClassification.useful),
    "Thiefs Cloak": ItemData(BASE_ITEM_ID + 131, ItemClassification.useful),
    "Sect Member": ItemData(BASE_ITEM_ID + 132, ItemClassification.useful),
    "Pumpkin": ItemData(BASE_ITEM_ID + 133, ItemClassification.useful),
    "Galaxy": ItemData(BASE_ITEM_ID + 134, ItemClassification.useful),
    "Banana King": ItemData(BASE_ITEM_ID + 135, ItemClassification.useful),
    "Red": ItemData(BASE_ITEM_ID + 136, ItemClassification.useful),
    "Yellow": ItemData(BASE_ITEM_ID + 137, ItemClassification.useful),
    "Green": ItemData(BASE_ITEM_ID + 138, ItemClassification.useful),
    "Grey": ItemData(BASE_ITEM_ID + 139, ItemClassification.useful),
    "Violet": ItemData(BASE_ITEM_ID + 140, ItemClassification.useful),
    "Light Blue": ItemData(BASE_ITEM_ID + 141, ItemClassification.useful),
    "Rainbow": ItemData(BASE_ITEM_ID + 142, ItemClassification.useful),
    "Lila": ItemData(BASE_ITEM_ID + 143, ItemClassification.useful),
    "Royal": ItemData(BASE_ITEM_ID + 144, ItemClassification.useful),
    "Aqua": ItemData(BASE_ITEM_ID + 145, ItemClassification.useful),
    "Orange": ItemData(BASE_ITEM_ID + 146, ItemClassification.useful),
    "Alpha Umbra": ItemData(BASE_ITEM_ID + 147, ItemClassification.useful),

    # Spirits - sample of major ones
    #"Faras Grace": ItemData(BASE_ITEM_ID + 160, ItemClassification.useful),
    #"Hammer King": ItemData(BASE_ITEM_ID + 161, ItemClassification.useful),
    #"Holy Centry": ItemData(BASE_ITEM_ID + 162, ItemClassification.useful),
    #"River Spirit": ItemData(BASE_ITEM_ID + 163, ItemClassification.useful),
    #"Angry Ambusher": ItemData(BASE_ITEM_ID + 164, ItemClassification.useful),
    #"Forest Guardian": ItemData(BASE_ITEM_ID + 165, ItemClassification.useful),
    #"Toxic Rat": ItemData(BASE_ITEM_ID + 166, ItemClassification.useful),
    #"Storm Centry": ItemData(BASE_ITEM_ID + 167, ItemClassification.useful),
    #"Blood Phantom": ItemData(BASE_ITEM_ID + 168, ItemClassification.useful),
    #"Frozen Soul": ItemData(BASE_ITEM_ID + 169, ItemClassification.useful),
}

# Filler items - common ore/consumables
filler_items = {
    # Ores
    "Ruby Ore": ItemData(BASE_ITEM_ID + 200, ItemClassification.filler, 0),
    "Sapphire Ore": ItemData(BASE_ITEM_ID + 201, ItemClassification.filler, 0),
    "Emerald Ore": ItemData(BASE_ITEM_ID + 202, ItemClassification.filler, 0),
    "Void Ore": ItemData(BASE_ITEM_ID + 203, ItemClassification.filler, 0),

    # Consumables
    #"Fire Essence": ItemData(BASE_ITEM_ID + 210, ItemClassification.filler, 0),
    #"Apple": ItemData(BASE_ITEM_ID + 211, ItemClassification.filler, 0),
    #"Rotten Apple": ItemData(BASE_ITEM_ID + 212, ItemClassification.filler, 0),
    #"Rice": ItemData(BASE_ITEM_ID + 213, ItemClassification.filler, 0),
    #"Rare Cheese": ItemData(BASE_ITEM_ID + 214, ItemClassification.filler, 0),
    #"Seagul Soup": ItemData(BASE_ITEM_ID + 215, ItemClassification.filler, 0),
    #"Flesh Eater": ItemData(BASE_ITEM_ID + 216, ItemClassification.filler, 0),
    #"Ice Crystal": ItemData(BASE_ITEM_ID + 217, ItemClassification.filler, 0),
    #"Boot": ItemData(BASE_ITEM_ID + 218, ItemClassification.filler, 0),
    #"Sand Relic": ItemData(BASE_ITEM_ID + 219, ItemClassification.filler, 0),
    #"Dead Rat": ItemData(BASE_ITEM_ID + 220, ItemClassification.filler, 0),

    # Money/currency
    #"Ore": ItemData(BASE_ITEM_ID + 230, ItemClassification.filler, 0),

    # Emotes and misc
    #"Duck": ItemData(BASE_ITEM_ID + 240, ItemClassification.filler, 0),
}

# Trap items
trap_items = {
    "Speed Change Trap": ItemData(BASE_ITEM_ID + 260, ItemClassification.trap, 0),
}

# Junk weights for randomization
junk_weights = {
    "Ruby Ore": 15,
    "Sapphire Ore": 20,
    "Emerald Ore": 10,
    "Fire Essence": 5,
    "Apple": 8,
    "Rice": 5,
    "Rare Cheese": 3,
    "Seagul Soup": 2,
    "Flesh Eater": 2,
    "Ice Crystal": 3,
    "Boot": 2,
    "Sand Relic": 5,
    "Dead Rat": 3,
    "Ore": 20,
    "Duck": 10,
    "Void Ore": 5,
}

trap_weights = {
    "Speed Change Trap": 100,
}

# Combine all item dictionaries
item_table = {
    **progression_items,
    **useful_items,
    **equipment_items,
    **filler_items,
    **trap_items,
}
