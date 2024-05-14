################## Scope ##################

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: <{enemies}>")


increase_enemies()
print(f"enemies outside function: <{enemies}>")


# Local Scope
def drink_potion():
    potion_strength = 2
    print(f"<Local Scope> allowed only inside a function <{potion_strength}>")


drink_potion()

# Global Scope
player_health = 20


def energy():
    print(f"<Global Scope> allowed inside a function <{player_health}>")


energy()
print(f"<Global Scope> allowed outside a function <{player_health}>")
