class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    This class is used to generate sequential serial numbers starting from a given
    start value. It also provides a method to reset the serial number to its
    original start value.

    Args:
        start (int): The initial value of the serial number.

    Example:
        >>> serial = SerialGenerator(start=100)
        >>> serial.generate()
        100
        >>> serial.generate()
        101
        >>> serial.generate()
        102
        >>> serial.reset()
        >>> serial.generate()
        100
    """

    def __init__(self, start):
        """Initialize the SerialGenerator with a start value."""
        self.start = start
        self.next_value = start  # Initialize next_value to start value

    def generate(self):
        """Generate and return the next sequential serial number.

        Returns:
            int: The next sequential serial number.
        """
        current_value = self.next_value
        self.next_value += 1  # Increment the next_value for the next call
        return current_value

    def reset(self):
        """Reset the serial number to its original start value."""
        self.next_value = self.start


# Usage example:
if __name__ == "__main__":
    serial = SerialGenerator(start=100)
    print(serial.generate())  # Output: 100
    print(serial.generate())  # Output: 101
    print(serial.generate())  # Output: 102
    serial.reset()
    print(serial.generate())  # Output: 100
