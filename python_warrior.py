import random
import time

# Question sets by difficulty level with multiple choices
questions = {
    'easy': [
        ("What is the output of `print(2 + 2)`?\nA) 3\nB) 4\nC) 5\nD) 2", 'B', 6),
        ("Which of the following is a valid variable name?\nA) my value\nB) my_value\nC) 2myValue\nD) my-value", 'B', 6),
        ("What does `len('hello')` return?\nA) 4\nB) 5\nC) 6\nD) 0", 'B', 6),
        ("Which data type is used to represent a sequence of characters?\nA) list\nB) int\nC) str\nD) float", 'C', 6),
        ("What is the output of `print('Hello World!')`?\nA) Hello World!\nB) 'Hello World!'\nC) Hello\nD) World", 'A', 6),
        ("What is the result of `3 * 3`?\nA) 6\nB) 8\nC) 9\nD) 7", 'C', 6),
        ("What is the output of `print(type(5))`?\nA) int\nB) str\nC) list\nD) dict", 'A', 6),
        ("What is the output of `print(True and False)`?\nA) True\nB) False\nC) 0\nD) 1", 'B', 6),
        ("What is the correct way to create a list in Python?\nA) list()\nB) []\nC) {}\nD) ''", 'B', 6),
        ("What is the output of `print(10 // 3)`?\nA) 3\nB) 3.0\nC) 4\nD) 2", 'A', 6),
    ],
    'medium': [
        ("Which of the following is not a mutable data type?\nA) list\nB) dict\nC) set\nD) tuple", 'D', 8),
        ("What will be the output of `print(bool(0))`?\nA) True\nB) False\nC) None\nD) 0", 'B', 8),
        ("What is the method to add an element to a set?\nA) add()\nB) append()\nC) insert()\nD) extend()", 'A', 8),
        ("Which of the following is used to handle exceptions?\nA) if-else\nB) try-except\nC) for-loop\nD) function", 'B', 8),
        ("What is the output of `print(sorted([3, 1, 2]))`?\nA) [1, 2, 3]\nB) [3, 2, 1]\nC) [3, 1, 2]\nD) [2, 3, 1]", 'A', 8),
        ("What is the correct syntax to create a function in Python?\nA) create function myFunction()\nB) def myFunction():\nC) function myFunction():\nD) def myFunction", 'B', 8),
        ("What is the output of `print('a' in 'banana')`?\nA) False\nB) True\nC) None\nD) 'a'", 'B', 8),
        ("Which of the following can be used to create a generator in Python?\nA) []\nB) ()\nC) {}\nD) str()", 'B', 8),
        ("What is the output of `print(list(range(3)))`?\nA) [0, 1, 2]\nB) [1, 2, 3]\nC) [0, 1, 2, 3]\nD) None", 'A', 8),
        ("How do you denote a comment in Python?\nA) //\nB) #\nC) <!-- -->\nD) /* */", 'B', 8),
    ],
    'hard': [
        ("Which of the following is true about Python dictionaries?\nA) Keys must be unique\nB) Values must be unique\nC) Both keys and values must be unique\nD) None of the above", 'A', 10),
        ("What is the output of `print([x**2 for x in range(5) if x % 2 == 0])`?\nA) [0, 1, 4]\nB) [0, 4, 16]\nC) [1, 4, 9]\nD) [0, 9]", 'B', 10),
        ("How do you define a class in Python?\nA) class MyClass:\nB) def MyClass:\nC) create class MyClass:\nD) MyClass:", 'A', 10),
        ("What does `__init__` method do in a class?\nA) Initializes the object\nB) Creates a new class\nC) Deletes the object\nD) None of the above", 'A', 10),
        ("What will be the output of `print(x is not 10)` where `x = 10`?\nA) True\nB) False\nC) None\nD) Error", 'B', 10),
        ("What is the output of `print(type([]))`?\nA) <class 'list'>\nB) <class 'dict'>\nC) <class 'set'>\nD) <class 'tuple'>", 'A', 10),
        ("What is the output of `print(None == False)`?\nA) True\nB) False\nC) None\nD) Error", 'B', 10),
        ("What is the purpose of the `pass` statement in Python?\nA) To skip the execution of a loop\nB) To define an empty class or function\nC) To raise an exception\nD) None of the above", 'B', 10),
        ("What is the output of `print(3 ** 2)`?\nA) 6\nB) 8\nC) 9\nD) 3", 'C', 10),
        ("Which of the following is a valid way to iterate through a list?\nA) for item in list:\nB) for item in range(list):\nC) for list in item:\nD) while list:", 'A', 10),
    ]
}

# Function to ask a question and return damage
def ask_question(difficulty): # difficulty is a string
    question_data = random.choice(questions[difficulty]) # question_data is a tuple
    question, correct_answer, attack_power = question_data # unpack the tuple
    return question, correct_answer, attack_power # return the unpacked values

# Main game function
def main():
    # Game Initialization
    player_hp = 100
    opponent_hp = 100
    print("\n\nWelcome to ** Python Warrior **!\n")
    time.sleep(2)
    print("In this game, you will battle an opponent using your Python knowledge.")
    time.sleep(2)
    print("You will take turns attacking each other by answering a random Python question.\nAnswer correctly to attack your opponent and reduce their HP.")
    time.sleep(2)
    print("When it is your opponents turn, you have a chance to block their attack by answering correctly. \nBoth players start with 100 HP.")
    time.sleep(2)
    print("\nLet the battle begin!")
    time.sleep(2)
    while player_hp > 0 and opponent_hp > 0:
        # Player's turn
        print("\nYour HP:", player_hp, "Opponent's HP:", opponent_hp)
        time.sleep(2)
        print("Choose your attack:")
        time.sleep(1)
        print("1. Novice Slash: 6 Atk Lvl Easy")
        time.sleep(1)
        print("2. Mid Kick: 8 Atk Lvl Medium")
        time.sleep(1)
        print("3. Heavy Uppercut: 10 Atk Lvl Hard")
        time.sleep(1)
        difficulty_choice = input("Select your attack by typing (1/2/3), and then Enter: ")

        if difficulty_choice == '1':
            difficulty = 'easy'
        elif difficulty_choice == '2':
            difficulty = 'medium'
        elif difficulty_choice == '3':
            difficulty = 'hard'
        else:
            print("Invalid choice. Please choose again.")
            continue
        
        question, correct_answer, attack_power = ask_question(difficulty)
        time.sleep(1)
        print("\nQuestion:", question)
        time.sleep(2)
        player_answer = input("Your answer (A, B, C, or D): ")
        time.sleep(1)
        
        if player_answer.upper() == correct_answer:
            opponent_hp -= attack_power
            time.sleep(1)
            print(f"Correct! Opponent takes {attack_power} damage.")
        else:
            time.sleep(1)
            print("Incorrect! No damage dealt.")
        
        # Opponent's turn (random question to block)
        print("\nOpponent's turn!")
        time.sleep(2)
        opponent_difficulty = random.choice(list(questions.keys()))
        opponent_question, opponent_correct_answer, opponent_attack_power = ask_question(opponent_difficulty)
        time.sleep(1)
        print("Opponent's question for you to block:", opponent_question)
        time.sleep(1)
        opponent_answer = input("Your answer (A, B, C, or D): ")
        
        if opponent_answer.upper() == opponent_correct_answer:
            time.sleep(1)
            print(f"You answered correctly! You block {opponent_attack_power} damage from your opponent.")
        else:
            player_hp -= opponent_attack_power
            time.sleep(1)
            print(f"You answered incorrectly! You take {opponent_attack_power} damage.")
    
    if player_hp <= 0:
        time.sleep(1)
        print("You have been defeated! Game Over.")
    elif opponent_hp <= 0:
        time.sleep(1)
        print("Congratulations! You defeated the opponent!")

# Run the game
if __name__ == "__main__":
    main()
