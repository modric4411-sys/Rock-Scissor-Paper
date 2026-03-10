import random

total_count = 0
comp_wins = 0
user_wins = 0
count_tie = 0

print("-----GAME-----")
print("""
1- Rock
2- Paper
3- Scissor""")

    User_choice = int(input("Enter your choice: "))
    while user_choice < 1 or user_choice > 3:
        print("INVALID INPUT.Try again.")


    if user_choice  == 1:
        user = "Rock"

    elif user_choice == 2:
        user = "Paper"

    else:
        user = "Scissor"

    print("USER Choice : ",user)

    print("-----Now my Turn-----")
    comp_choice = random.randint(1,3)


    if comp_choice ==1:
        computer = "Rock"

    elif comp_choice ==2:
        computer = "Paper"

    else:
        computer = "Scissor"

    print("COMPUTER CHOICE: ", computer)

    if user == computer:
        print("ITS A TIE")
        count_tie += 1
    elif (user == "Rock" and computer == "Scissor") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissor" and computer == "Paper") :
        print("User Won.")
        user_wins += 1
    else:
        print("Computer Won")
        comp_wins += 1
    total_count += 1

    ans = input("Do you want to play again?(y/n)")
    if ans == "y":
    else:
    print("-----Result-----")
    print("Total games played: ", total_count)
    print("User Wins: ", user_wins)
    print("TIE Matches: ", count_tie)


