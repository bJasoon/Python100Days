
#=================================================================
#Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
#print(potion_strength) # This does not work


#=================================================================
#Global Scope
enemies = "Skeleton"

def increase_enemies():
    global enemies
    enemies = "Zombies"
    print(f"Enemies inside fuction: {enemies}")

increase_enemies()
print(f"Enemies outside function {enemies}")

#Dangerous to modify global scope but okay to read
#Alternative: use function returns to modify the global scope

#=================================================================
#Global Constants
#Naming convention = use all caps for constants

PI = 3.14159
GOOGLE_URL = "https://www.google.com"