from random import choice

"""this challenge is similar to the 1st day challenge of 100 days of code , it is for generating a funny_word that 
combines two user input strings can be viewed on repl.it website using the following links 
@link:https://repl.it/@abdelkha/funny-word-generator?embed=1&output=1#main.py 
some of the used questions ar copied from https://pairedlife.com/etiquette/Funny-Questions-to-Ask-Your-Friends"""


def generate_funny_word():
    """asks the user for his answer to two questions, and returns a funny word that combines the user's answers"""

    questions = ["What's name of the city you grew up in\n", "What's your pet's name?\n", "What's your nickname?\n",
                 "What's your favorite dinosaur?\n", "What conspiracy theories do you believe in?\n",
                 "What songs are on your zombie killing soundtrack?\n",
                 "What's the last thing you did for the first time?\n", "What's your favorite smell?\n",
                 "If you could eat only one food for the rest of your life, what would it be?\n",
                 "What's the first thing you do when you are bored?\n",
                 " What's your most favorite animal in the world?\n",
                 "What will your last words be?\n", "What can you talk about for hours?\n",
                 "If you could have any super power, what would it be and why?\n",
                 "If you could have dinner with any three people from history, who would they be?\n",
                 "On a scale from one to ten, what's your favorite color?\n"]
    print("Welcome to the Funny Word Generator.\n")
    print("please answer the following question in few words.\n")
    question = choice(questions)  # chooses a random question from the list questions
    answer1 = input(f"{question}\n")  # asks the user the randomly chosen question, saves his answer in answer1
    question = choice(questions)  # chooses a random question from the list questions
    answer2 = input(f"{question}\n")  # asks the user the randomly chosen question, saves his answer in answer2
    print("Your band name could be " + answer1 + answer2)


if __name__ == '__main__':
    generate_funny_word()
