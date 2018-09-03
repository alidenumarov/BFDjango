def swap_case(s):
    return ''.join([a.upper() if a.islower() else a.lower() for a in s])