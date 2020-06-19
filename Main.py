# Main
from Paper import Paper
from Character import Character
import Dictionary


def main():
    test_paper = Paper("TestNumber1")
    test_paper.drawSentence("hello this is a test")
    test_paper.show()


if __name__ == "__main__":
    main()