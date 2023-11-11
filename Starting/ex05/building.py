
import sys


def main(text):
    """

    :param text:
    :return:
    """

    if text is None or text == '':
        text = input("What is the text to count?\n")
    elif len(sys.argv) != 2:
        print("AssertionError: Please provide only one string argument.")
        return

    upper_letters = sum(1 for char in text if char.isupper())
    lower_letters = sum(1 for char in text if char.islower())
    punctuation_marks = sum(
        1 for char in text if char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    digits = sum(1 for char in text if char.isdigit())
    spaces = sum(1 for char in text if char.isspace())

    total_characters = len(text)

    print(f"The text contains {total_characters} "
          f"character{'s' if total_characters != 1 else ''}:")
    print(f"{upper_letters} upper letter{'s' if upper_letters != 1 else ''}")
    print(f"{lower_letters} lower letter{'s' if lower_letters != 1 else ''}")
    print(f"{punctuation_marks} "
          f"punctuation mark{'s' if punctuation_marks != 1 else ''}")
    print(f"{spaces} space{'s' if spaces != 1 else ''}")
    print(f"{digits} digit{'s' if digits != 1 else ''}")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        main(None)
    else:
        main(sys.argv[1])
