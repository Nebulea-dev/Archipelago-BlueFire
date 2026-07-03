from BaseClasses import ItemClassification
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .Subclasses import ItemDict

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
    None, # Skip the Empty emote
]


def get_weapon_items(progressive_weapons: bool) -> List["ItemDict"]:
    """Build weapon items list conditionally based on progressive weapons option."""
    if progressive_weapons:
        return []

    return [
        None, # Skip the Dual Blades
        {"name": "Bloodstorm Blades", "count": 1, "classification": ItemClassification.useful},
        {"name": "Diamond Wings", "count": 1, "classification": ItemClassification.useful},
        {"name": "Shadow Casters", "count": 1, "classification": ItemClassification.useful},
        {"name": "Ember Twins", "count": 1, "classification": ItemClassification.useful},
        # Needed to repair the boilers
        {"name": "Iron Justice", "count": 1, "classification": ItemClassification.progression},
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

# TODO: Review and remove spirit items that no longer exist in the current game version
spirit_items: List["ItemDict"] = [
    {"name": "Faras Grace Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Hammer King Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Holy Centry Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "River Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Angry Ambusher Spirit", "count": 1, "classification": ItemClassification.useful},
    None, # Skip Secret Fruit Spirit
    None, # Skip Mind Controller Spirit
    {"name": "Frozen Soul Spirit", "count": 1, "classification": ItemClassification.useful},
    None, # Skip Howling Tree Spirit
    {"name": "Love Flower Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Storm Centry Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Blood Phantom Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Possessed Book Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Forest Guardian Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Moi The Dreadful Spirit", "count": 1, "classification": ItemClassification.useful},
    None, # Skip Stone Hunter Spirit
    {"name": "Golden Lust Spirit", "count": 1, "classification": ItemClassification.useful},
    None, # Skip the Spring Warrior Spirit
    {"name": "Onop Siblings Spirit", "count": 1, "classification": ItemClassification.useful},
    None, # Skip Candle Onop Spirit
    None, # Skip Stone Warrior Spirit
    {"name": "Toxic Rat Spirit", "count": 1, "classification": ItemClassification.useful},
    None, # Skip Summoned God Spirit
    None, # Skip Summoning Hand Spirit
    None, # Skip Betting Hand Spirit
    {"name": "Life Steal Spirit", "count": 1, "classification": ItemClassification.useful},
    None, # Skip Shadow Demon Spirit
    {"name": "Shadow Gru Spirit", "count": 1, "classification": ItemClassification.useful},
    {"name": "Flying Onop Spirit", "count": 1, "classification": ItemClassification.useful},
    None, # Skip Toxic Water Spirit
]


ability_items: List["ItemDict"] = [
    None, # Skip the Attack
    None, # Skip the Dash
    {"name": "Double Jump Ability", "count": 1, "classification": ItemClassification.progression},
    {"name": "Wall Run Ability", "count": 1, "classification": ItemClassification.progression},
    {"name": "Sprint Ability", "count": 1, "classification": ItemClassification.progression},
    None, # Skip the Down Smash
    {"name": "Spell Ability", "count": 1, "classification": ItemClassification.progression},
    None, # Skip the Grind Ability
    {"name": "Block Ability", "count": 1, "classification": ItemClassification.progression},
    {"name": "Spin Attack Ability", "count": 1, "classification": ItemClassification.progression},
]

regular_items: List["ItemDict"] = [
    None,  # NewEnumerator0 (Large Pouch) = ID 0 | passive item
    None,  # NewEnumerator1 (SmallPouch) = ID 1
    None,  # NewEnumerator6 (Old Key) = ID 2
    None,  # NewEnumerator12 (----) = ID 3 - Padding separation
    None,  # NewEnumerator15 (KinbankDebitCard) = ID 4 - Skip
    None,  # NewEnumerator18 (Sanctuary Stone) = ID 5
    None,  # NewEnumerator19 (Rare Key) = ID 6
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
    None,  # NewEnumerator7 (Book) = ID 17 | passive item
    None,  # NewEnumerator14 (Boot) = ID 18 - Skip
    None,  # NewEnumerator17 (IceCrystal) = ID 19 - Skip
    {"name": "Ruby Ore", "count": 1, "repeatable": True, "classification": ItemClassification.filler},  # NewEnumerator24 = ID 20 | active item
    {"name": "Sapphire Ore", "count": 1, "repeatable": True, "classification": ItemClassification.filler},  # NewEnumerator25 = ID 21 | active item
    {"name": "Emerald Ore", "count": 1, "repeatable": True, "classification": ItemClassification.filler},  # NewEnumerator31 = ID 22 | active item
    None,  # NewEnumerator27 (BremurPicture) = ID 23 - Skip
    None,  # NewEnumerator28 (OddRock) = ID 24 - Skip
    None,  # NewEnumerator29 (Souls) = ID 25 - Skip
    None,  # NewEnumerator30 (SandRelic) = ID 26 - Skip
    None,  # NewEnumerator9 (Rose) = ID 27
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
    None,  # NewEnumerator71 (Key Fire Master) = ID 56 | passive item
    None,  # NewEnumerator72 (Key Holy Master) = ID 57 | passive item
    None,  # NewEnumerator73 (Key Ice Master) = ID 58 | passive item
    None,  # NewEnumerator74 (Key Death Master) = ID 59 | passive item
    None,  # NewEnumerator75 (Key Uthas Temple) = ID 60 | passive item
    None,  # NewEnumerator76 (Key God Master) = ID 61 | passive item
    None,  # NewEnumerator77 (Key Steam) = ID 62 | passive item
    None,  # NewEnumerator78 (Key Graveyard Key) = ID 63 | passive item
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
    {"name": "Void Ore", "count": 1, "repeatable": True, "classification": ItemClassification.filler},  # NewEnumerator90 = ID 74 | active item
    None,  # NewEnumerator91 (Extra Large Pouch) = ID 75 | passive item
    None,  # NewEnumerator92 (Mana) = ID 76 - Skip
    None,  # NewEnumerator93 (GuardianSoul) = ID 77 - Skip
    None,  # NewEnumerator94 (CovenantSoul) = ID 78 - Skip
    None,  # NewEnumerator95 (GuardianKey) = ID 79 - Skip
    None,  # NewEnumerator96 (Duck) = ID 80 - Skip
    None,  # NewEnumerator97 (RobiBadge) = ID 81 - Skip
]

def get_key_items(progressive_pouches: bool) -> List["ItemDict"]:
    """Build key_items list conditionally based on progressive pouches option."""
    return [

        None if progressive_pouches else {"name": "Large Pouch", "count": 1, "classification": ItemClassification.useful},  # NewEnumerator0 = ID 0
        None,  # NewEnumerator1 (SmallPouch) = ID 1
        {"name": "Old Key", "count": 8, "classification": ItemClassification.progression},  # NewEnumerator6 = ID 2
        None,  # NewEnumerator12 (----) = ID 3 - Padding separation
        None,  # NewEnumerator15 (KinbankDebitCard) = ID 4 - Skip
        {"name": "Sanctuary Stone", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator18 = ID 5
        None,  # NewEnumerator19 (RareKey) = ID 6 - Skip
        None,  # NewEnumerator32 (ShadowFragment) = ID 7 - Skip
        None,  # NewEnumerator22 (PureShadowCatcher) = ID 8 - Skip
        None,  # NewEnumerator33 (BlackFire) = ID 9 - Skip
        None,  # NewEnumerator35 (Coin) = ID 10 - Skip
        None,  # NewEnumerator36 (VoidShards) = ID 11 - Skip
        None,  # NewEnumerator41 (HolyBlessing) = ID 12 - Skip
        None,  # NewEnumerator49 (SpiritCatcher) = ID 13 - Skip
        None,  # NewEnumerator50 (HouseKey) = ID 14 - Skip
        None,  # NewEnumerator23 (-------------) = ID 15 - Padding separation
        None,  # NewEnumerator39 (FireEssence) = ID 16
        {"name": "Book", "count": 5, "classification": ItemClassification.progression},  # NewEnumerator7 = ID 17 | passive item
        None,  # NewEnumerator14 (Boot) = ID 18 - Skip
        None,  # NewEnumerator17 (IceCrystal) = ID 19 - Skip
        None,  # NewEnumerator24 (Ruby Ore) = ID 20 | active item
        None,  # NewEnumerator25 (Sapphire Ore) = ID 21 | active item
        None,  # NewEnumerator31 (Emerald Ore) = ID 22 | active item
        None,  # NewEnumerator27 (BremurPicture) = ID 23 - Skip
        None,  # NewEnumerator28 (OddRock) = ID 24 - Skip
        None,  # NewEnumerator29 (Souls) = ID 25 - Skip
        None,  # NewEnumerator30 (SandRelic) = ID 26 - Skip
        {"name": "Rose", "count": 1, "classification": ItemClassification.useful},  # NewEnumerator9 = ID 27 | passive item
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
        {"name": "Key of Ember", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator71 = ID 56 | passive item
        {"name": "Holy Key", "count": 3, "classification": ItemClassification.progression},  # NewEnumerator72 = ID 57 | passive item
        {"name": "Key Ice Master", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator73 = ID 58 | passive item
        {"name": "Key Death Master", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator74 = ID 59 | passive item
        {"name": "Uthas Temple Key", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator75 = ID 60 | passive item
        {"name": "Key God Master", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator76 = ID 61 | passive item
        {"name": "Steam Key", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator77 = ID 62 | passive item
        {"name": "Graveyard Key", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator78 = ID 63 | passive item
        None,  # NewEnumerator79 (HouseContract) = ID 64 - Skip
        None,  # NewEnumerator80 (Mandoline) = ID 65 - Skip
        None,  # NewEnumerator81 (RareGlasses) = ID 66 - Skip
        None,  # NewEnumerator83 (RareSnow) = ID 67 - Skip
        None,  # NewEnumerator84 (ComposerLetter) = ID 68 - Skip
        None,  # NewEnumerator85 (Sprint) = ID 69 - Skip
        {"name": "Beira Vessel", "count": 1, "classification": ItemClassification.progression},  # NewEnumerator86 = ID 70 | passive item
        None,  # NewEnumerator87 (BeiraShards) = ID 71 - Skip
        None,  # NewEnumerator88 (BasicPouch) = ID 72 - Skip
        {"name": "Fire Essence Slot", "count": 3, "classification": ItemClassification.useful},  # NewEnumerator89 = ID 73 | passive item
        None,  # NewEnumerator90 (Void Ore) = ID 74 | active item
        None if progressive_pouches else {"name": "Extra Large Pouch", "count": 1, "classification": ItemClassification.useful},  # NewEnumerator91 = ID 75
        None,  # NewEnumerator92 (Mana) = ID 76 - Skip
        None,  # NewEnumerator93 (GuardianSoul) = ID 77 - Skip
        None,  # NewEnumerator94 (CovenantSoul) = ID 78 - Skip
        None,  # NewEnumerator95 (GuardianKey) = ID 79 - Skip
        None,  # NewEnumerator96 (Duck) = ID 80 - Skip
        None,  # NewEnumerator97 (RobiBadge) = ID 81 - Skip
    ]


def get_progressive_items(progressive_pouches: bool, progressive_weapons: bool) -> List["ItemDict"]:
    """Build progressive items list conditionally based on progressive pouches and weapons options."""
    return [
        {"name": "Progressive Pouch", "count": 2, "classification": ItemClassification.useful} if progressive_pouches else None,
        {"name": "Progressive Weapon", "count": 11, "classification": ItemClassification.progression} if progressive_weapons else None,
    ]


def get_all_items(progressive_pouches: bool, progressive_weapons: bool = False) -> List["ItemDict"]:
    """Build the complete items list, conditionally including progressive or regular pouches and weapons."""
    weapon_items_list = get_weapon_items(progressive_weapons)
    key_items_list = get_key_items(progressive_pouches)
    progressive_items_list = get_progressive_items(progressive_pouches, progressive_weapons)
    return (
        emote_items +
        weapon_items_list +
        tunic_items +
        spirit_items +
        ability_items +
        regular_items +
        key_items_list +
        progressive_items_list
    )

