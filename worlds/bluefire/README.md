# Blue Fire Archipelago World

This is the complete Archipelago integration for Blue Fire, a challenging soulslike exploration platformer.

## Implementation Summary

### Items (100 total)
- **15 Progression Items**: Keys and essential abilities (Double Jump, Wall Run, Sprint, Shield, Sanctuary Stone, etc.)
- **68 Useful Items**: Equipment (weapons, tunics, spirits), quest items, and special consumables
- **17 Filler Items**: Common drops, ore, money
- **Trap Items**: Speed change traps (configurable)
- **1 Victory Item**: Placed at Queen Chamber location

### Locations (50+ total)
- **14 Game Regions** organized hierarchically:
  - Fire Keep (8 locations) - Starting area
  - Arcane Tunnels (4 locations)
  - Crossroads / Well (2 locations)
  - Stoneheart City (1 location)
  - Forest Temple (5 locations)
  - Temple Gardens (1 location)
  - Abandoned Path / Tower (2 locations)
  - Uthas Temple (7 locations)
  - Temple of Gods (2 locations)
  - Firefall River (4 locations)
  - Steam House (3 locations)
  - Iron Caves / Sirion (2 locations)
  - Waterway (3 locations)
  - Void Challenges (6 optional locations)

### File Structure

#### Core Implementation Files

**Types.py** - Data structures and custom classes
- `BluefireLocation` and `BluefireItem` - Game-specific location and item types
- `ItemData` and `LocData` - Data NamedTuples for item and location definitions
- `StartingLocation` enum - Player starting position options

**Items.py** - Item definitions and pool generation
- 100 items organized into progression, useful, equipment, and filler categories
- `create_itempool()` - Generates the complete item pool based on options
- `create_item()` - Factory function for creating individual items
- `create_junk_items()` - Randomized filler item generation with trap probability

**Locations.py** - Location definitions by game region
- 50+ locations organized by in-game area
- `get_location_names()` - Returns location name to AP code mapping
- `get_total_locations()` - Counts valid locations based on options
- `is_valid_location()` - Checks if a location should be included
- Support for optional void challenge locations

**Regions.py** - Game world topology
- 14 regions representing game areas
- Hierarchical region structure matching game geography
- Entrance connections between regions representing progression flow
- Automatic location assignment to regions

**Rules.py** - Progression logic and access requirements
- Region entrance requirements (items, abilities, locations needed to progress)
- Location-specific requirements for complex checks
- Softlock prevention via `forbid_item()` to prevent item traps
- Victory condition set on Queen Chamber location requiring major items

**Options.py** - Player configuration options
- `StartingLocation` - Choose starting position (Lab, Crossroads, or Fire Keep West)
- `ExtraLocations` - Toggle void challenge locations (default: enabled)
- `TrapChance` - Percentage of filler items that become traps (0-100%, default: 0%)
- `SpeedChangeTrapWeight` - Weight of speed change traps in trap pool

**__init__.py** - World orchestration
- `BluefireWorld` - Main world class implementing Archipelago interface
- Web setup with theme and tutorial links
- Methods for generation, item/region creation, and slot data
- Integration of all components

## Progression Logic

The world uses a simplified but meaningful progression system based on the original Blue Fire game:

### Key Progression Gates

1. **Fire Keep** - Accessible from start, teaches basic movement
2. **Arcane Tunnels** - Requires Fire Keep progression, branching point to multiple areas
3. **Crossroads** - Accessible from Fire Keep, leads to Stoneheart City
4. **Forest Temple** - Requires Wall Run and Old Key, teaches advanced platforming
5. **Uthas Temple** - Requires Uthas Key, introduces combat challenges
6. **Temple of Gods** - Requires God Master Key and Sanctuary Stone
7. **Iron Caves / Rust Village** - Requires Steam House progression and Iron Justice
8. **Queen Chamber (Victory)** - Requires Sanctuary Stone, all major keys, Wall Run

### Ability-Based Gating

- **Double Jump** - Unlocks platforming areas and shortcuts
- **Wall Run** - Essential for high-difficulty platforming sections
- **Sprint** - Required for end-game challenges
- **Shield** - Useful but not required for progression

### Item-Based Gating

- **Old Keys** - Access various locked rooms throughout the world
- **Sanctuary Stone** - Required for major temples and end-game content
- **Weapon Requirements** - Some locations accessible only with specific weapons

## Testing Checklist

- [x] All files have valid Python syntax
- [x] 100 items defined with unique AP codes
- [x] 50+ locations defined with unique AP codes
- [x] 14 regions created with proper connections
- [x] Progression rules set up for all major areas
- [x] Victory condition implemented on Queen Chamber
- [x] Softlock prevention via forbid_item()
- [x] Starting location option configurable
- [x] Void challenge locations optional
- [x] Trap probability configurable

## Known Limitations / Notes

1. **Movement Requirements Approximation**: The original Blue Fire randomizer uses detailed movement flag requirements (walljump levels, no_walljump flags, etc.). This Archipelago implementation approximates these as item requirements (having Double Jump ≈ level of walljump ability) for simplicity. Future versions could be more granular.

2. **Money/Currency**: The original game tracks currency and uses shops. This implementation does not currently track currency as a progression item, instead using key items for gating.

3. **Spirit System**: While spirits (summonable entities) are included as items, the progression logic doesn't require specific spirits for any locations. They're treated as useful equipment.

4. **Emotes**: Emotes (dances/animations) from the original game are not included in this implementation. Future versions could add these as condition items.

5. **NPC Quests**: Complex NPC dialogue chains and multi-step quests are simplified to location requirements.

## Future Enhancement Opportunities

- Add more granular movement ability levels
- Implement currency tracking for shop-based progression
- Add spirit-specific logic requirements
- Include emote items with their own progression logic
- Expand void challenge locations with more detail
- Add difficulty options (e.g., no double jump mode, limited movements)
- Create custom music/cosmetic item drops
- Implement map/fast travel logic

## Credits

Created for Archipelago Multiworld Randomizer
Based on Blue Fire by Robi Studios
Progression logic translated from blue-fire-rando project

---

For more information about Archipelago, visit: https://github.com/ArchipelagoMW/Archipelago
