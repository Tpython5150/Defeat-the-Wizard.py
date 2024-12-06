from random import randint
# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.special_ability_1 = None
        self.special_ability_1 = None  
        self.is_invincible = False
        self.turn_counter = 0
        
    def attack(self, opponent, damage):
        if opponent.is_invincible:
            damage = 0
            opponent.is_invincible = False
        else:
            opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")
            
    def use_special_abilities(self, opponent):
        print("Choose a special ability to use: ")
        print(f"1. {self.special_ability_1.name}")
        print(f"2. {self.special_ability_2.name}")
        choice = input()
        if(choice == '1'):
            self.special_ability_1.activate(self, opponent)
        elif(choice == '2'):
            self.special_ability_2.activate(self, opponent)
        else:
            print("Invalid input. Choose 1 of 2 abilities!")
            
    def autouse_special_abilities(self, opponent):
        choice = randint(1, 2)
        if(choice == '1'):
            print(f"{self.name} uses {self.special_ability_1.name}")
            self.special_ability_1.activate(self, opponent)
        else:
            print(f"{self.name} uses {self.special_ability_2.name}")
            self.special_ability_2.activate(self, opponent)
        
    def heal(self, heal_amt):
        health_after_heal = self.health + heal_amt
        if(health_after_heal > self.max_health):
            self.health = self.max_health
        else:
            self.health = health_after_heal
        print(f"{self.name} heals for {heal_amt} health points!")
        self.is_invincible = True            
    def display_stats(self):
        self.is_invincible = True
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    
# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.special_ability_1 = SupermanPunch()
        self.special_ability_2 = DoubleBlock()
        

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.special_ability_1 = BlackOutSpell()
        self.special_ability_2 = Invisibility()

             
# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
        self.special_ability_1 = Thunder()
        self.special_ability_2 = ManaShield()
        
    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}.")
    

# Create Archer class
class Archer(Character):
    def __init__(self, name ):
        super().__init__(name, health=110, attack_power=65)
        self.special_ability_1 = DoubleShot()
        self.special_ability_2 = Evade()

            
# Create Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=75, attack_power=65) 
        self.special_ability_1 = HolyStrike()
        self.special_ability_2 = DivineShield()
        
# Base class for special abilities
class SpecialAbility:
    def __init__(self, name, description):
       self.name = name
       self.description = description 
       
    def activate(self, player, opponent):
        pass # Abstract method to be implememnted by subclass
    
    def activation_msg(self, player):
        print(f"{player.name} uses {self.name}!")  
##### Special Abilities #####

class DoubleShot(SpecialAbility): #Inherit from SpecialAbility
    def __init__(self):
        super().__init__(
            # Name
            "Double Shot",
            # Description
            "Deals double damage. (Archer)" 
        )

    # override
    def activate(self, player, opponent):
        self.activation_msg(player)
        player.attack(opponent, player.attack_power)
        player.attack(opponent, player.attack_power)
        print("Critical Hit!")

class Evade(SpecialAbility):
    def __init__(self):
        super().__init__(
            "Evade",
            "Evade the next attack. (Archer)"
        )

    def activate(self, player, opponent):
        self.activation_msg(player)
        player.is_invincible = True
        
class HolyStrike(SpecialAbility):
    def __init__(self):
        super().__init__(
            "Holy Strike",
            "Deals bonus damage. (Paladin)"
        )

    def activate(self, player, opponent):
        self.activation_msg(player)
        bonus_damage = randint(player.attack_power//2, player.attack_power)
        player.attack(opponent, player.attack_power + bonus_damage)
        print(f"{bonus_damage} bonus damage dealt!")        

class DivineShield(SpecialAbility):
    def __init__(self):
        super().__init__(
            "Divine Shield",
            "Block the next attack."
        )
        
    def activate(self, player, opponent):
        self.activation_msg(player)
        player.is_invincible = True
        
class SupermanPunch(SpecialAbility):
    def __init__(self):
        super().__init__(
            "Superman Punch",
            "Flying punch causing damage."
        )
        
    def activate(self, player, opponent):
        self.activation_msg(player)
        player.is_invincible = True
        player.attack(opponent, 5)
        
class DoubleBlock(SpecialAbility):
    def __init__(self):
        super().__init__(
            "Double Block",
            "Block the next attack."
        )
        
    def activate(self, player, opponent):
        self.activation_msg(player)
        player.is_invincible = True
        
class BlackOutSpell(SpecialAbility):
    def __init__(self):
        super().__init__(
            "Block Out Spell",
            "Makes oppenent, causes damage."
        )
        
    def activate(self, player, opponent):
        self.activation_msg(player)
        player.is_invincible = True
        player.attack(opponent, 2)
    

class Invisibility(SpecialAbility):
    def __init__(self):
        super().__init__(
            "Invisibility",
            "Player turn invisible avoiding next attack."
        )
        
    def activate(self, player, opponent):
        self.activation_msg(player)
        player.is_invincible = True    
        
class Thunder(SpecialAbility):
    def __init__(self):
        super().__init__(
            "Thunder",
            "Strikes a rondom number of times!"
    ) 
        
    def activate(self, player, opponent):
        self.activation_msg(player)
        strikes = randint(1, 5)
        for i in range(0, strikes):
            player.attack(opponent, player.attack_power)
        print(f"{player.name} hit {strikes} times!")

class ManaShield(SpecialAbility):
    def __init__(self):
        super().__init__(
            "Mana Shield",
            "Negates the next attack"
        )        
        
def activate(self, player, opponent):
        self.activation_msg(player)
        player.is_invincible = True
        
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    
    else:
        print("Invalid choice. Defaulting to Warrior.")
    return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        # player's turn
        while True: # Enables the player to schoose an action without taking damage
            print("\n--- Your Turn ---")
            print("1. Attack")
            print("2. Use Special Ability")
            print("3. Heal")
            print("4. View Stats")

            choice = input("Choose an action: ")

            if choice == '1':
                player.attack(wizard, randint(0, player.attack_power))
                break
            elif choice == '2':
                player.use_special_abilities(wizard)
                break
            elif choice == '3':
                player.heal(randint(1, wizard.attack_power))
                break
            elif choice == '4':
                player.display_stats()
                break
            else:
                print("Invalid choice. Try again.")
                
        # enemy's turn

        if wizard.health > 0:
            wizard.regenerate()
            wizard.turn_counter += 1
            wizard.turn_counter %= 3
            if wizard.turn_counter == 0:
                wizard.autouse_special_abilities(player)
            else:
                wizard.attack(player, randint(0, wizard.attack_power))
            
        # Check combantant's hps to display victory and defeat messages
        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

        if wizard.health <= 0:
            print(f"The wizard {wizard.name} has been defeated by {player.name}!")
            break
        
def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()