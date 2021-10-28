import VigenereDecrypt
import DetectLanguage
import re
import sys

import Constants


def loadingBar(count, total, size):
    percent = float(count) / float(total) * 100
    sys.stdout.write("\r" + str(int(count)).rjust(3, '0') + "/" + str(int(total)).rjust(3, '0'))


def openfile(lang):
    dictionary = Constants.pick_dict(lang)
    with open(dictionary, encoding="utf-8") as f:
        dictfile = f.readlines()
    return dictfile


def dictionaryhack(lang, word):
    pattern = re.compile('\W')
    word_dict = {}
    dictfile = openfile(lang)
    count = len(dictfile)
    iterator = 0
    for line in dictfile:
        loadingBar(iterator, count, 1)
        iterator += 1
        if len(word) < len(line):
            continue
        line = line.strip()
        line = re.sub(pattern, '', line)
        deciphered_word = VigenereDecrypt.decryption(lang, word, line)
        buffer_word = deciphered_word.split()
        isEnglish = DetectLanguage.DetectLanguage(lang, buffer_word)
        if isEnglish > 0.6:
            word_dict[line] = isEnglish
            print(" Слово:", line, ", вероятность связности текста: ", isEnglish, ';расшифровка:',
                  deciphered_word)
            if isEnglish > 0.8:
                choice = 0
                print("Найден наиболее подходящий ключ:", line, ";расшифровка - ", deciphered_word)
                print("Продолжить? (y/n)")
                choice = input()
                while choice != "y" and choice != "n":
                    print("(y/n)")
                    choice = input()
                if choice == "n":
                    break
    return VigenereDecrypt.decryption(lang, word, max(word_dict))
