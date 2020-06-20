# Main
from Paper import Paper
from Character import Character
import Dictionary


def main():
    input_text = open("input.txt", "r")
    text = input_text.read().replace('\n','')

    test_paper = Paper("Page 1")
    test_paper.drawSentence(text)
    test_paper.show()


if __name__ == "__main__":
    main()