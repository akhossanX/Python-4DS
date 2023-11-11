from ft_filter import ft_filter
from sys import argv


def filter_words_by_length(text, length):
    """

    :param text: str
    :param length: int
    :return: list of words
    """
    strings = text.split()
    return ft_filter(lambda s, size=length: len(s) > size, strings)


if __name__ == "__main__":
    if len(argv) != 3:
        print("AssertionError: the arguments are bad")
    else:
        string_input = argv[1]
        try:
            int_input = int(argv[2])
            result = filter_words_by_length(string_input, int_input)
            print(result)
        except ValueError:
            print("AssertionError: the arguments are bad")
