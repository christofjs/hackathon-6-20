# Main
from Paper import Paper
from Character import Character
import Dictionary


def main():
    test_paper = Paper("TestNumber1")
    test_paper.drawSentence("aaaaaaaaaaaaa aaaaaaaa  aaaaaaaaaa aaaaaaaa aaaaa aaaaaaaaa aaaaaaaa aaaa aaaa aaaaaaa aaaaaaaaaaa aaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaa aaaaaaaaaaaa")
    test_paper.show()


if __name__ == "__main__":
    main()