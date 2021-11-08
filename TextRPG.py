import random
import time
from threading import Timer
import sys


# List converter for level list only
def Convert(string):
    li = list(string.split(" "))
    return li


# List converter for inventory only
def Convert2(string):
    li = list(string.split(","))
    return li


# Converts an item from the inventory to a usable saving format
def reverse_convert(item):
    item_1 = item[0]  # Takes the ID Number of the item
    item_2 = item[1]  # Takes the (ATK/ DEF) Stat of the item

    if len(str(item)) == 1:  # Adds a zero in front of the ID if it's not 2 digits
        item_1 = "0" + str(item_1)
    if len(str(item_2)) == 1:  # Adds a zero in front of the Stat if it's not 2 digits
        item_2 = "0" + str(item_2)

    final_item = str(item_1) + str(item_2) + str(item[2])  # Converted into the final, usable save format
    return final_item


# Function that displays your profile
def profile():
    print("%s"
          "\n%s"
          "\nProfile of %s: "
          "\n%s"
          "\nLevel : %d"
          "\nGold : %d"
          "\nTotal EXP: %d"
          "\nExp to next level : %d"
          "\nGuild: %s"
          "\nAttack: %d"
          "\nDefense: %d"
          "\nWeapon: %s"
          "\nArmor: %s"
          % (line, line, username, username, level, gold, exp, exp_tnl, guild, atk, defense, weapon[2],
             armor[2]))


# Set save data function
def data(n_o_c_o, l_l, spe, spe_c, name, gld, lev, xp, xp_tnl, lin,
         gil, gil_t, ak, df, wep, arm, n_o_c, inv, m_b_f, b_n, d_n):
    file = open("TextRPGData.txt", "r+")
    file.truncate(0)
    file.close()
    file = open("TextRPGData.txt", "w")
    file.write("n_of_crates_opened = %d\n" % n_o_c_o)
    file.write("level_list = %s\n" % l_l)
    file.write("special = %d\n" % spe)
    file.write("special_c = %d\n" % spe_c)
    file.write("special_c2 = %d\n" % spe_c)
    file.write("username = %s\n" % name)
    file.write("gold = %d\n" % gld)
    file.write("level = %d\n" % lev)
    file.write("exp = %d\n" % xp)
    file.write("exp_tnl = %d\n" % xp_tnl)
    file.write("line = %s\n" % lin)
    file.write("guild = %s\n" % gil)
    file.write("guildT = %r\n" % gil_t)
    file.write("atk = %d\n" % ak)
    file.write("defense = %d\n" % df)
    file.write("%s\n" % wep)
    file.write("%s\n" % arm)
    file.write("n_of_crate = %d\n" % n_o_c)
    file.write("inventory = %s\n" % inv)
    file.write("mega_boss_factor = %s\n" % m_b_f)
    file.write("boss_name = %s\n" % b_n)
    file.write("discovered_name = %s" % d_n)


# Reset save data function
def reset():
    txt = open("TextRPGData.txt", "r+")
    txt.truncate(0)
    txt.close()
    txt = open("TextRPGData.txt", "w")
    txt.write("n_of_crates_opened = 0")
    txt.write("\nlevel_list = ")
    txt.write("\nspecial = 0")
    txt.write("\nspecial_c = 1")
    txt.write("\nspecial_c2 = 1")
    txt.write("\nusername =")
    txt.write("\ngold = 0")
    txt.write("\nlevel = 0")
    txt.write("\nexp = 0")
    txt.write("\nexp_tnl = 0")
    txt.write("\nline =")
    txt.write("\nguild =")
    txt.write("\nguildT = False")
    txt.write("\natk = 0")
    txt.write("\ndefense = 0")
    txt.write("\n0000No Weapon")
    txt.write("\n0000No Armor")
    txt.write("\nn_of_crate = 0")
    txt.write("\ninventory =")
    txt.write("\nmega_boss_factor = False")
    txt.write("\nboss_name =")
    txt.write("\ndiscovered_name =")


# Extracts integers from the Save Data
def int_extract(list_using_and_term, term):
    extracting = str(list_using_and_term)
    extracting = extracting.strip("\n")
    extracting = int(extracting[(len(term) + 3):])
    return extracting


# Extracts strings from the Save Data
def str_extract(using_list_and_term, using_term):
    extracting = str(using_list_and_term)
    extracting = extracting.strip("\n")
    extracting = str(extracting[(len(using_term) + 3):])
    return extracting


# Make sure the file Exists
try:
    f = open("TextRPGData.txt", "r")
    f.close()
except FileNotFoundError:
    f = open("TextRPGData.txt", "w")
    reset()
    f.close()

f = open("TextRPGData.txt", "r") # Opens text file (save data)
f420 = []  # List of all the lines in the save file

for x in range(1, 20):  # Enters all the save data into the list (f420)
    f420 += f.readlines(x)

n_of_crates_opened = int_extract(f420[0], "n_of_crate_opened")

level_list = str_extract(f420[1], "level_list")
if level_list != "":  # As long as level list isn't Empty
    level_list = Convert(level_list)
else:
    level_list = list(level_list)  # Creates an Empty list otherwise

special = int_extract(f420[2], "special")

special_c = int_extract(f420[3], "special_c")

special_c2 = int_extract(f420[4], "special_c2")

username = str_extract(f420[5], "username")
if username == "":
    username = None

gold = int_extract(f420[6], "gold")

level = int_extract(f420[7], "level")

exp = int_extract(f420[8], "exp")

exp_tnl = int_extract(f420[9], "exp_tnl")

line = str_extract(f420[10], "line")

guild = str_extract(f420[11], "guild")

guildT = str_extract(f420[12], "guildT")
if guildT == "False":
    guildT = ""  # If it's False, make it empty so it's read as False
guildT = bool(guildT)

atk = int_extract(f420[13], "atk")

defense = int_extract(f420[14], "defense")

weapon1 = f420[15]  # Transfers the Weapon from Save Data
weapon1 = weapon1.strip("\n")
weapon = [int(weapon1[:2]), int(weapon1[2:4]), str(weapon1[4:])]  # Remakes it as a list

armor1 = f420[16]  # Same thing as Weapon but for armor
armor1 = armor1.strip("\n")
armor = [int(armor1[:2]), int(armor1[2:4]), str(armor1[4:])]

n_of_crate = int_extract(f420[17], "n_of_crate")

inventory = str_extract(f420[18], "inventory")  # Transfers the inventory (as a string) from Save Data

inventory = inventory.strip("\n")
inventory = inventory.strip(" ")
inventory = inventory.strip("]")  # Strips all the unnecessary
inventory = inventory.strip("[")  # Syntax from the string
inventory = inventory.replace("\'", " ")
inventory = inventory.replace('\"', " ")

inventory = Convert2(inventory)  # Converts the string to a list

if len(inventory) == 1:
    inventory.clear()  # The inventory should never have only one term, empty it if it does
else:
    for x in range(len(inventory)):
        try:  # Separate each term into it's own list
            invent = inventory[0]
            inventory.remove(invent)
            invent = invent.strip("\n")
            invent = invent.strip()
            invent2 = [int(invent[:2]), int(invent[2:4]), invent[4:]]
            inventory.append(invent2)
        except IndexError:  # If the inventory has no terms (or somehow negative terms), then reset it to normal
            inventory = [[17, 3, "Beginner sword"], [18, 3, "Beginner shield"]]

mega_boss_factor = str_extract(f420[19], "mega_boss_factor")

if mega_boss_factor == "False":
    mega_boss_factor = ""

mega_boss_factor = bool(mega_boss_factor)

boss_name = str_extract(f420[20], "boss_name")

discovered_name = str_extract(f420[21], "discovered_name")

f.close()  # Closes the save data file

random_attack_stat = random.randint(15, 50)  # Sets a random atk stat for the RNG blade

# All the weapons
blade_of_logic = [1, 10, "Blade of Logic"]
charisma_hat = [5, 25, "Charisma + 50"]
crit_sword = [6, 20, "Critical hit blade"]
RNG_blade = [7, random_attack_stat, "RNG blade of legend"]
beginner_blade = [17, 3, "Beginner sword"]
spirit_sword = [30, 40, "Spirit Sword"]
diamond_sword = [31, 30, "Diamond Sword"]
stick = [32, 0, "Wimpy Stick"]
banana_on_stick = [33, 5, "Banana on a Stick"]
money_sword = [36, 5, "Money Sword"]
bojangles = [43, 45, "Bojangles Legendary Iced Tea"]

# All the armor
absolute_safety = [9, 40, "Absolute safety capsule"]
anti_dead = [10, 25, "Anti Dead"]
uno_reverse = [13, 15, "UNO reverse Card"]
mags_under = [14, 20, "Magazines under clothing"]
beginner_shield = [18, 3, "Beginner shield"]
diamond = [28, 40, "Diamond Chestplate"]
battle_armor = [29, 10, "Battle armor"]
banana_shoes = [34, 5, "Banana Shoes"]
banana_armor = [35, 20, "Full banana armor"]
x_defense = [37, 20, "X Defense"]
death_cheater = [39, 30, "Death Cheater"]
guard = [40, 40, "Rebellions Guard"]

# List of all words used in the combat
defence_words = ["defend", "protect", "denied", "cover", "dodge", "shield", "armor", "secure", "resist", "deter",
                 "block", "support", "shelter", "fortify", "barricade", "screen", "safety", "cushion", "bunker"]

# List of all the variable names of the weapons
weapon_list = [beginner_blade, blade_of_logic,
               charisma_hat, crit_sword,
               RNG_blade, spirit_sword, diamond_sword,
               stick, banana_on_stick, money_sword, bojangles]

# List of all the variable names of the armors
armor_list = [beginner_shield, absolute_safety, anti_dead, uno_reverse, mags_under,
              diamond, battle_armor, banana_shoes, banana_armor, x_defense,
              death_cheater, guard]

adventure = True  # Declares if you are on an adventure (If adventure is false, it means you're in an adventure)
doubleAtk = False  # Declares if you chose the raise attack command
turn = False  # Used in adventures to check if it's your turn to attack
user = False  # Used in the timer function of the adventure
count_of_tries = 0
inventory2 = []  # A second inventory used in saving your inventory
count = 0  # A counter used in saving your data
persist = False

print("Use !tutorial to view the tutorial")
while True:
    count += 1  # Count how many times you've gone through the loop

    weapon_input = reverse_convert(weapon)

    armor_input = reverse_convert(armor)

    if count > 2:
        for x in range(len(inventory)):  # Converts inventory items to strings (usable for save data)

            inventory_item = inventory[x]
            inventory2.append(reverse_convert(inventory_item))  # Appends converted items to inventory2

        if len(inventory2) > len(inventory):  # Takes care of any extra and unwanted terms in inventory2
            for x in range(len(inventory2) - len(inventory)):
                inventory2.pop()

    level_list2 = ""
    for x in range(1, len(level_list)):
        level_list2 += str(level_list[x - 1]) + " "
    if len(inventory2) != 0:  # Need to save with inventory2 in place
        data(n_of_crates_opened, level_list2, special, special_c, username, gold, level, exp, exp_tnl, line, guild,
             guildT, atk, defense, weapon_input, armor_input, n_of_crate, inventory2, mega_boss_factor, boss_name,
             discovered_name)
        print("Game Saved")
    elif count > 1:  # Print when the data isn't saved
        print("Data not Saved")
        
    user_input = input("").lower()
    
    if user_input != "" and "!" == user_input[0]:  # Requires commands to have ! at the beginning
        if not (user_input[1:7] == "create" or user_input[1:] == "tutorial") and username is None:
            print("You require a profile to do that command. Use !create profile or !tutorial to continue")
            continue  # Requires you to has a username to do any advanced commands
        elif user_input == "!reset":  # Resets all Save Data
            user_input = input("Are you sure? You can't undo this action! (Y/N)\n(the game will close if you select Y)")
            if user_input == "Y" or user_input == "y" or user_input == "!Y":
                reset()
                sys.exit()
            else:
                print("You did not reset")
                continue
        elif user_input[1:7] == "create":  # There are two different create commands, profile and guild
            if user_input[8:] == "profile":
                x = user_input  # Saves previous user input
                user_input = input("Please enter your username: ")
                username = user_input.strip("!")  # Creates all the players' assets
                gold = 100
                level = 1
                exp = 0
                exp_tnl = ((level * 2) * 1000) * ((level ** 0.5) / 2) - exp
                atk = 3
                defense = 3
                guild = None
                guildT = False
                guild_name = None
                line = "_" * ((len(username) * 2) + 6)
                special_c = 1
                special_c2 = 1
                if len(inventory) <= 2:  # Assure the inventory is proper
                    inventory = [[17, 3, "Beginner sword"], [18, 3, "Beginner shield"]]
                weapon = weapon_list[0]
                armor = armor_list[0]
                atk += weapon[1]
                defense += armor[1]
                profile()
            elif user_input[8:] == "guild":  # Creates your guild
                if gold >= 10000:
                    user_input = input("Please enter the name of your Guild: ")
                    guild_name = user_input.strip("!")
                    user_input = input("Are you sure? Y / N: ")
                    if user_input == "y" and username is not None:
                        gold -= 10000
                        guild = guild_name
                        guild_name = None
                        print("Congratulations, you now own a guild named %s" % guild)
                        guildT = True
                    elif user_input == "N" or user_input == "n":
                        print("Transaction cancelled")
                    else:
                        print("Invalid syntax, transaction cancelled (might need a username!)")
                else:
                    print("You don't have enough Gold! You have %d" % gold)
            else:
                continue  # Exits if user enter !create [incorrect syntax]
        elif user_input[1:] == "tutorial":  # Prints the tutorial
            print(
                "Tutorial:"
                "\nTo begin your adventure, you'll want to create a profile."
                " Use the command !create profile, you can't do anything before that."
                "\nAfter that command, you will be prompted to enter a username. You are not required to start your "
                "username with '!'"
                "\nAfter, the game will display your profile. Use the command !profile to view it."
                "\nYour profile contains everything about your character, from your level, to the amount of gold you "
                "\nhave, to the amount of exp required to level up, and the total amount of exp you've gathered "
                "throughout your adventure."
                "\n\nUse !inventory to view all the weapons gathered, \n1)Their number, \n2)Their stat \n3)Their name"
                "\nTo equip an item, use the command !equip, then you will get a prompt asking which item is"
                "\nto be equipped. Go in order of the list, so the first item is item one, the second item is"
                "\nitem 2 ect... The command !money shows you how much gold you have."
                "\n\nAdventuring is the only way to obtain exp and gold. Use the command "
                "\n!adventure to set off. You will then be prompted to enter what level of adventure you want to go on,"
                "\n for example, !adventure 1 will activate the adventure. You are allowed to tackle any level of "
                "\nadventure from the start, but keep in mind that adventures get longer and harder the "
                "\nhigher level you select!"
                "\nYou will then encounter an enemy. You'll have a few options:"
                "\n\nAttack: attacks the enemy"
                "\n\nRaise defense: doubles defense for next attack"
                "\n\nRaise attack: doubles damage done to enemy for next attack"
                "\n\nSpecial: Uses a special move that does super damage (you can only use it a limited number of "
                "times"
                "\n\nYou will be reminded of these keywords on your adventure, so don't worry about memorizing them."
                "\nAfter your turn, the enemy will attack. To minimize the damage, you will need to be fast."
                "\nThe game will tell you to input a word, spell it correctly, and enter it fast enough, amd damage"
                "\nwill be reduced by 33% (don't forget to hit enter after typing the word!)"
                "\nAdventures never need '!' at the beginning of words, so don't worry about that!"
                "\nOnce a level interval of 5, you will get a crate, use the command !crate open to open the crate."
                "\nYou also get another special use at every 5th level"
                "\nYou can use the command !create guild to create a guild. A guild has two main purposes:"
                "\n\n1) A guild gives you a 50% critical hit chance"
                "\n\n2) A guild has a 10% chance to heal you randomly between 10 and 50 hp during battle"
                "\nYou will need 10,000 Gold to create a guild"
                "\n\nYou can also reset the game with !reset")
            continue
        elif user_input[1:] == "profile" and username is not None:
            profile()  # Prints the profile
            if mega_boss_factor:
                print(discovered_name)
        elif user_input[1:] == boss_name:
            mega_boss_factor = False
            print("By calling out it's name, the bosses were scared off")
        elif user_input[1:] == "dev hack":  # Grants a variable (user inputted) amount of EXP
            user_input = input("How much exp do you want?")
            user_input = user_input.strip("!")
            exp += int(user_input)
        elif user_input[1:] == "money" and username is not None:
            print("You have %d gold" % gold)  # Prints how much money (gold) you have
        elif user_input[1:10] == "adventure" and username is not None:
            integer = False  # Used to see if your input has a proper integer in it
            adventure = False
            special = 0
            user_input = user_input[11:]
            while not integer:  # Finds what level adventure you want to go on
                try:
                    user_input = int(user_input)
                    user_input *= 2
                    user_input /= 2
                    integer = True  # Escapes the loop once you input an integer
                except ValueError:
                    print("That's not a number!")
                    user_input = input("What level of adventure do you want to go on? ")
            
            if True:  # Set to always run
                print("You went on an adventure!")  # Normal adventure
                player_health = ((level ** 2) * 10) + 100  # Sets player health
                progress_bar1 = int(user_input) + 1  # Printing a progress bar
                battle_revolution = int(user_input) + 2  # How many times the adventure can loop over
                enemy_poss = battle_revolution  # Possible enemy levels
                while not adventure:  # Continue a loop until either you complete the adventure or die
                    if adventure:
                        battle_revolution = -2  # Fail-safe to end the adventure
                    for i in range(1, battle_revolution):
                        if not adventure:
                            print(
                                "__________________|      |______________________________________________________________         "
                                "\n       ,---.     ,--.        ,---.  ,---.                                                         "
                                "\n       |oo  | _  \  `.       | oo | |  oo|                                                        "
                                "\no  o  o|~~  |(_) /   ;       | ~~ | |  ~~|o  o  o  o  o  o  o  o  o  o  o                         "
                                "\n       |/\/\|   '._,'        |/\/\| |/\/\|                                                        "
                                "\n__________________        ______________________________________________________________          "
                                "\n                  |      |                                                                        ")
                            time.sleep(2)
                        enemy_level = random.randint(0, enemy_poss - 1)  # Determines enemy level
                        enemy_health = random.randint((enemy_level * 10), (enemy_level * 20))  # Determines enemy health
                        enemy_dmg = (enemy_level * 20 + 1) - defense  # Determines enemy damage output
                        if not adventure:
                            print("You encountered an enemy of level %d" % enemy_level)
                            if enemy_level <= 0:
                                print("The enemy looked at you and fainted!, received 10 EXP")
                                exp += 10
                                y = 1
                                if adventure:
                                    y = 0
                                time.sleep(y)
                            elif enemy_level > 0:
                                while enemy_health > 0 and player_health > 0 and not adventure:
                                    user = True
                                    while not turn:
                                        print(
                                            "What will you do? (attack, raise defense (1 turn), raise attack (1 turn), "
                                            "special (%d times) cancel (cancel the adventure)) (Do not use '!' during "
                                            "an adventure)" % (
                                                    special_c2 - special))
                                        turn = False
                                        user_input2 = input("")
                                        if user_input2 == "attack":
                                            x = random.randint(15, 40)
                                            print("The enemy has %d health" % enemy_health)
                                            d = random.randint(atk, atk * 2)
                                            if doubleAtk:
                                                d *= 2
                                                doubleAtk = False
                                            if guildT:
                                                if random.randint(0, 1) == 1:
                                                    d *= 2
                                                    print("Your guild doubled your damage output")
                                            print("%d damage dealt" % d)
                                            enemy_health -= d
                                            if enemy_health <= 0:
                                                print("The enemy has 0 health left")
                                            else:
                                                print("The enemy has %d health left" % enemy_health)
                                            if enemy_health <= 0:
                                                print("Please hit enter to continue")
                                            turn = True
                                        elif user_input2 == "raise defense":
                                            enemy_dmg //= 2
                                            print("You reduced the next attack by %50")
                                            print("The enemy has %d health left" % enemy_health)
                                            turn = True
                                        elif user_input2 == "raise attack":
                                            print("Your attack has been raised for one turn")
                                            print("The enemy has %d health left" % enemy_health)
                                            turn = True
                                            doubleAtk = True
                                        elif user_input2 == "special" and special_c2 - special > 0:
                                            print("Special attack unleashed!")
                                            special += 1
                                            special_dmg = random.randint(atk * 2, atk * 4)
                                            if guildT:
                                                x = random.randint(0, 1)
                                                if x == 1:
                                                    special_dmg *= 2
                                                    print("You guild doubled your special damage")
                                            print("%d damage dealt" % special_dmg)
                                            enemy_health -= special_dmg
                                            if enemy_health <= 0:
                                                print("The enemy has 0 health left")
                                                print("Hit enter to continue")
                                            else:
                                                print("The enemy has %d health left" % enemy_health)
                                            turn = True
                                        elif user_input2 == "special" and special_c2 - special <= 0:
                                            print("You have no more specials left")
                                        elif user_input2 == "cancel":
                                            print("You left the adventure")
                                            print("Hit enter to continue")
                                            turn = True
                                            adventure = True
                                            player_health = 0
                                        else:
                                            print("that is not a proper command")
                                    user = False
                                    if adventure:
                                        user = True
                                    heal = random.randint(1, 10)
                                    if guildT:
                                        if heal == 1:
                                            add = random.randint(10, 50)
                                            player_health += add
                                            print("You guild healed you %d hp" % add)
                                    enemy_dmg = enemy_level * 20 + 1
                                    time.sleep(random.randint(2, 4))
                                    x = random.randint(0, len(defence_words) - 1)
                                    y = defence_words[x]
                                    if enemy_health > 0 and not adventure:
                                        print("Please input: %s" % y)
                                    out_of_time = False
                                    start_time = time.time()


                                    def time_ran_out():
                                        if not user and not adventure and turn:
                                            print(' You took full damage for being too slow')
                                            print("Hit enter to continue")


                                    if not user and enemy_health > 0:
                                        t = Timer(3, time_ran_out)
                                        t.start()
                                    user_input3 = input("")
                                    if time.time() - start_time >= 3 and user_input3 != "" and user_input3 != y:
                                        user_input3 = "garbage"
                                    if (user_input3 == "" or user_input3 != y) and enemy_health > 0:
                                        out_of_time = True
                                    if user_input3 == y and not out_of_time and enemy_health > 0:
                                        if time.time() - start_time <= 1.5:
                                            print("Amazing, 25% damage received!")
                                            enemy_dmg //= 4
                                        else:
                                            print("Amazing, 33% damage received!")
                                            enemy_dmg //= 3
                                        print("You took %d damage" % enemy_dmg)
                                        player_health -= enemy_dmg
                                        print("You have %d health remaining" % player_health)
                                    elif out_of_time and (
                                            user_input3 == "" or user_input3 != y) and enemy_health > 0 and not adventure:
                                        if user_input3 != y and user_input3 == "garbage":
                                            print(" You took full damage because you misspelled the word")
                                        print("You took %d damage" % enemy_dmg)
                                        player_health -= enemy_dmg
                                        print("You have %d health remaining" % player_health)
                                    turn = False
                                if enemy_health <= 0:
                                    print("Congratulations, you defeated an enemy!")

                                    if weapon[0] == 32:
                                        exp += ((((enemy_level * 100) + int(enemy_level ** 0.5)) + int(enemy_level * 50)
                                                 ) * 2)
                                        gold += (enemy_level * 100 + int(enemy_level ** 0.5)) * 2
                                        print("You got double EXP and Gold for using the Wimpy Stick")
                                        print("You received %d exp" % (
                                                (((enemy_level * 100) + int(enemy_level ** 0.5)) + int(enemy_level * 50)
                                                 )
                                                * 2))
                                        print("You received %d gold" % ((enemy_level * 100 + int(enemy_level ** 0.5))
                                                                        * 2))
                                        progress_bar = ((i / progress_bar1) * 100)
                                        print("You have completed %.2f%% of the adventure" % float(progress_bar))
                                        time.sleep(1)
                                    elif weapon[0] == 36:
                                        print(
                                            "The enemy turned to gold as the sword you wield harnesses the midas touch")
                                        print("You received double gold")
                                        exp += ((enemy_level * 100) + int(enemy_level ** 0.5) + int(enemy_level * 50))
                                        gold += (enemy_level * 100 + int(enemy_level ** 0.5)) * 2
                                        print("You received %d exp" % (
                                                ((enemy_level * 100) + int(enemy_level ** 0.5)) + int(enemy_level * 50))
                                              )
                                        print(
                                            "You received %d gold" % (enemy_level * 100 + int(enemy_level ** 0.5)) * 2)
                                        progress_bar = ((i / progress_bar1) * 100)
                                        print("You have completed %.2f%% of the adventure" % float(progress_bar))
                                        time.sleep(1)
                                    elif weapon[0] == 7:
                                        print("You defeated the enemy with the power of RNJesus")
                                        exp += ((enemy_level * 100) + int(enemy_level ** 0.5) + int(enemy_level * 50))
                                        gold += (enemy_level * 100 + int(enemy_level ** 0.5))
                                        print("You received %d exp" % (
                                                ((enemy_level * 100) + int(enemy_level ** 0.5)) + int(enemy_level * 50))
                                              )
                                        print("You received %d gold" % (enemy_level * 100 + int(enemy_level ** 0.5)))
                                        progress_bar = ((i / progress_bar1) * 100)
                                        print("You have completed %.2f%% of the adventure" % float(progress_bar))
                                        time.sleep(1)
                                    elif weapon[0] == 8:
                                        print("The enemies attack's were useless")
                                        exp += ((enemy_level * 100) + int(enemy_level ** 0.5) + int(enemy_level * 50))
                                        gold += (enemy_level * 100 + int(enemy_level ** 0.5))
                                        print("You received %d exp" % (
                                                ((enemy_level * 100) + int(enemy_level ** 0.5)) + int(enemy_level * 50))
                                              )
                                        print("You received %d gold" % (enemy_level * 100 + int(enemy_level ** 0.5)))
                                        progress_bar = ((i / progress_bar1) * 100)
                                        print("You have completed %.2f%% of the adventure" % float(progress_bar))
                                        time.sleep(1)
                                    else:
                                        exp += ((enemy_level * 100) + int(enemy_level ** 0.5) + int(enemy_level * 50))
                                        gold += (enemy_level * 100 + int(enemy_level ** 0.5))
                                        print("You received %d exp" % (
                                                ((enemy_level * 100) + int(enemy_level ** 0.5)) + int(enemy_level * 50))
                                              )
                                        print("You received %d gold" % (enemy_level * 100 + int(enemy_level ** 0.5)))
                                    progress_bar = ((i / progress_bar1) * 100)
                                    print("You have completed %.2f%% of the adventure" % float(progress_bar))
                                    time.sleep(1)
                            if player_health <= 0 and not adventure:
                                print("You died and failed the adventure")
                                adventure = True
                                special_c2 = special_c
                    adventure = True
                if player_health > 0 and not adventure:
                    print("You have completed the adventure")
                    adventure = True
                    special_c2 = special_c
            user_input = str(user_input)
            print("Please input commands to continue")
        exp_tnl = ((level * 2) * 1000) * ((level ** 0.5) / 2) - exp
        while exp_tnl <= 0:
            if username is not None:
                exp_tnl = ((level * 2) * 1000) * ((level ** 0.5) / 2) - exp
            if exp_tnl <= 0 and username is not None:
                print("You leveled up!")
                level += 1
                atk += 3
                defense += 3
                print("You are now level %d" % level)
                print("Stats increase, atk + 3, def + 3")
                exp_tnl = (level * 2 * 1000) * ((level ** 0.5) / 2) - exp
            if level % 5 == 0 and level != 0 and level not in level_list:
                print("Congratulations, you received a crate.")
                n_of_crate += 1
                special_c += 1
                special_c2 += 1
                print("Your special attack capacity went up one from %d to %d" % (special_c - 1, special_c))
                level_list.append(level)
        if user_input[1:] == "crate open" and n_of_crate > 0:
            print("You opened a crate")
            n_of_crate -= 1
            if random.randint(0, 1) == 1:
                x = random.randint(0, len(weapon_list) - 1)
                print(weapon_list[x])
                x = weapon_list[x]
                if x in inventory:
                    print("Uh oh! You already have this item! That item gets + 5 attack stat!")
                    x[1] += 5
                    print(x)
                else:
                    inventory.append(x)
                print("You received " + x[2])
            else:
                x = random.randint(0, len(armor_list) - 1)
                print(armor_list[x])
                x = armor_list[x]
                if x in inventory:
                    print("Uh oh! You already have this item! That item gets + 5 defense stat!")
                    x[1] += 5
                    print(x)
                else:
                    inventory.append(x)
                print("You received " + x[2])
            n_of_crates_opened += 1
        elif user_input[1:] == "crate open" and n_of_crate <= 0:
            print("You have no more crates")
        elif user_input[1:] == "crates":
            print("You have %d unopened crates" % n_of_crate)
        elif user_input[1:] == "inventory":
            if len(inventory) > 6:
                x = 0
                y = len(inventory) // 6
                if len(inventory) % 6 >= 0.5:
                    y += 1
                for i in range(1, y + 1):
                    x += 6
                    y = x - 6
                    if x > len(inventory):
                        x = len(inventory)
                    print(inventory[y:x])
            else:
                print(inventory)
        elif user_input[1:6] == "equip":
            equip = user_input[7:]
            equip1 = False
            while not equip1:
                try:
                    equip = int(equip)
                    equip -= 1
                    equip1 = True
                except ValueError:
                    print("That's not a proper number!")
                    equip = input(
                        "What number is the item \n(in order of the list, for example, the item you have equipped"
                        " in the first slot is item 1): ")
            equip = int(equip)
            if int(equip) > len(inventory):
                print("You don't have an item that's %drd in your inventory" % equip)
            elif inventory[equip] in weapon_list:
                equipping = inventory[equip]
                moving = weapon
                inventory.remove(equipping)
                inventory.insert(0, equipping)
                inventory.remove(moving)
                inventory.append(moving)
                weapon = equipping
                atk -= moving[1]
                atk += equipping[1]
                print("%s is now equipped as your weapon" % weapon[2])
            elif inventory[equip] in armor_list:
                equipping = inventory[equip]
                moving = armor
                inventory.remove(equipping)
                inventory.insert(0, equipping)
                inventory.remove(moving)
                inventory.append(moving)
                armor = equipping
                defense -= moving[1]
                defense += equipping[1]
                print("%s is now equipped as your armor" % armor[2])
    else:
        print("All commands on the home menu require '!'")
        continue
