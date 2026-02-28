#exersice 21
import random

list_of_words = ["volcano","mirror","puzzle","rocket","whisper","nebula","anchor","velvet","jungle","meteor","cipher","bubble","crystal","shadow","thunder","marble","cactus","galaxy","ladder","magnet","pirate","quantum","robot","silver","tornado","unicorn","vortex","wizard","xenon","yogurt","zephyr","alchemy","avalanche","blizzard","compass","dragon","ember","fossil","gravity","harvest","illusion","jigsaw","karma","labyrinth","matrix","nectar","obsidian","phantom","quartz","riddle","sapphire","temple","utopia","voyage","wander","xylophone","yeti","zenith","artifact","breeze","capsule","dynamo","echo","flame","glacier","hazard","inferno","jungle","keystone","legend","mirage","nomad","orbit","paradox","quest","radar","shelter","talisman","universe","voyager","wildfire","xenolith","yearn","zodiac","arcade","binary","cosmic","delta","eclipse","fusion","goblin","horizon","impact","jupiter","kingdom","lab","momentum","nebulae","oxygen","portal","quiver"]

hang_man_art = {0: ("   ",
                    "   ",
                    "   "),
               1: (" o "
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/ "),
               6: (" o ",
                   "/|\\",
                   "/ \\ ")}

def display_man(wrong_guesses):
    print("***************")
    for line in hang_man_art[wrong_guesses]:
        print(line)
    print("***************")

def check1(x):
    if not x.isalpha():
        return "invalid"

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    is_running = True
    answer = random.choice(list_of_words)
    hint = ["_"] * len(answer)
    wrong_answer = 0
    guessed_letter = set()
    while is_running:
        display_man(wrong_answer)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letter:
            print("You have already used this letter")
            continue

        guessed_letter.add(guess)

        ok = check1(guess)
        if ok =="invalid":
            print("enter a valid value")
            continue

        if len(guess) != 1:
            print("Enter only a single letter")
            continue

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_answer += 1
            if wrong_answer > 6 :
                print("You lost")
                print(f"The answer was {answer}")
                is_running = False

        if "_" not in hint:
            print(f"the word was: {answer}")
            print("You won")
            is_running = False



if __name__ == "__main__":
    main()