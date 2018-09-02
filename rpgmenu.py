print("Welcome to the RPG menu: Choose your preferred option by typing the shortcode or number")
print("q: Return to main menu")

exec(open("./rpgnames.py").read())
menu_choice = input("Please enter your choice:")
if menu_choice == "q":
    import DiceRoller
else:
    with open('rpgcodes.py', 'r') as codes:
        shortcodes = [line.strip() for line in codes]

if menu_choice in shortcodes[:]:
    rpgfile = "./rpg" + menu_choice + ".py"
    exec(open(rpgfile).read())
else:
    print("Sorry I don't have that RPG")

