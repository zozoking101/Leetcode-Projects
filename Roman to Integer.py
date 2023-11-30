def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    i = 0
    p = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Iterate over each character in s, except the last one
    for j in range(len(s) - 1):
        # If the value of the current numeral is less than the value of the next numeral,
        # subtract the current value from the result
        if p[s[j]] < p[s[j+1]]:
            i -= p[s[j]]
        # Otherwise, add the current value to the result
        else:
            i += p[s[j]]

    # Add the value of the last numeral to the result
    i += p[s[-1]]

    return i