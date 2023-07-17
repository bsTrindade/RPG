class Character:
    base_attack = 0
    base_defense = 0
    base_hp = 0
    level = 1
    xp = 0
    char_name = "Character Class"
    name = "Player Name"

    ATTACK_MULTIPLIER_CONST = 0.5
    DEFENSE_MULTIPLIER_CONST = 0.4
    HP_MULTIPLIER_CONST = 4
    
    def __init__(self, name="Any", level=1):
        self.level = level
        self.name = name
        self.char_name = self.__class__.__name__
        self.set_status_based_on_level()

    def set_status_based_on_level(self):
        self.attack = self.base_attack * self.level * round(self.base_attack*self.ATTACK_MULTIPLIER_CONST)
        self.defense = self.base_defense * self.level * round(self.base_defense*self.DEFENSE_MULTIPLIER_CONST)
        self.hp = self.base_hp + self.HP_MULTIPLIER_CONST * (self.level - 1)

    def calculate_fight_xp(self):
        return 50 * (1 + ((self.level - 1) * ((1/100 * 10))))
    
    def necessary_xp_to_level_up(self):
        return 100 * (1 + ((self.level - 1) * ((1/100 * 15))))
    
    def earn_xp(self, earned_xp):
        self.xp += earned_xp
        necessary_exp = self.necessary_xp_to_level_up()
        if self.xp >= necessary_exp:
            extra_exp = self.xp - necessary_exp
            self.level_up(extra_exp)
    
    def level_up(self, extra_exp):
        self.level += 1
        self.xp = extra_exp
        self.set_status_based_on_level()