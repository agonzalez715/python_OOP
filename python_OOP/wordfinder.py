import random

class WordFinder:
    """
    WordFinder class to read words from a file and provide a random word.
    Attributes:
        words (list): A list of words read from the file.
    """
    def __init__(self, filepath):
        """
        Initialize a new WordFinder instance.
        Reads words from a file located at 'filepath', stores them in a list,
        and prints out the number of words read.
        Args:
            filepath (str): The path to the file containing words.
        """
        self.words = self.read_words(filepath)
        print(f"{len(self.words)} words read")

    def read_words(self, filepath):
        """
        Read words from a file and return them as a list.
        Each line in the file is treated as a separate word. Trailing 
        newlines are removed from each word.
        Args:
            filepath (str): The path to the file containing words.
        Returns:
            list: A list of words from the file.
        """
        with open(filepath, 'r') as file:
            return [line.strip() for line in file]

    def random(self):
        """
        Return a random word from the list of words.
        This method does not re-read the file, but instead uses the list
        of words already read into memory.
        Returns:
            str: A random word from the list.
        """
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """
    SpecialWordFinder is a subclass of WordFinder.
    It is designed to handle files with blank lines and comments (lines starting with #).
    """
    def read_words(self, filepath):
        """
        Overridden method to read words from a file, ignoring blank lines and comments.
        Args:
            filepath (str): The path to the file containing words.
        Returns:
            list: A list of words from the file, excluding blank lines and comments.
        """
        with open(filepath, 'r') as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#')]

# Example usage
swf = SpecialWordFinder("/Users/student/special_words.txt")
print(swf.random())
print(swf.random())
print(swf.random())
