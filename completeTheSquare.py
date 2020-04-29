'''
Created by: Lionel Lewis 

Takes a B value from the user and uses it to 
perform a mathematical
function  called Completing The Square.
'''

# Uni-Code characters for the Square Root and Square symbols.
SQUARE_ROOT = u'\u221A'
SQUARED = u'\u00B2'

# Function that calculates the value of B
def completeTheSquare(b):
    b1 = b
    b2 = b ** 2
    return int(b1), int(b2)

# Main function that formats the equation and gets the input from the user.
if __name__ == "__main__":
    b = int(input('Enter value for b\n>>> '))
    print()
    print('x' + SQUARED, '+', str(b) + "x")
    b1, b2 = completeTheSquare(b)
    print("(x + {}/{})".format(b1, 2) + SQUARED + " - " + "{}/{}".format(b2, 4))