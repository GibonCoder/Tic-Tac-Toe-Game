class Interface:
    def __init__(self):
        self._player_char = ''
        self._bot_char = ''
        self.continue_game = True

    def choose_char(self, char):
        match char.upper():
            case 'X':
                self._player_char = 'X'
                self._bot_char = 'O'
            case 'O':
                self._player_char = 'O'
                self._bot_char = 'X'
            case '0':
                self.continue_game = False


