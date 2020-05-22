#!/usr/bin/python3
"""the text_indentation module"""


def text_indentation(text):
    """puts two new lines after these characters in a string: ., :, and ?
    Args:
        text: the string to print
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for char in ".?:":
        text = (char + "\n\n").join(
            [sen.strip(" ") for sen in text.split(char)])
    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
