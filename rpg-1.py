"""In this simple RPG game, the hero fights the goblin. He has the options to:
1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee"""

print("=-=" * 20)
print("                         GAME TIME")
print("=-=" * 20)
print("\nRemember: YOU are the hero here.")
# create a main class to store info for all characters
class Character:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
        

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        enemy.health -= self.power
        return enemy.health

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.power} power.")


# create a main function
def main():

    goblin = Character(6, 2, "Globin")
    hero = Character(10, 5, "Hero")
    
    
    while goblin.alive() and hero.alive():
        user_input = int(input("\nWhat do you want to do?\n1. fight goblin\n2. do nothing\n3. flee\n> "))
        # Print hero and goblin status after each user input
        hero.print_status()
        goblin.print_status()
        if user_input == 1:
        # Hero attacks goblin
            hero.attack(goblin)
            if not hero.alive():
                print("\nYou are dead.")
            if goblin.health > 0:
        # Goblin attacks hero
                goblin.attack(hero)
            if not goblin.alive():
                print("\nGoblin is dead.")
            if goblin.alive():
                print("\nGoblin still in the game. Watch out.")
        elif user_input == 2:
        # Hero does nothing, but Goblin still attacking
            goblin.attack(hero)
            print("\nOops. Goblin has attacked you! Fight back!")
            if not goblin.alive():
                print("\nGoblin is dead.")
            if not hero.alive():
                print("\nYou are dead. Too late to fight back :(")
        elif user_input == 3:
            print("\nGoodbye.")
            break
        else:
            print("\nInvalid input %r" % user_input)

main()
