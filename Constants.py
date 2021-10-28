import os


def pick_dict(lang):
    if lang == "ru":
        dictionary = os.path.join(os.path.dirname(__file__),'russian.txt')
    else:
        dictionary = os.path.join(os.path.dirname(__file__),'english.txt')
    return dictionary

def pick_alphabet(lang):
    if lang == 'ru':
        alphabet =  ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
    if lang == 'en':
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    return alphabet

def pick_frequent(lang):
    if lang == "ru":
        freqLetters=["О","Е","А","И","Н","Т","С","Р","В","Л","К","М","Д","П","У","Я","Ы","Ь","Г","З","Б","Ч","Й","Х","Ж","Ш","Ю","Ц","Щ","Э","Ф","Ъ","Ё"]
    else:
        freqLetters = ["E","T","A","O","I","N","S","H","R","D","L","C","U","M","W","F","G","Y","P","B","V","K","J","X","Q","Z"]
    return freqLetters

kasiskiMinSize = 3
kasiskiMaxSize = 20