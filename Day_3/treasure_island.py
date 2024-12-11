print('''
       {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
           / HHH  \
          /  \_/   \
        {}          {}
''')
flavor_text_crossroad = '''
You come across a fork in the road going left and going right.
You feel an ominous aura radiating from the one of the roads. 
Which way do you go? Type 'left' or 'right'\n
'''
flavor_text_lake = '''
The ominous feeling passes as you choose the right path.
At the end of the road sits a lake with numerous small splashes populating it.
Do you risk swimming to get your destination faster or wait for a boat? Type 'wait' or 'swim'\n
'''
flavor_text_doors = '''
As you ride the boat across the lake, various man-eating trouts jump up and attempt to bite you. 
Thankfully you are safe in the boat. 
You arrive to mysterious island with 3 standing colored doors with nothing behind them.
The colors of the door are Red, Blue and Yellow.
Which one do you open? Type 'red', 'yellow' or 'blue'\n
'''

flavor_text_win = '''
You opened the yellow door and and find a enormous pirate treasure chest
As you opened it, gold coins, jewelry and gold objects spew out of the chest.

YOU FOUND THE TREASURE!
'''
flavor_text_lose = '''
The world suddenly turns black as you lose all sensation within your body.

GAME OVER!
'''
print("Welcome to Treasure Island\nYour mission is find the treasure.\n")

if (input(flavor_text_crossroad)) in {"left", "Left"}: # Could have use .lower() function to ensure the answers are all lowercase
    if input(flavor_text_lake) in {"wait", "Wait"}:
        if input(flavor_text_doors) in {"yellow", "Yellow"}:
            print(flavor_text_win)
        else:
            print(flavor_text_lose)
    else:
        print(flavor_text_lose)
else:
    print(flavor_text_lose)

