import random  # Import the random module to choose random words

# Global variable to keep track of the highest score
highest_score = 0

def main():
    global highest_score
    
    # Lists of words by difficulty level
    easy_words = [
        "cat", "dog", "sun", "tree", "book", "pen", "car", "chair", "house", "ball",
        "run", "jump", "eat", "sit", "play", "read", "write", "sleep", "walk", "talk",
        "big", "small", "hot", "cold", "good", "bad", "happy", "sad", "fast", "slow"
    ]
    medium_words = [
        "apple", "banana", "orange", "window", "garden", "flower", "pencil", "bottle", "school", "market",
        "listen", "answer", "travel", "enjoy", "decide", "create", "imagine", "discover", "explain", "follow",
        "beautiful", "friendly", "ancient", "mysterious", "careful", "comfortable", "dangerous", "powerful", "patient", "wonderful"
    ]
    hard_words = [
        "ancient", "complex", "fragile", "genuine", "humble", "immense", "modest", "mysterious", "precious", "reliable",
        "scarce", "serene", "sincere", "sturdy", "subtle", "timid", "unique", "vivid", "wholesome", "zealous",
        "ardent", "blissful", "candid", "daunting", "elusive", "fervent", "graceful", "hasty", "intrepid", "luminous"
    ]

    # Encouraging messages
    messages = ["Try again!", "You can do it!", "Keep going!", "Don't give up!", "Almost there!"]

    # Welcome message
    print()
    print("*"*8,"Welcome to the password guessing game","*"*8)
    print()

    # Ask the user to choose difficulty level
    print("Enter your difficulty level (Easy, Medium or Hard) : ")
    level = input().lower()  # Convert input to lowercase to handle case-insensitive input
    print()

    # Select a random word based on chosen difficulty
    if level == 'easy':
        word = random.choice(easy_words)
    elif level == 'medium':
        word = random.choice(medium_words)
    elif level == 'hard':
        word = random.choice(hard_words)
    else:
        print("Invalid Choice!!....We are choosing easy level by default.")
        word = random.choice(easy_words)

    print(f"The secret word has {len(word)} letters.")
    print()

    attempts = 0  # Counter for the number of guesses
    score = 100   # Start score at 100
    previous_guesses = []  # Track previous guesses

    print("----Start Guessing the Secret Word----")
    print()

    # Main game loop
    while True:
        guess = input("Enter your guessed word: ").lower()  # Take guess input and convert to lowercase
        attempts += 1  # Increment attempt count
        previous_guesses.append(guess)  # Add guess to list
        print("Previous guesses:", previous_guesses)

        # Check if guessed word is correct
        if guess == word:
            print()
            print(f"Yayyy! Congratulations!!!...\nYou guessed the correct word in {attempts} attempts.")
            print(f"Your Score: {score}")
            if score > highest_score:
                highest_score = score  # Update highest score
                print(f"🏆 New High Score! Highest Score: {highest_score}")
            else:
                print(f"Highest Score: {highest_score}")
            break  # Exit the loop if correct

        # Deduct 10 points for wrong attempt
        score -= 10
        if score < 0:
            score = 0  # Ensure score doesn't go negative
        
        # Generate hint: show correct letters in correct position, underscores for others
        hint = ""
        for i in range(len(word)):
            if i < len(guess) and guess[i] == word[i]:
                hint += guess[i]  # Correct letter in correct position
            else:
                hint += '_'  # Placeholder for wrong/missing letters
        print("Hint: "+ hint)
        print(random.choice(messages))  # Encouraging message

         # First letter hint after 3 attempts
        if attempts == 3:
            print()
            print(f"Hint: The first letter is '{word[0]}'")
            print()

        # After 3 attempts, give the option to quit
        if attempts >= 3:
            print()
            ch = input("Do you want to give up or continue the game??(Y/N): ").lower()
            if ch == 'y':
                print()
                print(f"Better luck next time!!....\nThe Secret Word was *{word}*.")
                score = 0
                print(f"Your Score: {score}")
                print(f"Highest Score: {highest_score}")
                break  # Exit loop if player gives up
        
        MAX_ATTEMPTS = 10
        if attempts >= MAX_ATTEMPTS:
            print(f"Out of attempts! The word was {word}.")
            break

        print()

    # End of the game
    print()
    print("Game Over....")
    print()

    # Ask if player wants to play again
    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again == 'y':
        main()  # Restart the game
    else:
        print(f"Thank you for playing! Highest Score this session: {highest_score}")

# Run the game only if this file is executed directly
if __name__ == '__main__':
    main()
