"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
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
        """Adding constructor"""
        self.start = self.next = start
    def generate(self):
        """Return next serial"""
        self.start += 1
        return self.next - 1
    def reset(self):
        """Reset the origianl start"""
        self.start = self.next 


