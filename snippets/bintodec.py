def bin2dec(bin):
    """
    This fucntion takes a binary digit in 
    form of python list, with the least
    significant bit last and trasforms
    it into binary number
    """
    remainder = bin
    dec = 0
    current = 1
    # As long, as there are any items left
    # in the bin list, we take the last
    # item an if it is a one (the bit is on) 
    # we add current power of two (that is 1,2,4,8 etc.)
    # then we multiply the current by two an move on
    while bin:
        if remainder.pop():
            dec += current
        current *= 2
    return dec
       

# We will use assertions to test our code
# If it doesnt go the way expected, exception is raised
assert(bin2dec([0]) == 0)
assert(bin2dec([1]) == 1)
assert(bin2dec([1,0,1]) == 5)

# In windows, the terminal window goes away too quick
# so we just wait for any key
raw_input("Press any key")
