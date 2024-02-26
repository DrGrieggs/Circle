# Accept input for the diameter and cast it to an integer
diameter = int(input())
# Accept input for the character to use
ch = input()
# Caluclate the size of a region of the cicle
pads = diameter//3

# Use a for loop to generate each row of the circle
for x in range(diameter):
    # Check to see if we're in the top region of the circle, where you add more symbols each row
    if x < pads:
        # The pad vlaue should decrease as x increases
        rpads = pads-x
    # Check if you're in the bottom of the circle where the number of symbols decreases
    elif diameter - x <= pads:
        # you want to have the pad value increase as x increases, starting at 0 for 2*pads
        rpads = abs(diameter - (1+x) - pads)
    # otherwise you're in the middle of the circle where the number of rows stays constant
    else:
        # you don't pad with any spaces in this case
        rpads = 0
    # build the string with the appropriate numbers of symbols and spaces
    print(" "*rpads*2 + ch*(diameter - 2 *rpads) * 2 + " "*rpads*2)