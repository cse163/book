class Dog:
    """
    Represents a dog with a name
    """
    
    def __init__(self, name):
        """
        Initializes a new dog with the given name
        """
        self.name = name

    def bark(self):
        """
        Prints a message saying this dog barked
        """
        print(self.name + ': Woof')
