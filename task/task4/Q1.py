#program taht stimulate game of rolling a dice.Roll the dice until you get 6 and count number of rolls it take to get 6.print count using brak statement.

def roll_dice():
    count=0
    while True:
        roll=int(input("Enter result of dice (1-6):"))
        count+=1
        print(f"roll {count}:{roll}")
        if roll==6:
            break
    print(f"It took {count} rolls to get a 6.")

roll_dice()