import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("🌟 Welcome to the Python Number Guessing Game! 🌟")
print(f"✨ I'm thinking of a number between { lowest_num } and { highest_num }. Can you guess it? ✨")

while is_running:
    guess = input("🤔 Please Enter Your Guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1  # Correctly incrementing the number of guesses

        if guess < lowest_num or guess > highest_num:
            print("🚫 Oops! That number is out of range. Please try again!")
            print(f"✨ Remember, select a number between {lowest_num} and {highest_num}. ✨")
        
        elif guess < answer:
            print("⬇️ Too low! Give it another shot!")
        elif guess > answer:
            print("⬆️ Too high! You're getting closer!")
        else:
            print(f"🎉 Hooray! You guessed it! The answer was {answer}.")
            print(f"👏 You found the number in {guesses} guesses! Well done!")
            is_running = False
    
    else:
        print("❌ That's not a valid guess. Please enter a number.")
        print(f"✨ Remember, select a number between {lowest_num} and {highest_num}. ✨")

print("💖 Thanks for playing! Hope you had fun! 💖")
