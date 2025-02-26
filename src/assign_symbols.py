def assign_symbols():
    """Takes input from user and returns the symbols for the players."""
    symbol = input("Choose your symbol (X/O): ").upper()
    while symbol not in ['X', 'O']:
        symbol = input("Invalid symbol! Choose your symbol (X/O): ").upper()
    if symbol == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'