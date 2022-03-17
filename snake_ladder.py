from sys import platform
import time 
import random


die_value=6
sleep=1
Start=1
Exit=2

Easy=1
Medium=2
Hard=3

position_1=0
position__2=0

ladd_values=[]
ladder_positions=[]

snk_value=[]
snk_position=[]

start_up= int(input("Press 1 to start, 2 to exit: "))
if (start_up==Start):
    print("Good, proceeding to next action")
    time.sleep(sleep)

else:
    print('Goodbye')


player_1=None
while not player_1:
    player_1=str(input("Please enter a valid name for first player: "))

player_2=None
while not player_2:
    player_2=str(input("Please enter a valid name for player 2: "))

    print("\nThis match will be played between "+ player_1 +  " and "  + player_2+ "\n")

print()
time.sleep(sleep)

print("Now choose a difficulty. 1 for easy, 2 for medium, and 3 for hard")

Difficulty=int(input("Good, now choose a difficulty: "))
if (Difficulty==Easy):
    print("\nMust be your first, time, Don't worry")
    print()
    print(f"{player_1} and {player_2} are at positon 0")

    ladd_easy=6
    snk_easy=3

    for i in range(0,ladd_easy):
        ladd_values.append(random.randint(10,40))
        ladder_positions.append(random.randint(9,85))

    for i in range(0,snk_easy):
        snk_value.append(random.randint(12,20))
        snk_position.append(random.randint(20,70))

    print(f"\nLadders are at these positions:{ladder_positions}")
    print(f"\nSnakes are at these positions:{snk_position}")
    time.sleep(1)
    while position_1<100 and position__2<100:
        input(f"\n{player_1}, Press enter to roll the die")
        roll_1=random.randint(1,die_value)
        print(f"\nyou rolled a {roll_1}")
        position_1+=roll_1
        print(f"\n{player_1} Your positions is {position_1}")
        l=-1
        p=-1
        for i in range(0,ladd_easy):
            l+=1
            if position_1==ladder_positions[l]:
                position_1+=ladd_values[l]
                print(f"\nYou have landed on a ladder!!, Your position is now {position_1}")
        for i in range(0,snk_easy):
            p+=1
            if position_1==snk_position[p]:
                position_1-=snk_value[p]
                print(f"\nYou have landed on a snake!, Your position is now {position_1}")
        time.sleep(1)
        if position_1>=100:
            print(f"\nCONGRADULATIONS {player_1} YOU HAVE WON!!!!!!")

        if position_1<100:
            str(input(f"\n{player_2}, press enter roll the die"))
            roll2=random.randint(1,die_value)
            position__2+=roll2
            print(f"\n{player_2} Your position is {position__2}")
            l=-1
            p=-1
            for i in range(0,ladd_easy):
                l+=1
                if position__2==ladder_positions[l]:
                    position__2+=ladd_values[l]
                    print(f"\n{player_2} you have landed on a ladder!, Your position is now {position__2}")
            for i in range(0,snk_easy):
                p+=1
                if position__2==snk_position[p]:
                    position__2-=snk_value[p]
                    print(f"\n{player_2} You have landed on a snake!, Your positions is now {position__2}")
        time.sleep(1)
        if position__2>=100:
            print(f"\n{player_2} CONGRADULATIONS YOU HAVE WON!!")

elif (Difficulty==Medium):
    print("\nGood luck to the both of you")
    print(f"\n{player_1} and {player_2} are at positon 0")

    ladd_med=5
    snk_med=10

    for i in range(0,ladd_med):
        ladd_values.append(random.randint(10,20))
        ladder_positions.append(random.randint(5,80))

    for i in range(0,snk_med):
        snk_value.append(random.randint(10,20))
        snk_position.append(random.randint(30,78))

    print(f"\nLadders are at these positions:{ladder_positions}")
    print(f"\nSnakes are at these positions:{snk_position}")
    time.sleep(1)
    while position_1<100 and position__2<100:
        input(f"{player_1}, Press enter to roll the die")
        roll_1=random.randint(1,die_value)
        print(f"\n{player_1} rolled a {roll_1}")
        position_1+=roll_1
        print(f"\n{player_1} Your positions is {position_1}")
        l=-1
        p=-1
        for i in range(0,ladd_med):
            l+=1
            if position_1==ladder_positions[l]:
                position_1+=ladd_values[l]
                print(f"\nYou have landed on a ladder!!, Your position is now {position_1}")
        for i in range(0,snk_med):
            p+=1
            if position_1==snk_position[p]:
                position_1-=snk_value[p]
                print(f"\nYou have landed on a snake!, Your position is now {position_1}")
        time.sleep(1)
        if position_1>=100:
            print(f"\nCONGRADULATIONS {player_1} YOU HAVE WON!!!!!!")

        if position_1<100:
            str(input(f"\n{player_2}, press enter roll the die"))
            roll2=random.randint(1,die_value)
            position__2+=roll2
            print(f"\n{player_2} rolled a {roll2}")
            print(f"\n{player_2} Your position is {position__2}")
            l=-1
            p=-1
            for i in range(0,ladd_med):
                l+=1
                if position__2==ladder_positions[l]:
                    position__2+=ladd_values[l]
                    print(f"\n{player_2} you have landed on a ladder!, Your position is now {position__2}")
            for i in range(0,snk_med):
                p+=1
                if position__2==snk_position[p]:
                    position__2-=snk_value[p]
                    print(f"\n{player_2} You have landed on a snake!, Your positions is now {position__2}")
        time.sleep(1)
        if position__2>=100:
            print(f"\n{player_2} CONGRADULATIONS YOU HAVE WON!!")

elif (Difficulty==Hard):
    print("\nSo it is challenge you want, well It is a CHALLENGE YOU GET!!, MWAHAHAHAHAHAAAA ")
    print(f"\n{player_1} and {player_2} are at positon 0")

    ladd_hrd=4
    snk_hrd=12

    for i in range(0,ladd_hrd):
        ladd_values.append(random.randint(10,20))
        ladder_positions.append(random.randint(8,80))

    for i in range(0,snk_hrd):
        snk_value.append(random.randint(10,20))
        snk_position.append(random.randint(30,97))

    print(f"\nLadders are at these positions:{ladder_positions}")
    print(f"\nSnakes are at these positions:{snk_position}")
    time.sleep(1)
    while position_1<100 and position__2<100:
        input(f"\n{player_1}, Press enter to roll the die")
        roll_1=random.randint(1,die_value)
        print(f"\n{player_1} rolled a {roll_1}")
        position_1+=roll_1
        print(f"\n{player_1} Your positions is {position_1}")
        l=-1
        p=-1
        for i in range(0,ladd_hrd):
            l+=1
            if position_1==ladder_positions[l]:
                position_1+=ladd_values[l]
                print(f"\nYou have landed on a ladder!!, Your position is now {position_1}")
        for i in range(0,snk_hrd):
            p+=1
            if position_1==snk_position[p]:
                position_1-=snk_value[p]
                print(f"\nYou have landed on a snake!, Your position is now {position_1}")
        time.sleep(1)
        if position_1>=100:
            print(f"\nCONGRADULATIONS {player_1} YOU HAVE WON!!!!!!")

        if position_1<100:
            str(input(f"\n{player_2}, press enter roll the die"))
            roll2=random.randint(1,die_value)
            position__2+=roll2
            print(f"\n{player_2} rolled a {roll2}")
            print(f"\n{player_2} Your position is {position__2}")
            l=-1
            p=-1
            for i in range(0,ladd_hrd):
                l+=1
                if position__2==ladder_positions[l]:
                    position__2+=ladd_values[l]
                    print(f"\n{player_2} you have landed on a ladder!, Your position is now {position__2}")
            for i in range(0,snk_hrd):
                p+=1
                if position__2==snk_position[p]:
                    position__2-=snk_value[p]
                    print(f"\n{player_2} You have landed on a snake!, Your positions is now {position__2}")
        time.sleep(1)
        if position__2>=100:
            print(f"\n{player_2} CONGRADULATIONS YOU HAVE WON!!")
