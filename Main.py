# Main
from Paper import Paper
from Character import Character
import Dictionary


def main():
    test_paper = Paper("TestNumber1")
    test_paper.drawSentence("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ut elit eu mauris sodales tristique id ut arcu. Mauris ac nunc lacinia, feugiat lectus id, efficitur quam. Integer lobortis bibendum velit vitae viverra. Vestibulum placerat nulla id urna imperdiet ultrices. Sed efficitur porttitor metus ut fringilla. Cras blandit metus et lorem elementum ornare. Nullam cursus pharetra sapien, sed dapibus lorem sagittis non. Curabitur eget semper mauris, at rutrum purus. Donec bibendum volutpat lectus, vitae efficitur quam. Vivamus nec justo sem. Nam porta malesuada nisl eu congue. Praesent euismod risus augue, ac fringilla ipsum blandit et. Morbi et vehicula justo. Nunc accumsan a orci eget vehicula. Praesent tristique ipsum a nisl vulputate, a accumsan ante finibus. Nam pretium lacus in libero aliquam dapibus.")
    test_paper.show()


if __name__ == "__main__":
    main()