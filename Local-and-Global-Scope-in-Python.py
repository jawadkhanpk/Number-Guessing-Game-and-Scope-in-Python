################## Scope ##################

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: <{enemies}>")


increase_enemies()
print(f"enemies outside function: <{enemies}>\n")


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
print(f"<Global Scope> allowed outside a function <{player_health}>\n")

# Modifying a Global Variable way:1

enemies1 = 33
def increase_enemies1():
    # global keyword is used to modify a global variable inside a function
    global enemies1
    enemies1 +=1
    print(f"enemies1 inside a function: {enemies1}")

increase_enemies1()
print(f"enemies1 outside a function: {enemies1}")





# Modifying a Global Variable way:2

enemies2 = 10
def increase_enemies2():
    print(f"enemies2 inside a function: {enemies2}")
    return enemies2 + 1

enemies2 = increase_enemies2()
print(f"enemies2 outside a function: {enemies2}")
