diameter = input()
pads = diameter//3
for x in range(diameter):
    if x < pads:
        rpads = pads - x
    elif diameter - x <= pads:
        rpads = abs(diameter - (1 + x) - pads) 
    else:
        rpads = 0
    print(" "*(rpads*2) + "*" * ((diameter - 2 *rpads)*2) + " " * (rpads * 2))
