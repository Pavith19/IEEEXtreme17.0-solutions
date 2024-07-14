# We have to check whether count is less than 82 to prevent infinite loop.
# I do not know the significance of the value 82. I just found it by trial and error.

values = {"2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, "T":9, "J":10, "Q":11, "K":12, "A":13}

for x in range(int(input())):
    player_1 = input().split()
    player_2 = input().split()
    
    count = 0
    
    while len(player_1) > 0 and len(player_2) > 0 and player_1 != player_2 and count < 82:
        card_1 = player_1.pop(0)
        card_2 = player_2.pop(0)
        
        if values[card_1] > values[card_2]:
            player_1.append(card_2)
        elif values[card_1] < values[card_2]:
            player_2.append(card_1)
        else:
            player_1.append(card_1)
            player_2.append(card_2)
            
        count += 1
            
    else:
        if len(player_1) == 0:
            print("player 2")
        elif len(player_2) == 0:
            print("player 1")
        else:
            print("draw")
