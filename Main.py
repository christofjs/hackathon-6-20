# Main
from Paper import Paper
from Character import Character
import Config
import Dictionary


def main():
    test_paper = Paper("TestNumber1")
    test_character = Character("111111")
    test_paper.drawChar(test_character, 10, 10)
    test_paper.show()


if __name__ == "__main__":
    main()