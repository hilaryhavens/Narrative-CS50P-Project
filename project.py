import sys
import os.path
import re
from validator_collection import checkers
from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    """Ask user to input a website with text or plaintext file."""
    file = input("Website / txt file: ")

    """Function to check if input is website or file."""
    if format_check(file) is not True:
        print("Incorrect input or file not found.")
        sys.exit(1)

    """Open file and write text to space in memory."""
    text = file_open(file)

    """Count and print total number of words in text."""
    words = len(text.split())
    # Placeholder
    print(f"{words} words in text.")

    """Count total number of "I"s in text."""
    inum = inum_count(text)
    # Placeholder
    print(f"{inum} I's in text.")

    """Calculate "I" to word ratio in text and print."""
    irat = float(inum / words)
    print(f"The I to word ratio is {irat}.")

    """Prediction of narrative type."""
    type = nar_type(irat)
    print(f"The narrative voice is {type}.")


def format_check(x):
    """
    Conditional statement checking if input is website or file.
    First, check if input is a valid web address (because some web addresses end with .txt).
    """
    if checkers.is_url(x) == True:
        return True

    """If not, check if the file extension is txt and if such a file exists in the directory."""
    if x.endswith(".txt"):
        path = "./" + x
        check_file = os.path.isfile(path)
        if check_file == True:
            return True


def file_open(x):
    """If input is a website, run this function to process text."""
    if checkers.is_url(x):
        html = urlopen(x).read()
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        return text

    """If input is txt file, run this function to process text."""
    if x.endswith(".txt"):
        """Open file and return content of text"""
        f = open(x, "r")
        text = f.read()
        return text


def inum_count(x):
    """Calculate number of i's in text.
    First convert text to lowercase."""
    text = x.lower()
    """Use regular expressions to find number of I's and return the length of that list."""
    matches = re.findall(r"\s[i](\s|')", text)
    inum = len(matches)
    return inum


def nar_type(x):
    """Based on known examples from data.txt and their I ratio, predict narrative type with cutoffs."""
    if x > 0.024:
        result = "probably first-person or epistolary"
    elif x < 0.016:
        result = "unlikely first-person or epistolary"
    else:
        result = "ambiguously first-person or epistolary"
    return result


if __name__ == "__main__":
    main()
