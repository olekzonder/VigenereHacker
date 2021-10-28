import CaesarShiftHacker
import VigenereDecrypt
import DetectLanguage
import itertools
def findPossibleKeys(lang,word,keylen):
    word = ''.join(word.strip().split())
    word = list(map(''.join,zip(*[iter(word)]*keylen)))
    decipherDict = {}
    for i in range(0,keylen):
        cachelist = ''.join([letter[i] for letter in word])
        decipherDict[i] = 0
        decipherDict[i] = CaesarShiftHacker.hack(lang,cachelist)
    return decipherDict

def finalProcessing(lang,decipherDict,word,keylen):
    for indexes in itertools.product(range(3),repeat=keylen):
        key = ''
        for i in range(keylen):
            key += decipherDict[i][indexes[i]][0]
        decryption = VigenereDecrypt.decryption(lang,word,key)
        score = DetectLanguage.DetectLanguage(lang,decryption)
        if score > 0.8:
            choice = 0
            print("Ключ:", key, ", расшифровка: ", decryption)
            print("Продолжить? (y/n)")
            choice = input()
            while choice != "y" and choice != "n":
                print("(y/n)")
                choice = input()
            if choice == "n":
                return key