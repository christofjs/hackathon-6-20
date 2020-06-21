# Main
from Paper import Paper
import Dictionary
import os


def getInput(file):  # To open the file
    input_text = open(file, "r")
    return input_text.read().replace('\n', '')


def main():

    exit = False

    while not exit:

        #  Main Menu

        print("Welcome to the Braille Converter!"
              "\n====="
              "\n(1) Information Menu"
              "\n(2) Convert input from console"
              "\n(3) Convert input from 'input.txt'"
              "\n(4) Exit program")

        input_valid = False
        while not input_valid:
            choice = input("Enter option:")
            if choice in ["1", "2", "3", "4"]:
                choice = int(choice)
                input_valid = True
            else:
                print("Invalid input, try again.")

        # Information screen

        if choice == 1:
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

        # Translation options

        if choice == 2 or choice == 3:

            # Submenu for creating a paper

            print("=" * 25)
            input_valid = False
            while not input_valid:
                name = input("Enter name of paper:")
                if len(name) > 0:
                    input_valid = True
                else:
                    print("Invalid input, try again.")

            paper_name = name

            # Ask if it is mirrored

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

            if choice == 3:  # If user chose to read from file
                text = getInput("input.txt")
                for letter in text:
                    if Dictionary.DICTIONARY.get(letter) is None and not letter.isupper():  # Make sure text is valid
                        print("'" + letter + "' is an invalid character."
                                             "\nFix input.txt and run the program again.")
                        input("Press Enter to exit...")
                        quit()  # If input.txt has invalid char, exit program

            else:  # If user chose console input
                print("=" * 25)
                input_valid = False
                while not input_valid:
                    text = input("Enter text to convert:")
                    for letter in text:
                        if Dictionary.DICTIONARY.get(letter) is None and not letter.isupper():  # Make sure console input is valid
                            print("'" + letter + "' is an invalid character, try again.")
                            input_valid = False
                            break
                        else:
                            input_valid = True

            if not os.path.isdir("./output"):  # If output folder doesn't exist, make one
                os.mkdir("./output")

            paper = Paper(paper_name)

            print("=" * 25 + "\nWorking...")

            if is_mirrored:  # Make it mirrored
                paper.drawMirroredSentence(paper.convertBrailleCharacter(text))
            else:
                paper.drawSentence(paper.convertBrailleCharacter(text))
            print("Done.")

            # If they want to do it again

            input_valid = False
            while not input_valid:
                is_exit = input("Would you like to exit the program? (Y/N):")
                if is_exit in ["y", "Y", "n", "N"]:
                    input_valid = True
                else:
                    print("Invalid input, try again")

            if is_exit in ["y", "Y"]:
                exit = True

        # Exit

        elif choice == 4:
            input("Exiting...")
            exit = True

    print("\n\n\n\n\n")


if __name__ == "__main__":
    main()
