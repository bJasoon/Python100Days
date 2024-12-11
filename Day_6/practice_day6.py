#=================================
#functions

def my_function():
    print("Hello")
    print("Bye")
    
my_function()


#==================================
## Reboorg's world
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def move_2_squares():
#     move()
#     move()

# move_2_squares()
# turn_left()
# move_2_squares()
# turn_left()
# move_2_squares()
# turn_left()
# move_2_squares()
# turn_left()

# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()

#==================================
# Reeborg's World Hurdle 1
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# for routine in range(0, 6):
#     jump()

#====================================
#While Loops
# Reeborg's World Hurdle 2
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while not at_goal():
#     jump()

#====================================
# Reeborg's Hurdle 3
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     #move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()
    
#====================================
# Reboorg's Hurdle 4
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while not wall_in_front():
#         move()
#     turn_left()
    
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()
#=====================================
# Reboorg's World Maze
# There is a possibility of an infinite loop within this. Check the udemy course for details
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
    
