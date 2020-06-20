# Main
from Paper import Paper
from Character import Character
import Dictionary
import os

def getInput(file):
    input_text = open(file, "r")
    return input_text.read().replace('\n', '')


def main():

    exit = False
    while not exit:
        print("Welcome to the Braille Converter!"
              "\n====="
              "\n(1) Convert input from 'input.txt'"
              "\n(2) Convert input from console"
              "\n(3) Exit program"
              "\n(4) Information Menu")
        input_valid = False
        while not input_valid:
            choice = input("Enter option:")
            if choice in ["1", "2", "3", "4"]:
                choice = int(choice)
                input_valid = True
            else:
                print("Invalid input, try again.")

        if choice == 1 or choice == 2:

            print("=" * 25)
            input_valid = False
            while not input_valid:
                name = input("Enter name of paper:")
                if len(name) > 0:
                    input_valid = True
                else:
                    print("Invalid input, try again.")

            paper_name = name

            print("=" * 25)
            input_valid = False
            while not input_valid:
                mirrored = input("Mirrored paper? (Y/N):")
                if mirrored in ["y", "Y", "n", "N"]:
                    input_valid = True
                else:
                    print("Invalid input, try again.")

            is_mirrored = False
            if mirrored in ["Y", "y"]:
                is_mirrored = True

            if choice == 1:
                text = getInput("input.txt")
            else:
                print("=" * 25)
                input_valid = False
                while not input_valid:
                    choice = input("Enter text to convert:")
                    for letter in choice:
                        if Dictionary.DICTIONARY.get(letter) is None:
                            print("'" + letter + "' is an invalid character, try again.")
                            input_valid = False
                            break
                        else:
                            input_valid = True
                text = choice

            if not os.path.isdir("./output"):
                os.mkdir("./output")

            paper = Paper(paper_name)

            print("=" * 25 + "\nWorking...")

            if is_mirrored:
                paper.drawMirroredSentence(paper.convertBrailleCharacter(text))
            else:
                paper.drawSentence(paper.convertBrailleCharacter(text))
            print("Done.")

            input_valid = False
            while not input_valid:
                choice = input("Would you like to exit the program? (Y/N):")
                if choice in ["y", "Y", "n", "N"]:
                    input_valid = True
                else:
                    print("Invalid input, try again")

            if choice in ["y", "Y"]:
                exit = True

        elif choice == 3:
            input("Exiting...")
            exit = True

        elif choice == 4:
            print("=" * 25 + "\nINFORMATION MENU\n=====")
            print("ABOUT"
                  "\n====="
                  "\nThis program was created for the OSU Hack-a-thon of Summer 2020 (Theme: Accessibility). "
                  "\nThe objective is to make creating braille easier and more accessible. "
                  "\nTypical braille stamping equipment is hard to get and expensive, "
                  "\nhowever one can use this program to make low-budget braille."
                  "\n====="
                  "\nHOW TO USE"
                  "\n====="
                  "\nEnter large input into 'input.txt' or use the console for smaller batches"
                  "\nFinished pages are saved in the the 'output' directory"
                  "\nTo make braille, simply convert your input using one of the options, "
                  "\nchoose to have the paper mirrored, and poke the dots with a blunt point."
                  "\nThe resulting indentations represent braille."
                  "\n====="
                  "\nCONFIG"
                  "\n====="
                  "\nTo configure the color, size, fitting, and spacing of the braille markings, see Config.py"
                  "\nTo configure braille translations, see Dictionary.py"
                  "\n\n")
            input("Press Enter to return to main menu...")
    print("\n\n\n\n\n")




if __name__ == "__main__":
    main()
