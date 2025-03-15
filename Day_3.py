print('''                           _______________________
                           \_____________________/
                            \       __O__       /
                             \      =(_)=      /              +
            +                _\  ___________  /_         .  . . .
             . . +          (  \/ ___   ___.\/  )       +.. .. .+
             .. .. :         \    (o)) ((o)    /       ... .. . .
            .. : .. .:. .    (_)    /   \    (_)      ..+.. + ...+
            . .+ . ++. .       \:. (_   _) .:/         +  + :.. + :
             . __... . +        )::::\_/::::(            :. __  . .
             _(  \ __ .        (:::\_|_|_/:::)          __ /  )_
            (  \  (  \      __  \:::\_|_/:::/  __      /  )  /  )
             \  \  \  \    /  )  \:::::::::/  (  \    /  /  /  /
            ( \  \  \  \__/  /    |\:::::/|    \  \__/  /  /  //)
             \ \_ \_ \_     / ____| |___| |____ \     _/ _/ _/ /
              \            /_/ ||   |___|   || \_\            /
               \          /\   ||  (_____)  ||   /\          /
                \________/ \\  ||___________||  // \________/
   ______________\\_______//    |___________|   \\______//_________________
                  \______/_:                   :_\______/ ''')
print("welcome to Treasure island.")
direction = input("Your mission is to find the treasure.\n left or wight? \n")
if direction == "left":
    x = input("nice choice now choose to swim or wait!\n")
    if x == "wait":
        door = input("its good for you to wait.\n which door blue , yellow or red")
        if door == "yellow":
            print("You Win!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")