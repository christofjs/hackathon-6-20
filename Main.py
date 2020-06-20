# Main
from Paper import Paper
from Character import Character
import Dictionary


def getInput(file):
    input_text = open(file, "r")
    return input_text.read().replace('\n', '')


def main():

    text = getInput("input.txt")

    test_paper = Paper("Page 1")
    test_paper.drawSentence(text)
    test_paper.show()


if __name__ == "__main__":
    main()