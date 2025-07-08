"""
Practice choosing the right class attribute access method based on design intent.

Requirements:
- Create a `GameCharacter` class with:
  - Class attributes: `max_level = 50`, `base_stats = {"strength": 10, "magic": 5}`
  - Instance attributes: `name`, `current_level` (set in __init__)
  - Method `level_progress()` that returns "{name} is level {current_level} of {?} max"
  - Method `get_stat(stat_name)` that returns base_stats[stat_name]

- Create a `Warrior` class that inherits from `GameCharacter`:
  - Class attribute: `base_stats = {"strength": 15, "magic": 3}` (warrior-specific stats)
  - DO NOT define __init__ (inherit automatically)
  - Add method `strength_bonus()` that calculates current_level * {?} strength stat

- Create a `Mage` class that inherits from `GameCharacter`:
  - Class attribute: `max_level = 60` (mages can level higher)
  - DO NOT define __init__ (inherit automatically)  
  - Add method `spell_power()` that calculates current_level * {?} magic stat
  - Add method `check_global_level_cap()` that returns the original game's max_level

YOUR TASK: For each {?}, choose ONE of these approaches and justify why:
- self.attribute
- self.__class__.attribute  
- GameCharacter.attribute

Consider: Should subclasses be able to override? Do you want original or specific values?

Test Scenario:
warrior = Warrior("Conan", 25)
mage = Mage("Gandalf", 45)

# Your implementations will determine these outputs:
print(warrior.level_progress())         # What max_level should show?
print(warrior.strength_bonus())         # Which strength value to use?
print(mage.spell_power())               # Which magic value to use?
print(mage.check_global_level_cap())    # Which max_level to return?
"""

class GameCharacter:
    max_level = 50
    base_stats = {"strength": 10, "magic": 5}

    def __init__(self, name, current_level):
        self.name = name
        self.current_level = current_level

    def level_progress(self):
        return f"{self.name} is level {self.current_level} of {self.__class__.max_level} max" 
        # should be only overridable by a sublcass (all Warriors and Mages share the same max level I assume?)
        # max level should not be overridden by any instance, they all need to adhere to the max level
    
    def get_stat(self, stat_name):
        return self.base_stats[stat_name] 
        # should be overridable by a GameCharacter instance and a child/subclass
        # return self.__class_.base_stats[stat_name] alternatively, if this will be only overridable by a parent class NOT an instance 
        # but I assume that every instance could change their stats, so follow the hierarchy (instance -> class -> parent class)
    
class Warrior(GameCharacter):
    base_stats = {"strength": 15, "magic": 3}

    def strength_bonus(self):
        return self.current_level * self.__class__.base_stats["strength"] 
        # self.current_level because that is defined in the GameCharacter class and could be overriden by any instance
        # self.__class__.base_stats because you want this specific subclass attribute
        # this bonus will apply to all warrior instances, so you always need to get this subclasses magic base state

class Mage(GameCharacter):
    max_level = 60

    def spell_power(self):
        return self.current_level * self.__class__.base_stats["magic"]
        # self.current_level because that is defined in the GameCharacter class and could be overriden by an instance
        # self.__class__.base_stats because you want this specific subclass attribute - theyre not defined in this case, but could be 
        # since they're not not special attributes for the Mage you could also just do GameCharacter.base_stats but this is less flexible
        # most likely mages should get an extra bonus for magic base stat over any base stat
    
    def check_global_level_cap(self):
        return GameCharacter.max_level # always return the max level from the GameCharacter class

#Test cases with the above design choices:
warrior = Warrior("Conan", 25)
mage = Mage("Gandalf", 45)

print(warrior.level_progress())         # "Conan is level 25 of 50 max"
print(warrior.strength_bonus())         # 375 (25 * 15)
print(mage.spell_power())              # 225 (45 * 5) 
print(mage.check_global_level_cap())    # 50