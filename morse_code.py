"""
You have received a secret message! unfortunately you can’t just read it, it is encoded in Morse code. 
Your task is : implement a function that would take the morse code as input 
and return a human-readable string. 3 spaces are used : separate words and 
Extra spaces before or after the code have no meaning and should be ignored..
"""

morseDecoder = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0",
    "": " ",
    ".-.-.-": ".",
    "--..--": ",",
    "---...": ".",
    "..--..": "?",
    "-.-.--": "!",
    "...---...": "SOS",
    "-....-": "''",
    "-..-.": "/",
    "-.--.-": "()",
    ".--.-.": "@",
    "-...-": "=",
}

def decode_morse(morseCode):
    words = morseCode.strip().split(' ')
    return " ".join(list(map(lambda word: morseDecoder.get(word, ""), words)))

morseCode = "-.-- --- ..-   .... .- ...- .   .-   -... .. --.   -... .-. .- .. -.   ..-. --- .-.   -.- --- - .-.. .. -."
print(decode_morse(morseCode))