from BaseClasses import ItemClassification
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .subclasses import ItemDict

base_id = 437000

useful_skip_balancing: ItemClassification = ItemClassification(
    ItemClassification.useful + ItemClassification.skip_balancing
)
useful_progression: ItemClassification = ItemClassification(ItemClassification.progression + ItemClassification.useful)


emote_items: List["ItemDict"] = [
    {"name": "Wave Emote", "count": 1, "classification": ItemClassification.progression},
    {"name": "Applause Emote", "count": 1, "classification": ItemClassification.progression},
    {"name": "Levitation Emote", "count": 1, "classification": ItemClassification.progression},
    {"name": "Windmill Emote", "count": 1, "classification": ItemClassification.progression},
    {"name": "Hat Kid Emote", "count": 1, "classification": ItemClassification.progression},
    {"name": "Triceps Emote", "count": 1, "classification": ItemClassification.progression},
    {"name": "Aggressive Emote", "count": 1, "classification": ItemClassification.progression},
    {"name": "No Emote", "count": 1, "classification": ItemClassification.progression},
    {"name": "Photo Emote", "count": 1, "classification": ItemClassification.progression},
    {"name": "Celebration Emote", "count": 1, "classification": ItemClassification.progression},
    {"name": "Kung Fu Emote", "count": 1, "classification": ItemClassification.progression},
    {"name": "Techno Emote", "count": 1, "classification": ItemClassification.progression},
    {"name": "Party Emote", "count": 1, "classification": ItemClassification.progression},
    {"name": "Hello Emote", "count": 1, "classification": ItemClassification.progression},
    {"name": "Empty Emote", "count": 1, "classification": ItemClassification.progression}, # TODO : I don't think that's a real emote
]


weapon_items: List["ItemDict"] = [
    None, # Skip the Dual Blades
    {"name": "Bloodstorm Blades", "count": 1, "classification": ItemClassification.useful},
    {"name": "Diamond Wings", "count": 1, "classification": ItemClassification.useful},
    {"name": "Shadow Casters", "count": 1, "classification": ItemClassification.useful},
    {"name": "Ember Twins", "count": 1, "classification": ItemClassification.useful},
    {"name": "Iron Justice", "count": 1, "classification": ItemClassification.useful},
    {"name": "Ice Destroyers", "count": 1, "classification": ItemClassification.useful},
    {"name": "Peace Keepers", "count": 1, "classification": ItemClassification.useful},
    {"name": "Steel Shanks", "count": 1, "classification": ItemClassification.useful},
    {"name": "Breemur Family Swords", "count": 1, "classification": ItemClassification.useful},
    {"name": "Silver Blades", "count": 1, "classification": ItemClassification.useful},
    {"name": "Kina Defenders", "count": 1, "classification": ItemClassification.useful},
]


tunic_items: List["ItemDict"] = [
    None, # Skip the Shadow Cloack
    {"name": "Fire Garment Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Onop Coat Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Performer Costume Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Merchants Robe Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Bunny Suit Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Forest Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Pure Shadow Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Silver Cloack Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Golden Robe Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Steam Worker Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Thiefs Cloack Tunic", "count": 1, "classification": ItemClassification.filler},
    None, # Skip the empty Tunic
    {"name": "Sect Member Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Pumpkin Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Galaxy Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Banana King Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Red Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Yellow Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Green Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Grey Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Violet Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Light Blue Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Rainbow Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Lila Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Royal Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Aqua Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Orange Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Void Master Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Duck Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Cursed Duck Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Alpha Umbra Tunic", "count": 1, "classification": ItemClassification.filler},
    {"name": "Discord Winner Contest Tunic", "count": 1, "classification": ItemClassification.filler},
]


spirit_items: List["ItemDict"] = [
    {"name": "Faras Grace Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Hammer King Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Holy Centry Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "River Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Angry Ambusher Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Secret Fruit Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Mind Controller Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Frozen Soul Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Howling Tree Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Love Flower Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Storm Centry Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Blood Phantom Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Possessed Book Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Forest Guardian Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Onop Siblings Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Moi The Dreadful Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Stone Hunter Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Golden Lust Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Candle Onop Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Stone Warrior Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Toxic Rat Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Summoned God Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Summoning Hand Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Life Steal Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Shadow Demon Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Shadow Gru Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Flying Onop Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Toxic Water Spirit", "count": 1, "classification": ItemClassification.useful},
]


ability_items: List["ItemDict"] = [
    {"name": "Double Jump Ability", "count": 1, "classification": ItemClassification.progression},
    None, # Skip the Dash
    None, # Skip the Attack
    {"name": "Down Smash Ability", "count": 1, "classification": ItemClassification.progression},
    {"name": "Wall Run Ability", "count": 1, "classification": ItemClassification.progression},
    {"name": "Grind Ability", "count": 1, "classification": ItemClassification.progression},
    {"name": "Sprint Ability", "count": 1, "classification": ItemClassification.progression},
    {"name": "Spell Ability", "count": 1, "classification": ItemClassification.progression},
    {"name": "Block Ability", "count": 1, "classification": ItemClassification.progression},
    {"name": "Spin Attack Ability", "count": 1, "classification": ItemClassification.progression},
]


regular_items: List["ItemDict"] = [
    {"name": "Large Pouch", "count": 1, "classification": ItemClassification.useful},
    None, # Skip small pouch
    {"name": "Old Key", "count": 5, "classification": ItemClassification.progression},
    {"name": "Book", "count": 5, "classification": ItemClassification.progression},
    {"name": "Rose", "count": 1, "classification": ItemClassification.useful},
    None, # Skip ----- separation
    None, # Skip Boot
    None, # Skip Kinbank Credit Card
    None, # Skip Ice Crystal
    {"name": "Sanctuary Stone", "count": 1, "classification": ItemClassification.progression},
    {"name": "Rare Key", "count": 5, "classification": ItemClassification.progression},
    None, # Skip Pure Shadow Catcher
    None, # Skip --------------- separation
    {"name": "Ruby Ore", "count": 1, "classification": ItemClassification.useful},
    {"name": "Sapphire Ore", "count": 1, "classification": ItemClassification.useful},
    None, # Skip Dead Rat
    None, # Skip Bremur Picture
    None, # Skip Odd Rock
    None, # Skip Souls
    None, # Skip Sand Relic
    {"name": "Emerald Ore", "count": 1, "classification": ItemClassification.useful},
    None, # Skip Shadow Fragment
    None, # Skip Black Fire
    None, # Skip Abyss Potion
    None, # Skip Coin
    None, # Skip Void Shards
    None, # Skip Fire Essence
    None, # Skip Shadow Potion
    None, # Skip Holy Blessing
    None, # Skip Rice
    None, # Skip Carrot Potion
    None, # Skip Apple
    None, # Skip Rotten Apple
    None, # Skip Medicine
    None, # Skip Spirit Catcher
    None, # Skip House Key
    None, # Skip Life Elixir
    None, # Skip Royal Elixir
    None, # Skip Boulder Powder
    None, # Skip Rare Cheese
    None, # Skip Seagul Soup
    None, # Skip Flesh Eater
    None, # Skip Shard Cluster
    None, # Skip Forest Bug
    None, # Skip Poisoned Plant
    None, # Skip --------------- separation
    None, # Skip Dash
    None, # Skip Double Jump
    None, # Skip Spin Attack
    None, # Skip Wall Run
    None, # Skip Fire Ball
    None, # Skip Down Smash
    None, # Skip Shield
    None, # Skip Spirit Slot
    None, # Skip Void Key
    None, # Skip Necklace
    {"name": "Key Fire Master", "count": 1, "classification": ItemClassification.progression},
    {"name": "Key Holy Master", "count": 1, "classification": ItemClassification.progression},
    {"name": "Key Ice Master", "count": 1, "classification": ItemClassification.progression},
    {"name": "Key Death Master", "count": 1, "classification": ItemClassification.progression},
    {"name": "Key Uthas Temple", "count": 1, "classification": ItemClassification.progression},
    {"name": "Key God Master", "count": 1, "classification": ItemClassification.progression},
    {"name": "Key Steam", "count": 1, "classification": ItemClassification.progression},
    {"name": "Key Graveyard Key", "count": 1, "classification": ItemClassification.progression},
    None, # Skip House Contract
    None, # Skip Mandoline
    None, # Skip Rare Glasses
    None, # Skip Rare Snow
    None, # Skip Composer Letter
    None, # Skip Sprint
    None, # Skip Beira Vessel
    None, # Skip Beira Shards
    None, # Skip Basic Pouch
    None, # Skip Fire Essence Slot
    {"name": "Void Ore", "count": 1, "classification": ItemClassification.useful},
    {"name": "Extra Large Pouch", "count": 1, "classification": ItemClassification.useful},
    None, # Skip Mana
    None, # Skip Guardian Soul
    None, # Skip Covenant Soul
    None, # Skip Guardian Key
    None, # Skip Duck
    None, # Skip Robi Badge
]


all_items: List["ItemDict"] = (
    emote_items +
    weapon_items +
    tunic_items +
    regular_items +
    ability_items +
    regular_items
)
