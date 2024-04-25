import random
from replit import clear
def game():
    difficulty = input("Choose your difficulty. Type 'easy' or 'hard'.").lower()

    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    else:
        print("Invalid input.")
    
    rand_num = []
    for nums in range(1,101):
        rand_num.append(nums)
        

    rand_num = random.choice(rand_num)

    
    end_of_game = False
    while not end_of_game:
        
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess"))
        if guess != rand_num:
            lives -=1
        if lives == 0:
            end_of_game = True
            print(f"You Lost, The number was ")
        if guess> rand_num:
            print("Too high.\nGuess Again.")
        elif guess < rand_num:
            print("Too low.\nGuess Again.")
        elif guess == rand_num:
            end_of_game = True
            print("You won")
                
    
        
    
    restart = input("Do yo want to play the game again?")
    if restart == 'yes':
        clear()
        game()

game()
            