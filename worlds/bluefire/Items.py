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
    {"name": "Iron Justice", "count": 1, "classification": ItemClassification.progression}, # Needed to repair the boilers
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

# TODO : Many of them are not in the game anymore, remove them
spirit_items: List["ItemDict"] = [
    {"name": "Faras Grace Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Hammer King Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Holy Centry Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "River Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Angry Ambusher Spirit", "count": 1, "classification": ItemClassification.useful},
    # Skip Secret Fruit Spirit
    # Skip Mind Controller Spirit
    {"name": "Frozen Soul Spirit", "count": 1, "classification": ItemClassification.useful},
    # Skip Howling Tree Spirit
    {"name": "Love Flower Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Storm Centry Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Blood Phantom Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Possessed Book Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Forest Guardian Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Onop Siblings Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Moi The Dreadful Spirit", "count": 1, "classification": ItemClassification.useful},
    # Skip Stone Hunter Spirit
    {"name": "Golden Lust Spirit", "count": 1, "classification": ItemClassification.useful},
    # Skip Candle Onop Spirit
    # Skip Stone Warrior Spirit
    {"name": "Toxic Rat Spirit", "count": 1, "classification": ItemClassification.useful},
    # Skip Summoned God Spirit
    # Skip Summoning Hand Spirit
    {"name": "Life Steal Spirit", "count": 1, "classification": ItemClassification.useful},
    # Skip Shadow Demon Spirit
    {"name": "Shadow Gru Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Flying Onop Spirit", "count": 1, "classification": ItemClassification.useful},
    # Skip Toxic Water Spirit
]


ability_items: List["ItemDict"] = [
    None, # Skip the Attack
    None, # Skip the Dash
    {"name": "Double Jump Ability", "count": 1, "classification": ItemClassification.progression},
    {"name": "Wall Run Ability", "count": 1, "classification": ItemClassification.progression},
    {"name": "Sprint Ability", "count": 1, "classification": ItemClassification.progression},
    None, # Skip the Down Smash
    {"name": "Spell Ability", "count": 1, "classification": ItemClassification.progression},
    {"name": "Grind Ability", "count": 1, "classification": ItemClassification.progression},
    {"name": "Block Ability", "count": 1, "classification": ItemClassification.progression},
    {"name": "Spin Attack Ability", "count": 1, "classification": ItemClassification.progression},
]


regular_items: List["ItemDict"] = [
    {"name": "Large Pouch", "count": 1, "classification": ItemClassification.useful},  # NewEnumerator0 = ID 0 | passive item
    None,  # NewEnumerator1 (SmallPouch) = ID 1
    {"name": "Old Key", "count": 5, "classification": ItemClassification.progression},  # NewEnumerator6 = ID 2
    None,  # NewEnumerator12 (----) = ID 3 - Padding separation
    None,  # NewEnumerator15 (KinbankDebitCard) = ID 4 - Skip
    {"name": "Sanctuary Stone", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator18 = ID 5
    {"name": "Rare Key", "count": 5, "classification": ItemClassification.progression},  # NewEnumerator19 = ID 6
    None,  # NewEnumerator32 (ShadowFragment) = ID 7 - Skip
    None,  # NewEnumerator22 (PureShadowCatcher) = ID 8 - Skip
    None,  # NewEnumerator33 (BlackFire) = ID 9 - Skip
    None,  # NewEnumerator35 (Coin) = ID 10 - Skip
    None,  # NewEnumerator36 (VoidShards) = ID 11 - Skip
    None,  # NewEnumerator41 (HolyBlessing) = ID 12 - Skip
    None,  # NewEnumerator49 (SpiritCatcher) = ID 13 - Skip
    None,  # NewEnumerator50 (HouseKey) = ID 14 - Skip
    None,  # NewEnumerator23 (-------------) = ID 15 - Padding separation
    None,  # NewEnumerator39 (FireEssence) = ID 16 - Skip
    {"name": "Book", "count": 5, "classification": ItemClassification.progression},  # NewEnumerator7 = ID 17 | passive item
    None,  # NewEnumerator14 (Boot) = ID 18 - Skip
    None,  # NewEnumerator17 (IceCrystal) = ID 19 - Skip
    {"name": "Ruby Ore", "count": 1, "classification": ItemClassification.useful},  # NewEnumerator24 = ID 20 | active item
    {"name": "Sapphire Ore", "count": 1, "classification": ItemClassification.useful},  # NewEnumerator25 = ID 21 | active item
    {"name": "Emerald Ore", "count": 1, "classification": ItemClassification.useful},  # NewEnumerator31 = ID 22 | active item
    None,  # NewEnumerator27 (BremurPicture) = ID 23 - Skip
    None,  # NewEnumerator28 (OddRock) = ID 24 - Skip
    None,  # NewEnumerator29 (Souls) = ID 25 - Skip
    None,  # NewEnumerator30 (SandRelic) = ID 26 - Skip
    {"name": "Rose", "count": 1, "classification": ItemClassification.useful},  # NewEnumerator9 = ID 27
    None,  # NewEnumerator34 (AbyssPotion) = ID 28 - Skip
    None,  # NewEnumerator40 (ShadowPotion) = ID 29 - Skip
    None,  # NewEnumerator44 (CarrotPotion) = ID 30 - Skip
    None,  # NewEnumerator42 (Rice) = ID 31 - Skip
    None,  # NewEnumerator45 (Apple) = ID 32 - Skip
    None,  # NewEnumerator46 (RottenApple) = ID 33 - Skip
    None,  # NewEnumerator47 (Medicine) = ID 34 - Skip
    None,  # NewEnumerator51 (LifeElixir) = ID 35 - Skip
    None,  # NewEnumerator52 (RoyalElixir) = ID 36 - Skip
    None,  # NewEnumerator53 (BoulderPowder) = ID 37 - Skip
    None,  # NewEnumerator54 (RareCheese) = ID 38 - Skip
    None,  # NewEnumerator55 (SeagulSoup) = ID 39 - Skip
    None,  # NewEnumerator56 (FleshEater) = ID 40 - Skip
    None,  # NewEnumerator57 (ShardCluster) = ID 41 - Skip
    None,  # NewEnumerator58 (ForestBug) = ID 42 - Skip
    None,  # NewEnumerator26 (DeadRat) = ID 43 - Skip
    None,  # NewEnumerator59 (PoisonedPlant) = ID 44 - Skip
    None,  # NewEnumerator60 (---------------) = ID 45 - Padding separation
    None,  # NewEnumerator61 (Dash) = ID 46 - Skip
    None,  # NewEnumerator62 (DoubleJump) = ID 47 - Skip
    None,  # NewEnumerator63 (SpinAttack) = ID 48 - Skip
    None,  # NewEnumerator64 (WallRun) = ID 49 - Skip
    None,  # NewEnumerator65 (FireBall) = ID 50 - Skip
    None,  # NewEnumerator66 (DownSmash) = ID 51 - Skip
    None,  # NewEnumerator67 (Shield) = ID 52 - Skip
    None,  # NewEnumerator68 (SpiritSlot) = ID 53 - Skip
    None,  # NewEnumerator69 (VoidKey) = ID 54 - Skip
    None,  # NewEnumerator70 (Necklace) = ID 55 - Skip
    {"name": "Key Fire Master", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator71 = ID 56 | passive item
    {"name": "Key Holy Master", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator72 = ID 57 | passive item
    {"name": "Key Ice Master", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator73 = ID 58 | passive item
    {"name": "Key Death Master", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator74 = ID 59 | passive item
    {"name": "Key Uthas Temple", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator75 = ID 60 | passive item
    {"name": "Key God Master", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator76 = ID 61 | passive item
    {"name": "Key Steam", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator77 = ID 62 | passive item
    {"name": "Key Graveyard Key", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator78 = ID 63 | passive item
    None,  # NewEnumerator79 (HouseContract) = ID 64 - Skip
    None,  # NewEnumerator80 (Mandoline) = ID 65 - Skip
    None,  # NewEnumerator81 (RareGlasses) = ID 66 - Skip
    None,  # NewEnumerator83 (RareSnow) = ID 67 - Skip
    None,  # NewEnumerator84 (ComposerLetter) = ID 68 - Skip
    None,  # NewEnumerator85 (Sprint) = ID 69 - Skip
    None,  # NewEnumerator86 (BeiraVessel) = ID 70 - Skip
    None,  # NewEnumerator87 (BeiraShards) = ID 71 - Skip
    None,  # NewEnumerator88 (BasicPouch) = ID 72 - Skip
    None,  # NewEnumerator89 (FireEssenceSlot) = ID 73 - Skip
    {"name": "Void Ore", "count": 1, "classification": ItemClassification.useful},  # NewEnumerator90 = ID 74 | active item
    {"name": "Extra Large Pouch", "count": 1, "classification": ItemClassification.useful},  # NewEnumerator91 = ID 75 | passive item
    None,  # NewEnumerator92 (Mana) = ID 76 - Skip
    None,  # NewEnumerator93 (GuardianSoul) = ID 77 - Skip
    None,  # NewEnumerator94 (CovenantSoul) = ID 78 - Skip
    None,  # NewEnumerator95 (GuardianKey) = ID 79 - Skip
    None,  # NewEnumerator96 (Duck) = ID 80 - Skip
    None,  # NewEnumerator97 (RobiBadge) = ID 81 - Skip
]


all_items: List["ItemDict"] = (
    emote_items +
    weapon_items +
    tunic_items +
    spirit_items +
    ability_items +
    regular_items
)
