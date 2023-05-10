class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

def testStringManipulator():
    # Create a new StringManipulator object
    sm = StringManipulator()

    # Get a string from the user
    sm.getString()

    # Print the string in upper case
    sm.printString()

# Call the test function
testStringManipulator()
