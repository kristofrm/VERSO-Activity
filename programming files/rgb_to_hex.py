def rgb_to_hex(r, g, b):
    # Gets maximum value in range of 0 to minimum of 255 to r, g, b value
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    # Returns r, g, b values in hex format
    return '{:02X}{:02X}{:02X}'.format(r, g, b)


# test with hex_color = rgb_to_hex(255, 127, 0) # returns "FF7F00"
