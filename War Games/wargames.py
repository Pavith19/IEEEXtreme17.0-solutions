def play_game(deck1, deck2):
    seen = set()
    while deck1 and deck2:
        current_state = (tuple(deck1), tuple(deck2))
        if current_state in seen:
            return "draw"
        seen.add(current_state)

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if values[card1] > values[card2]:
            deck1.append(card1)
            deck1.append(card2)
        elif values[card2] > values[card1]:
            deck2.append(card2)
            deck2.append(card1)
        else:
            deck1.append(card1)
            deck2.append(card2)

    if not deck1:
        return "player 2"
    elif not deck2:
        return "player 1"

values = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12, "A": 13}

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0].strip())
    if 1 <= n <= 25:
        results = []
        for i in range(1, 2*n, 2):
            deck1 = data[i].strip().split()
            deck2 = data[i+1].strip().split()
            result = play_game(deck1, deck2)
            results.append(result)
        
        for result in results:
            print(result)

if __name__ == "__main__":
    main()
