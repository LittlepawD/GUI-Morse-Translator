

MORSE_DICT_ATM = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "CH": "----",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/",
}
MORSE_DICT_MTA = {v: k for k, v in MORSE_DICT_ATM.items()}
MORSE_DICT_MTA[""] = " "        # Pro mezery
TO_ASCII = {
    'Ě':'E',
    'Š':'S',
    'Č':'C',
    'Ř':'R',
    'Ž':'Z',
    'Ý':'Y',
    'Á':'A',
    'Í':'I',
    'É':'E',
    'Ú':'U',
    'Ů':'U',
    'Ť':'T',
}

class Morse:

    def __init__(self):
        pass

    def enc(self,message):
        'Encrypts given message to morse code.'
        msg_translated = []
        for n, veta in enumerate(message.split('. ')):
            msg_translated.append('')
            for char in veta.upper():
                if char in TO_ASCII:
                    print(f'Changing "{char}" to "{TO_ASCII[char]}".')
                    char = TO_ASCII[char]
                if char in MORSE_DICT_ATM:
                    msg_translated[n] += MORSE_DICT_ATM[char]
                else:
                    print(f'\tWarning: Trying to encrypt "{char}", character not found in the dictionary.')
                if char != ' ' and char in MORSE_DICT_ATM:
                    msg_translated[n] += '/'  # Za charakter vlozi /, pokud neni mezera

            # print(f'Prave prelozena veta: "{msg_translated[n]}"')
            msg_translated[n].strip('/')  # Odebere lomitka na konci. ?? Dela se to takhle?? - jo, muze byt
        return '//'.join(msg_translated)  # Spoji jednotlive vety '/'

    def dec(self,message):
        'Decrypts given message from morse to plaintext.'
        if type(message) != str:
            raise TypeError('Input has to be a string.')
        msg_alph = []
        for n, vety in enumerate(message.split('///')):
            msg_alph.append('')
            for char in vety.split('/'):
                if char in MORSE_DICT_MTA:
                    msg_alph[n] += MORSE_DICT_MTA[char]
                else:
                    print(f'\tWarning: Trying to encrypt "{char}", character not found in the dictionary.')
            msg_alph[n] = msg_alph[n].strip(' ')
            msg_alph[n] += "."  # Prida tecku na konec vety
        return " ".join(msg_alph)  # Vrati vety spojene mezerami

def is_morse(string: str) -> bool:
    for char in string[:100]:
        if char.isalnum:
            return False
    if "." in string or "-" in string:
        return True
    return False
    
if __name__ == '__main__':
    # Testing translate functions...
    # msg = 'Ja jsem ja. Nebo. Kdo?'
    testmsg_morse = '.-/..../---/.---///...-/.../../-.-./..../-./../'

    # print(Morse().enc(msg))
    print(Morse().dec(testmsg_morse))