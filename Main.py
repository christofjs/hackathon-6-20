# Main
from Paper import Paper
from Character import Character
import Dictionary


def main():
    test_paper = Paper("TestNumber1")
    test_paper.drawSentence("hello 9999 hello 123 hi 123 123")
    test_paper.show()


if __name__ == "__main__":
    main()