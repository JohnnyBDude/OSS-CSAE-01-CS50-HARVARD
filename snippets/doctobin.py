def doc2bin(doc):
    """
    This super simple function takes a
    decimal digit and transforms it into
    a list of ones and zeroes as if it 
    was encoded in binary.
    (Which it is not, because it is a list
    of integers really)
    """
    remainder = doc
    bin = []
    while remainder > 0:
        bin.append(remainder % 2)
        remainder = remainder // 2

    # We want least significant piece at the end
    # just as we have it in decimal.
    # So we return the list in reversed order
    return bin[::-1]

print doc2bin(1)
print doc2bin(2)
print doc2bin(7)

# In windows, the terminal window goes away too quick
# so we just wait for any key
raw_input()
