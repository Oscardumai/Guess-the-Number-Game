import random
import time
import sys

class GuessTheNumberGame:
    def __init__(self):
        self.min_range = 1
        self.max_range = 100
        self.max_attempts = 7
        self.score = 0
        self.high_scores = []
    
    def display_welcome(self):
        """Display welcome message and game instructions"""
        print("🎯" * 30)
        print("           WELCOME TO GUESS THE NUMBER GAME!")
        print("🎯" * 30)
        print(f"\nI'm thinking of a number between {self.min_range} and {self.max_range}")
        print(f"You have {self.max_attempts} attempts to guess it correctly!")
        print("\nLet's see how good your intuition is! 🤔")
        print("-" * 60)
    
    def get_difficulty_level(self):
        """Let player choose difficulty level"""
        print("\nChoose difficulty level:")
        print("1. Easy (1-50, 10 attempts)")
        print("2. Medium (1-100, 7 attempts)")
        print("3. Hard (1-200, 5 attempts)")
        print("4. Custom (You choose the range and attempts)")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-4): "))
                if choice == 1:
                    self.min_range, self.max_range, self.max_attempts = 1, 50, 10
                elif choice == 2:
                    self.min_range, self.max_range, self.max_attempts = 1, 100, 7
                elif choice == 3:
                    self.min_range, self.max_range, self.max_attempts = 1, 200, 5
                elif choice == 4:
                    self.get_custom_settings()
                else:
                    print("Please enter a number between 1-4")
                    continue
                break
            except ValueError:
                print("Please enter a valid number!")
    
    def get_custom_settings(self):
        """Get custom game settings from player"""
        while True:
            try:
                self.min_range = int(input("Enter minimum number: "))
                self.max_range = int(input("Enter maximum number: "))
                self.max_attempts = int(input("Enter number of attempts: "))
                
                if self.min_range >= self.max_range:
                    print("Maximum must be greater than minimum!")
                    continue
                if self.max_attempts <= 0:
                    print("Attempts must be positive!")
                    continue
                break
            except ValueError:
                print("Please enter valid numbers!")
    
    def get_hint(self, guess, secret_number, attempt):
        """Provide helpful hints to the player"""
        difference = abs(guess - secret_number)
        
        if attempt == 1:
            if secret_number % 2 == 0:
                print("💡 Hint: The number is even!")
            else:
                print("💡 Hint: The number is odd!")
        elif attempt == 3:
            if guess < secret_number:
                print("💡 Hint: You're getting warmer! 🔥")
            else:
                print("💡 Hint: You're getting colder! ❄️")
        elif difference <= 5:
            print("💡 Hint: You're very close! Almost there!")
        elif difference <= 15:
            print("💡 Hint: You're getting warm!")
        else:
            print("💡 Hint: You're quite far away. Keep trying!")
    
    def play_round(self):
        """Play one round of the game"""
        secret_number = random.randint(self.min_range, self.max_range)
        attempts_used = 0
        
        print(f"\n🔮 I've chosen a number between {self.min_range} and {self.max_range}!")
        print(f"You have {self.max_attempts} attempts. Good luck! 🍀")
        
        for attempt in range(1, self.max_attempts + 1):
            attempts_used = attempt
            attempts_left = self.max_attempts - attempt
            
            print(f"\nAttempt {attempt}/{self.max_attempts}")
            if attempts_left > 0:
                print(f"Attempts remaining: {attempts_left}")
            
            while True:
                try:
                    guess = int(input(f"Enter your guess ({self.min_range}-{self.max_range}): "))
                    if self.min_range <= guess <= self.max_range:
                        break
                    else:
                        print(f"Please enter a number between {self.min_range} and {self.max_range}!")
                except ValueError:
                    print("Please enter a valid number!")
            
            if guess == secret_number:
                print(f"\n🎉 CONGRATULATIONS! You guessed it in {attempt} attempts!")
                self.score += (self.max_attempts - attempt + 1) * 10
                return True, attempts_used
            
            # Provide feedback and hints
            if guess < secret_number:
                print("📈 Too low! Try a higher number.")
            else:
                print("📉 Too high! Try a lower number.")
            
            # Give hints every few attempts
            if attempt % 2 == 0 or attempts_left <= 2:
                self.get_hint(guess, secret_number, attempt)
        
        print(f"\n😔 Game Over! The number was {secret_number}")
        return False, attempts_used
    
    def update_high_scores(self, player_name, score):
        """Update and display high scores"""
        self.high_scores.append((player_name, score))
        self.high_scores.sort(key=lambda x: x[1], reverse=True)
        self.high_scores = self.high_scores[:5]  # Keep only top 5 scores
        
        print("\n🏆 HIGH SCORES 🏆")
        print("-" * 20)
        for i, (name, score) in enumerate(self.high_scores, 1):
            print(f"{i}. {name}: {score} points")
    
    def play_again(self):
        """Ask player if they want to play again"""
        while True:
            choice = input("\nWould you like to play again? (y/n): ").lower()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' or 'n'")
    
    def run(self):
        """Main game loop"""
        print("Loading game...")
        time.sleep(1)
        
        # Get player name
        player_name = input("Enter your name: ").strip() or "Player"
        
        while True:
            self.display_welcome()
            self.get_difficulty_level()
            
            won, attempts = self.play_round()
            
            if won:
                print(f"⭐ Current score: {self.score} points")
                if attempts == 1:
                    print("🏆 PERFECT GUESS! First try! Legendary! 🏆")
            
            self.update_high_scores(player_name, self.score)
            
            if not self.play_again():
                print(f"\nThanks for playing, {player_name}! 👋")
                print(f"Final score: {self.score} points")
                print("Come back soon! 🎮")
                break
            
            # Reset for new game (keep high scores)
            self.score = 0
            print("\n" + "="*60)

# Run the game
if __name__ == "__main__":
    game = GuessTheNumberGame()
    game.run()